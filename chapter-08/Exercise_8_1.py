# -*- coding: utf-8 -*-
# Calculator


# 第一部分
# 类定义

# 定义了用于存储历史记录的队列类型 Queue
class Queue:
    def __init__(self):
        self.items = []
        self.length = 10
        for i in range(self.length):
            self.items.append('0')
    def addItem(self, num):
        tempItems = self.items
        tempItems[1:] = self.items[0:len(self.items) - 1]
        tempItems[0] = str(num)
        self.items = tempItems

# 第二部分
# 引用必要的库
# platform 库用于判断操作系统类型并更改 UI 显示
# Tkinter 库用于实现图形用户界面
# tkMessageBox 库用于弹出消息提示框
# tkSimpleDialog 库用于弹出对话框收集数据
# tkFileDialog 库用于保存文件
# math 库用于进行数学计算

import platform
from Tkinter import *
from tkMessageBox import *
from tkSimpleDialog import *
from tkFileDialog import *
from math import *

# 第三部分
# 定义全局变量
# rawString 为当前处理数字的字符串表示
# calcNum 存储当前处理的数字
# history 为 Queue 类型对象，用于存放历史记录（10个）

rawString = '';
calcNum = 0.0
history = Queue()

# 第四部分
# 定义函数

# a.基础操作函数

# updateTextBox()
# 用于更新文本框内容与当前处理数字匹配

def updateTextBox():
    global rawString
    # frame.focus_set()
    try:
        e.set(rawString)
    except:
        pass

# updateNumber()
# 用于将小键盘输入的文本转换为数字待处理

def updateNumber():
    global rawString, calcNum, history
    # frame.focus_set()
    if rawString != '':
        calcNum = eval(rawString)
    else:
        rawString = '0'

# getHistory(index)
# 用于得到索引为 index 的历史记录数值

def getHistory(index):
    global calcNum, history
    updateNumber()
    calcNum = history.items[index]
    updateString()
    updateTextBox()

# updateString():
# 更新字符串的显示
# 并更新菜单栏中的历史记录数值
def updateString():
    global rawString, calcNum
    # frame.focus_set()
    rawString = str(calcNum)
    history.addItem(calcNum)
    historyMenu.delete(0, 10)
    historyMenu.add_command(label = '1 - ' + history.items[0], command = lambda: getHistory(0))
    historyMenu.add_command(label = '2 - ' + history.items[1], command = lambda: getHistory(1))
    historyMenu.add_command(label = '3 - ' + history.items[2], command = lambda: getHistory(2))
    historyMenu.add_command(label = '4 - ' + history.items[3], command = lambda: getHistory(3))
    historyMenu.add_command(label = '5 - ' + history.items[4], command = lambda: getHistory(4))
    historyMenu.add_command(label = '6 - ' + history.items[5], command = lambda: getHistory(5))
    historyMenu.add_command(label = '7 - ' + history.items[6], command = lambda: getHistory(6))
    historyMenu.add_command(label = '8 - ' + history.items[7], command = lambda: getHistory(7))
    historyMenu.add_command(label = '9 - ' + history.items[8], command = lambda: getHistory(8))
    historyMenu.add_command(label = '10 - ' + history.items[9], command = lambda: getHistory(9))

# clearAll()
# 用于清空所有输入信息
def clearAll():
    global calcNum, rawString
    rawString = '0'
    updateTextBox()
    updateNumber()

# pressNumberButton(numValue)
# 按下 numValue 对应的按键时触发
# 将文本框中的显示进行更新

def pressNumberButton(numValue):
    global rawString
    numStr = str(numValue)
    if not numStr in "0123456789":
        return
    if rawString == '0':
        rawString = numStr
    else:
        rawString += numStr
    updateTextBox()

# pressBackspaceButton()
# 删除最后一个字符
def pressBackspaceButton(event = ''):
    global rawString
    rawString = rawString[:-1]
    updateTextBox()



def pressDotButton():
    global rawString
    if not '.' in rawString:
        rawString += '.'
    updateTextBox()

def pressInverseButton(event = ''):
    global rawString
    if rawString[0] == '-':
        rawString = rawString.replace('-','')
    else:
        rawString = '-' + rawString
    updateNumber()
    updateTextBox()

