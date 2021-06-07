from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .filters import CountryFilter, StateFilter, AddressFilter
from django_filters.utils import translate_validation
from .serializers import *
from .models import Country, State, Address

# Create your views here.


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_all_countries(request):
    filter_set = CountryFilter(request.GET, queryset=Country.objects.all())
    if not filter_set.is_valid():
        raise translate_validation(filter_set.errors)
    serializer = CountrySerializer(filter_set.qs, many=True)
    return JsonResponse({'countries': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_states_by_country(request, country_id):
    filter_set = StateFilter(request.GET, queryset=State.objects.filter(country__pk=country_id))
    if not filter_set.is_valid():
        raise translate_validation(filter_set.errors)
    serializer = StateSerializer(filter_set.qs, many=True)
    return JsonResponse({'states': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_address_by_state(request, state_id):
    filter_set = AddressFilter(request.GET, queryset=Address.objects.filter(state__pk=state_id))
    if not filter_set.is_valid():
        raise translate_validation(filter_set.errors)
    serializer = AddressSerializer(filter_set.qs, many=True)
    return JsonResponse({'addresses': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_detail_address(request, address_id):
    address_model = Address.objects.get(pk=int(address_id))
    if not address_model:
        raise Address.DoesNotExist
    address_data = {
        'name': address_model.name,
        'road_no': address_model.road_no,
        'house_no': address_model.house_no,
        'state': address_model.state.name,
        'country': address_model.state.country.name,
    }
    return JsonResponse({'address': address_data}, safe=False, status=status.HTTP_200_OK)


