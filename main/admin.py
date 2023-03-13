from django.contrib import admin
from django.utils.html import format_html

from .models import Application, News, GAGAGA, Review


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'status')
    list_filter = ('status', 'date')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'date')


@admin.register(GAGAGA)
class GAGAGAAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="160" />'.format(obj.img.url))

    image_tag.short_description = 'Image'
    list_display = ('image_tag',)


admin.site.register(News)