def getKeyInput(event):
    # print 'Pressed', event.char
    if event.char == '0':
        pressNumberButton(0)
    elif event.char == '1':
        pressNumberButton(1)
    elif event.char == '2':
        pressNumberButton(2)
    elif event.char == '3':
        pressNumberButton(3)
    elif event.char == '4':
        pressNumberButton(4)
    elif event.char == '5':
        pressNumberButton(5)
    elif event.char == '6':
        pressNumberButton(6)
    elif event.char == '7':
        pressNumberButton(7)
    elif event.char == '8':
        pressNumberButton(8)
    elif event.char == '9':
        pressNumberButton(9)
    elif event.char == '0':
        pressNumberButton(0)
    elif event.char == '.':
        pressDotButton()
    else:
        pass

def getArgument(operationName = 'operationName', argumentDescription = 'argumentDescription'):
    r = askfloat('输入一个数', '操作“' + operationName + '”需要一个数作为“' + argumentDescription + '”。')
    return r

def operatorAdd():
    global calcNum
    updateNumber()
    try:
        calcNum = calcNum + getArgument('加法', '加数')
        updateString()
        updateTextBox()
    except:
        pass
def operatorMinus():
    global calcNum
    updateNumber()
    try:
        calcNum = calcNum - getArgument('减法', '减数')
        updateString()
        updateTextBox()
    except:
        pass

def operatorTimes():
    global calcNum
    updateNumber()
    try:
        calcNum = calcNum * getArgument('乘法', '乘数')
        updateString()
        updateTextBox()
    except:
        pass

def operatorDivide():
    global calcNum
    updateNumber()
    try:
        s = getArgument('除法', '除数')
        if s != 0:
            calcNum = calcNum * 1.0 / s
            updateString()
            updateTextBox()
        else:
            showerror('错误', '除数不应该为 0')
    except:
        pass

def operatorMod():
    global calcNum
    updateNumber()
    try:
        s = getArgument('取模', '模数')
        if s % 1 == 0 and calcNum % 1 == 0:
            calcNum = int(calcNum) % int(s)
            updateString()
            updateTextBox()
        else:
            showerror('错误', '必须对整数取模')
    except:
        pass

def operatorFactorial():
    global calcNum
    updateNumber()
    if calcNum >= 0 and calcNum % 1 == 0:
        try:
            calcNum = factorial(calcNum)
            updateString()
            updateTextBox()
        except OverflowError:
            showerror('错误', '数字太大。')
    else:
        showerror('错误', '未定义负数与小数的阶乘')

def operatorAbs():
    global calcNum
    updateNumber()
    calcNum = abs(calcNum)
    updateString()
    updateTextBox()

def operatorInverse():
    global calcNum
    updateNumber()
    calcNum = -calcNum
    updateString()
    updateTextBox()

def operatorBaiFenShu():
    global calcNum
    updateNumber()
    calcNum = calcNum / 100.0
    updateString()
    updateTextBox()

def operatorDaoGuoLai():
    global calcNum
    updateNumber()
    if calcNum != 0:
        calcNum = 1.0 / calcNum
        updateString()
        updateTextBox()
    else:
        showerror('错误', '取倒数操作无法作用于 0')

def operatorSiSheWuRu():
    global calcNum
    updateNumber()
    calcNum = int(round(calcNum))
    updateString()
    updateTextBox()

def operatorSheQuXiaoShu():
    global calcNum
    updateNumber()
    calcNum = int(calcNum)
    updateString()
    updateTextBox()

def operatorSin():
    global calcNum
    updateNumber()
    calcNum = sin(calcNum)
    updateString()
    updateTextBox()

def operatorCos():
    global calcNum
    updateNumber()
    calcNum = cos(calcNum)
    updateString()
    updateTextBox()

def operatorTan():
    global calcNum
    updateNumber()
    if cos(calcNum) != 0:
        calcNum = tan(calcNum)
        updateString()
        updateTextBox()
    else:
        showerror('错误', 'Tan 操作无法作用于此数')

def operatorCot():
    global calcNum
    updateNumber()
    if sin(calcNum) != 0:
        calcNum = cos(calcNum) / sin(calcNum)
        updateString()
        updateTextBox()
    else:
        showerror('错误', 'Cot 操作无法作用于此数')

def operatorSec():
    global calcNum
    updateNumber()
    if cos(calcNum) != 0:
        calcNum = 1.0 / cos(calcNum)
        updateString()
        updateTextBox()
    else:
        showerror('错误', 'Sec 操作无法作用于此数')

