
import numpy as np
import random
#! /usr/bin/env python
#coding=utf-8

import ctypes,sys

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

# 字体颜色定义 ,关键在于颜色编码，由2位十六进制组成，分别取0~f，前一位指的是背景色，后一位指的是字体色
#由于该函数的限制，应该是只有这16种，可以前景色与背景色组合。也可以几种颜色通过或运算组合，组合后还是在这16种颜色中

# Windows CMD命令行 字体颜色定义 text colors
FOREGROUND_BLACK = 0x00 # black.
FOREGROUND_DARKBLUE = 0x01 # dark blue.
FOREGROUND_DARKGREEN = 0x02 # dark green.
FOREGROUND_DARKSKYBLUE = 0x03 # dark skyblue.
FOREGROUND_DARKRED = 0x04 # dark red.
FOREGROUND_DARKPINK = 0x05 # dark pink.
FOREGROUND_DARKYELLOW = 0x06 # dark yellow.
FOREGROUND_DARKWHITE = 0x07 # dark white.
FOREGROUND_DARKGRAY = 0x08 # dark gray.
FOREGROUND_BLUE = 0x09 # blue.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_SKYBLUE = 0x0b # skyblue.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_PINK = 0x0d # pink.
FOREGROUND_YELLOW = 0x0e # yellow.
FOREGROUND_WHITE = 0x0f # white.


# Windows CMD命令行 背景颜色定义 background colors
BACKGROUND_BLUE = 0x10 # dark blue.
BACKGROUND_GREEN = 0x20 # dark green.
BACKGROUND_DARKSKYBLUE = 0x30 # dark skyblue.
BACKGROUND_DARKRED = 0x40 # dark red.
BACKGROUND_DARKPINK = 0x50 # dark pink.
BACKGROUND_DARKYELLOW = 0x60 # dark yellow.
BACKGROUND_DARKWHITE = 0x70 # dark white.
BACKGROUND_DARKGRAY = 0x80 # dark gray.
BACKGROUND_BLUE = 0x90 # blue.
BACKGROUND_GREEN = 0xa0 # green.
BACKGROUND_SKYBLUE = 0xb0 # skyblue.
BACKGROUND_RED = 0xc0 # red.
BACKGROUND_PINK = 0xd0 # pink.
BACKGROUND_YELLOW = 0xe0 # yellow.
BACKGROUND_WHITE = 0xf0 # white.



# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool

#reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

###############################################################
#暗蓝色
#dark blue
def printDarkBlue(mess):
    set_cmd_text_color(FOREGROUND_DARKBLUE)
    sys.stdout.write(mess)
    resetColor()

#暗绿色
#dark green
def printDarkGreen(mess):
    set_cmd_text_color(FOREGROUND_DARKGREEN)
    sys.stdout.write(mess)
    resetColor()

#暗天蓝色
#dark sky blue
def printDarkSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_DARKSKYBLUE)
    sys.stdout.write(mess)
    resetColor()

#暗红色
#dark red
def printDarkRed(mess):
    set_cmd_text_color(FOREGROUND_DARKRED)
    sys.stdout.write(mess)
    resetColor()

#暗粉红色
#dark pink
def printDarkPink(mess):
    set_cmd_text_color(FOREGROUND_DARKPINK)
    sys.stdout.write(mess)
    resetColor()

#暗黄色
#dark yellow
def printDarkYellow(mess):
    set_cmd_text_color(FOREGROUND_DARKYELLOW)
    sys.stdout.write(mess)
    resetColor()

#暗白色
#dark white
def printDarkWhite(mess):
    set_cmd_text_color(FOREGROUND_DARKWHITE)
    sys.stdout.write(mess)
    resetColor()

#暗灰色
#dark gray
def printDarkGray(mess):
    set_cmd_text_color(FOREGROUND_DARKGRAY)
    sys.stdout.write(mess)
    resetColor()

#蓝色
#blue
def printBlue(mess):
    set_cmd_text_color(FOREGROUND_BLUE)
    sys.stdout.write(mess)
    resetColor()

#绿色
#green
def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()

#天蓝色
#sky blue
def printSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_SKYBLUE)
    sys.stdout.write(mess)
    resetColor()

