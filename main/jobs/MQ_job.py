#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 12:51:12 2017

@author: benwu
"""
import pykka
from celery import Celery

class MQ_job(pykka.ThreadingActor):
    def __init__(self,key):
        super(MQ_job, self).__init__()
        self.broker = ""
        self.topics = ""
        if key:
            print("MQ_job Initiated!")
            self.MQ_connection()
    
    def MQ_connection(self):
        #read config & celery connection
        print("celery connecting...")
        app = Celery('tasks', backend='amqp', broker='amqp://140.119.19.110')

    def on_receive(self, message):
        print("MQ_job recieved msg "+str(message))