def operatorCsc():
    global calcNum
    updateNumber()
    if sin(calcNum) != 0:
        calcNum = 1.0 / sin(calcNum)
        updateString()
        updateTextBox()

def operatorArcSin():
    global calcNum
    updateNumber()
    if calcNum <= 1 and calcNum >= -1:
        calcNum = asin(calcNum)
        updateString()
        updateTextBox()
    else:
        showerror('错误', 'ArcSin 操作只能被作用于 [-1, 1] 内的数')

def operatorArcCos():
    global calcNum
    updateNumber()
    if calcNum <= 1 and calcNum >= -1:
        calcNum = acos(calcNum)
        updateString()
        updateTextBox()
    else:
        showerror('错误', 'ArcCos 操作只能被作用于 [-1, 1] 内的数')

def operatorArcTan():
    global calcNum
    updateNumber()
    calcNum = atan(calcNum)
    updateString()
    updateTextBox()

def operatorSinh():
    global calcNum
    updateNumber()
    calcNum = sinh(calcNum)
    updateString()
    updateTextBox()

def operatorCosh():
    global calcNum
    updateNumber()
    calcNum = cosh(calcNum)
    updateString()
    updateTextBox()

def operatorTanh():
    global calcNum
    updateNumber()
    calcNum = tanh(calcNum)
    updateString()
    updateTextBox()

def operatorAngToRad():
    global calcNum
    updateNumber()
    calcNum = calcNum * pi / 180.0
    updateString()
    updateTextBox()

def operatorRadToAng():
    global calcNum
    updateNumber()
    calcNum = calcNum * 180.0 / pi
    updateString()
    updateTextBox()

def operatorSquare():
    global calcNum
    updateNumber()
    try:
        calcNum = calcNum ** 2
        updateString()
        updateTextBox()
    except OverflowError:
        showerror('错误', '数字太大。')

def operatorCube():
    global calcNum
    updateNumber()
    try:
        calcNum = calcNum ** 3
        updateString()
        updateTextBox()
    except OverflowError:
        showerror('错误', '数字太大。')

def operatorAnyCiFang():
    global calcNum
    updateNumber()
    try:
        s = getArgument('次方', '次方数')
        calcNum = calcNum ** s
        updateString()
        updateTextBox()
    except OverflowError:
        showerror('错误', '数字太大。')
    except:
        pass

def operatorSqrt():
    global calcNum
    updateNumber()
    if calcNum >= 0:
        calcNum = calcNum ** 0.5
        updateString()
        updateTextBox()
    else:
        showerror('错误', '只能对正数开平方')

def operatorCuberoot():
    global calcNum
    updateNumber()
    calcNum = calcNum ** (1.0 / 3)
    updateString()
    updateTextBox()

def operatorAnyCiFangRoot():
    global calcNum
    updateNumber()
    try:
        if calcNum >= 0:
            s = getArgument('次方根', '开方次数')
            calcNum = calcNum ** (1.0 / s)
            updateString()
            updateTextBox()
        else:
            showerror('错误', '此操作仅对正数有效')
    except:
        pass

def operatorZiRanMiZhiShu():
    global calcNum
    updateNumber()
    try:
        calcNum = 2.718281828 ** calcNum
        updateString()
        updateTextBox()
    except OverflowError:
        showerror('错误', '数字太大。')

def operatorTwoMiZhiShu():
    global calcNum
    updateNumber()
    try:
        calcNum = 2 ** calcNum
        updateString()
        updateTextBox()
    except OverflowError:
        showerror('错误', '数字太大。')

def operatorTenMiZhiShu():
    global calcNum
    updateNumber()
    try:
        calcNum = 10 ** calcNum
        updateString()
        updateTextBox()
    except OverflowError:
        showerror('错误', '数字太大。')

def operatorAnyNumberMiZhiShu():
    global calcNum
    updateNumber()
    try:
        s = getArgument('幂指数', '底数')
        calcNum = s ** calcNum
        updateString()
        updateTextBox()
    except OverflowError:
        showerror('错误', '数字太大。')
    except:
        pass

def operatorZiRanDuiShu():
    global calcNum
    updateNumber()
    if calcNum > 0:
        calcNum = log(calcNum)
        updateString()
        updateTextBox()
    else:
        showerror('错误', '取对数操作只能被作用于正数')

def operatorTwoDuiShu():
    global calcNum
    updateNumber()
    if calcNum > 0:
        calcNum = log(calcNum) / log(2)
        updateString()
        updateTextBox()
    else:
        showerror('错误', '取对数操作只能被作用于正数')

