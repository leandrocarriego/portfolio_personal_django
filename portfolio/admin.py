from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, BooleanFieldListFilter
from django.utils.html import format_html

from .models import Technology, Category, Project, ProjectImage, Experience, Contact, File, Description


admin.site.register(Description)

admin.site.register(Category)


@admin.register(Technology)
class TechnologyAdmin(ModelAdmin):
    list_display = ('name', 'priority', 'icono', 'visible')
    list_filter = [
        ("visible", BooleanFieldListFilter),
    ]
    search_fields = ('name',)
    ordering = ['priority']

    def icono(self, obj):
        if obj.icon:
            return format_html('<img src={} width="30" height="auto" />', obj.icon.url)
        else: 
            return "No hay imagen"

class ProjectImageInline(TabularInline):
    model = ProjectImage


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ('title', 'category', 'client')
    list_filter = [
        'category',
    ]
    inlines = [ProjectImageInline]


@admin.register(Experience)
class ExperienciaAdmin(ModelAdmin):
    list_display = ('position', 'employer', 'start', 'end')


@admin.register(Contact)
class ContactoAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date')


@admin.register(File)
class CVAdmin(ModelAdmin):
    list_display = ('name', 'uploaded')
