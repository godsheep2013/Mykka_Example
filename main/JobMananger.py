#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 09:45:36 2017

@author: benwu
"""

import pykka
import json
from jobs import *

class JobMananger(pykka.ThreadingActor):
    def __init__(self):
        super(JobMananger, self).__init__()
        self.jobs = []

        print("JobMananger Initiated!")
        self.loadConfig()
        self.createJobs()
        #self.killAll()
            
    def loadConfig(self):
        try:
            rf = open('../resources/jobConfig.json','r').read()
            print(rf)
            config = json.loads(rf)
            self.jobs = config['jobs']
        except:
            print("[ERR]error while reading jobConfig file.")

    def createJobs(self):
        for job in self.jobs:
            creation = eval(str(job)+".start()")
    def killAll(self):
        ActorSystem.stop_all()

    def on_receive(self, message):
        print("JobMananger recieved!"+str(message))

    