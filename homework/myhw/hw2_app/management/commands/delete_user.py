from django.core.management.base import BaseCommand
from hw2_app.models import Client  # Используйте имя вашего приложения, здесь это 'hw2_app'

class Command(BaseCommand):
    help = 'Удалить клиента по ID'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='ID клиента')

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']

        try:
            client = Client.objects.get(pk=client_id)
            client.delete()
            self.stdout.write(self.style.SUCCESS(f'Клиент с ID {client_id} успешно удален.'))
        except Client.DoesNotExist:
            self.stderr.write(self.style.ERROR(f'Клиент с ID {client_id} не найден.'))