from django.utils.translation import ugettext as _
from django.conf.urls import url


from ella_attachments.views import download_attachment
from ella_attachments.utils import slugify

urlpatterns = [
    url(r'^%s/(?P<slug>.*)' % slugify(_('download')), download_attachment, name='ella_attachments-download'),
]
