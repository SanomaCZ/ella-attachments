from ella.utils.settings import Settings

CUSTOM_SUBDIR = ''
UPLOAD_TO = CUSTOM_SUBDIR and 'attachments/%s/%%Y/%%m/%%d' % CUSTOM_SUBDIR or 'attachments/%Y/%m/%d'

attachments_settings = Settings('ella_attachments.conf', 'ATTACHMENTS')
