# arr=range(1,11)
# print(arr[0])
# print(arr[1])
# print(arr[2])
#
# for number in arr:
#     print('안녕',number)

# arr=[1,2,3,4,5,6,7,8,9,10]
# for x in arr:
#     print(x)



# result=0
# arr=[1,2,3,4,5,6,7,8,9,10]
# for x in arr:
#     result=result+x
# print(result)

# result=0
# for x in range(1,101):
#     result+=x
# print(result)

# for x in range(1,101):
#     if (x % 2)==0:
#         print(x)

# for x in range(1,101):
#     if (x % 2)==1:
#         print(x)

#기초문법
# #1 ~ 5
# for x in range(1, 6):
#     print(x,end='')
#
#     for y in range(1, 6):
#         print(y,end='')
#
#     print()


# 1
# 12
# 123
# 1234
# 12345
for x in range(1, 6):
    for y in range(1, x+1):
        print(y, end='')
    print()

