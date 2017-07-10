#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 12:51:12 2017

@author: benwu
"""
import pykka

class Example_job(pykka.ThreadingActor):
    def __init__(self):
        super(Example_job, self).__init__()
        print("Example_job Initiated!")
        #Do something after initiating?
            
    def on_receive(self, message):
        print("Example_job recieved msg "+ str(message))
        #Do something after received msg?