from django.contrib import admin

from .models import Resource
from .models import Upvotes

admin.site.register(Resource)
admin.site.register(Upvotes)