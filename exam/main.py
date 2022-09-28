#Task 1:
list = ['b' , 'd' , 'g' , 'a' , 'z']
print(list)

for i in range(0,len(list)) :
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

print(list)

#Task 2:

date1 = input("please enter first date")
date2 = input("please enter second date")

spildate1 = date1.split("/")
spildate2 = date2.split("/")
print(int(spildate1[2])-int(spildate2[2]),'Years,',int(spildate1[1])-int(spildate2[1]),'Month,',int(spildate1[0])-int(spildate2[0]),'Days')
#Task 3:
number = input('Please enter number')
for i in number:
    if (int(i) % int(number)) == 0:
        output ='NO'
        break
    else:
        output ='Yes'

print(output)