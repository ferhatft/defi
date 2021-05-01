from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import DictionaryModel,ReporModel
from .forms import DictionaryForm, AnswerinlineModelForm,ReportModelForm
from profiles.models import UserProfile
from taggit.models import Tag

from django.db.models import Count

from django.core.mail import send_mail
# filter
from django.db.models import Q
# Create your views here.


def dictionary(request, tag_slug=None, *args, **kwargs):

    dictionaryies = DictionaryModel.objects.all()

    if 'scrollid' in request.session:
        scrollid = request.session['scrollid']
    else:
        scrollid = None 
        print("session hatarı ___________________________")



    dic_by_coms = DictionaryModel.objects.all() \
        .annotate(num_posts=Count('dictionaryanswers')) \
        .order_by('-num_posts')[:10]

    common_tags = DictionaryModel.tags.most_common()[:20]
    try:
        userprofiletuple =  UserProfile.objects.get_or_create(user=request.user)
        userprofile = userprofiletuple[0]
    except:
        userprofile = 'AnonymousUser'
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        dictionaryies = dictionaryies.filter(tags=tag)
    else:
        tag = None

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = DictionaryForm(request.POST)
            if form.is_valid():

                main_context = form.cleaned_data['main_context']
                title = form.cleaned_data['title']
                form.save(commit=False)
                form.instance.author = userprofile

                new_dict = form.save()

                return redirect(reverse("dictionarydetail", kwargs={'cats': new_dict.slug }))
        else:
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = DictionaryForm()
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # messages.error(
                #     request, "Herhangi bir arama kriteri girmediniz!")
                return redirect(reverse('dictionary'))

            queries = Q(title__icontains=query) | Q(
                main_context__icontains=query)
            dictionaryies = dictionaryies.filter(queries)
    context = {
        'dictionaryies': dictionaryies,
        'dic_by_coms': dic_by_coms,
        'common_tags': common_tags,
        'userprofile': userprofile,
        'form': form,
        'tag': tag,
        'scrollid':scrollid,
    }

    return render(request, "dictionary.html", context)




def all_dictionary(request, tag_slug=None, *args, **kwargs):

    dictionaryies = DictionaryModel.objects.all()

    all_dic_by_coms = DictionaryModel.objects.all() \
        .annotate(num_posts=Count('dictionaryanswers')) \
        .order_by('-num_posts')

    common_tags = DictionaryModel.tags.most_common()[:20]
    try:
        userprofiletuple =  UserProfile.objects.get_or_create(user=request.user)
        userprofile = userprofiletuple[0]
    except:
        userprofile = 'AnonymousUser'
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        dictionaryies = dictionaryies.filter(tags=tag)
    else:
        tag = None

  
    context = {
        'dictionaryies': dictionaryies,
        'all_dic_by_coms': all_dic_by_coms,
        'common_tags': common_tags,
        'userprofile': userprofile,
        'tag': tag,
    }

    return render(request, "dictionary.html", context)



def dictionarydetail(request, cats):
    dictionary = get_object_or_404(DictionaryModel, slug=cats)
    allblogs = DictionaryModel.objects.all()
    answers = dictionary.dictionaryanswers.all()

    common_tags = DictionaryModel.tags.most_common()[:20]
    dic_by_coms = DictionaryModel.objects.all() \
        .annotate(num_posts=Count('dictionaryanswers')) \
        .order_by('-num_posts')[:10]

    uzantı = dictionary.slug

    if request.method == 'POST':
        try:
            userprofiletuple =  UserProfile.objects.get_or_create(user=request.user)
            userprofile = userprofiletuple[0]
        except:
            userprofile = 'AnonymousUser'
            return redirect(reverse("account_login"))
        form = AnswerinlineModelForm(request.POST)
        if form.is_valid():

            main_context = form.cleaned_data['main_context']
            form.save(commit=False)
            form.instance.dictionary = dictionary
            form.instance.author = userprofile

            form.save()

            return redirect(reverse("dictionarydetail", kwargs={'cats': uzantı}))
    else:
        form = AnswerinlineModelForm()

    context = {
        'allblogs': allblogs,
        'dic_by_coms': dic_by_coms,
        'common_tags': common_tags,
        'obj': dictionary,
        'answers': answers,
        'form': form,
    }

    return render(request, "dictionary-detail.html", context)


