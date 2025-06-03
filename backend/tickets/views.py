# Create your views here.
import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import TrainTicket


class TicketListView(View):
    """获取所有车票信息"""
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request):
        tickets = TrainTicket.objects.all()
        data = [{
            'id': t.id,
            'train_number': t.train_number,
            'departure': t.departure,
            'destination': t.destination,
            'departure_time': t.departure_time.strftime('%Y-%m-%d %H:%M'),
            'seat_type': t.seat_type,
            'price': str(t.price),
            'available_seats': t.available_seats
        } for t in tickets]
        return JsonResponse(data, safe=False)


class PurchaseTicketView(View):
    """购票接口"""
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request):
        print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
        if not request.user.is_authenticated:
            return JsonResponse({'error': '请先登录'}, status=401)

        data = json.loads(request.body)
        ticket_id = data.get('ticket_id')

        try:
            ticket = TrainTicket.objects.get(id=ticket_id)
        except TrainTicket.DoesNotExist:
            return JsonResponse({'error': '车票不存在'}, status=404)

        if ticket.available_seats <= 0:
            return JsonResponse({'error': '已无余票'}, status=400)

        # 模拟购票逻辑
        ticket.available_seats -= 1
        ticket.owner = request.user  # 绑定用户
        ticket.save()

        return JsonResponse({
            'message': '购票成功',
            'remaining_seats': ticket.available_seats
        })


class BookingView(View):
    """<UNK>"""
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request):
        print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
        if not request.user.is_authenticated:
            return JsonResponse({'error': '用户未登录'}, status=401)
        data = json.loads(request.body)
        ticket_id = data.get('ticket_id')
        try:
            ticket = TrainTicket.objects.get(id=ticket_id)
        except TrainTicket.DoesNotExist:
            return JsonResponse({'error': '<UNK>'}, status=404)
        if ticket.available_seats <= 0:
            return JsonResponse({'error': '<UNK>'}, status=400)
        ticket.available_seats -= 1
        ticket.owner = request.user
        ticket.save()
        return JsonResponse({
            'message': '<UNK>',
            'remaining_seats': ticket.available_seats
        })