def operatorTenDuiShu():
    global calcNum
    updateNumber()
    if calcNum > 0:
        calcNum = log(calcNum) / log(10)
        updateString()
        updateTextBox()
    else:
        showerror('错误', '取对数操作只能被作用于正数')

def operatorAnyDiDuiShu():
    global calcNum
    updateNumber()
    try:
        s = getArgument('取对数', '真数')
        if calcNum > 0 and s > 0 and s != 1:
            calcNum = log(calcNum) / log(s)
            updateString()
            updateTextBox()
        else:
            if s == 1:
                showerror('错误', '底数不能为 1')
            elif s <= 0:
                showerror('错误', '底数必须为正数')
            if calcNum <= 0:
                showerror('错误', '真数必须为正数')
    except:
        pass

def inputConst(const):
    global calcNum
    updateNumber()
    calcNum = const
    updateString()
    updateTextBox()

def exportTenResults():
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    outputText = "";
    for i in range(10):
        outputText += 'No.' + str(i + 1) + ':' + history.items[i] + "\n"
    f.write(outputText)
    f.close()

def clearHistory():
    history.items = []
    for i in range(history.length):
        history.items.append('0')
    updateNumber()
    updateString()

def aboutThisApp():
    showinfo('关于计算器', 'Based on Python 2.7.14 (v2.7.14:84471935ed)')
# 第五部分
# GUI 界面布局设计
root = Tk()

root.title('计算器')
root.resizable(0, 0)
root.bind('<Key>', getKeyInput)
root.bind('-', pressInverseButton)
root.bind('<BackSpace>', pressBackspaceButton)

e = StringVar()
# 针对 Windows 的菜单布局的 fix
if platform.system() == 'Windows':
    root.geometry("205x240")
    Entry(root, width = 21, state = 'readonly', textvariable = e).place(x = 25, y = 20)
else:
    root.geometry("210x195")
    Entry(root, width = 16, state = 'readonly', textvariable = e).place(x = 25, y = 20)
Button(root, text = ' 1 ', width = 4, height = 1, command = lambda: pressNumberButton(1)).place(x = 26, y = 59)
Button(root, text = ' 2 ', width = 4, height = 1, command = lambda: pressNumberButton(2)).place(x = 83, y = 59)
Button(root, text = ' 3 ', width = 4, height = 1, command = lambda: pressNumberButton(3)).place(x = 139, y = 59)
Button(root, text = ' 4 ', width = 4, height = 1, command = lambda: pressNumberButton(4)).place(x = 26, y = 90)
Button(root, text = ' 5 ', width = 4, height = 1, command = lambda: pressNumberButton(5)).place(x = 83, y = 90)
Button(root, text = ' 6 ', width = 4, height = 1, command = lambda: pressNumberButton(6)).place(x = 139, y = 90)
Button(root, text = ' 7 ', width = 4, height = 1, command = lambda: pressNumberButton(7)).place(x = 26, y = 120)
Button(root, text = ' 8 ', width = 4, height = 1, command = lambda: pressNumberButton(8)).place(x = 83, y = 120)
Button(root, text = ' 9 ', width = 4, height = 1, command = lambda: pressNumberButton(9)).place(x = 139, y = 120)
Button(root, text = ' 0 ', width = 4, height = 1, command = lambda: pressNumberButton(0)).place(x = 26, y = 150)
Button(root, text = ' . ', width = 4, height = 1, command = pressDotButton).place(x = 83, y = 150)
Button(root, text = ' ⇍ ', width = 4, height = 1, command = pressBackspaceButton).place(x = 139, y = 150)


# 注意 macOS 不支持根菜单目录的 add_command
m = Menu(root, tearoff = 0)
m.add_command(label = '清      空', command = clearAll)

Amenu = Menu(m, tearoff = 0)
m.add_cascade(label = '基本操作', menu = Amenu)
Amenu.add_command(label = '加...    +', command = operatorAdd)
Amenu.add_command(label = '减...    −', command = operatorMinus)
Amenu.add_command(label = '乘...    ×', command = operatorTimes)
Amenu.add_command(label = '除...    ÷', command = operatorDivide)
Amenu.add_command(label = '模...    %', command = operatorMod)
Amenu.add_separator()
Amenu.add_command(label = '倒数', command = operatorDaoGuoLai)
Amenu.add_command(label = '百分数', command = operatorBaiFenShu)
Amenu.add_command(label = '相反数', command = operatorInverse)
Amenu.add_command(label = '绝对值', command = operatorAbs)
Amenu.add_command(label = '阶乘', command = operatorFactorial)
Amenu.add_separator()
Amenu.add_command(label = '四舍五入取整', command = operatorSiSheWuRu)
Amenu.add_command(label = '舍去小数部分', command = operatorSheQuXiaoShu)

