import time
import test
def getTime():
    t = time.localtime()
    tList = [t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec]
    # if tList[0] == 12 and tList[1] == 17 :
    if tList[0] == 12 and tList[1] == 23 and tList[2] == 14 and tList[3] == 59 and tList[4] == 33:
        return True
    else:
        return False
while True:
    # print(getTime())
    if getTime():
        test.main()
        break
