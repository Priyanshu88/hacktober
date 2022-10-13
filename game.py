a="round."
b="lot of"
c="dust."
print("Earth is")
print(a)
print("Moon has",b,c)
age=input("Enter age")
x=age*2
print(x)
a=1
for i in range(10):
    a=a+(i+1)
print(a)
n=20/10*0
if(n<0):
    print("a")
if(n>0):
    print("b")
if(n==0):
    print("c")
a=0
while(a<10):
    a=a+2
    print(a)
for i in range(1,11):
    if(i%2==0):
        print(i)
L=['Practice','makes','the','man','perfect.']
L.sort()
for e in L:
    print(e)
l=['we','were','here','together']
for i in range(3):
    print(l[i])
l=[]
for i in range(5):
    if(i%2==0):
        l.append("Even")
    else:
        l.append("Odd")
print(l)
import random
l=[]
for i in range(10):
    l.append(random.randint(0,10))
l.sort()
l.reverse()
print(l)
def sum(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    return t

l=[1,2,3,4,5,6,7,8,9,10]
to=sum(l)
print(to)
with open('file.txt','w') as file:
    file.write('hey there!!')
file.close()

with open('file.txt','a') as file:
    file.write('writing this file again')

with open('file.txt','r') as file:
    print(file.read())
with open('file.txt','w') as file:
    file.write('100111011')
file.close()

with open('file.txt','r') as file:
    L=list(file.read())
file.close()

for i in range(len(L)):
    if(i%2==0)and(L[i]=='0'):
        L[i]='1'
    if(i%2!=0)and(L[i]=='1'):
        L[i]='0'
print(L)

