#33
# print('-'*80)

#34
# t1='python'
# t2='java'
# t=t1+' '+t2+' '
# print(t *5)

#35
# name1='김민수'
# age1=10
#
# name2='이철희'
# age2=13
#
# print('이름:%s 나이:%d' %(name1,age1))
# print('이름:%s 나이:%d' %(name2,age2))

# 036
# name1='김민수'
# age1=10
#
# name2='이철희'
# age2=13
#
# print('이름:{} 나이:{}'.format(name1,age1))
# print('이름:{} 나이:{}'.format(name2,age2))

# 037
# name1='김민수'
# age1=10
#
# name2='이철희'
# age2=13
# print(f'이름:{name1} 나이:{age1}')
# print(f'이름:{name2} 나이:{age2}')

# 038
# 상장주식수='5,969,782,550'
# 상장주식수=상장주식수.replace(',','')
# print(int(상장주식수))
#,콤마가 있는 경우 바로 int가 먹지 않으므로 리플레이스로 없애주고 출력한다

# 039
# 분기 ='2020/03(E) (IFRS연결)'
# print(분기[:7])

# 040
# data='   삼성전자    '
# data=data.strip()   #스트립은 공백제거
# print(data,len(data))

# 041
# ticker='btc_krw'
# ticker=ticker.upper() #어퍼는 소문자를 대문자로
# print(ticker)

#042
# ticker='BTC_KRW'
# ticker=ticker.lower()
# print(ticker)

#043
# a='hello'
# a=a.capitalize()  #첫글자만 대문자로 변경
# print(a)

#044
# file_name='보고서.xlsx'
# print(file_name.endswith('xlsx'))

# 045
# file_name='보고서.xlsx'
# print(file_name.endswith(('xlsx','xls')))

# 046
