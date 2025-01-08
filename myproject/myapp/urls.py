from django.urls import path
from . import views
# from django.urls import path
from .views import (
    AccountListCreateView,
    AccountRetrieveUpdateDeleteView,
    DestinationListCreateView,
    DestinationRetrieveUpdateDeleteView,
    AccountDestinationsView,
    DataHandlerView,
)


urlpatterns = [
    path('home/', views.home),
    path('task/', views.task), 

    # Account URLs
    path('accounts/', AccountListCreateView.as_view(), name='account-list-create'),
    path('accounts/<int:pk>/', AccountRetrieveUpdateDeleteView.as_view(), name='account-detail'),
    
    # Destination URLs
    path('destinations/', DestinationListCreateView.as_view(), name='destination-list-create'),
    path('destinations/<int:pk>/', DestinationRetrieveUpdateDeleteView.as_view(), name='destination-detail'),

    # Get destinations for account
    path('accounts/<uuid:account_id>/destinations/', AccountDestinationsView.as_view(), name='account-destinations'),

    # Data Handler URL
    path('server/incoming_data/', DataHandlerView.as_view(), name='incoming-data'),
]

