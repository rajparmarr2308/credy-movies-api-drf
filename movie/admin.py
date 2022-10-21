from django.contrib import admin

# Register your models here.
from .models import Collection,Movie,MovieCollection

admin.site.register(Collection)
admin.site.register(Movie)
admin.site.register(MovieCollection)