#红色
#red
def printRed(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()

#粉红色
#pink
def printPink(mess):
    set_cmd_text_color(FOREGROUND_PINK)
    sys.stdout.write(mess)
    resetColor()

#黄色
#yellow
def printYellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    sys.stdout.write(mess)
    resetColor()

#白色
#white
def printWhite(mess):
    set_cmd_text_color(FOREGROUND_WHITE)
    sys.stdout.write(mess)
    resetColor()

##################################################

#白底黑字
#white bkground and black text
def printWhiteBlack(mess):
    set_cmd_text_color(FOREGROUND_BLACK | BACKGROUND_WHITE)
    sys.stdout.write(mess)
    resetColor()

#白底黑字
#white bkground and black text
def printWhiteBlack_2(mess):
    set_cmd_text_color(0xf0)
    sys.stdout.write(mess)
    resetColor()


#黄底蓝字
#white bkground and black text
def printYellowRed(mess):
    set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()


##############################################################

if __name__ == '__main__':
    
    print
printSkyBlue("hello!\n")
name = input("请输入你的名字！")
print("你好，",name,"!")
printSkyBlue("你的目标是击败魔龙哦~")
strange = 1
feel = 5
tried = 0
live = 100
beat = 0
money = 0
dragon = 1000
afhauwhi = 0
printYellow("说明: \n您的攻击力大于30才可以去挑战魔龙。\n心情如果小于0则会降低工作效率哦~\n如果太过于劳累(大于10)则会扣除生命，记得多留意！\n祝您游戏愉快！\n ")
while afhauwhi == 0:
	if tried >10:
		printRed("你太累了！\n生命下降了10.快去休息一下吧！")
		live = live -10
	if tried >15:
		printRed("你超级累了！\n生命又下降了5.快去休息一下吧！")
		live = live -5
	if live <1:
		printRed("Game Over!\n你死了！\n ")
		break
	if live>100:
		live=100
	if feel >5:
		feel = 5
	else:
		pass
		printWhite("\n")
		print("您现在的攻击力是:",strange,',\n您现在的心情是:',feel,",\n您现在的劳累度是:",tried,",\n您现在的生命是:",live,",\n您还有",money,"元。")
		printBlue("现在要干什么呢？")
		num = int(input("输入1去工作，输入2去娱乐，输入3去买药，输入4去打魔龙！"))
		if num == 1:
			x = (random.randint(1,10))
			y = (random.randint(1,4))
			money = money + x
			strange = strange + y
			tried = tried + 1
			z = (random.randint(0,10))
			if feel <0:
				printDarkRed("你太累了，工资减少了，并且不获得攻击力。")
				x = x - 3
				y = 0
				if x<0:
					x = 0
			printSkyBlue("")
			print("你在工地搬砖，获得了",x,"元,\n增加了",y,"点攻击力，\n疲劳+1\n ")
			if z == 6:
				printRed("你和包工头有点冲突，你的心情下降了1！\n ")
				feel = feel - 1
			if z == 2:
				printRed("你因为工资的事情和包工头争论，你的钱少了10元，生命下降了10！\n ")
				money = money - 10
				live = live - 10
		if num == 2:
			feel += 1
			tried = tried -4
			if feel > 5:
				feel = 5
			if tried < 0:
				tried = 0
			pass
			printDarkPink("你去玩了，心情+1，疲劳-4\n ")
		if num == 3:
			if money <5:
				printRed("没钱买啥药嘞？")
			else:
				z = (random.randint(0,10))
				if z == 0:
					money = money - 1
					live = live +40
					printDarkRed("你只花了1元买了一瓶特效药，生命+40\n")
				if z == 1:
					money = money - 5
					live = live +10
					printSkyBlue("你花了5元买了一瓶假药，生命+10\n")
				if z>1:
					money = money - 2
					live = live +20
					printDarkPink("你花2元买了一瓶药，生命+20\n")
		if num == 4:
			z = (random.randint(0,10))
			if strange < 30:
				printDarkRed("你的力量还不够哦，需要再多练习！\n")
			elif strange <40:
				printDarkPink("你攻击了魔龙，你对他造成了100点伤害，他的反击让你减少了30生命，疲劳增加了2！\n")
				live = live - 30
				dragon = dragon - 100
				tried = tried +2
			else:
				printSkyBlue("你的攻击非常有效！你对他造成了300点伤害！\n")
				dragon = dragon -300
				if z <5:
					print("你的生命下降了10，疲劳增加了1！\n")
					live = live - 10
					tried = tried +2
				else:
					print("你躲避了魔龙的攻击，甚至很轻松！\n")
			if dragon <0:
				printDarkPink("你打败了魔龙！\n")
				printDarkRed("祝贺你通关了！\n")
				printDarkBlue("作者：逍遥风鉴事\n")
				printDarkGray("感谢游玩！\n")
				break
			else:
				print("魔龙还剩",dragon,"点血。\n ")
		elif num == "":
			print("总得输入点什么吧？")
pass
input("按\"Enter\"退出.")