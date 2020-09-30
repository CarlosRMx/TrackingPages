
from django.shortcuts import render
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Count




#models ----------------------------------
from Clients.models import Client 
from Clients.serializers import ClientSerializer

from Clients.models import Package
from Clients.serializers import PackageSerializer

from Clients.models import Administrator
from Clients.serializers import AdministratorSerializer 
#--------------------------

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

#----------------------------------
class PackageList(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class PackageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

#--------------------------- Administrator
class AdministratorList(generics.ListCreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class AdministratorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

#Reports

class TotalPackages_warehouse(generics.ListAPIView):
    serializer_class=PackageSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    
    def get_queryset(self):
        return Package.objects.filter(state_package="In_Warehouse").aggregate(Count('state_package'))

class TotalPackages_transit(generics.ListAPIView):
    serializer_class=PackageSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    
    def get_queryset(self):
        return Package.objects.filter(state_package="In_Transit").aggregate(Count('state_package'))

class TotalPackages_delievered(generics.ListAPIView):
    serializer_class=PackageSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    
    def get_queryset(self):
        return Package.objects.filter(state_package="Delivered").aggregate(Count('state_package'))

#----------------- Login Administrator
class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('client:administration_package')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,*kwargs)

    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

class Logout(APIView):
    def get(self,request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)