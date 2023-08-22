# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:27:30 2023

@author: hp
"""

import sys
class ATM_MACHINE:
    def enter_password(self):
        self.password=int(input("Enter your four digit password:"))
        if self.password==1234:
            print(f"Congratulations you have successfully login!")
        else:
            raise ValueError ("Wrong Password.Unable to login")
    def total_balance(self):
    
        self.balance=10000
        print(f"Your account balance is {self.balance}")
    def select_options(self):
        press_button=int(input("Select your choice:"))
        if press_button==1:
            print("Savings")
            saving_amount=int(input("Enter amount you want to save."))
            self.balance=self.balance+saving_amount
            print(f"Total balance is: {self.balance}")
            sys.exit()
        elif press_button==2:
            print("Transaction") 
            transicted_amount=int(input("Enter amount you want to transiction."))
            self.balance=self.balance-transicted_amount
            print(f"Remaing balance is: {self.balance}")
            sys.exit()
        elif press_button==3:
            print("Current")
        else:
            raise ValueError("You press wrong button.")
    
    def withdraw_money(self):
        withdraw_amount=int(input("Enter amount you want to withdraw."))
        if withdraw_amount<self.balance:
            self.balance=self.balance-withdraw_amount
            print(f"Your remaining balance is: {self.balance}")
            print(f"Your withdraw amount is: {withdraw_amount}")
        else:
            raise ValueError("Insufficient balance.")
    def payment_receipt(self):
        self.raceed_charges=2.5
        select_options=int(input("Do you want to receive payment receipt?"))
        if select_options==1:
            print("yes.")
            self.balance=self.balance-self.raceed_charges
            print(f"Raceed charges {self.raceed_charges}rupess are deducted from your account.")
            print(f"Your remaining balance after all deduction is {self.balance}")
        else:
            print("No")
obj=ATM_MACHINE()
obj.enter_password()
obj.total_balance()
obj.select_options()
obj.withdraw_money()           
obj.payment_receipt()
    
    
    
    
    
    
    
    
    
    
    
    
    