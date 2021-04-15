from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Hello World</h1>")

def tweet_detail_view(request,tweet_id, *args, **kwargs):
    """
    REST API VIEW
    consume by JavaScrpt/ Swift/ Java/ iOS/ Android
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
        
    

