from django.contrib import admin
from .models import Application, News, GAGAGA, Review


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'status')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'date')


admin.site.register(News)
admin.site.register(GAGAGA)
