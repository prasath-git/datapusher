from django.shortcuts import render
from .models import Vegetable
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')



def task(request):
    return render(request, 'task.html')


# def dash(request):
#     return render(request, 'dash.html')

# def task(request):
#     vegetables = Vegetable.objects.all().values()
#     return JsonResponse(list(vegetables), safe=False)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer
import requests

# Account CRUD
class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# Destination CRUD
class DestinationListCreateView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

# Get Destinations for a given account
from django.core.exceptions import ValidationError
class AccountDestinationsView(APIView):
    def get(self, request, account_id):
        try:
            # Validate UUID format
            account = Account.objects.get(account_id=account_id)
            destinations = account.destinations.all()
            serializer = DestinationSerializer(destinations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response({"error": "Invalid account_id format"}, status=status.HTTP_400_BAD_REQUEST)

# Data Handler
class DataHandlerView(APIView):
    def post(self, request):
        app_secret_token = request.headers.get('CL-X-TOKEN')
        if not app_secret_token:
            return Response({"error": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            account = Account.objects.get(app_secret_token=app_secret_token)
        except Account.DoesNotExist:
            return Response({"error": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        if not isinstance(data, dict):
            return Response({"error": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)

        destinations = account.destinations.all()
        for destination in destinations:
            headers = destination.headers
            url = destination.url
            method = destination.http_method
            try:
                if method == "GET":
                    response = requests.get(url, params=data, headers=headers)
                elif method == "POST":
                    response = requests.post(url, json=data, headers=headers)
                elif method == "PUT":
                    response = requests.put(url, json=data, headers=headers)
                response.raise_for_status()
            except requests.RequestException as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"success": "Data sent to all destinations"}, status=status.HTTP_200_OK)

