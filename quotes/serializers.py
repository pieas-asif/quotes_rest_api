from rest_framework import serializers
from .models import Quotes


class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = ('id', 'name', 'date_added', 'body')
