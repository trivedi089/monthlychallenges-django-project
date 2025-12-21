from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Exercise daily for 20 minutes")

def feb_challenge(request):
    return HttpResponse("No fast food for entire month")

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text =  "Exercise daily for 20 minutes"
    elif month == "feburaury":
        challenge_text = "No fast food for entire month"
    elif month == "march":
        challenge_text = "Wake up early and do meditation"
    else :
        challenge_text = "This month was not supported!"
    return HttpResponse(challenge_text)

def monthly_challenge_by_number(request, month):
    return HttpResponse(f"Month number: {month}")