from django.urls import path

from challenges import views

urlpatterns = [
    #path('january/',views.index,name='index'),
    #path('feburuary/',views.feb_challenge,name='index'),

    path("<int:month>/",views.monthly_challenge_by_number), #this should be first otherwise django will treat it as string
    path("<str:month>/", views.monthly_challenge),

]