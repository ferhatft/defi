
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from dictionary.models import DictionaryModel
from bilgi.models import İnformationModel
from django.db.models import Count
from .models import UserProfile
from .forms import UserprofileForm
from taggit.models import Tag



# Create your views here.

@login_required
def Userprofile(request):

    userprofile =  UserProfile.objects.get_or_create(user=request.user)
    
    userprofile =  get_object_or_404(UserProfile,user=request.user)
  

    all_tag_list = []


    dic_tag_list = DictionaryModel.objects.filter(author=userprofile)
    inf_tag_list = İnformationModel.objects.filter(author=userprofile)


    if not dic_tag_list == [] :
        for x in dic_tag_list:

            query = x.tags.names()
        
            for i in query:
                all_tag_list.append(i)



    if not inf_tag_list == [] :
        for x in inf_tag_list:

            query = x.tags.names()
        
            for i in query:
                all_tag_list.append(i)


    if all_tag_list == [] :
        all_tag_list = ['Sık kullandığın Taglar burada görünecek']

    if inf_tag_list != [] or  dic_tag_list != [] :
        word_counter = {}
        for word in all_tag_list:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1

        popular_words = sorted(word_counter, key = word_counter.get, reverse = True)

        top_3 = popular_words[:3]

        print(top_3)
        

    dictionary     = DictionaryModel.objects.filter(author=userprofile)
    information    = İnformationModel.objects.filter(author=userprofile)

    countdictionary     = dictionary.count()
    countinformation    = information.count()


    context = {
        'userprofile': userprofile,
        'dictionary':dictionary,
        'information':information,
        'countdictionary': countdictionary,
        'countinformation':countinformation,
        'top_3':top_3,
    }
    return render(request, "UserProfile.html", context)


def UpdateUserprofile(request):

    userprofile = get_object_or_404(UserProfile, user=request.user)

    form = UserprofileForm(
        request.POST or None,
        request.FILES or None,
        instance=userprofile)

    if request.method == "POST":
        if form.is_valid():
            abaout = form.cleaned_data['abaout']
            # form.save(commit=False)
            # form.instance.author = userprofile

            form.save()

            # uzantı = title.lower().replace(' ', '-')
            return redirect(reverse("Userprofile"))

    context = {
        'form': form
    }
    return render(request, "UpdateUserprofile.html", context)






def dictionary_update(request, slug):
    dictionary = get_object_or_404(DictionaryModel, slug=slug)
    form = DictionaryForm(
        request.POST or None,
        request.FILES or None,
        instance=dictionary)
    try:
        userprofile = get_object_or_404(UserProfile, user=request.user)
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
