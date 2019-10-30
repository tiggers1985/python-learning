#!/usr/local/bin python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------------
# use print to output debug messages
#-------------------------------------------------------------------------------------------------------------------------

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            print('no attr %s exist' % key)
    
    def __setattr__(self,key, value):
        self[key] = value

