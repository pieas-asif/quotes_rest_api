from django.urls import path, include
from rest_framework import routers
from .views import HomeView, QuotesView, RandomQuotesView

router = routers.DefaultRouter()
router.register('quotes', QuotesView)
router.register('randomQuotes', RandomQuotesView, 'random')

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('api/', include(router.urls)),
]
