from django.shortcuts import render
from rest_framework.response import Response
from board.models import Board
from rest_framework.views import APIView
from .serializers import MarketSerializer

class BoardListAPI(APIView):
    def get(self, request):
        queryset = Board.objects.all()
        print(queryset)
        serializer = MarketSerializer(queryset, many=True)
        return Response(serializer.data)