Bmenu = Menu(m, tearoff = 0)
m.add_cascade(label = '三角函数', menu = Bmenu)
Bmenu.add_command(label = '求正弦        Sin', command = operatorSin)
Bmenu.add_command(label = '求余弦        Cos', command = operatorCos)
Bmenu.add_command(label = '求正切        Tan', command = operatorTan)
Bmenu.add_command(label = '求余切        Cot', command = operatorCot)
Bmenu.add_command(label = '求正割        Sec', command = operatorSec)
Bmenu.add_command(label = '求余割        Csc', command = operatorCsc)
Bmenu.add_separator()
Bmenu.add_command(label = '求反正弦    ArcSin', command = operatorArcSin)
Bmenu.add_command(label = '求反余弦    ArcCos', command = operatorArcCos)
Bmenu.add_command(label = '求反正切    ArcTan', command = operatorArcTan)
Bmenu.add_separator()
Bmenu.add_command(label = '求双曲正弦   Sinh', command = operatorSinh)
Bmenu.add_command(label = '求双曲余弦   Cosh', command = operatorCosh)
Bmenu.add_command(label = '求双曲正切   Tanh', command = operatorTanh)
Bmenu.add_separator()
Bmenu.add_command(label = '弧度转角度', command = operatorRadToAng)
Bmenu.add_command(label = '角度转弧度', command = operatorAngToRad)

Cmenu = Menu(m, tearoff = 0)
m.add_cascade(label = '次方开方', menu = Cmenu)
Cmenu.add_command(label = '平方', command = operatorSquare)
Cmenu.add_command(label = '立方', command = operatorCube)
Cmenu.add_command(label = '任意次方...', command = operatorAnyCiFang)
Cmenu.add_separator()
Cmenu.add_command(label = '平方根', command = operatorSqrt)
Cmenu.add_command(label = '立方根', command = operatorCuberoot)
Cmenu.add_command(label = '任意次方根...', command = operatorAnyCiFangRoot)

Dmenu = Menu(m, tearoff = 0)
m.add_cascade(label = '对数指数', menu = Dmenu)
Dmenu.add_command(label = 'e 的幂指数', command = operatorZiRanMiZhiShu)
Dmenu.add_command(label = '2 的幂指数', command = operatorTwoMiZhiShu)
Dmenu.add_command(label = '10 的幂指数', command = operatorTenMiZhiShu)
Dmenu.add_command(label = '任意数的幂指数...', command = operatorAnyNumberMiZhiShu)
Dmenu.add_separator()
Dmenu.add_command(label = '自然对数', command = operatorZiRanDuiShu)
Dmenu.add_command(label = '以 2 为底的对数', command = operatorTwoDuiShu)
Dmenu.add_command(label = '以 10 为底的对数', command = operatorTenDuiShu)
Dmenu.add_command(label = '任意底对数...', command = operatorAnyDiDuiShu)

historyMenu = Menu(m, tearoff = 0)
m.add_cascade(label = '历史记录', menu = historyMenu)
historyMenu.add_command(label = '1 - ' + history.items[0], command = lambda: getHistory(0))
historyMenu.add_command(label = '2 - ' + history.items[1], command = lambda: getHistory(1))
historyMenu.add_command(label = '3 - ' + history.items[2], command = lambda: getHistory(2))
historyMenu.add_command(label = '4 - ' + history.items[3], command = lambda: getHistory(3))
historyMenu.add_command(label = '5 - ' + history.items[4], command = lambda: getHistory(4))
historyMenu.add_command(label = '6 - ' + history.items[5], command = lambda: getHistory(5))
historyMenu.add_command(label = '7 - ' + history.items[6], command = lambda: getHistory(6))
historyMenu.add_command(label = '8 - ' + history.items[7], command = lambda: getHistory(7))
historyMenu.add_command(label = '9 - ' + history.items[8], command = lambda: getHistory(8))
historyMenu.add_command(label = '10 - ' + history.items[9], command = lambda: getHistory(9))

