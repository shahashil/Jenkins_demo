import sys
input_2=""
n = input()
m=0
l=0
array=[]
main_array={}
for i in range (0,n):
    inp=raw_input()
    array=(inp.split())
    main_array[array[0]] = array[1]
for i in range(0,n):
    take = raw_input()
    if take in main_array :
        print (take+"="+main_array[take])
    else :
        print ("Not found")
