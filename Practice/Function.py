# def pos_neg_sort(list1):
#     A = list1
#     for i in range(0, len(A) - 1):
#         if A[i] < 0:
#             continue
#         for j in range(i + 1, len(A)):
#             if A[j] < 0:
#                 continue
#             else:
#                 if A[i] > A[j]:
#                     temp = A[i]
#                     A[i] = A[j]
#                     A[j] = temp
#     return A
#
#
# Fin=pos_neg_sort([6, 3, -2, 5, -8, 2, -2])
# print(Fin)

# def first_n_vowels(str1,n):
#     li=[]
#     vo_W=["a","i","e","o","u"]
#     for i in range(0,len(str1)):
#         if str1[i] in vo_W:
#             li.append(str1[i])
#             if len(li)==n:
#                 return li
#                 break
#
#     if len(li) < n:
#         return "invalid"
# print(first_n_vowels("major league", 5))

def electricity_bill(bill):
    total=0
    for i in range(1,bill+1):
        if i<=100:

            total=total+1
            print(i)
            print(total)
        elif i>100 and i<=200 :
            total=total+2
        elif i>200 and i<=300:
            total = total + 3
        elif i > 300 and i<= 500:
            total=total+4
        elif i > 500:
            total=total+4
    tax=total/10
    total=total+tax
    total=total+15
    return total

print(electricity_bill(300))







