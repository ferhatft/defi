from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib.auth.models import Permission, User

from django.contrib.auth.decorators import login_required, permission_required

from .models import NewsModel
from django import forms
from .forms import AnswerinlineModelForm,NewsForm

from django.forms import modelformset_factory, inlineformset_factory

from ckeditor.widgets import CKEditorWidget

# bilgi import
from taggit.models import Tag
from django.db.models import Count

from profiles.models import UserProfile
# filter

from django.db.models import Q


# Create your views here.

def news(request, tag_slug=None, *args, **kwargs):

    obj = NewsModel.objects.all()
    rest = obj.filter(anahaber=False)
    anahaber = obj.filter(anahaber=True)
    

    new_by_coms = NewsModel.objects.all() \
        .annotate(num_posts=Count('NewsModelAnswer')) \
        .order_by('-num_posts')[:10]

    common_tags = NewsModel.tags.most_common()[:20]

    try:
        userprofile = get_object_or_404(UserProfile, user=request.user)
    except:
        userprofile = 'AnonymousUser'

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        obj = obj.filter(tags=tag)
    else:
        tag = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # messages.error(
                #     request, "Herhangi bir arama kriteri girmediniz!")
                return redirect(reverse('bilgi'))

            queries = Q(title__icontains=query) | Q(
                intro__icontains=query)
            obj = obj.filter(queries)

    context = {
        'rest': rest,
        'anahaber':anahaber,
        'new_by_coms': new_by_coms,
        'common_tags': common_tags,
        'userprofile': userprofile,
        'tag': tag,
    }

    return render(request, 'news.html', context)


def newsdetay(request, slug):

    allblogs = NewsModel.objects.all()

    news = get_object_or_404(NewsModel, slug=slug)

    answers = news.NewsModelAnswer.all()

    common_tags = NewsModel.tags.most_common()[:20]

    dic_by_coms = NewsModel.objects.all() \
        .annotate(num_posts=Count('NewsModelAnswer')) \
        .order_by('-num_posts')[:10]

    uzantı = news.slug

    if request.method == 'POST':
        try:
            userprofile = get_object_or_404(UserProfile, user=request.user)
        except:
            userprofile = 'AnonymousUser'
            return redirect(reverse("account_login"))
        form = AnswerinlineModelForm(request.POST)
        if form.is_valid():

            main_context = form.cleaned_data['main_context']
            form.save(commit=False)
            form.instance.news = news
            form.instance.author = userprofile

            form.save()

            return redirect(reverse("newsdetay", kwargs={'slug': uzantı}))
    else:
        form = AnswerinlineModelForm()

    context = {
        'news': news,
        'dic_by_coms': dic_by_coms,
        'common_tags': common_tags,
        'answers': answers,
        'form': form,
    }

    return render(request, 'newsdetay.html', context)



@login_required
# @permission_required('bilgi.add_informationModel')
def Addnews(request):

    user = get_object_or_404(User, pk=request.user.id)
    if not user.has_perm('haber.add_newsmodel'): 
        print('___________            yes              ______________')
        context = {
        }
        return render(request, "need-perm.html", context)

    try:
        userprofile = get_object_or_404(UserProfile, user=request.user)
    except:
        userprofile = 'AnonymousUser'
        return redirect(reverse("account_login"))

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = NewsForm(request.POST, request.FILES)
            if form.is_valid():

                intro = form.cleaned_data['intro']
                title = form.cleaned_data['title']
                # backimage       = form.cleaned_data['backimage']

                form.save(commit=False)
                form.instance.author = userprofile

                form.save()

                return redirect('news')
        else:

            return HttpResponseRedirect('/accounts/login/')
    else:
        form = NewsForm()

    context = {
        'form': form,
    }

    return render(request, 'addnews.html', context)



@login_required
def new_update(request, slug):
    if not request.user.has_perm('haber.change_newsmodel'):
        context = {
        }
        return render(request, "need-perm.html", context)

    newobj = get_object_or_404( NewsModel , slug=slug)
    form = NewsForm(
        request.POST or None,
        request.FILES or None,
        instance=newobj)
    try:
        userprofile = get_object_or_404(UserProfile, user=request.user)

        if request.user.has_perm('haber.change_newsmodel'):
            print('yes')
        else:
            print('no')

    except:
        userprofile = 'AnonymousUser'
        return redirect(reverse("account_login"))

    if request.method == "POST":
        if form.is_valid():
            

            intro           = form.cleaned_data['intro']
            title           = form.cleaned_data['title']
            # backimage       = form.cleaned_data['backimage']

            
            form.save(commit=False)
            form.instance.author = userprofile

            form.save()

            uzantı = newobj.slug

            return redirect(reverse("newsdetay", kwargs={'slug': uzantı}))
            
    context = {
        'form': form
    }
    return render(request, "updatenew.html", context)




@login_required
def new_delete(request, slug):
    new = get_object_or_404( NewsModel, slug=slug)
    if not request.user.has_perm('haber.delete_newsmodel'):
        return render(request, "need-perm.html")
    new.delete()
    return redirect(reverse("news"))