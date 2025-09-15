from rest_framework import serializers
from board.models import Board

class MarketSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Board       
        fields = '__all__'          