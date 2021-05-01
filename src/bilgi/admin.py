from django.contrib import admin
from .models import İnformationModel,AnswerinlineModel
# Register your models here.

# admin.site.register(İnformationModel)



class AnswerinlineModelAdmin(admin.TabularInline):
    model = AnswerinlineModel
    extra = 0
    # readonly_fields = ('AnswerinlineModel',)


class İnformationModelAdmin(admin.ModelAdmin):

    inlines = (AnswerinlineModelAdmin,)

    fields = ('title','author','rating','created_date', 'intro')

    readonly_fields = ('rating','created_date')

    list_display = ('title', 'rating', 'author',)

    list_filter = ('created_date', 'rating',)

    ordering = ('-created_date',)


admin.site.register(İnformationModel, İnformationModelAdmin)