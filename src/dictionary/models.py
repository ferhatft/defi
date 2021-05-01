from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from profiles.models import UserProfile
from taggit.managers import TaggableManager
from vote.models import VoteModel

import re

# Create your models here.

"""
    VoteModel
    - Add field num_vote_down to dictionarymodel
    - Add field num_vote_up to dictionarymodel
    - Add field vote_score to dictionarymodel

"""

class DictionaryModel(VoteModel,models.Model):
    title                   = models.CharField(unique=True,max_length=500,verbose_name = "Ana Başlık ", blank=True)
    slug                    = models.SlugField(blank=True, null=True,verbose_name='uzantı')
    rating                  = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True,verbose_name="Öne çıkarma")
    author                  = models.ForeignKey(UserProfile, on_delete=models.CASCADE,verbose_name='Başlık Sahibi')
    created_date            = models.DateTimeField(auto_now_add=True,null=True,verbose_name="Oluşturulma Tarihi")
    main_context            = models.TextField( verbose_name = "Giriş Paragrafı  Ekleyin" , blank=True, null=True )
    tags                    = TaggableManager()
    
    def __str__(self):
        return '%s %s' % (self.title, self.id)

    
    def save(self, *args, **kwargs):
        # value  = self.title
        # re.sub(r'[^\w\s-]', '', value.lower()).strip()
        # self.title = self.title.lower()
        # self.title = re.sub(r'[^\w\s-]', '', self.title.lower()).strip()

        title =  slugify(self.title)
        if self.slug == None:
            self.slug = title

        return super(DictionaryModel, self).save(*args, **kwargs)

        
    def get_absolute_url(self):
        try:
            if self.slug:
                return "/dictionary/detail/{str}/".format(str=self.slug)
        except:
            return "/dictionary/detail/{str}/".format(str=self.title.lower().replace('-',' '))

        # return "/{str}/".format(str=self.title.lower().replace('-',' '))

    def num_comment(self):
        num_comment = AnswerinlineModel.objects.filter(dictionary=self).count()
        return num_submissions

        
    class Meta:
        ordering = ['title']
        verbose_name = 'Sözlük yazısı'
        verbose_name_plural = 'Sözlük Yazıları'
        
    @property
    def comment_count(self):
        return AnswerinlineModel.objects.filter(dictionary=self).count()




class AnswerinlineModel(models.Model):
    dictionary              = models.ForeignKey(DictionaryModel, related_name='dictionaryanswers', on_delete=models.CASCADE,blank=True, null=True)
    rating                  = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True,verbose_name="Öne çıkarma")
    author                  = models.ForeignKey(UserProfile, on_delete=models.CASCADE,verbose_name='Görüş Sahibi')
    created_date            = models.DateTimeField(auto_now_add=True,null=True,verbose_name="Oluşturulma Tarihi")
    main_context            = models.TextField(blank=True, null=True )

    
    def __str__(self):
        return '%s %s' % (self.author, self.id)


    
    class Meta:
        ordering = ['created_date']
        verbose_name = 'Cevap'
        verbose_name_plural = 'Cevaplar'





STATUS = (
    ('beklemede', 'Beklemede'),
    ('olumlu', 'Olumlu'),
    ('olumsuz', 'Olumsuz'),
)


class ReporModel(models.Model):
    dictionary              = models.ForeignKey(DictionaryModel, related_name='dictionaryreported', on_delete=models.CASCADE,blank=True, null=True)
    author                  = models.ForeignKey(UserProfile, on_delete=models.CASCADE,verbose_name='Görüş Sahibi')
    created_date            = models.DateTimeField(auto_now_add=True,null=True,verbose_name="Oluşturulma Tarihi")
    status                  = models.CharField(max_length=50, choices=STATUS, default='beklemede',verbose_name='Durum')
    main_context            = models.TextField(null=True)

    
    def __str__(self):

        date = self.created_date.strftime('%b, %Y')
        return '%s tarihinde %s tarafından' % ( date,self.author  )


    class Meta:
        ordering = ['created_date']
        verbose_name = 'Şikayet'
        verbose_name_plural = 'Şikayetler'