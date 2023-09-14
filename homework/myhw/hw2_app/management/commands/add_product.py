from django.core.management.base import BaseCommand
from hw2_app.models import Product  

class Command(BaseCommand):
    help = 'Добавить новый товар'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Название товара')
        parser.add_argument('description', type=str, help='Описание товара')
        parser.add_argument('price', type=float, help='Цена товара')
        parser.add_argument('quantity', type=int, help='Количество товара')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        description = kwargs['description']
        price = kwargs['price']
        quantity = kwargs['quantity']

        try:
            product = Product.objects.create(name=name, description=description, price=price, quantity=quantity)
            self.stdout.write(self.style.SUCCESS(f'Товар "{product.name}" успешно добавлен!'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Произошла ошибка: {str(e)}'))