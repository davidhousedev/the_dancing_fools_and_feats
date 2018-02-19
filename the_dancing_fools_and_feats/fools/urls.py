from django.urls import path
from . import views

urlpatterns = [
    path('classes_and_dance',
         views.ClassAndDanceView.as_view(),
         name='fools-classes-dance'),
    path('staff',
         views.StaffView.as_view(),
         name='fools-staff'),
    path('getting_here',
         views.GettingHereView.as_view(),
         name='fools-getting-here'),
    path('contact',
          views.ContactView.as_view(),
          name='fools-contact'),
    path('',
         views.IndexView.as_view(),
         name='fools-index')
]
