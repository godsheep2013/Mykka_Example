#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 10:31:36 2017

@author: benwu
"""

import pykka.debug
import logging
import signal
from JobMananger import JobMananger



class ms_controller():
    def run(self):
        #!level=logging.DEBUG
        logging.basicConfig()
        signal.signal(signal.SIGUSR1, pykka.debug.log_thread_tracebacks)

        ActorSystem = pykka.ActorRegistry
        ActorSystem.stop_all()

        try:
            JobMananger.start()
        except :
            print("[ERR] micro service starting exception.")


ms_controller().run()