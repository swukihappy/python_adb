# -*- coding:utf-8 -*-

import os
import sys
import time

# 配置文件

remote_path_photo="/Users/zdx/Desktop/screencap/photo/"
remote_path_log="/Users/zdx/Desktop/screencap/log/"
packagename_hint="com.yuncheapp.android.pearl"



argv_len=len(sys.argv)
if argv_len > 1:
	accept=sys.argv[1]
else:
	accept=""

#help文档

def adb_help():
	print("-- clear：清除缓存信息;\n-- scr：截取手机屏幕，并保存至电脑;\n-- get_act：获取顶层activity;\n-- log：获取日志\n")


# 检查设备是否连接成功

def check_connect():
	connect_flag=False
	q=os.popen("adb get-state").read()
	if str(q).startswith("device") == True:
		print("设备已连接成功")
		connect_flag = True
		return connect_flag
	else:
		print("请检查设备连接")
		return connect_flag

#  判断是否有输入packagename

def check_packagename():
	if argv_len>2:
		packagename=sys.argv[2]
		return packagename,accept
	else:
		packagename=packagename_hint
		return packagename

## 函数调用

time =str(time.time())
connect_flag=check_connect()
packagename=check_packagename()
if accept == "help":
	adb_help()

if connect_flag==True:
	# 清除缓存信息
	if accept=="clear":
		os.system("adb shell pm clear "+packagename)
		print(packagename)

	#  屏幕截图-保存至电脑

	elif accept=="scr":
		os.system("adb shell screencap -p /sdcard/"+time+".png")
		print("success")
		os.system("adb pull /sdcard/"+time+".png "+remote_path_photo)
		os.system("adb shell rm /sdcard/"+time+".png")
	#	要获取当前界面的Activity：
	elif accept=="get_act":
		os.system("adb shell dumpsys activity top | grep ACTIVITY")
	#	输出日志到电脑
	elif accept=="log":
		print("success")
		os.system("adb logcat > "+remote_path_log+"alllog"+time+".txt")
		os.system("adb logcat *:E> "+remote_path_log+"Elog"+time+".txt")
		os.system("adb logcat *：E | grep "+packagename+"> "+remote_path_log+"Onelog"+time+".txt")

