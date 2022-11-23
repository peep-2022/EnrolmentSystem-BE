from datetime import datetime
import time

sysStartTime = 'None'
sysEndTime = 'None'

def setSysStartTime(inputTime):
    global sysStartTime
    sysStartTime = inputTime


def setSysEndTime(inputTime):
    global sysEndTime
    sysEndTime = inputTime


def sysStartTime():
    global sysStartTime
    return sysStartTime


def sysEndTime():
    global sysEndTime
    return sysEndTime