MathConstMenu = Menu(m, tearoff = 0)
m.add_cascade(label = '数学常数', menu = MathConstMenu)

MathConstMenu.add_command(label = '圆周率', command = lambda: inputConst(3.14159265358979324))
MathConstMenu.add_command(label = '自然对数的底数', command = lambda: inputConst(2.71828182845905))
MathConstMenu.add_separator()
ShuLun = Menu(MathConstMenu, tearoff = 0)
MathConstMenu.add_cascade(label = '数论', menu = ShuLun)
ShuLun.add_command(label = 'MRB 常数', command = lambda: inputConst(1.60669515241529))
ShuLun.add_command(label = '阿拉底-格林斯蒂德常数', command = lambda: inputConst(0.8093940205))
ShuLun.add_command(label = '艾狄胥-波温常数', command = lambda: inputConst(1.60669515241529))
ShuLun.add_command(label = '波特常数', command = lambda: inputConst(1.4670780794))
ShuLun.add_command(label = '恩布里-特勒菲森常数', command = lambda: inputConst(0.70258))
ShuLun.add_command(label = '哥伦布-迪克曼常数', command = lambda: inputConst(0.624329988543551))
ShuLun.add_command(label = '海芙纳-萨纳克-麦克理常数', command = lambda: inputConst(0.353236371854996))
ShuLun.add_command(label = '拉马努金-索德耐尔常数', command = lambda: inputConst(1.45136923488338))
ShuLun.add_command(label = '兰道-拉马努金常数', command = lambda: inputConst(0.76422365378221))
ShuLun.add_command(label = '利维常数', command = lambda: inputConst(3.27582291872181))
ShuLun.add_command(label = '孪生素数常数', command = lambda: inputConst(0.66016181584687))
ShuLun.add_command(label = '梅塞尔-梅尔滕斯常数', command = lambda: inputConst(0.261497212847643))
ShuLun.add_command(label = '米尔斯常数', command = lambda: inputConst(1.30637788386308))
ShuLun.add_command(label = '尼文常数', command = lambda: inputConst(1.70521114010537))
ShuLun.add_command(label = '双胞胎素数的布朗常数', command = lambda: inputConst(1.9021605823))
ShuLun.add_command(label = '四胞胎素数的布朗常数', command = lambda: inputConst(0.87058838))
ShuLun.add_command(label = '塑性常数', command = lambda: inputConst(1.32471795724475))
ShuLun.add_command(label = '维斯瓦纳斯常数', command = lambda: inputConst(1.13198824))
ShuLun.add_command(label = '辛钦常数', command = lambda: inputConst(2.68545200106531))

ShuXue = Menu(MathConstMenu, tearoff = 0)
MathConstMenu.add_cascade(label = '数学', menu = ShuXue)
ShuXue.add_command(label = '阿培里常数', command = lambda: inputConst(1.20205690315959))
ShuXue.add_command(label = '巴克豪斯常数', command = lambda: inputConst(1.45607494858269))
ShuXue.add_command(label = '黄金分割常数', command = lambda: inputConst(1.61803398874989))
ShuXue.add_command(label = '卡亨常数', command = lambda: inputConst(0.6434105463))
ShuXue.add_command(label = '拉普拉斯极限', command = lambda: inputConst(0.662743419349182))
ShuXue.add_command(label = '欧拉常数', command = lambda: inputConst(0.577215664901533))
ShuXue.add_command(label = '通用抛物线常数', command = lambda: inputConst(2.29558714939264))
ShuXue.add_command(label = '谢尔宾斯基常数', command = lambda: inputConst(2.58498175957925))
ShuXue.add_command(label = '圆周率', command = lambda: inputConst(3.14159265358979324))
ShuXue.add_command(label = '自然对数的底数（欧拉数）', command = lambda: inputConst(2.71828182845905))

ShuXueFenXi = Menu(MathConstMenu, tearoff = 0)
MathConstMenu.add_cascade(label = '数学分析', menu = ShuXueFenXi)
ShuXueFenXi.add_command(label = '巴克豪斯常数', command = lambda: inputConst(0.280169499023869))
ShuXueFenXi.add_command(label = '弗朗森-罗宾逊常数', command = lambda: inputConst(2.80777024202852))
ShuXueFenXi.add_command(label = '欧米伽常数', command = lambda: inputConst(0.567143290409784))

