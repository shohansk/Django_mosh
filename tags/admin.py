from django.contrib import admin

# Register your models here.
from .models import Tag,TaggedItem


admin.site.register(Tag)
admin.site.register(TaggedItem)