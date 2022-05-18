import time
t= int(input("enter your time in second:- "))
while t:
    mins,sec=divmod(t,60)
    timer='{:02d}:{:02d}'.format(mins,sec)
    print(timer)
    time.sleep(1)
    t-=1
print("done!")