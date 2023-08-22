# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 22:18:28 2023

@author: hp
"""

#Convert Pakistani Currency into America,Austrailia,England,
#Japan,Malaysia,Saudia,Turkey currencies?


class CurrencyConvertor:
    def __init__(self,pakistani_amount,american_exchangerate,austrailian_exchangerate,british_exchangerate,japani_exchangerate,mlaysia_exchangerate,saudia_exchangerate,turkish_exchangerate):
        self.pakistani_amount=pakistani_amount
        self.american_exchangerate=american_exchangerate
        self.austrailian_exchangerate=austrailian_exchangerate
        self.british_exchangerate=british_exchangerate
        self.japani_exchangerate=japani_exchangerate
        self.mlaysia_exchangerate=mlaysia_exchangerate
        self.saudia_exchangerate=saudia_exchangerate
        self.turkish_exchangerate=turkish_exchangerate
    def American_dollars(self):
        american_dollars=self.pakistani_amount * self.american_exchangerate
        print(f"{self.pakistani_amount} rupess equal to {american_dollars} USD.")
    def Austrailian_dollars(self):
        austrailian_dollars=self.pakistani_amount * self.austrailian_exchangerate
        print(f"{self.pakistani_amount} rupess equal to {austrailian_dollars} AUD.")
    def British_pound(self):
        british_pound=self.pakistani_amount * self.british_exchangerate
        print(f"{self.pakistani_amount} rupess equal to {british_pound} GBP.")
    def Japanese_yen(self):
        japanese_yen=self.pakistani_amount * self.japani_exchangerate
        print(f"{self.pakistani_amount} rupess equal to {japanese_yen} JPY.")
    def Mlaysian_ringit(self):
        malaysian_ringit=self.pakistani_amount * self.mlaysia_exchangerate
        print(f"{self.pakistani_amount} rupess equal to {malaysian_ringit:2f} MYR.")
    def Saudi_ryal(self):
        saudi_riyal=self.pakistani_amount *  self.saudia_exchangerate
        print(f"{self.pakistani_amount} rupess equal to {saudi_riyal} SAR.")
    def Turkish_lira(self):
        turkish_lira=self.pakistani_amount * self.turkish_exchangerate
        print(f"{self.pakistani_amount} rupess equal to {turkish_lira} TRY.")
        
obj=CurrencyConvertor(15340, 0.0035, 0.0054, 0.0028, 0.52, 0.017, 0.014, 0.10)
obj.American_dollars()
obj.Austrailian_dollars()
obj.British_pound()
obj.Japanese_yen()
obj.Mlaysian_ringit()
obj.Saudi_ryal()
obj.Turkish_lira()