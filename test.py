a = input (" ")
b = input (" ")
c = input (" ")

print(a)
print(b)
print(c)

"Hello world"

"Python is fun"

""" Life is too short, You need python """

''' Life is too short, You need python  '''

multiline = "Life is too short\nYou need python"

print(multiline)

multiline = """
Life is too short
You need python
"""
print(multiline)

head = 'python'
tail = 'is too fun'0
head + tail 

head * 3

tail * 7

'=' * 50 

print('=' * 50)

a = "Life is good"
print(a)

head = "jun is"
tail = "man"
head + tail 

tail * 7

head * 6

tail * 3 


a = "path"
b = "one"
a* 2

print("="* 50)

a = "Life is"
len(a)
a = ' life is good '
a[0:4]
a[1:2]
a[2:5]
a[0:]
a[:20]
a[:]
a[1:2]

a= "20100331Rainy"
a[0:9]
a[-5:]
a[8:13]
a[0:9]+a[-5:]
year = a[0:4]
year
month = a[4:6]
month


"현재 온도는 %d도입니다." % 20
"I eat % apple" % 3
"I eat % apple" % 4
"I eat % apple" % 5

"저는 %s개의 사과를 먹었다." % "세" 
"저는 %s개의 사과를 먹었다." % "네"

number = 3
number = 4

"I eat %d apple" % number

number = 10 
day = "three"

"I eat %d apples. so i was sick for %s days" %(number, day)

"I have %s apples" % 3
number = 7
money = "three"
"L pay %s dallors and I want to go back home at %d a clock" %(money, number)


"%10s" % "hi"
"%-10s" % "hi"
"%10d" % 2
"%-20d" % 3

"%0.4f" % 1.3334456
"%10.4f" % 1.320548580
"%0.3f" % 2.435435


"I eat {} apples" .format("five")
"I eated {} apples.".format(3)

number = 3
nubmer = 4
"I eat {} apples".format(number)
"I hate {} my brother so mouch".format(number)

number = 3
day = 4
"I ate {} apples. so I was sick for {} days." .format(nubmer, day)
"I ate %d appels. so i was sick for %s days." %(number,day)

"{0:<9}".format("hi")
"{0:<3}".format("hello")
"{0:^3}".format("hello")


"{0:=^10}".format("hello")
"{0:!<10}".format("hi")

y= 3.11123817483
"{0:0.4f}".format(y)

"and".format()
"{{and}}".format()

name = "홍길동"
age = 24

f'나의 이름은 {name}입니다.나이는 {age} 입니다.'

f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

f'나는 내년이 되면 {age+1} 살이 됩니다.'
f'나는 내년이면 {age+1}살이 된다.'

d= {'name': '홍길동', 'age' : 30}
f'너의 이름은 {d["name"]} 이고, 나이는 {d["age"]} 살입니다.'
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

f'{"hi":<10}'
y= 3.44454549589
f'{y:0.4f}'
f'{y:0.4f}'

a = "ssddt"
a.find('k')
a.index('k')



".".join('abcd')
"!".join("oh")

a = "        HI       "
a.upper()
a.lower()
a.lstrip()
a.rstrip()
a.strip()

a = "Life is so good"
a.replace("Life", "jub")

a.split()
a.split(" ")

odd = {1,2,3,4,5}|\
odd

a = {}
b = {1,2,3,4,"바보"}
c = {"응1",'응2','응3','응4','응5'}
e = [1, 2, ['Life', 'is']]
a
b
c
d
e

a= [1,2,3,['a','b',['c','d']]]
a

a[-1][-1][:4]

a = [1,2,3,4,5]
a[0:2]
a[:2]
a[:-3]

a= [1,2,3]
b = [4,5,6]
a+b
a*3+b

a = [1,2,3]
len(a)
str(a[1])+"hi"

a = [1,2,3]
a[1] = 4
a

del a[:2]
del a[:-1]
a

a = [1,2,3]
a.append([4,5,6])
a

a = [1,4,3,2]
a.sort()
a

a = ['가','나','다']
a.sort()
a

a=  ['a','b','c']
a.sort()
a.reverse()
a.index("d")
a.index('나')


a = [1,2,3]
a.insert(0,4)
a.append(4)
a.remove(2)


a = [1,2,3]
a.pop()
a.pop()
a.pop()
a.count()
a.extend([4,5])
a.append(4)
a.append(5)
a.insert(1,3)
a

a = 'life is a good'
len(a)
a[2]
a[-1]
' I have %s apples' % 'go'
'I have %s colors' % 4
'I have %d%% hours' % 2
'%10s' % 'hi'
'%-10s'% 'hi'
'%7.4f' % 3.24364
'%10.4f' % 3.545645
'I eat {0} apples'.format('five')
number = 10
day = 'three'
'I ate {number} apple. so I was sick for {day} days'.format(number=10, day=3)
'{0:>10}'.format("hi")
'{0:^10}'.format('hi')
'{0:=^10}'.format('hi')
'{0:!<10}'.format('hi')

name = '홍길동'
age = 30 
f'나의 이름은 {name} 입니다. 나이는 {age} 입니다.'

age = 30 
f'나는 내년이면 {age+1} 살이 된다.'

d = {'name': '홍길동', 'age':30}
f'나의 이름은 {d["name"]} 입니다. 나이는 {d["age"]} 입니다.' 
 

a= [1,2,3]
a.extend([4,5])
a

a.remove(1)
a

a.insert(1,5)
a

a.append(5)
a


a.pop()
a

a.index(5)
a

a.reverse()
a

a.sort()

a = [1,2,3]
a.append(4)
a
del a[1]
a
a.append([5,6])
a

a.sort()

a = [1,4,3,2]
a.sort()
a

