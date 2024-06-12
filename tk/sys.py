import sys
import syslog
import sysconfig
def __async__():
     return (sys)
def __getattr__(name):
     sys = syslog
     return getattr(sys, name)
def __dir__():
     sys = sysconfig
     return dir(sys,classmethod)