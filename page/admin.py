from django.contrib import admin
from page.models import FreeFireAccount


@admin.register(FreeFireAccount)
class FreeFireAccountModelAdmin(admin.ModelAdmin):
    pass
