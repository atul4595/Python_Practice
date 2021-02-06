# def is_alogrism(str1):
#     for i in range(0,len(str1)):
#         if (str1.lower()).count(str1[i].lower())>1:
#             return False
#
#     else:
#         return True
#
# print(is_alogrism("PasSword"))
# def list_of_multiples(n1,n2):
#     st_1=n1
#     st_2=n2
#     l1=[]
#     i=1
#     while i<=st_2:
#         l1.append(st_1*i)
#         i=i+1
#     return l1
# print(list_of_multiples(12, 10))
# def cap_space(x):
#     """This is a recursive function
#     to find the factorial of an integer"""
#     str1=""
#     for i in range(0,len(x)):
#         if x[i].isupper():
#             str1=str1+" "+x[i].lower()
#         else:
#             str1 = str1 + x[i]
#     return str1
# print(cap_space("iLoveMyTeapot"))

def even_odd_transform(inpu,n):
    if n>0:
        li = []
        for i in range(0,len(inpu)):
            if inpu[i]%2==0:
                li.append(inpu[i]-2)
            else:
                li.append(inpu[i] +2)

        n=n-1
        print("current value of n: " ,n)
        print(li)
        if n==0:
            return li
        else:
            # return even_odd_transform(li,n)
            print("MESSAGE")
            even_odd_transform(li,n)


print(even_odd_transform([3, 4, 9], 3))



