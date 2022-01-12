from django.contrib import admin
from .models import Booking, UserProfile

# Register your models here.
admin.site.site_header = 'Pauls Kitchen Dashboard'

admin.site.register(Booking)
admin.site.register(UserProfile)

