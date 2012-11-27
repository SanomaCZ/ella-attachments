from django.test import TestCase
from django.template import Template, Context

from ella_attachments.models import Type, Attachment


class TestAttachmentWithType(TestCase):
    def setUp(self):
        self.type = Type.objects.create(name='Plain text', slug='plain-text', mimetype='text/plain')
        self.attachment = Attachment.objects.create(name='Text', slug='text', type=self.type)

    def test_box_rendering(self):
        t = Template('{% box simple for attachment %}{% endbox %}')
        c = Context({'attachment': self.attachment})
        rendered = t.render(c)
        self.assertEqual(rendered, 'Text\n')