a.reverse()

a = ['a','c','b']
a.reverse()
a.sort()
a
a = [1,2,3]
a.index(3)

a.insert(2,4)
a.append(5)
a.remove(1)
a.remove(6)

a.pop()
a

a = [1,2,3,1]
a.count(1)
a.count(5)

a = [2,3,4]
a.extend([3,5])
a

################## 튜플 ###########################################################3


t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',('ab','cd'))

t1 = (1,2,'a','b')
del t1[0]

t1[0] = 'b'

t1 = (1,2,'a','b')
t2 = (3,4)
t1[0]
t1[3]

t1[1:]
t1+t2
t1 *3
t2 *4

len(t1)
t1

dic = {'name':'pey', 'phone':'01099933233','birth':'1118'}
dic

a = {1:'hi'}
a[2] = 'b'
a

a['name'] = 'pey'
a

del a[1]
a

b = {'김연아':'피겨스케이팅', '류현진':'야구',"박지성" : "축구"}
b['김연아']

grade = {'key': 10, 'juliet' : 99}
grade[{'key'}]

grade['key']

a = {1:'b', 2: 'c'}
a[1]

a = {1 : 'c', 2: 'b'}
a

a ={1 : 'b', 2 : 't'}
a[1] 

a['name'] = 'jin'

a = {[1,2] : 'hi'}
a

a = {'name': 'jin', 'age' : 22 , 'live' : 'seoul'}
a['name','age','live']
list(a.keys())
list(a.values())
list(a.items())
a.clear()
a

print(a.get('phone'))
a.get('too', 'bar')

'name' in a
'phone' in a
'true' in a 


####집합#####

s1 = set([1,2,3])
s2 = set('hello')

s1 = set([1,2,3])
l1 = list(s1)
l1

t1 = tuple(s1)
t1

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
s1 & s2
s1.intersection(s2)

s1 | s2
s1 | s2 & s1
s1 - s2
s1.difference(s2)

s1 = set({1,2,3})
s1.add(4)
s1
s1.update([4,5,6])
s1.remove(4)
s1

a = True
b = False

type(a)
type(b)

1==1
1<2
1>2

a = [1,2,3,4]
a = 0
if [a>3]:
    print('참')
else:
    print('거짓')

bool([1,2,3])
bool([])
bool([[[]]])

a = 1
b = "python"
c = [1,2,3]

a
b
c


a = [1,2,3]
id(a)

a = [2,3,4]
id(a)

a = [1,2,3]
b = a
id(a)
id(b)

a is b
b = a[:]
a[1] = 4
id(a)
id(b)
a
b

a,b =  ('python','java')
(a,b) = 'python', 'java'

a = 13
bool(a%2 == 0)

a = "881120-1068234"
a[0:6]
a[-7]

a = "a:b:c:d"
a.replace(':','#')
a.replace(":","")
a

a = [1,3,5,4,2]
a.sort()
a.reverse()
a

a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
result

a = (1,2,3)
a = a + (4,)
a

a = dict()
a

a = {'A':90, 'B':80, 'C':70}

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
##set에대입
aset = set(a)
##리스트로 만들고 a에 대입
a = list(aset)
a

t2 = (0,)
t2

t1 = (1,2,3,4)
del t1[1]

t1 = [1,2,3,4]
del t1[0]
t1

t1 = (1,2,'a','b')
t1[0] = 'c'
t1

t1 = (1,2,'a','b')
t1[1]

t1[:2]


t1 = (1,2,3,4)
t2 = (3,4,5,6)
t1 * 3
t1 + t2


len(t1)

dic = {'이름' : '홍길동', 'age' : '24'}
dic

dic['사람'] = 'b'
dic

del dic['이름']
dic['사람']

dic = {[1,2,3] : 'hi'}
dic

list(dic.keys())

list(dic.values())

list(dic.items())

dic.get('이름')
dic.get('age')

dic.get('too','bar')

'age' in dic 

s1 = set({1,2,3})
s1

d2 = set('hello')
d2

d2 = set('memmory')
f2 = list(d2)
f2

s1 = set({1,2,3,4,5,7,8,9})
s2 = set({2,3,4,7,8,9})
s1 & s2

s1.intersection(s2)


age = int(input("몇살? "))
if age < 19:
    print('애들은 가라')

age = int(input("몇살? "))
print(age)
if age < 19:print("애들은 가라")



a = 3
if a == 3:
    print("3이다")
if a > 5:
    print("5보다 크다")
if a < 5:
    print("5보다 작다")


##오후##

money  = True
if money:
    print('택시를 타고 가라')
else:
    print("같이 가라")


money = True
if money:
    print("택시를")
    print("타고")
    print("가라")


money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


1 in [2,3,4]

'a' in ('a','b','c')

't' not in 'python'

pocket = ['paper', 'cellphone']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print('걸어서 집에가라')


if "paper" in pocket:
    print('그냥 가 ')


pocket = ['money', 'name']
if 'n' in pocket:
    pass
else:
    print("가자")


score = 10 
messege = "success" if score >= 60  else "falure"

message = "success" if score >= 60 else "failure"


tree = 0 
while tree <10:
    tree = tree + 1
    print("나무를 %d번 찍었습니다." %tree)
    if tree == 10:
        print("나무를 넘어갑니다.")



prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number: """

number = 0 
while number !=4:
    print(prompt)
    number = int(input())


coffee = 10
money = 300 
while money:
    print('돈을 받았으니 커피를 줍니다.')
    coffee = coffee -1
    print('남은 카피의 양은 %d개입니다.' %coffee)
    if coffee==0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


a = 0
while a < 10:
    a  = a+1
    if a%2 == 0 : continue
    print(a)




