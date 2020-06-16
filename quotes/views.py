from django.views.generic import TemplateView
from rest_framework import viewsets, generics
from .models import Quotes
from .serializers import QuotesSerializer


def random_quotes_id():
    quotes = Quotes.objects.all().order_by('?').first()
    return quotes.id


class HomeView(TemplateView):
    template_name = "home.html"


class QuotesView(viewsets.ModelViewSet):
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer


class RandomQuotesView(viewsets.ModelViewSet):
    serializer_class = QuotesSerializer

    def get_queryset(self):
        return Quotes.objects.all().filter(id=random_quotes_id())
