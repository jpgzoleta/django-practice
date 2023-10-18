from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Item
from .serializers import ItemSerializer
from rest_framework.decorators import api_view


# Create your views here.
def home(request):
    return HttpResponse("Hello World")


@api_view(["GET"])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return JsonResponse({"items": serializer.data})
