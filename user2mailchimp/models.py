import logging
import mailchimp

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .settings import MAILCHIMP_ASSOC, MAILCHIMP_API_KEY,MAILCHIMP_LIST_NAME


logger = logging.getLogger(__name__)


@receiver(pre_save)
def user_pre_save(sender, instance, raw, using, update_fields, **kwargs):
    """When user change its email, we want to update our mailing list"""

    # is user ? (or subclasses)
    if not isinstance(instance, AbstractUser):
        return

    try:
        update_member(instance)

    # on production, this app must not block the user
    except Exception as e:
        logger.error(e)
        if settings.DEBUG:
            raise
        raise


def update_member(user):
    """User change infos, we want to update our mailing list

    :param user: Django User model
    """
    if not MAILCHIMP_API_KEY:
        raise ValueError('MAILCHIMP_API_KEY not set!')

    if not MAILCHIMP_LIST_NAME:
        raise ValueError('MAILCHIMP_LIST_NAME not set!')

    # Has old value ? (on update user)
    old_user = None
    if user.pk:
        # we retrieve the old user object
        old_user = user.__class__.objects.get(pk=user.pk)

        # Mailchip value not changed, we quit.
        if not [True for k in MAILCHIMP_ASSOC.values() if
                getattr(old_user, k) != getattr(user, k)]:
            return

    # Get user infos
    infos = {m: getattr(user, u) for m, u in MAILCHIMP_ASSOC.items()}

    # email required for Mailchimp (user created by django admin has not email)
    if not infos.get('EMAIL'):
        logger.warning('User %s has no email' % user)
        return

    # Get api object and mailing list id
    api = mailchimp.Mailchimp(MAILCHIMP_API_KEY)
    list_id = api.lists.list({'name': MAILCHIMP_LIST_NAME})['data'][0]['id']

    # send to mailchip
    email = {'email': getattr(old_user, 'email') or user.email}
    api.lists.subscribe(list_id, email, infos, double_optin=False,
                        update_existing=True)
