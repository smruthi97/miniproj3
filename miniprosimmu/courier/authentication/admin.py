from django.contrib import admin

# Register your models here.

from .models import Register
from .models import Staff_Detail

admin.site.register(Register)
admin.site.register(Staff_Detail)