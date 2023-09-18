import logging
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render
from models import Client, Product
from django.http import HttpResponse

# Create your views here.
logger = logging.getLogger(__name__)

def user_orders(request, client_id):
    client = Client.objects.get(pk=client_id)
    return render(request, 'user_orders.html', {'client': client})

def index(request):
    logger.info('Index page accessed successfully!')
    return HttpResponse("welcome to the future!=)")

def client_orders_week(request, client_id):
    end_date = timezone.now()
    start_date = end_date - timedelta(days=7)

    
    client = Client.objects.get(pk=client_id)

    
    products = Product.objects.filter(orderitem__order__client=client, 
                                      orderitem__order__order_date__range=(start_date, end_date)).distinct()

    context = {
        'client': client,
        'products': products,
        'period': 'неделю'
    }

    return render(request, 'client_orders.html', context)

def client_orders_month(request, client_id):
   
    end_date = timezone.now()
    start_date = end_date - timedelta(days=30)  # 30 дней назад

   
    client = Client.objects.get(pk=client_id)

    
    products = Product.objects.filter(orderitem__order__client=client, 
                                      orderitem__order__order_date__range=(start_date, end_date)).distinct()

    context = {
        'client': client,
        'products': products,
        'period': 'месяц'
    }

    return render(request, 'client_orders.html', context)

def client_orders_year(request, client_id):
    
    end_date = timezone.now()
    start_date = end_date - timedelta(days=365) 

    client = Client.objects.get(pk=client_id)

    
    products = Product.objects.filter(orderitem__order__client=client, 
                                      orderitem__order__order_date__range=(start_date, end_date)).distinct()

    context = {
        'client': client,
        'products': products,
        'period': 'год'
    }

    return render(request, 'client_orders.html', context)