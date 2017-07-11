#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 12:51:12 2017

@author: benwu
"""
import pykka
import json
from celery import Celery

class MQ_job(pykka.ThreadingActor):
    def __init__(self):
        super(MQ_job, self).__init__()
        print("MQ_job Initiated!")
        self.broker = ""
        self.sub_topic = []

        self.loadConfig()
        self.MQ_connection()

    def loadConfig(self):
        try:
            rf = open('../resources/mqConfig.json','r').read()
            print(rf)
            config = json.loads(rf)
            self.broker = config['broker']
            self.sub_topic = config['sub_topic']
        except:
            print("[ERR]error while reading mqConfig file.")
    
    def MQ_connection(self):
        print("celery connecting...")
        app = Celery('tasks', backend='amqp', broker='amqp://%s' % self.broker)

    def on_receive(self, message):
        print("MQ_job recieved msg "+str(message))