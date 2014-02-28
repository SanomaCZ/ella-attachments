try:
    from django.utils.text import slugify
except ImportError:
    from django.template.defaultfilters import slugify
