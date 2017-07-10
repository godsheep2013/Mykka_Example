#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 03:02:12 2017

@author: benwu
"""

import pykka

class Example_job2(pykka.ThreadingActor):
    def __init__(self):
        super(Example_job2, self).__init__()
        print("Example_job2 Initiated!")
        self.do_something()
    def do_something(self):
        #send testing messages to Example_job.
        pykka.ActorRegistry.get_by_class_name('Example_job')[0].tell({'msg':'hello?','from':'Example_job2'})
            
        
    def on_receive(self, message):
        print("Example_job2 recieved msg "+str(message))