# -*- coding: utf-8 -*-
import os
import time
import csv


class AppOperate(object):
    def __init__(self):
        self.content = ""
        self.appStartTime = 0
# app冷启动
    def appStart(self):
        cmd = "adb shell am start -W -n com.kingsoft.calendar/.GuidePageActivity"
        self.content = os.popen(cmd)
# app关闭
    def appStop(self):
        cmd = "adb shell am force-stop com.kingsoft.calendar"
        os.popen(cmd)
# app启动时间
    def appLaunchTime(self):
        for informationOfAppStart in self.content.readlines():
            if "ThisTime" in informationOfAppStart:
                self.appStartTime = informationOfAppStart.split(":")[1]
                break
        return self.appStartTime

class AppController(object):
    def __init__(self, count):
        self.app = AppOperate()
        self.counter = count
        self.allDataOfTime = [("timestamp", "elapsedtime")]
# app单次运行
    def appRunOnce(self):
        self.app.appStart()
        elapsedtime = self.app.appLaunchTime()
        self.app.appStop()
        currenttime = self.getCurrentTime()
        self.allDataOfTime.append((currenttime, elapsedtime))

# app运行次数
    def appRun(self):
        while self.counter > 0:
            self.appRunOnce()
            self.counter = self.counter - 1

# 获取到当前时间
    def getCurrentTime(self):
        osCurrentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return osCurrentTime

# 数据保存到CSV文件
    def saveDataToCSV(self):
        csvfile = file("appstarttime.csv", "wb")
        appStartTimeWriter = csv.writer(csvfile)
        appStartTimeWriter.writerows(self.allDataOfTime)
        csvfile.close()

# 脚本执行
if __name__ == '__main__':
    testAppStartTime = AppController(10)
    testAppStartTime.appRun()
    testAppStartTime.saveDataToCSV()
    #注释