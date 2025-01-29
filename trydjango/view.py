"""
to render html web pages
"""

from django.http import HttpResponse
from article.models import article
from django.template.loader import render_to_string


def article_home(request):



    return HttpResponse()

# def article_home  


#     obj = article.objects.get(id=1)
#     # # a = obj.title
#     # HTML_STRING =f"""<h1>Hellow {obj.title}</h1>
#     # """
#     my_list=[1, 2, 3, 4, 5]



def home(request, id=None, **kwargs):

    print(id, "and", kwargs,f'and {request}', 'and again')

    obj = article.objects.get(id=1)
    content = {
        "my_list":article.objects.all(),
        "title":obj.title,
        "content": obj.content,
    }
    HTML_STRING = render_to_string("home_view.html", context=content)
    """take in a request (django send request)
    return html as a response (we pick to return the response)
    """
    return HttpResponse(HTML_STRING)