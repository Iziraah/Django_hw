from django.core.management.base import BaseCommand
from hw2_app.models import Product  

class Command(BaseCommand):
    help = 'Удалить товар по ID'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help='ID товара')

    def handle(self, *args, **kwargs):
        product_id = kwargs['product_id']

        try:
            product = Product.objects.get(pk=product_id)
            product.delete()
            self.stdout.write(self.style.SUCCESS(f'Товар с ID {product_id} успешно удален.'))
        except Product.DoesNotExist:
            self.stderr.write(self.style.ERROR(f'Товар с ID {product_id} не найден.'))