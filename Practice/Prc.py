# Number_1=int(input("Please enter 1st number"))
# Number_2=int(input("Please enter 2nd number: "))
# Number_3=int(input("Please enter the 3rd number: "))
# if abs(Number_2-Number_1)==1 or abs(Number_2-Number_1)==1:
#   if abs(Number_2-Number_3)>=2 or abs(Number_3-Number_2)>=2:
#     print(True)
#   else:
#     print(False)
# else:1
#   print(False)

import csv
a=[1,2,3,4]
b=[7,8,"",10]

# d=list(zip(a,b))
with open('C:\\Users\\Jayendra\\Desktop\\Chrome\\trial.csv','w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(["Col1","Col2"])
    for i,j in zip(a,b):
        csvwriter.writerow([i,j])