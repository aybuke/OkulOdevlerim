def insertionSort(alist):
    karsilastirma=0
    yerdegistirme=0
    for index in range(0,len(alist)):
        karsilastirma=karsilastirma+1
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
          yerdegistirme=yerdegistirme+1
          alist[position]=alist[position-1]
          position = position-1
        alist[position]=currentvalue
    print("karsilastirma sayisi :",karsilastirma)
    print("yerdegistirme sayisi :" ,yerdegistirme)


def createAnArray(size):
    import random
    array=[]
    for i in range(0,size):
        array.append(int(random.uniform(-1000,1000)))
    return array
size=int(input("size ?"))
alist=createAnArray(size)
import time
t_start=time.time()
insertionSort(alist)
t_end=time.time()

for i in range(0,len(alist)):
    print(i,".item",alist[i])
print("n kare",size*size,"time:",t_end-t_start)
