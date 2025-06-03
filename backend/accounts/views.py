# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import CustomUser


class RegisterView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request):
        data = json.loads(request.body)
        phone = data.get('phone')
        password = data.get('password')
        name = data.get('name')
        id_card = data.get('id_card')

        if CustomUser.objects.filter(phone=phone).exists():
            return JsonResponse({'error': '手机号已注册'}, status=400)

        user = CustomUser.objects.create_user(
            username=phone,
            phone=phone,
            password=password,
            name=name,
            id_card=id_card
        )
        return JsonResponse({'message': '注册成功'})


from django.views import View
from django.http import JsonResponse
import json


from django.contrib.auth import authenticate, login

class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        phone = data.get('phone')
        password = data.get('password')

        # 使用 Django 的 authenticate() 触发所有认证后端
        user = authenticate(request, phone=phone, password=password)

        if user:
            login(request, user)  # 设置 Session 和 Cookie
            return JsonResponse({'message': '登录成功', 'name': user.name})
        return JsonResponse({'error': '手机号或密码错误'}, status=400)

