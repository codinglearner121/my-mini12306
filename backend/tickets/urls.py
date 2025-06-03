from django.urls import path

from .views import TicketListView, BookingView

urlpatterns = [
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
    path('book/', BookingView.as_view(), name='book-ticket'),
]