from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
import time

# Create your views here.

def index(request):
    return render(request, "page/index.html")


def posts(request):

    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # Generate list of posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")


    # Artificially delay speed of response
    time.sleep(1)


    # Return list of posts
    return JsonResponse({
        "posts": data
    })
