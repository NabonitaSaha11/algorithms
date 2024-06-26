# -*- coding: utf-8 -*-
"""task3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NpJRCmYNFCm0TmK-hUEYmrQqsaO2OP2B
"""

input=open("input3_1.txt","r")
output=open("output3_1.txt","w")
n=input.readline().split()

new=[]
for val in range(int(n[1])):
  new.append(input.readline().split())

adjacent_list={}
for u,v in new:
  if u not in adjacent_list:
    adjacent_list[u]=[v]
  else:
    adjacent_list[u].append(v)
  if v not in adjacent_list:
    adjacent_list[v]=[u]
  else:
    adjacent_list[v].append(u)


visited=set()
start="1"
stack1=[]
stack1.append(start)

while len(stack1)!=0:
  curr=stack1.pop()
  if curr not in visited:
    output.write(curr+" ")
    visited.add(curr)

    for val in adjacent_list[curr]:
      if val not in visited:
        stack1.append(val)

input.close()
output.close()