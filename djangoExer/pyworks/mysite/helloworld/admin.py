from django.contrib import admin
from .models import AddWord
# Register your models here.
class AddWordAdmin(admin.ModelAdmin):
    list_display=('id','word_text','date_time')

admin.site.register(AddWord,AddWordAdmin)