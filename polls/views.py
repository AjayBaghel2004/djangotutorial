from django.http import HttpsResponse

def index(request):
    return HttpsResponse("Hello, world. You are at the polls index.")


