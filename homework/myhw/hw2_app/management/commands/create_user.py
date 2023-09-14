from django.core.management.base import BaseCommand
from hw2_app.models import Client 

class Command(BaseCommand):
    help = 'Создать нового клиента'

    def handle(self, *args, **kwargs):
        name = input('Введите имя клиента: ')
        email = input('Введите адрес электронной почты клиента: ')
        phone_number = input('Введите номер телефона клиента: ')
        address = input('Введите адрес клиента: ')

        try:
            client = Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
            self.stdout.write(self.style.SUCCESS(f'Клиент "{client.name}" успешно создан!'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Произошла ошибка: {str(e)}'))