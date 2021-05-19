import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
    # print(request.user or None)
    # print(args, kwargs)
    # return HttpResponse("<h1>Hello World</h1>")
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, "pages/home.html", context = {"username": username}, status = 200)

def tweets_list_view(request, *args, **kwargs):
    return render(request, "tweets/list.html")

def tweets_detail_view(request, tweet_id, *args, **kwargs):
    return render(request, "tweets/detail.html", context = {"tweet_id": tweet_id})


# def tweet_create_view_pure_django(request, *args, **kwargs):
#     '''
#     REST API Create View -> DRF
#     '''
#     user = request.user
#     if not request.user.is_authenticated:
#         user = None
#         if request.is_ajax():
#             return JsonResponse({}, status=401)
#         return redirect(settings.LOGIN_URL)
#     # print("ajax",request.is_ajax())
#     form = TweetForm(request.POST or None)
#     # print('post data is',request.POST)
#     next_url = request.POST.get("next") or None
#     # print("next url", next_url)
#     if form.is_valid():
#         obj = form.save(commit=False) 
#         #Here with commit = False we are not saving the form in database
#         #In this case, it’s up to you to call save() on the resulting model instance. 
#         # This is useful if you want to do custom processing on the object before saving it, 
#         # or if you want to use one of the specialized model saving options. commit is True by default.

#         #do other form related things
#         obj.user = user
#         obj.save()
#         if request.is_ajax():
#             return JsonResponse(obj.serialize(), status=201)  #201 == created items
#         if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
#             return redirect(next_url)
#         form = TweetForm()
#     if form.errors:
#         if request.is_ajax():
#             return JsonResponse(form.errors, status=400)
#     return render(request, 'components/forms.html', context={'form': form})

# def tweet_list_view_pure_django(request, *args, **kwargs):
#     """
#     REST API VIEW
#     consumed by JavaScrpt/ Swift/ Java/ iOS/ Android
#     return json data
#     """
#     qs = Tweet.objects.all()
#     tweet_list = [x.serialize() for x in qs ]
#     data = { 
#         "isUser" : False,
#         "response": tweet_list,
#     }
#     return JsonResponse(data)


# def tweet_detail_view_pure_django(request,tweet_id, *args, **kwargs):
#     """
#     REST API VIEW
#     consumed by JavaScrpt/ Swift/ Java/ iOS/ Android
#     return json data
#     """

#     data = {
#         "id" : tweet_id,
#     }
#     status = 200
#     try:
#         obj = Tweet.objects.get(id=tweet_id)
#         data['content'] = obj.content
#     except:
#         data['message'] = "Not Found"
#         status = 404

#     # return HttpResponse(f"<h1>Hello {tweet_id}-{obj.content}</h1>")
#     #jsonresponse will take data dictionary of some kind and return it back
    
#     return JsonResponse(data, status=status)  #json.dumps content_type = '/application/json'
        
    

