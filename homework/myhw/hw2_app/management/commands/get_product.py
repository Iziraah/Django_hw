from django.core.management.base import BaseCommand
from hw2_app.models import Product  

class Command(BaseCommand):
    help = 'Получить информацию о товаре по ID'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help='ID товара')

    def handle(self, *args, **kwargs):
        product_id = kwargs['product_id']

        try:
            product = Product.objects.get(pk=product_id)
            self.stdout.write(f'ID товара: {product.id}')
            self.stdout.write(f'Название: {product.name}')
            self.stdout.write(f'Описание: {product.description}')
            self.stdout.write(f'Цена: {product.price}')
            self.stdout.write(f'Количество: {product.quantity}')
        except Product.DoesNotExist:
            self.stderr.write(self.style.ERROR(f'Товар с ID {product_id} не найден.'))