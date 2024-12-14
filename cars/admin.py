from django.contrib import admin

from django.contrib import admin
from .models import SliderImage

class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')
    search_fields = ('title',)
    list_editable = ('order',)

admin.site.register(SliderImage, SliderImageAdmin)

