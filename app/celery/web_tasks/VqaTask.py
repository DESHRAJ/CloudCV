__author__ = 'clint'
import sys
path = '/home/ubuntu/cloudcv/cloudcv_gsoc'
sys.path.append(path)

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cloudcv17.settings")

from celery import Celery

import json
import operator
import traceback
import numpy as np
import os
import os.path
import redis
from app.log import log, log_to_terminal, log_error_to_terminal, log_and_exit

#from app.executable.vqa_answer_image import vqa_answer, vqa_answer2
import app.conf as conf

celery = Celery('VqaFeatTask', backend = 'redis://0.0.0.0:6379/0', broker='redis://0.0.0.0:6379/0')

r = redis.StrictRedis(host='localhost', port=6379, db=0)

@celery.task
def answerQuestion(feat_path, question, socketid, imageid):
    try:
            print 'Thinking...'
            # For now, using numpy archives
            feat_path = feat_path + '.npy'
            #ans = vqa_answer(feat_path, question)

            log_to_terminal("Answer for " + imageid + " : " + str(ans), socketid)

            # tags = sorted(tags.iteritems(), key=operator.itemgetter(1), reverse=True)
            web_result = {}
            # web_result[imageid] = ans

            r.publish('chat', json.dumps({'web_result': json.dumps(web_result), 'socketid': str(socketid)}))

            log_to_terminal('Thank you for using CloudCV', socketid)

    except Exception as e:
        log_to_terminal(str(traceback.format_exc()), socketid)

@celery.task
def answerQuestion2(feat_path, question, socketid, imageid):
    try:
        print 'Thinking...'
        feat_path = feat_path + '.npy'
        feat = np.load(feat_path)
        r.publish('test_aws', json.dumps({'imgFeatures': feat.tolist(),
                              'question': question,
                              'imageid': imageid, 'socketid': socketid}))

        # ans = vqa_answer2(feat_path, question)
        # log_to_terminal("Answer for "+ imageid + " : " + str(ans), socketid)
        # web_result = {}
        # web_result[imageid] = ans
        # r.publish('chat', json.dumps({'web_result': json.dumps(web_result), 'socketid': str(socketid)}))

        # log_to_terminal('Thank you for using CloudCV', socketid)

    except Exception as e:
        log_to_terminal(str(traceback.format_exc()), socketid)
