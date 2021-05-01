from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class UserProfile(models.Model):
    """
    A user profile model for everthing
  
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='Nick')
    abaout = models.TextField(verbose_name='Hakkında',max_length=500, blank=True, null=True)
    profileimage = models.ImageField(verbose_name='Profil Resmi',blank=True, null=True)

    
    # default_phone_number = models.CharField(max_length=20, null=True, blank=True , verbose_name='Varsayılan Telefon NUmarası')
    # default_street_address1 = models.CharField(max_length=80, null=True, blank=True,verbose_name='Varsayılan Adres')
    # # default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    # default_town_or_city = models.CharField(max_length=40, null=True, blank=True, verbose_name='Varsayılan Şehir')
    # default_county = models.CharField(max_length=80, null=True, blank=True, verbose_name='Varsayılan İlçe')
    # default_postcode = models.CharField(max_length=20, null=True, blank=True ,verbose_name='Varsayılan Posta Kodu')
    # # default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username
