from django.shortcuts import render
from article.models import article
from django.contrib.auth.decorators import login_required
from .forms import article_form
# from django.db.models import Q


# Create your views here.
from  .models import article

def article_search_view(request):
    # context = {}
    query = request.GET.get('query')
    print(query)
    qs = article.objects.search(query=query)

    context={
        "object_list":qs
    } 
    # print(query)
    # if query is not None:
    #     # lookups = Q(title__icontains=query) | Q(content__icontains=query) #for performing complex query search 
    #     #assuming you want to perform a complex lookup in to field we use the pipe for example
    #     #Q(title__icontains=query)|Q(content__icontains=query)...> what this will do is to perform the search in both field of title and content  
    #     # qs = article.objects.filter(lookups)
    #     qs = article.objects.search(query)

    # # # print(request.GET)
    # # if request.method == 'GET ':

    # #     number=request.GET.get("query")
    #     #print(number)
    return render(request, "article/search.html", context=context)

def article_detail_view(request, slug=None):
    article_obj = None
    print(slug)
    if slug is not None:
        try:
            article_obj = article.objects.get(slug=slug)
        except:
            pass

    context = {
        "object": article_obj
    }
    return render(request, "article/detail.html", context=context)

    # a quation why is the request pass in as an argument to the render function that is returned
@login_required
def article_create(request, id=None):
# note for user to be eble to add a article content the user most be login we anothe way to monitor is user is login is by using the @login_required
    form = article_form(request.POST or None )

    context={
        'form': form
    }

    if form.is_valid():
        article_object = form.save()# this is a shortcut that prevent me from making use of code below to shorten the code length
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # # title1 = form.cleaned_data.get("content")
        # print(title, content)
        context['form'] = article_form() #this line of code help clear the form out, for it to recieve new input
        # article_object = article.objects.create(title = title, content = content)
        print('this here is ', article_object.title)
        context['object']= article_object
            
    return render(request, "article/create.html", context=context)
