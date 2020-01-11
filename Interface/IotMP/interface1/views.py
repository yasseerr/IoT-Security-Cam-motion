from django.shortcuts import render

# Create your views here.
def home_interface(request):
    var_dict = {'name':"yasser"}
    return render(request,'index.html',var_dict)