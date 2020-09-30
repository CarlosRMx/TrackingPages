from django.db import models
from django.core.validators import RegexValidator

# Create your models here



class Package(models.Model):
    """Model definition for Package."""

    name_sender= models.CharField(max_length=30, null= False)
    destination_address= models.CharField(max_length=30, null=False)
    date_received= models.DateTimeField(auto_now_add=True)
    State=[
        ('In_Warehouse','Warehouse'),
        ('In_Transit','Tranist'),
        ('Delivered','Delivered')

    ]
    state_package= models.CharField(choices=State, max_length=20,default='In_Warehouse')

    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Package."""

        verbose_name = 'Package'
        verbose_name_plural = 'Packages'
        ordering=['date_received']

    def __str__(self):
        """Unicode representation of Package."""
        return self.name_sender


class Client(models.Model):
    """Model definition for Client."""

    first_name= models.CharField(max_length=30,null=False)
    last_name= models.CharField(max_length=30, null=False)
    doc_identification=models.CharField(max_length=20,blank=False)
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number=models.CharField(validators=[phone_regex], max_length=17,blank=False)
    

    class Meta:
        """Meta definition for Client."""

        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


    def __str__(self):
        """Unicode representation of Client."""
        return self.first_name +" "+ self.last_name

class Administrator(models.Model):
    """Model definition for Administrator."""

    package_guide= models.CharField(max_length=8, null=False)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    package= models.ForeignKey(Package,on_delete=models.CASCADE)
    creation_date=models.DateField(auto_now_add=True)
    ubication= models.CharField(max_length=30, blank=True)

    class Meta:
        """Meta definition for Administrator."""

        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrators'
        ordering=['creation_date']


    def __str__(self):
        """Unicode representation of Administrator."""
        return self.package_guide +" - "+ str(self.creation_date)
