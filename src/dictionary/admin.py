from django.contrib import admin

from dictionary.models import DictionaryModel,AnswerinlineModel,ReporModel
# Register your models here.



class AnswerinlineModelAdmin(admin.TabularInline):
    model = AnswerinlineModel
    extra = 0
    # readonly_fields = ('AnswerinlineModel',)


class ReportinlineModelAdmin(admin.TabularInline):
    model = ReporModel
    extra = 0
    # readonly_fields = ('AnswerinlineModel',)


class DictionaryModelAdmin(admin.ModelAdmin):

    inlines = (AnswerinlineModelAdmin,ReportinlineModelAdmin)

    readonly_fields = ('rating',)
    
    # fields = ('title','author','rating','created_date', 'summary' , 'intro')  düzenle

    list_display = ('title', 'rating', 'author',)

    list_filter = ('created_date', 'rating',)

    ordering = ('-created_date',)


admin.site.register(DictionaryModel, DictionaryModelAdmin)




class ReportModelAdmin(admin.ModelAdmin):

    readonly_fields = ('main_context','author',)
    
    # fields = ('title','author','rating','created_date', 'summary' , 'intro')  düzenle

    list_display = ( 'author', 'created_date','status', 'dictionary',)

    list_filter = ('status', 'created_date',)

    ordering = ('-created_date',)

admin.site.register(ReporModel,ReportModelAdmin)