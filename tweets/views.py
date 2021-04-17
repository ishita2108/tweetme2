import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "pages/home.html", context = {}, status = 200)

def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    consumed by JavaScrpt/ Swift/ Java/ iOS/ Android
    return json data
    """
    qs = Tweet.objects.all()
    tweet_list = [{"id": x.id, "content":x.content, "likes":random.randint(0,122) } for x in qs ]
    data = { 
        "isUser" : False,
        "response": tweet_list,
    }
    return JsonResponse(data)


def tweet_detail_view(request,tweet_id, *args, **kwargs):
    """
    REST API VIEW
    consumed by JavaScrpt/ Swift/ Java/ iOS/ Android
    return json data
    """

    data = {
        "id" : tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404

    # return HttpResponse(f"<h1>Hello {tweet_id}-{obj.content}</h1>")
    #jsonresponse will take data dictionary of some kind and return it back
    
    return JsonResponse(data, status=status)  #json.dumps content_type = '/application/json'
        
    

