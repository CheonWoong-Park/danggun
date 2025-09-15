from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Board
from .serializers import BoardSerializer
from django.utils import timezone

# GET /?inbase=true or false
@api_view(['GET'])
def board_list(request):
    in_base = request.query_params.get('inbase', 'false').lower() == 'true'
    
    if in_base:
        allowed_regions = ["공작사", "작근단", "작통단", "31 전대"]
        boards = Board.objects.filter(region__in=allowed_regions)
    else:
        boards = Board.objects.all()
    
    # Serialize the boards
    serializer = BoardSerializer(boards, many=True)
    
    # Extract the desired fields from the serialized data
    filtered_data = [
        {
            "id": board["id"],
            "name": board["name"],
            "price": board["price"],
            "serial": board["serial"],
            "region": board["region"],
            "seller": board["seller"],
        }
        for board in serializer.data
    ]
    
    return Response({"status": "success", "data": filtered_data})


# GET /board/{articles_id}
@api_view(['GET'])
def board_detail(request, articles_id):
    try:
        board = Board.objects.get(id=articles_id)
        serializer = BoardSerializer(board)
        return Response({"status": "success", "data": serializer.data})
    except Board.DoesNotExist:
        return Response({"status": "error", "message": "Board not found"}, status=404)

# GET /selling
@api_view(['GET'])
def user_selling(request):
    boards = Board.objects.filter(seller='일병 박천웅')  # Always fetch where seller is 박천웅
    serializer = BoardSerializer(boards, many=True)
    
    filtered_data = [
        {
            "id": board["id"],
            "name": board["name"],
            "price": board["price"],
            "serial": board["serial"],
            "date": board["date"],
        }
        for board in serializer.data
    ]
    
    return Response({"status": "success", "data": filtered_data})

# POST /selling/add
@api_view(['POST'])
def add_board(request):
    data = request.data.copy()
    data['date'] = timezone.now()  # Automatically set the time of creation
    serializer = BoardSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    return Response({"status": "error", "message": serializer.errors}, status=400)


# GET /board/delete/{id}
@api_view(['GET'])
def delete_board(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    board.delete()  # Delete the board entry
    return Response({"status": "success", "message": "Board deleted successfully."})