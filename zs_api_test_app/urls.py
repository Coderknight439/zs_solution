from django.urls import include, path, re_path
from . import views

urlpatterns = [
                path('get_countries/', views.get_all_countries),
                path('get_state_by_country/<int:country_id>/', views.get_states_by_country),
                path('get_address_by_state/<int:state_id>/', views.get_address_by_state),
                path('get_detail_address/<int:address_id>/', views.get_detail_address),
]