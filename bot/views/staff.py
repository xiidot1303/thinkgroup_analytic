# app/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bot.models import Staff

@api_view(["GET"])
def check_staff(request, user_id):
    try:
        staff = Staff.objects.get(user_id=user_id)
        return Response({"id": staff.id, "name": staff.name})
    except Staff.DoesNotExist:
        return Response({"error": "Staff not found"}, status=status.HTTP_404_NOT_FOUND)
