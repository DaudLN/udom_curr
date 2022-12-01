# from django_static_jquery_ui
from django.contrib import admin
from .models import Program
# Register your models here.


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Media:
        css = {
            "all": ['jquery-ui/jquery-ui.min.css',
                    'jquery-ui/themes/ui-lightness/theme.css'
                    ]
        }
        js = [
            'jquery-ui/external/jquery/jquery.js',
            'jquery-ui/jquery-ui.min.js',
            'jquery-ui/i18n/datepicker-zh-Hans.js',
        ]
