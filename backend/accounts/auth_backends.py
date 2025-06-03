from django.contrib.auth.backends import BaseBackend

from .models import CustomUser


class PhoneAuthBackend(BaseBackend):
    def authenticate(self, request, phone=None, password=None):
        try:
            user = CustomUser.objects.get(phone=phone)
            if user.check_password(password):
                return user
            return None
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None