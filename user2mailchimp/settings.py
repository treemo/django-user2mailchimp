from django.conf import settings

MAILCHIMP_API_KEY = getattr(settings, 'MAILCHIMP_API_KEY', '')
MAILCHIMP_LIST_NAME = getattr(settings, 'MAILCHIMP_LIST_NAME', '')
MAILCHIMP_ASSOC = getattr(settings, 'MAILCHIMP_ASSOC', {
    # mailchimp name:  user object value
    'FNAME': 'first_name',
    'LNAME': 'last_name',
    'EMAIL': 'email',
})
