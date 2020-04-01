#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py


#运算符
'''
+   加  两个对象相加
-   减  得到负数或是一个数减去另一个数
*   乘  两个数相乘
/   除  两个数除以
%   取模    返回除法的余数
**  幂      返回x的y次幂


'''
print( 1 + 2 )
print( 1 - 2 )
print( 1 * 2 )      #
print( 1 / 2 )
print( 1 // 2 )  #取整数
print( 7 % 4 )   #取余数
print( 2 ** 3 )  #幂,解释：2 x 3 的次方



a = 20 
b = 10

if a == b :
    print("1  a 等于 b ")  #返回1，为真
else:
    print("0  a 等于 b")  #返回0，为假

if a != b :
    print("1  a 不等于 b")  #返回1，为真
else:
    print("0  a 不等于 b")  #返回0，为假

if a > b :
    print("1   a 大于 b")  #返回1，为真
else:
    print("0  a 大于 b ")  #返回0，为假

a = 5
b = 20 

if a <= b :
    print("1   a  小于等于  b")  #返回1，为真
else:
    print("0  a  小于等于  b")  #返回0，为假

if b > a :
    print("1  a  大于等于  b")  #返回1，为真
else:
    print("0  a  大于等于  b")  #返回0，为假





a = 20
b = 10


a +=b       #  a = a + b
print(a)

a *= b      #  a = a * b
print(a)

a  /= b
print(a)

a %= b
print(a)

a **= b
print(a)


#