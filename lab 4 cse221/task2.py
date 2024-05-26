# -*- coding: utf-8 -*-
"""task2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NiHBDGYdqL3_lThrXsKLzoJTO-2Et0fd
"""

input=open("input2_2.txt","r")
output=open("output2_2.txt","w")
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

start="1"
visited=set()
queue=[]
queue.append(start)

while len(queue)!=0:
  curr=queue.pop(0)
  visited.add(curr)
  output.write(curr+" ")
  for val in adjacent_list[curr]:
    if val not in visited:
      queue.append(val)
      visited.add(val)

input.close()
output.close()