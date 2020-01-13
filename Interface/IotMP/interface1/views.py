from django.shortcuts import render
from django.conf import settings
import manage
import requests
import os
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def home_interface(request):
    logger.debug('is logger working')
    ##TODO load the files from here when finished with the prototype
    images_list = [os.path.dirname(manage.__file__)+'/static/captures/'+ \
        x for x in os.listdir(os.path.dirname(manage.__file__)+'/static/captures/')]
    #logger.debug(len(images_list))
    var_dict = {'name':"yasser",'images_list':images_list}
    return render(request,'index.html',var_dict)

def capture_image():
    capture_id = getattr(settings,'capture_id',0)
    setattr(settings,'capture_id',capture_id+1)
    url = 'http://192.168.43.207/capture'
    downloaded_image = requests.get(url)
    #print(dj_settings)
    with open(os.path.dirname(manage.__file__)+'/static/captures/capture'+str(capture_id)+'.jpg', 'wb+') as f:
        f.write(downloaded_image.content)

def reset_system(request):
    setattr(settings, 'capture_id', 0)
    return home_interface(request)

def capture_view(request):
    capture_image()
    return 'render'

