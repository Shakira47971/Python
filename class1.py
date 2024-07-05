print("Hello world")
#comment
x=7
y=7
c=x+y
print(c)
print(type(x))
n="shakira"
print (len(n))
x=str("hello")
print(x+str(y))
x=f"I am Shakira {y}"
print(x)
if(x==y):
    print("true")
nEven=0
nOdd=0
Sum=0
e=[]
o=[]
i=1
while i<=100:
    if i%2==0:
          nEven=nEven+1
          e.append(i)
         

         
         
    else:
          nOdd=nOdd+1
          o.append(i)
         
         
    i+=1
print("Even Number Total:",nEven)
print("Odd Number Total:",nOdd)

for even in e:
    print(even)
    Sum=sum(e)
print("Sum of Even Number:",Sum)

print("Odd number:")   
for odd in o:
    print(odd)
    Sum=sum(o)
print("Sum of Odd Number:",Sum)


for i in range(1,101,2):
    print( i)