ZuHeXue = Menu(MathConstMenu, tearoff = 0)
MathConstMenu.add_cascade(label = '组合学', menu = ZuHeXue)
ZuHeXue.add_command(label = '高斯-库兹明-维尔辛常数', command = lambda: inputConst(0.303663002898733))
ZuHeXue.add_command(label = '卡塔兰常数', command = lambda: inputConst(0.915965594177219))
ZuHeXue.add_command(label = '李布方冰常数', command = lambda: inputConst(1.5396007178))
ZuHeXue.add_command(label = '耶尔常数', command = lambda: inputConst(1.0986858055))

PhysicsConstMenu = Menu(m, tearoff = 0)
m.add_cascade(label = '物理常数', menu = PhysicsConstMenu)

TianTiWuLi = Menu(PhysicsConstMenu, tearoff = 0)
PhysicsConstMenu.add_cascade(label = '天体物理学', menu = TianTiWuLi)
TianTiWuLi.add_command(label = '地球赤道半径（米）', command = lambda: inputConst(6378137))
TianTiWuLi.add_command(label = '地球的施瓦茨希尔德半径（2GM/C²）', command = lambda: inputConst(0.00887005622))
TianTiWuLi.add_command(label = '地球公转周期（恒星年）（秒）', command = lambda: inputConst(31558149.8))
TianTiWuLi.add_command(label = '地球公转周期（回归年）（秒）', command = lambda: inputConst(31556925.2))
TianTiWuLi.add_command(label = '地球质量（千克）', command = lambda: inputConst(5.9722e+24))
TianTiWuLi.add_command(label = '地球自转周期（秒）', command = lambda: inputConst(86164.09053))
TianTiWuLi.add_command(label = '一光年（米）', command = lambda: inputConst(9.4607304725808e+15))
TianTiWuLi.add_command(label = '秒差距（米）', command = lambda: inputConst(3.08568025e+16))
TianTiWuLi.add_command(label = '太阳表面温度（开）', command = lambda: inputConst(5778))
TianTiWuLi.add_command(label = '太阳赤道半径（米）', command = lambda: inputConst(695500000))
TianTiWuLi.add_command(label = '太阳的施瓦茨希尔德半径（2GM/C²）', command = lambda: inputConst(2953.25008))
TianTiWuLi.add_command(label = '太阳光度（瓦）', command = lambda: inputConst(3.839e+26))
TianTiWuLi.add_command(label = '太阳质量（千克）', command = lambda: inputConst(1.98892e+30))
TianTiWuLi.add_command(label = '一天文单位（米）', command = lambda: inputConst(149597870700))
TianTiWuLi.add_command(label = '央斯基（央）（W·Hz/m²）', command = lambda: inputConst(1e-26))
TianTiWuLi.add_command(label = '宇宙背景辐射温度（开）', command = lambda: inputConst(2.725))

WuLiHuaXue = Menu(PhysicsConstMenu, tearoff = 0)
PhysicsConstMenu.add_cascade(label = '物理化学', menu = WuLiHuaXue)
WuLiHuaXue.add_command(label = '阿伏伽德罗常数（1/mol）', command = lambda: inputConst(6.02214129e+23))
WuLiHuaXue.add_command(label = '玻尔兹曼常数（J/K）', command = lambda: inputConst(1.3806488e-23))
WuLiHuaXue.add_command(label = '第二辐射常数（m·K）', command = lambda: inputConst(0.01438777))
WuLiHuaXue.add_command(label = '第一辐射常数（W·m²）', command = lambda: inputConst(3.74177153e-16))
WuLiHuaXue.add_command(label = '第一辐射常数(光谱辐射)（W·m²/sr）', command = lambda: inputConst(1.191042869e-16))
WuLiHuaXue.add_command(label = '法拉第常数（C/mol）', command = lambda: inputConst(96485.3365))
WuLiHuaXue.add_command(label = '理想气体的摩尔体积（0℃，273.15K，100kPa）（m³/mol）', command = lambda: inputConst(0.022710953))
WuLiHuaXue.add_command(label = '理想气体的摩尔体积（0℃，273.15K，101.325kPa）（m³/mol）', command = lambda: inputConst(0.022413968))
WuLiHuaXue.add_command(label = '理想气体的摩尔体积（20℃，273.15K，101.325kPa）（m³/mol）', command = lambda: inputConst(0.024055115))
WuLiHuaXue.add_command(label = '洛施米特常数（1/m³）', command = lambda: inputConst(2.6867805e+25))
WuLiHuaXue.add_command(label = '普适气体常数（J/K/mol）', command = lambda: inputConst(8.3144621))
WuLiHuaXue.add_command(label = '斯特蕃-玻尔兹曼常数（W/m²/K⁴）', command = lambda: inputConst(5.670373e-8))
WuLiHuaXue.add_command(label = '维恩位移定律常数（m·K）', command = lambda: inputConst(0.0028977721))
WuLiHuaXue.add_command(label = '原子质量单位（u）（千克）', command = lambda: inputConst(1.660538921e-27))