@login_required
def dictionary_create(request):
    try:
        userprofiletuple =  UserProfile.objects.get_or_create(user=request.user)
        userprofile = userprofiletuple[0]
    except:
        userprofile = 'AnonymousUser'

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = DictionaryForm(request.POST)
            if form.is_valid():

                main_context = form.cleaned_data['main_context']
                title = form.cleaned_data['title']
                form.save(commit=False)
                form.instance.author = userprofile

                form.save()

                return redirect('dictionary')
        else:

            return HttpResponseRedirect('/accounts/login/')
    else:
        form = DictionaryForm()

    context = {
        'userprofile': userprofile,
        'form': form,
    }

    return render(request, "dictionary_create.html", context)


@login_required
def dictionary_update(request, slug):
    dictionary = get_object_or_404(DictionaryModel, slug=slug)
    form = DictionaryForm(
        request.POST or None,
        request.FILES or None,
        instance=dictionary)
    try:
        userprofiletuple =  UserProfile.objects.get_or_create(user=request.user)
        userprofile = userprofiletuple[0]
    except:
        userprofile = 'AnonymousUser'
        return redirect(reverse("account_login"))

    if request.method == "POST":
        if form.is_valid():
            main_context = form.cleaned_data['main_context']
            title = form.cleaned_data['title']
            form.save(commit=False)
            form.instance.author = userprofile

            form.save()

            uzantı = title.lower().replace(' ', '-')
            return redirect(reverse("dictionarydetail", kwargs={'cats': uzantı}))

    context = {
        'form': form
    }
    return render(request, "dictionary-update.html", context)

@login_required
def dictionary_delete(request, slug):
    dictionary = get_object_or_404(DictionaryModel, slug=slug)
    dictionary.delete()
    return redirect(reverse("dictionary"))


@login_required
def dictionary_report(request,slug):
    
    dictionary = get_object_or_404(DictionaryModel, slug=slug)
    userprofiletuple =  UserProfile.objects.get_or_create(user=request.user)
    userprofile = userprofiletuple[0]

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReportModelForm(request.POST)
            if form.is_valid():

                main_context = form.cleaned_data['main_context']
                form.save(commit=False)
                form.instance.author = userprofile
                form.instance.dictionary = dictionary

                form.save()
                
                reportid = str(ReporModel.objects.last().id)

                useremail = userprofile.user.email 
                send_mail (
                'Yeni Bir şikayet var ', # subject
                main_context + '\n' +  'link = ' + 'http://localhost:8000/admin/dictionary/repormodel/'+ reportid +'/change/' + '\n' , #message
                'tugrul.tf51@gmail.com', #from email admin
                ['tugrul.tf51@gmail.com'], # To email    
                )

                send_mail (
                'Bildiriminiz İçin teşekkür ederiz', # subject
                'İletişime geçtiğiniz için teşekkür ederiz en kısa sürede size dönüş yapılacaktır', #message
                'tugrul.tf51@gmail.com', #from email
                [useremail], # To email    
                )

                return redirect('dictionary') # teşekkür sayfasına göndeririz sonrasında 
        else:
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = ReportModelForm()

    context = {
        'dictionary':dictionary,
        'userprofile': userprofile,
        'form': form,
    }

    return render(request, "dictionary_report.html", context)




@login_required
def dic_upwote(request,id):
    user_id = request.user.id

    if request.method == "POST":
        dictionary = get_object_or_404(DictionaryModel, id=request.POST.get('dict_id') )
        if dictionary.votes.exists(user_id):
            dictionary.votes.delete(user_id)
        else:   
            dictionary.votes.up(user_id)
    else:
        url = request.path 
        a = url.rsplit('/')
        dic_id = a[3]

        dictionary = get_object_or_404(DictionaryModel, id=dic_id)

        if dictionary.votes.exists(user_id):
            dictionary.votes.delete(user_id)
        else:   
            dictionary.votes.up(user_id)

    
    request.session['scrollid'] = id

    return redirect(reverse("dictionary"))
    # return redirect(reverse("dictionary", kwargs={'scrollid': id}))

@login_required
def dic_dawnvote(request,id):
    user_id = request.user.id

    if request.method == "POST":
        dictionary = get_object_or_404(DictionaryModel, id=request.POST.get('dict_id') )
        if dictionary.votes.exists(user_id):
            dictionary.votes.delete(user_id)
        else:   
            dictionary.votes.down(user_id)
    else:
        url = request.path 
        a = url.rsplit('/')
        dic_id = a[3]

        dictionary = get_object_or_404(DictionaryModel, id=dic_id)

        if dictionary.votes.exists(user_id):
            dictionary.votes.delete(user_id)
        else:   
            dictionary.votes.down(user_id)

    request.session['scrollid'] = id

    return redirect(reverse("dictionary"))




