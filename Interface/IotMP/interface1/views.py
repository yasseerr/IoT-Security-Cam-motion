from django.shortcuts import render
from django.conf import settings
import manage
import requests
import os
import logging
import threading
#from Interface.IotMP.
from CaptureThread import CaptureThread

logger = logging.getLogger(__name__)

captureThread = CaptureThread()

# Create your views here.
def home_interface(request):
    logger.debug('is logger working')
    ##TODO load the files from here when finished with the prototype
    #logger.debug(len(images_list))
    var_dict = {'name':"yasser"}
    return render(request,'main.html',var_dict)


def reset_system(request):
    setattr(settings, 'capture_id', 0)
    images_list = [os.path.dirname(manage.__file__)+'/static/captures/' + \
        x for x in os.listdir(os.path.dirname(manage.__file__)+'/static/captures/')]
    for img_path in images_list:
        os.remove(img_path)
    return home_interface(request)


def refresh(request):
    if not captureThread.isRunning:
        captureThread.run()
    images_list = [os.path.dirname(manage.__file__)+'/static/captures/' +
        x for x in os.listdir(os.path.dirname(manage.__file__)+'/static/captures/')]
    #logger.debug(len(images_list))
    var_dict = {'name':"yasser",'images_list':images_list}
    return render(request,"index.html",var_dict)


    
