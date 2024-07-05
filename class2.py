def  mul(a,b):
    print(a*b)
mul(4,5)
def sum(a,b):
    print(a+b)
    print(f"sum of {a}+{b} is{a+b}")
sum(4,5)

x=lambda a:a/100*10000
print(x(5))
eList=['1','2','3']
print(eList[0])
eList.pop()
print(eList)
eList.pop(1)
print(eList)
eList.append(4)
print(eList)
List=[1,2,3,4,'c']
sum=0
for item in List:
    try:
  
        Sum=sum+item
    except:
         print("error")
         continue
    print(sum)