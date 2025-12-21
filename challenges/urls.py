from django.urls import path

from challenges import views

urlpatterns = [
    #path('january/',views.index,name='index'),
    #path('feburuary/',views.feb_challenge,name='index'),

    path("<str:month>/", views.monthly_challenge)
]