YuZhouXue = Menu(PhysicsConstMenu, tearoff = 0)
PhysicsConstMenu.add_cascade(label = '宇宙学', menu = YuZhouXue)
YuZhouXue.add_command(label = '普朗克常数（J·s）', command = lambda: inputConst(6.62606957e-34))
YuZhouXue.add_command(label = '万有引力常数（m³/kg/s²）', command = lambda: inputConst(6.67384e-11))
YuZhouXue.add_command(label = '约化普朗克常数（J·s）', command = lambda: inputConst(1.054571726e-34))
YuZhouXue.add_command(label = '真空中光速（m/s）', command = lambda: inputConst(299792458))

HunDunLiLun = Menu(PhysicsConstMenu, tearoff = 0)
PhysicsConstMenu.add_cascade(label = '混沌理论', menu = HunDunLiLun)
HunDunLiLun.add_command(label = '第一费根鲍姆常数', command = lambda: inputConst(4.66920160910299))
HunDunLiLun.add_command(label = '第二费根鲍姆常数', command = lambda: inputConst(2.50290787509589))

DianCiXue = Menu(PhysicsConstMenu, tearoff = 0)
PhysicsConstMenu.add_cascade(label = '电磁学', menu = DianCiXue)
DianCiXue.add_command(label = '玻尔磁子（J/T）', command = lambda: inputConst(9.27400968))
DianCiXue.add_command(label = '磁通量子（Wb）', command = lambda: inputConst(2.067833758e-15))
DianCiXue.add_command(label = '电导量子（1/Ω）', command = lambda: inputConst(7.7480917346e-5))
DianCiXue.add_command(label = '电导量子的倒数（Ω）', command = lambda: inputConst(12906.4037217))
DianCiXue.add_command(label = '核磁子（J/T）', command = lambda: inputConst(5.05078353e-27))
DianCiXue.add_command(label = '元电荷的电荷量（C）', command = lambda: inputConst(1.602176565e-19))
DianCiXue.add_command(label = '克里青常数（Ω）', command = lambda: inputConst(25812.8074434))
DianCiXue.add_command(label = '库伦常数（N·m²/C²）', command = lambda: inputConst(8987551787.36818))
DianCiXue.add_command(label = '约瑟夫逊常数（Hz/V）', command = lambda: inputConst(483597870000000))
DianCiXue.add_command(label = '真空磁导率（N/A²）', command = lambda: inputConst(1.25663706143592e-6))
DianCiXue.add_command(label = '真空介电常数（F/m）', command = lambda: inputConst(8.85418781762039e-12))
DianCiXue.add_command(label = '真空阻抗（Ω）', command = lambda: inputConst(376.730313461771))

CaiYongZhi = Menu(PhysicsConstMenu, tearoff = 0)
PhysicsConstMenu.add_cascade(label = '采用值', menu = CaiYongZhi)
CaiYongZhi.add_command(label = '标准大气压（帕）', command = lambda: inputConst(101325))
CaiYongZhi.add_command(label = '标准重力加速度（m/s²）', command = lambda: inputConst(9.80665))
CaiYongZhi.add_command(label = '摩尔质量常数（kg/mol）', command = lambda: inputConst(0.001))
CaiYongZhi.add_command(label = 'C¹²的摩尔质量（kg/mol）', command = lambda: inputConst(0.012))

ZaQiZaBa = Menu(m, tearoff = 0)
m.add_cascade(label = '杂七杂八', menu = ZaQiZaBa)
ZaQiZaBa.add_command(label = '导出最近的 10 个结果...', command = exportTenResults)
ZaQiZaBa.add_command(label = '清空历史记录', command = clearHistory)
ZaQiZaBa.add_separator()
ZaQiZaBa.add_command(label = '关于计算器...', command = aboutThisApp)

root.config(menu = m)

clearAll()

root.mainloop()
