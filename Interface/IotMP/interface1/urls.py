from django.urls import path
from interface1 import views


urlpatterns = [
    path(r'',views.home_interface)
]
