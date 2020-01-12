from django.urls import path
from interface1 import views


urlpatterns = [
    path('reset',views.reset_system),
    path(r'',views.home_interface)
]
