
'''   PART1:
What does this stuff mean: *args, **kwargs? And why would we use it?'''



'''   PART2:
Write down what these functions calls return ?'''



def f(*args,**kwargs):
    print(args, kwargs)

l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}

#f(1,2,3)
#f(1,2,3,"groovy")
#f(a=1,b=2,c=3)
#f(a=1,b=2,c=3,zzz="hi")
#f(1,2,3,a=1,b=2,c=3)
#f(*l,**d)
#f(*t,**d)
#f(1#,2,*t)
#f(q="winning",**d)
#f(1,2,*t,q="winning",**d)

#---------------------------------------------------------------------------------------------------


def f2(arg1,arg2,*args,**kwargs):
    print(arg1,arg2, args, kwargs)

#f2(1,2,3)
#f2(1,2,3,"groovy")
#f2(arg1=1,arg2=2,c=3)
#f2(arg1=1,arg2=2,c=3,zzz="hi")
#f2(1,2,3,a=1,b=2,c=3)