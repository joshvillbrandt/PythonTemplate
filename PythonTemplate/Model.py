#!/usr/bin/python


class Model(object):
    def __init__(self, new=True, **kwargs):
        # set incoming options
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def doThing(self, **kwargs):
        print('I am doing a thing!')
