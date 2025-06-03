from django.db import models

from accounts.models import CustomUser  # 引用自定义用户模型


# Create your models here.

class TrainTicket(models.Model):
    train_number = models.CharField(max_length=10, verbose_name='车次')  # G123/K456等
    departure = models.CharField(max_length=50, verbose_name='出发地')
    destination = models.CharField(max_length=50, verbose_name='目的地')
    departure_time = models.DateTimeField(verbose_name='出发时间')
    seat_type = models.CharField(max_length=20, choices=[
        ('二等座', '二等座'),
        ('一等座', '一等座'),
        ('商务座', '商务座')
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='票价')
    available_seats = models.PositiveIntegerField(default=100, verbose_name='余票')  # 模拟库存
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)  # 所属用户

    def __str__(self):
        return f"{self.train_number} {self.departure}→{self.destination}"
