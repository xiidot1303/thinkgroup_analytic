from django import template
from app.utils import *
from bot.models import Staff

register = template.Library()

@register.filter()
def index(l, i):
    return l[i]

@register.filter()
def is_even_number(number):
    if number != 0 and number%2 == 0:
        return True
    else:
        return False

@register.filter()
def length_form(form):
    return len(form.fields)


@register.simple_tag
def check_staff(telegram_user_id):
    """
    Check if Telegram user_id exists in Staff model.
    Returns staff object or None.
    """
    try:
        return Staff.objects.get(user_id=telegram_user_id)
    except Staff.DoesNotExist:
        return None