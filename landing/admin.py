from django.contrib import admin
from .models import *
# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
    # подтягивает из модели Subscriber имена полей и записывает
    list_display = [field.name for field in Subscriber._meta.fields]
    # добавляем фильтр по полю name
    list_filter = ['name']
    # поиск по name и email
    search_fields = ['name', 'email']
    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)