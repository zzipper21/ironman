# class JSS:
#     def __init__(self):
#         self.name=input('이름:')
#         self.age=input('나이:')
#     def show(self):
#         print('나의 이름은 {}, 나이는 {}세 입니다.'.format(self.name, self.age))
# a=JSS()
# a.show()
#
# class JSS2(JSS):
#     def __init__(self):
#         self.name=input('이름:')
#         self.age+input('나이:')
#     def show(self):
#         print('나의 이름은 {}, 나이는 {}입니다.'.format(self.name,self.age))
#

# class fourcal:
#     def __init__(self,first,second):
#         self.first=first
#         self.second=second
#     def add(self):
#         result=self.first+self.second
#         return result
#
#     def sub(self):
#         result = self.first - self.second
#         return result
#
#     def mul(self):
#         result = self.first * self.second
#         return result
#
#     def div(self):
#         result = self.first / self.second
#         return result

# a=fourcal(4,2)
# print(a.add())
# print(a.first)
# print(a.second)
# print(int(a.div()))



# class morefourcal(fourcal):
#     def pow(self):
#         result=self.first ** self.second
#         return result
#
# class safefourcal(fourcal):
#     def div(self):
#         if self.second==0:
#             return 0
#         else:
#             return self.first/self.second
# class failfourcal(fourcal):
#     def mul(self):
#         if self.second==0:
#             return 'fail'
#         else:
#             return self.first * self.second


# a=morefourcal(4,2)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())
# print(a.pow())
#
# a=safefourcal(4,0)
# print(a.div())
#
# a=failfourcal(4,0)
# print(a.mul())
#
# # mod1.py
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b

# mod1=open('mod1.py','w',encoding='utf8')
# mod1.write('def add(a,b):\n')
# mod1.write('    return a+b\n')
# mod1.write('def sub(a,b):\n')
# mod1.write('    return a-b\n')
# mod1.close()

# import mod1
# print(mod1.add(8,9))
# print(mod1.sub(18,4))
#
# from mod1 import add
# print(add(9,4))
#
# from mod1 import add,sub
# print(add(9,4),sub(7,4))

# if __name__=='__main__':

# mod1=open('mod1.py','a',encoding='utf8')
# mod1.write('print(add(8,4))\n')
# mod1.write('print(sub(8,4))')
# mod1.close()

# import mod1



# mod2=open('mod2.py','w',encoding='utf8')
# mod2.write('pi=3.141592\n')
# mod2.write('class math:\n')
# mod2.write('    def solv(self,r):\n')
# mod2.write('        return pi*(r**2)\n')
# mod2.write('def add(a,b):\n')
# mod2.write('    return a+b')
# mod2.close()

# import mod2
# print(mod2.pi)
#
# a=mod2.math()
# print(a.solv(2))

# modt=open('modt.py','w',encoding='utf8')
# modt.close()



# import game.sound.echo
# print(game.sound.echo.echo_test())
# from game.sound import echo
# print(echo.echo_test())

# a=[(1,2),(3,4),(4,5)]
# for (first,last) in a:
#     print((first+last))

# marks=[90,25,67,45,80]
# number=0
# for mark in marks:
#     number=number+1
#     if mark < 60: continue
#     print('%d번 학생은 합격입니다.' %number)
#     # else:
#     # print('%d번 학생은 불합격입니다'%number)

# render.py
# from game.sound.echo import echo_test
# def render_test():
#     print('render')
#     echo_test()

# from game.graphic.render import render_test
# print(render_test())

# f=open('나없는파일','r')
# FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'

# print(4/0)
# ZeroDivisionError: division by zero

# a=[1,2,3]
# a[4]
# IndexError: list index out of range

# try:
#     a=[1,2,3]
#     a[4]
# except IndexError as e:
#     print(e)
#
# try:
#     a=[1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)
#
# try:
#     a=[1,2]
#     print(a[3])
#     4/0
# except (IndexError,ZeroDivisionError) as e:
#     print(e)

# try:
#     f=open('나없는파일','r')
# except FileNotFoundError:
#     pass

# class bird:
#     def fly(self):
#         # raise NotImplementedError
#         # print('very fast')
#         # pass
# class Eagle(bird):
#     pass
#
# eagle=Eagle()
# eagle.fly()

# 예외 만들기

# class MyError(Exception):
#     pass
#
# def say_nick(nick):
#     if nick =='바보':
#         raise MyError()
#     print(nick)
#
# # say_nick('천사')
# # say_nick('바보')
#
# try:
#     say_nick('천사')
#     say_nick('바보')
# except MyError:
#     print('허용되지 않는 별명입니다.')

# f=open('나없는파일','r')
# 없는 파일을 열려고 시도하면 filenotfounderror오류가 발생한다.

# 4/0
# 4를 0으로 나누려니까 ZeroDivisionError오류가 발생한다.

a=[1,2,3]
print(a[2])
print('asdsdf')
