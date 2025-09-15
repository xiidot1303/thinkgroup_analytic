from django.urls import path, re_path
from bot.views import botwebhook
from config import BOT_API_TOKEN
from django.conf import settings
from django.conf.urls.static import static
from config import DEBUG
from bot.views.newsletter import NewsletterView
from bot.views.staff import check_staff

urlpatterns = [
    path(BOT_API_TOKEN, botwebhook.BotWebhookView.as_view()),
    path('send-newsletter/', NewsletterView.as_view()),
    path("api/check-staff/<int:user_id>/", check_staff, name="check_staff"),

]

if DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)