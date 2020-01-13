from django.conf import settings
import threading
import requests
import os
import logging
import manage


class CaptureThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.isRunning = False
    
    def run(self):
        if self.pir_status()=='y':
            self.capture_image()

        

    def capture_image(self):
        capture_id = getattr(settings, 'capture_id', 0)
        setattr(settings, 'capture_id', capture_id+1)
        url = 'http://192.168.43.207/capture'
        downloaded_image = requests.get(url)
        #print(dj_settings)
        with open(os.path.dirname(manage.__file__)+'/static/captures/capture'+str(capture_id)+'.jpg', 'wb+') as f:
            f.write(downloaded_image.content)


    def pir_status(self):
        url = 'http://192.168.43.207/pir_check'
        respense = requests.get(url)
        return respense.content.decode('utf-8')
