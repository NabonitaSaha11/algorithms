# -*- coding: utf-8 -*-
"""task1A

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZaqpY8LwirfmfkcuOum3ls7-6036HF9o
"""

input=open("input1a_1.txt","r")
output=open("output1a_1.txt","w")
n=input.readline()
vertices=n[0]

import numpy as np
arr=np.zeros((int(vertices)+1,int(vertices)+1),dtype=int)


for i in range(int(n[2])):
  new=input.readline().split()
  row=new[0]
  col=new[1]
  val=new[2]
  arr[int(row)][int(col)]=val
for i in range ((int(vertices)+1)):
  for j in range((int(vertices)+1)):
    output.write(str(arr[i][j])+" ")

  output.write("\n")