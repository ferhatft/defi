from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib.auth.models import Permission, User

from django.contrib.auth.decorators import login_required , permission_required

from .models import İnformationModel

from django.forms import modelformset_factory, inlineformset_factory
from .forms import İnformationForm, AnswerinlineModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget

# bilgi import
from taggit.models import Tag
from django.db.models import Count

from profiles.models import UserProfile
# filter

from django.db.models import Q


# Create your views here.


def bilgi(request, tag_slug=None, *args, **kwargs):

    obj = İnformationModel.objects.all()

    dic_by_coms = İnformationModel.objects.all() \
        .annotate(num_posts=Count('informationanswers')) \
        .order_by('-num_posts')[:10]

    common_tags = İnformationModel.tags.most_common()[:20]

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
        'obj': obj,
        'dic_by_coms': dic_by_coms,
        'common_tags': common_tags,
        'userprofile': userprofile,
        'tag': tag,
    }

    return render(request, 'bilgi.html', context)


def bilgidetay(request, slug):

    allblogs = İnformationModel.objects.all()

    info = get_object_or_404(İnformationModel, slug=slug)

    answers = info.informationanswers.all()

    common_tags = İnformationModel.tags.most_common()[:20]

    dic_by_coms = İnformationModel.objects.all() \
                    .annotate(num_posts=Count('informationanswers')) \
                    .order_by('-num_posts')[:10]

    uzantı = info.slug

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
            form.instance.information = info
            form.instance.author = userprofile

            form.save()

            return redirect(reverse("bilgidetay", kwargs={'slug': uzantı}))
    else:
        form = AnswerinlineModelForm()

    context = {
        'info': info,
        'dic_by_coms': dic_by_coms,
        'common_tags': common_tags,
        'answers': answers,
        'form': form,
    }

    return render(request, 'bilgidetay.html', context)

@login_required
# @permission_required('bilgi.add_informationModel')
def Addbilgi(request):

    user = get_object_or_404(User, pk=request.user.id)
    if not user.has_perm('bilgi.add_i̇nformationmodel'): 
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
            form = İnformationForm(request.POST, request.FILES)
            if form.is_valid():

                intro = form.cleaned_data['intro']
                title = form.cleaned_data['title']
                # backimage       = form.cleaned_data['backimage']

                form.save(commit=False)
                form.instance.author = userprofile

                form.save()

                return redirect('bilgi')
        else:

            return HttpResponseRedirect('/accounts/login/')
    else:
        form = İnformationForm()

    context = {
        'form': form,
    }

    return render(request, 'addbilgi.html', context)

@login_required
def infromation_update(request, slug):
    if not request.user.has_perm('information.infromation_update'):
        context = {
        }
        return render(request, "need-perm.html", context)

    infoobj = get_object_or_404( İnformationModel, slug=slug)
    form = İnformationForm(
        request.POST or None,
        request.FILES or None,
        instance=infoobj)
    try:
        userprofile = get_object_or_404(UserProfile, user=request.user)

        if request.user.has_perm('information.infromation_update'):
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

            # uzantı =  title.lower().replace(' ','-')
            return redirect(reverse("bilgidetay", kwargs={'slug': slug}))
            
    context = {
        'form': form
    }
    return render(request, "updatebilgi.html", context)




@login_required
def infromation_delete(request, slug):
    infromation = get_object_or_404( İnformationModel, slug=slug)
    request.user.refresh_from_db()
    if not request.user.has_perm('bilgi.delete_informationmodel'):
        print('-------------------------------------------------------------------------------------------')
        print(request.user.has_perm('bilgi.delete_informationmodel'))
        print(request.user)
        return render(request, "need-perm.html")
    
    infromation.delete()
    return redirect(reverse("bilgi"))





