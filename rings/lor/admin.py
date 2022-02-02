from django.contrib import admin
from .models import Favorite, Quote


# Register your models here.
admin.site.register(Favorite)
admin.site.register(Quote)