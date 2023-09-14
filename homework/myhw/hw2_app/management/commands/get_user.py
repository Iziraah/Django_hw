from django.core.management.base import BaseCommand
from hw2_app.models import Client  # Используйте имя вашего приложения, здесь это 'hw2_app'

class Command(BaseCommand):
    help = 'Получить данные клиента по ID'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='ID клиента')

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']

        try:
            client = Client.objects.get(pk=client_id)
            self.stdout.write(f'ID: {client.id}')
            self.stdout.write(f'Имя: {client.name}')
            self.stdout.write(f'Email: {client.email}')
            self.stdout.write(f'Номер телефона: {client.phone_number}')
            self.stdout.write(f'Адрес: {client.address}')
        except Client.DoesNotExist:
            self.stderr.write(self.style.ERROR(f'Клиент с ID {client_id} не найден.'))