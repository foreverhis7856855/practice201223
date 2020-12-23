Python 3.7.5 (default, Nov  7 2019, 10:50:52) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> if a == 10:
	print('10입니다.')

	
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    if a == 10:
NameError: name 'a' is not defined
>>> if a==10:
	print('10입니다.')
	a

	
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    if a==10:
NameError: name 'a' is not defined
>>> if a == 10:
	print('10입니다.')

	
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    if a == 10:
NameError: name 'a' is not defined
>>> x = 10
>>> x
10
>>> x, y, z = 10, 20, 30
>>> y
20
>>> a = 10
>>> b = 20
>>> c = a + b
>>> c
30
>>> input()
Hello, world!
'Hello, world!'
>>> a = int(input('첫 번째 숫자를 입력하세요: '))
첫 번째 숫자를 입력하세요: 
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a = int(input('첫 번째 숫자를 입력하세요: '))
ValueError: invalid literal for int() with base 10: ''
>>> b = int(input('두 번째 숫자를 입력하세요: '))
두 번째 숫자를 입력하세요: 30
>>> 
