from django.contrib import admin

from .models import Record

admin.site.register(Record)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('price', 'amount', 'type')
