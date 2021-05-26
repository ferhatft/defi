from django.contrib import admin
from .models import  NewsModel, AnswerinlineModel
# Register your models here.

# admin.site.register(NewsModel)



class AnswerinlineModelAdmin(admin.TabularInline):
    model = AnswerinlineModel
    extra = 0
    # readonly_fields = ('AnswerinlineModel',)


class NewsModelAdmin(admin.ModelAdmin):

    inlines = (AnswerinlineModelAdmin,)

    fields = ('title', 'tags','slug','author','backimage','rating','created_date' , 'intro','anahaber',)

    readonly_fields = ('rating','created_date')

    list_display = ('title', 'rating', 'author',)

    list_filter = ('created_date', 'rating',)

    ordering = ('-created_date',)


admin.site.register(NewsModel, NewsModelAdmin)