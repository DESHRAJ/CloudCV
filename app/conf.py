__author__ = 'parallels'
import os

import sys
path = '/home/ubuntu/cloudcv/cloudcv17'
sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cloudcv17.settings")

from django.conf import settings

# user
USER = 'ubuntu'
# directory where all pictures reside
PIC_DIR = os.path.join(settings.MEDIA_ROOT, 'pictures', 'cloudcv')


# directory for classification job related stuff.
LOCAL_CLASSIFY_JOB_DIR = os.path.join(settings.MEDIA_ROOT, 'pictures', 'classify')
if not os.path.exists(LOCAL_CLASSIFY_JOB_DIR):
    os.makedirs(LOCAL_CLASSIFY_JOB_DIR)

# directory for classification demo images
LOCAL_DEMO_PIC_DIR = os.path.join(settings.MEDIA_ROOT,'pictures', 'demo')

# directory for classification demo images
LOCAL_DEMO_POI_PIC_DIR = os.path.join(settings.MEDIA_ROOT,'pictures', 'poiDemo')

# directory for imagestitch demo images
LOCAL_DEMO1_PIC_DIR = os.path.join(settings.MEDIA_ROOT,'pictures', 'demo1')

# directory where all the executables reside
EXEC_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'executable')
# directory for VQA demo images
SHOW_KNOWN_DEMO_IMAGES = False

if SHOW_KNOWN_DEMO_IMAGES:
    LOCAL_DEMO_VQA_PIC_DIR = os.path.join(settings.MEDIA_ROOT,'pictures', 'vqaDemo')
else:
    LOCAL_DEMO_VQA_PIC_DIR = os.path.join(settings.MEDIA_ROOT,'pictures', 'vqaDemo', 'test2014')
# PIC_URL
PIC_URL = '/media/pictures/cloudcv/'

# CAFFE DIRECTORY
CAFFE_DIR = '/home'+'/ubuntu/' + 'caffe'
LOG_DIR = os.path.join(settings.BASE_ABS_DIR, 'logs')
DEMO_VQA_LOG_FILE = os.path.join(settings.BASE_ABS_DIR, 'logs')
