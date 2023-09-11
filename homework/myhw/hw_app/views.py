from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed successfully!')
    return HttpResponse("welcome to the future!=)")


def about(request):
    logger.info('About page accessed successfully!')
    return HttpResponse("About me. My name is Mariia and I'm glad to see you!")
