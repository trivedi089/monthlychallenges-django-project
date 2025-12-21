from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Exercise daily forn 20 minutes")

