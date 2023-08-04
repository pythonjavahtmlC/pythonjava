#!/usr/bin/python3
#别人可能做过这个代码，但是这是我自己写出来的，没有看过其他任何人的代码，所一不要怀疑是我抄袭了你的代码。
import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "当前时间:" + time.asctime(t)
 
print(str);    
