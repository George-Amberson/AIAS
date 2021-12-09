import random
import pyperclip as clipboard 
import subprocess as sbp
import matplotlib.pyplot  as plt
import numpy as np
from scipy.signal import savgol_filter
def handinput():
    str=""
    print("Введите строку: ", end="")
    str=input()
    return str

def generateinput(_type=0, _letters="", _len=0):
    _str=""
    random.seed()
    if(not(_type)):
        print("Введите буквы из которых будет сгенерирована строка без пробелов одной строкой: ", end="")
        letters=input()
        print("Введите желаемую длинну строки: ", end="")
        len=int(input())
        for i in range(len):
            _str+=letters[random.randint(0,len)]
    else:
        _str=str(2)+" "+_letters+" "+str(_len)
    return _str

def concatenateinput(_type=0, _word="", _k=0):
    _str=""
    if(not(_type)):
        print("Введите конкатенируемое слово: ", end="")
        word=input()
        print("Введите степень конкатенации: ", end="")
        k=int(input())
        for i in range(k):
            _str+=word
    else:
        word = _word
        k=_k
        _str="3"+" "+word+" "+str(k)
    return _str
    

def handtesting():   
    strArray=["",""]
    for i in range(2):
        print("Выберите тип задания строки\n1-непосредственный ввод\n2-образование слов из равновероятно встречающихся букв\n3-образование конкатенированного к раз слова из s введенных букв: ", end="")
        Type=int(input())
        if(Type==1): strArray[i]=handinput()
        elif(Type==2): strArray[i]=generateinput()
        elif(Type==3): strArray[i]=concatenateinput()
    clipboard.copy("0"+" "+strArray[0]+' '+strArray[1])
    r =sbp.run(r"..\Release\MathPart.exe", stdout=sbp.PIPE).stdout
    print("results: {0}nanosec for NaiveAlgorithm {1}nanosec for KMPAlgorithm".format(float(r[2:r.find(' ')]),float(r[r.find(' ')+1:len(r)-1])))


def grafick(t_x,t1_y,t2_y,name):
    t1_y = savgol_filter(t1_y, 51, 3)
    t2_y=savgol_filter(t2_y, 51, 3)
    plt.figure(name[-1],figsize=(5,5))
    plt.title(name)
    plt.plot(t_x,t1_y, 'r', label='NaiveAlgorithm')
    plt.plot(t_x,(t2_y),'b', label="KMPAlgorithm")
    plt.legend()
    plt.show()

def test3():
    _str,substr="",""
    t1_x,t1_y,t2_y=[],[],[]
    for i in range(1,1000000+1,10000):
        _str=concatenateinput(_type=1,_word="aaaaab", _k=i)
        substr=concatenateinput(_type=1,_word="aaaaa", _k=1)
        clipboard.copy("1"+" "+_str+" "+substr)
        result =sbp.run(r"..\Release\MathPart.exe", stdout=sbp.PIPE, stderr=sbp.PIPE)
        r=str(result.stdout)
        print(r)
        t1_x.append(i)
        t1_y.append(float(r[2:r.find(' ')]))
        t2_y.append(float(r[r.find(' ')+1:len(r)-1]))
    grafick(t_x=t1_x,t1_y=t1_y,t2_y=t2_y,name="Test 3")
   


def test1():
    _str,substr="",""
    t1_x,t1_y,t2_y=[],[],[]
    for i in range(1,1011,10):
        _str=concatenateinput(_type=1,_word="ab", _k=i*1000)
        substr=concatenateinput(_type=1,_word="ab", _k=i)
        clipboard.copy("1"+" "+_str+" "+substr)
        result =sbp.run(r"..\Release\MathPart.exe", stdout=sbp.PIPE, stderr=sbp.PIPE)
        r=str(result.stdout)
        print(r)
        t1_x.append(i)
        t1_y.append(float(r[2:r.find(' ')]))
        t2_y.append(float(r[r.find(' ')+1:len(r)-1]))
    grafick(t_x=t1_x,t1_y=t1_y,t2_y=t2_y,name="Test 1")
  

def test2():
    _str,substr="",""
    t1_x,t1_y,t2_y=[],[],[]
    for i in range(1,1010001,10000):
        _str=generateinput(_type=1,_letters="ab",_len=1000001)
        substr=concatenateinput(_type=1,_word="a",_k=i)
        clipboard.copy("1 "+_str+" "+substr)
        result =sbp.run(r"..\Release\MathPart.exe", stdout=sbp.PIPE, stderr=sbp.PIPE)
        r=str(result.stdout)
        print(r)
        t1_x.append(i)
        t1_y.append(float(r[2:r.find(' ')]))
        t2_y.append(float(r[r.find(' ')+1:len(r)-1]))
    grafick(t_x=t1_x,t1_y=t1_y,t2_y=t2_y,name="Test 2")
    
test1()
test2()
test3()


