import os,sys,json
import   os
from sys import *

x=1
y =2
z= 3

def badFunction( a,b,c ):
    X = 10
    unused_var = "nobody cares about me"
    if a==True:
        return(a+b+c+X)
    elif a ==False:
        return(0)

def another_bad_function(reallyLongArgumentNameThatExceedsLineLength, anotherReallyLongArgumentNameThatExceedsLineLength, yetAnotherLongArgumentNameThatWillCauseLineLengthViolations):
    l = [1,2,3,4,5]
    d = {'key':'value','another_key':'another_value'}
    try:
        pass
    except:
        pass
    return l,d

class myClass:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def MyMethod( self ):
        lambda x: x*2
        return self.x+self.y

myObj=myClass(1,2)
print(myObj.MyMethod())
result=badFunction(True,2,3   )