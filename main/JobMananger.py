#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 09:31:36 2017

@author: benwu
"""

import pykka
import sys
import json
from jobs import *

ActorSystem = pykka.ActorRegistry
ActorSystem.stop_all()

class JobMananger(pykka.ThreadingActor):
    def __init__(self):
        super(JobMananger, self).__init__()
        self.jobs = []
        self.key = 'True'

        if key:
            print("JobMananger Initiated!")
            self.loadConfig()
            self.createJobs()
            #self.killAll()
            
    def loadConfig(self):
        rf = open('../resources/jobConfig.json','r').read()
        print(rf)
        config = json.loads(rf)
        self.jobs = config['jobs']
        
    def createJobs(self):
        for job in self.jobs:
            print(str(job)+".start(key=%s)" % self.key)
            creation = eval(str(job)+".start(key=%s)" % self.key)
            
    def killAll(self):
        ActorSystem.stop_all()
            
            
    def on_receive(self, message):
        print("JobMananger recieved!"+str(message))
        
        



if __name__ == '__main__':
    JobMananger = JobMananger.start()
    