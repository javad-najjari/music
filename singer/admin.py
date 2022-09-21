from django.contrib import admin
from .models import Singer



class SingerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_day', 'short_about', 'get_styles')

    def get_styles(self, obj):
        return ', '.join([S.title for S in obj.styles.all()])


admin.site.register(Singer, SingerAdmin)

