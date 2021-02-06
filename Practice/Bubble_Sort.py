def Buuble_sort(num):
    for i in (len(num )-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp

def Selection_sort(num):
    for i in range(len(num)-1):
        mins=i
        for j in range(i,len(num)):
            if num[j]<num[mins]:
                mins=j

        temp = num[i]
        num[i] = num[mins]
        num[mins] = temp


nums=[90,73,88,76,47,25]
# Buuble_sort(nums)
# print(nums)
#
# Selection_sort(nums)
# print(nums)

def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        print(anchor)
        j = i - 1
        while j>=0 and anchor < elements[j]:
            print(anchor)
            print(elements[j])
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor

elements = [15,45,29,10,9,15,28]
insertion_sort(elements)
print(elements)