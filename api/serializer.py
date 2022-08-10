from rest_framework import serializers
from api.models import Quote


class QuotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'
