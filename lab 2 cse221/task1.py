# -*- coding: utf-8 -*-
"""task1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jvS8p8thEIBMjhYOEFHAFMd9CMRbDx6B
"""

#TASK 01 ER 1

input=open("input1a.txt","r")
output=open("output1a.txt","w")

line1=input.readline().split()
#print(line1)

n=int(line1[0])
target=int(line1[1])
numbers=input.readline().split()
#print(numbers)
available=False
for i in range(int(line1[0])):
  for j in range(int(i)+1,int(line1[0])):
    sum=int(numbers[i])+int(numbers[j])
    if sum==target:
      output.write(str(i+1)+" "+str(j+1))
      available=True
  if available==True:
      break
if available==False:
  output.write("IMPOSSIBLE")
input.close()
output.close()

#task 01 er 02

input=open("input1b.txt","r")
output=open("output1b.txt","w")

line1=input.readline().split()
#print(line1)

n=int(line1[0])
target=int(line1[1])
numbers=input.readline().split()
#print(numbers)
left=0
right=len(numbers)-1
while left<right:
  sum=int(numbers[left])+int(numbers[right])
  if sum==target:
    output.write(str(left+1)+" "+str(right+1))
    break
  elif sum>target:
    right=right-1
  elif sum<target:
    left=left+1
if right<=left and sum!=target:
  output.write("IMPOSSIBLE")
input.close()
output.close()