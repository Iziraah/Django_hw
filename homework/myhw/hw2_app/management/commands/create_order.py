from django.core.management.base import BaseCommand
from hw2_app.models import Client, Product, Order, OrderItem
from django.utils import timezone
from random import randint

class Command(BaseCommand):
    help = 'Создает заказы для пользователей'

    def handle(self, *args, **kwargs):
        
        clients = Client.objects.all()

       
        products = Product.objects.all()

        
        for client in clients:
            order_date = timezone.now()  
            order = Order.objects.create(client=client, total_amount=0, order_date=order_date)

            
            for _ in range(randint(1, 5)):  
                product = products[randint(0, len(products) - 1)]
                quantity = randint(1, 10)  
                OrderItem.objects.create(order=order, product=product, quantity=quantity)

            
            order_items = OrderItem.objects.filter(order=order)
            total_amount = sum(item.product.price * item.quantity for item in order_items)
            order.total_amount = total_amount
            order.save()

            self.stdout.write(self.style.SUCCESS(f'Заказ успешно создан для {client.name} с датой {order_date}'))
