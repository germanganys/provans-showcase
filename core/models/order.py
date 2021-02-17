from django.db import models


class Order(models.Model):
    order_time = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=64)
    name = models.CharField(max_length=64)

    STATUS_CHOICES = (
        ('IN_PROCESS', 'Ещё не подтверждён'),
        ('CONFIRMED', 'Подтверждён'),
        ('REJECTED', 'Отклонён'),
        ('FINISHED', 'Завершён'),
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='IN_PROCESS')

    def __str__(self):
        return 'Заказ № {}, на {}, тел: {}'.format(self.id, self.order_time.date(), self.phone_number)

    @staticmethod
    def get_orders_in_process():
        return Order.objects.filter(status='IN_PROCESS')

    @staticmethod
    def get_confirmed_orders():
        return Order.objects.filter(status='CONFIRMED')

    @staticmethod
    def get_finished_or_rejected_orders():
        return Order.objects.filter(status__in=['FINISHED', 'REJECTED'])

    @staticmethod
    def reject_order(order_id):
        order = Order.objects.get(id=order_id)
        order.status = 'REJECTED'
        order.save()

    @staticmethod
    def confirm_order(order_id):
        order = Order.objects.get(id=order_id)
        order.status = 'CONFIRMED'
        order.save()

    @staticmethod
    def finish_order(order_id):
        order = Order.objects.get(id=order_id)
        order.status = 'FINISHED'
        order.save()
