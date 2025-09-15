from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Expense
from app.services.bot_service import send_newsletter_api


@receiver(post_save, sender=Expense)
def set_expense_date(sender, instance, created, **kwargs):
    # if created and not instance.date:
    if not instance.date:
        instance.date = timezone.now().date()
        instance.save(update_fields=["date"])

        # send newsletter to user about new expense
        send_newsletter_api.delay(
            bot_user_id=instance.staff.user_id,
            text = f"✅ Yangi xarajat yaratildi\n\n" \
                f"📍 Filial: {instance.branch.name}\n" \
                f"📂 Kategoriya: {instance.category.name}\n" \
                f"👤 Xodim: {instance.staff.name}\n" \
                f"💵 Summasi: {instance.amount} so‘m\n" \
                f"📝 Izoh: {instance.description if instance.description else 'Izoh berilmagan'}\n" \
                f"📅 Sana: {instance.date}\n"
        )
