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


#比较运算符
'''
==      等于 - 比较对象是否相等
!=      不等于 - 比较两个对象是否不相等
>       大于 - 返回x是否大于y
<       小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。
>=      大于等于 - 返回x是否大于等于y。
<=      小于等于 - 返回x是否小于等于y。
'''
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



#赋值运算
'''
=    简单的赋值运算符
+=   加法赋值给运算符
-=   减法赋值给运算符
*=   乘法赋值给运算符
/=   除法赋值运算符
%=   取模赋值运算符
**=  幂赋值运算符
//=  取整除赋值运算符
'''

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
