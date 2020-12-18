from functools import reduce
lis=[1,2,3,4,5]
sum=reduce(lambda a,b:a+b,lis)
print(sum)
