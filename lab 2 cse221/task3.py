# -*- coding: utf-8 -*-
"""task3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XRAYymYzlt_WAXDwb4_BES1pliJpIeeL

Task 03
"""

with open("input3.txt","r") as file :
  content=file.read()

with open("input3.txt","r") as file :
  value=file.readline()
  list1=[]

  for i in range(int(value)):
    list1.append(file.readline().split())


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)
def merge(left,right):
    merged=[]
    i = j = 0
    while i < len(left) and j < len(right):
        if int(left[i][1]) <= int(right[j][1]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged

final=mergesort(list1)


count=0
new=[]
with open("output3.txt","w") as file:
   for i in range(len(final)):
     if i==0:
      new.append(final[i])
      count+=1
     else:
      if new[-1][1]<=final[i][0]:
        new.append(final[i])
        count+=1


   file.write(str(count))
   file.write("\n")
   for i in new:
    for val in i:
      file.write(str(val))
      file.write(" ")
    file.write("\n")