from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_challenges_dict.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

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
    months = list(monthly_challenges_dict.keys())
    if(month>len(months)):
        return HttpResponse("Invalid month")
    redirect_month = months[month-1] #0-based-indexing
    redirect_path = reverse("month-challenge",args = [redirect_month]) #challenge/january
    return HttpResponseRedirect(redirect_path) #loose coupling

monthly_challenges_dict = {
    "january" : "Exercise daily for 20 minutes",
    "feburaury" : "No fast food for entire month",
    "march" : "Wake up early and do meditation",
    "april" : "Exercise daily for 20 minutes",
}

def monthly_challenge_dictionary_method(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponse("Not found")


