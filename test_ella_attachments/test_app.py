from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.template import Template, Context, NodeList

from ella_attachments.models import Type, Attachment
from ella_attachments.views import download_attachment


class TestApp(TestCase):
    def setUp(self):
        self.plain_text_type = Type.objects.create(
            name='Plain text', slug='plain-text', mimetype='text/plain'
        )
        self.plain_text_attachment = Attachment.objects.create(
            name='Simple text', slug='simple-text', type=self.plain_text_type
        )
        self.plain_text_attachment.attachment = SimpleUploadedFile('simple', 'simple text')
        self.plain_text_attachment.save()

        self.none_type_attachment = Attachment.objects.create(
            name='None type', slug='none-type',
        )
        self.none_type_attachment.attachment = SimpleUploadedFile('plain.txt', 'plain.txt')
        self.none_type_attachment.save()

    def test_box_without_params(self):
        # attachment with text/plain mimetype
        pta = self.plain_text_attachment
        box = pta.box_class(pta, 'some-box', NodeList())

        c = Context({'attachment': pta})
        box.prepare(c)

        context = box.get_context()
        self.assertEqual(context['name'], 'Simple text')
        self.assertEqual(context['description'], None)
        self.assertEqual(context['attachment'], pta.attachment)
        self.assertEqual(context['type_name'], 'Plain text')
        self.assertEqual(context['type_mimetype'], 'text/plain')

        template_list = box._get_template_list()
        self.assertEqual(template_list, [
            'box/content_type/ella_attachments.attachment/simple-text/some-box.html',
            'box/content_type/ella_attachments.attachment/type/plain-text/some-box.html',
            'box/content_type/ella_attachments.attachment/some-box.html',
            'box/content_type/ella_attachments.attachment/box.html',
            'box/some-box.html',
            'box/box.html',
        ])

        # attachment with no mimetype
        nta = self.none_type_attachment
        box = nta.box_class(nta, 'some-box', NodeList())

        c = Context({'attachment': nta})
        box.prepare(c)

        context = box.get_context()
        self.assertEqual(context['name'], 'None type')
        self.assertEqual(context['description'], None)
        self.assertEqual(context['attachment'], nta.attachment)
        self.assertEqual(context['type_name'], None)
        self.assertEqual(context['type_mimetype'], None)

        template_list = box._get_template_list()
        self.assertEqual(template_list, [
            'box/content_type/ella_attachments.attachment/none-type/some-box.html',
            'box/content_type/ella_attachments.attachment/some-box.html',
            'box/content_type/ella_attachments.attachment/box.html',
            'box/some-box.html',
            'box/box.html',
        ])

    def test_box_with_params(self):
        pta = self.plain_text_attachment
        t = Template('name: N\n'
                     'description: D\n'
                     'attachment: A\n'
                     'type_name: TN\n'
                     'type_mimetype: TM\n')
        box = pta.box_class(pta, 'simple', t.nodelist)

        c = Context({'attachment': pta})
        box.prepare(c)

        context = box.get_context()
        self.assertEqual(context['name'], 'N')
        self.assertEqual(context['description'], 'D')
        self.assertEqual(context['attachment'], 'A')
        self.assertEqual(context['type_name'], 'TN')
        self.assertEqual(context['type_mimetype'], 'TM')

    def tests_for_full_models_coverage(self):
        self.assertEqual(unicode(self.plain_text_type), u'Plain text')
        self.assertEqual(self.plain_text_attachment.get_download_url(), '/download/simple-text')
        self.assertEqual(self.plain_text_attachment.get_absolute_url(),
                         self.plain_text_attachment.attachment.url)
        self.assertTrue(self.plain_text_attachment.filename().startswith('simple'))
        self.assertEqual(unicode(self.plain_text_attachment), 'Simple text')

    def test_download_attachment_view(self):
        response = download_attachment(None, 'simple-text')
        self.assertEqual(response['Content-Type'], 'text/plain')
        self.assertEqual(response['Content-Disposition'],
                         'attachment; filename="%s"' % self.plain_text_attachment.filename())
        self.assertEqual(response.content, 'simple text')

        response = download_attachment(None, 'none-type')
        self.assertEqual(response['Content-Type'], 'text/plain')
