from rest_framework import serializers
from Clients.models import Client 
from Clients.models import Package
from Clients.models import Administrator


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model=Client
        fields=['id','first_name','last_name','doc_identification','phone_number']


class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model=Package
        fields=['id','name_sender','destination_address','state_package',]

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Administrator
        fields=['id','package_guide','client','package','ubication']
