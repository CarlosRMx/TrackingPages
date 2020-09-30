from django.urls import path
from Clients import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('clients/', views.ClientList.as_view(), name='client_list'),
    path('clients/<int:pk>/', views.ClientDetail.as_view()),
    path('packages/', views.PackageList.as_view(), name='package_list'),
    path('packages/<int:pk>/', views.PackageDetail.as_view()),
    path('administration/', views.AdministratorList.as_view(), name='administration_package'),
    path('administration/<int:pk>/', views.AdministratorDetail.as_view()),
    path('total_w_packages/',views.TotalPackages_warehouse.as_view()),
    path('total_t_packages/',views.TotalPackages_transit.as_view()),
    path('total_d_packages/',views.TotalPackages_delievered.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)