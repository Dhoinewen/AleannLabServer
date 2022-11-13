from django.contrib import admin

# Register your models here.
from .models import User, Rank

admin.site.register(User)
admin.site.register(Rank)
