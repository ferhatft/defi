from django.db import models

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from profiles.models import UserProfile
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class NewsModel(models.Model):
    title                   = models.CharField(unique=True,max_length=500,verbose_name = "Haber Başlığı ", blank=True)
    slug                    = models.SlugField(blank=True, null=True,verbose_name='uzantı')
    tags                    = TaggableManager()
    anahaber                = models.BooleanField(default=False,verbose_name='ana haber')
    sliderhaber             = models.BooleanField(default=False,verbose_name='slider ekle')
    rating                  = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True,verbose_name="Öne çıkarma")
    author                  = models.ForeignKey(UserProfile, on_delete=models.CASCADE,verbose_name='Haber Sahibi')
    created_date            = models.DateTimeField(auto_now_add=True,null=True,verbose_name="Oluşturulma Tarihi")
    backimage               = models.ImageField(null=True,verbose_name='ana resim "1920-1100"')
    intro                   = RichTextUploadingField(blank=True, null=True, verbose_name='içerik')
    summary                 = models.TextField(blank=True, null=True,)


    def __str__(self):
        return '%s %s' % (self.title, self.id)

    
    def save(self, *args, **kwargs):
        title =  slugify(self.title)
        summary   =  self.intro[3:86]
        
        self.slug = title

        self.summary = summary

        return super(NewsModel, self).save(*args, **kwargs)

        
    def get_absolute_url(self):
        try:
            if self.slug:
                return "/news/read/{str}/".format(str=self.slug)
        except:
            return "/news/read/{str}/".format(str=self.title.lower().replace('-',' '))

        # return "/{str}/".format(str=self.title.lower().replace('-',' '))

    def get_update_url(self):
        try:
            if self.slug:
                return "/news/update/{str}/".format(str=self.slug)
        except:
            return "/news/update/{str}/".format(str=self.title.lower().replace('-',' '))

        # return "/{str}/".format(str=self.title.lower().replace('-',' '))
    def get_delete_url(self):
        try:
            if self.slug:
                return "/news/delete/{str}/".format(str=self.slug)
        except:
            return "/news/delete/{str}/".format(str=self.title.lower().replace('-',' '))

        # return "/{str}/".format(str=self.title.lower().replace('-',' '))

        
    class Meta:
        ordering = ['title']
        verbose_name = 'Haber yazısı'
        verbose_name_plural = 'Haber Yazıları'


    def num_comment(self):
        num_comment = AnswerinlineModel.objects.filter(information=self).count()
        return num_submissions

        
    @property
    def comment_count(self):
        return AnswerinlineModel.objects.filter(information=self).count()



class AnswerinlineModel(models.Model):
    news             = models.ForeignKey(NewsModel, related_name='NewsModelAnswer', on_delete=models.CASCADE,blank=True, null=True)
    rating                  = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True,verbose_name="Öne çıkarma")
    author                  = models.ForeignKey(UserProfile, on_delete=models.CASCADE,verbose_name='Görüş Sahibi',related_name='comment_owner')
    created_date            = models.DateTimeField(auto_now_add=True,null=True,verbose_name="Oluşturulma Tarihi")
    main_context            = models.TextField(  blank=True, null=True )

    
    def __str__(self):
        return '%s %s' % (self.author, self.id)

    class Meta:
        ordering = ['created_date']
        verbose_name = 'Cevap'
        verbose_name_plural = 'Cevaplar'
