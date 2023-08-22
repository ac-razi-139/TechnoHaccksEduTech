# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 22:23:54 2023

@author: hp
"""

class TemperatureConvertor:
    def __init__(self,celcius):
        self.celcius=celcius
    def Fehrenheit_temperature(self):
        F=1.8*self.celcius + 32
        print(f"Temperature in fehrenheit is: {F}F")
obj=TemperatureConvertor(25)
obj.Fehrenheit_temperature()
        