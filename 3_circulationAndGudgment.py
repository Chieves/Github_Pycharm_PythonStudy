# 数学运算符
# + - * /
# % 取模 返回除法的余数
# ** 幂 a**b a的b次方
# // 取整除，返回商的整数部分

# 逻辑控制与循环
# 逻辑判断——True & False
# 布尔表达式
import random

print(1 > 2)
print(1 < 2 < 3)
print(42 != '42')
print('Name' == 'name')
print('M' in 'Magic')
number = 12
print(number is 12)

# 比较运算符 == != > < <= >=
# 多条件的比较
middle = 5
print(1 < middle < 10)
# 变量的比较
two = 1 + 1
three = 1 + 3
print(two < three)
# 字符串的比较
print('Eddie Van Helen' == 'eddie van helen')
# 两个函数产生的结果进行比较
print(abs(-10) > len('length of this word'))
# 不同类型的对象不能使用“<,>,<=,>=”进行比较，却可以使用'=='和'!='
# '<>'和'!='是一样的
print(42 == 'the answer')
print(42 != 'the answer')
# 浮点和整数虽然是不通类型，但是不影响到比较运算
print(5.0 == 5)
print(3.0 > 1)
# 布尔类型的比较 True = 1 , False = 0
print(True > False)
print(True + False > False + False)

# 成员运算符与身份运算符 in 和 is
# 列表 list
album = ['Black Star', 'David Bowie', 25, True]
album.append('new song')
print(album[0], album[-1])
# in 后面是一个集合形态的对象
print('Black Star' in album)
# is 和 is not，它们是表示身份鉴别（Identity Operator）的布尔值
# in 和 not in，则表示归属关系的布尔运算符号（Membership Operator）
# 在Python中任何一个对象都要满足身份（Identity）、类型（Type）、值（Value）这三个点，缺一不可
the_Eddie = 'Eddie'
name = 'Eddie'
print(the_Eddie == name)
print(the_Eddie is name)
# 在Python中任何对象都可以判读其布尔值，除了0、None和所有空的序列
# 与集合（列表、字典、集合）布尔值为False之外，其它都为True
print(0)
print([])
print('')
print(False)
print(None)
# 当你想设定一个变量，但又没想好它应该等于什么值时，可以赋值为None
a_thing = None
print(a_thing)

# 布尔运算符 （Boolean Operator)
# not x , x and y , x or y
print(1 < 3 and 2 < 5)
print(1 < 3 and 2 > 5)
print(1 < 3 or 2 > 5)
print(1 > 3 or 2 > 5)

# 条件控制 if...else
# if(关键字） condition(成立的条件):(冒号)
# (缩进)      do something
# elif(关键字）condition:
# (缩进）      do something
# else(关键字):
# (缩进）     do something
# 用一句话概括 if...else 结构的作用：如果...条件是成立的，就做...；反之，就做...
# 所谓条件（condition)指的是条件成立，即是返回值为 True 的布尔表达式。

password_list = ['*#*#', '12345']


def account_login():
    password = input('Please Input Your Password:')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_correct:
        print('Login Success!')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changed successfully!')
        account_login()
    else:
        print('Wrong password or invalid input')
        account_login()


account_login()


# 创建10个文本
def tex_creation():
    path = 'E://Python/Code/GitPython/ReadWriteFiles/'
    for name in range(1, 11):
        with open(path + str(name) + '.txt', 'w') as text:
            text.write(str(name))
            text.close()
            print('Done!')


tex_creation()


# 计算复利
def invest(amount, rate, time):
    print("principal amount:{}".format(amount))
    for t in range(1, time + 1):
        amount = amount * (1 + rate)
        print("year {}:${}".format(t, amount))


invest(100, .05, 8)
invest(2000, .025, 5)


# 输出1-100所有偶数
def even_print():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)


even_print()


# 猜大小的小游戏
def roll_dice(numbers=3, points=None):
    print('< ROLL THE DICE! >')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1, 7)
        points.append(point)
        numbers = numbers - 1
    return points


def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return 'big'
    elif isSmall:
        return 'small'


def start_game():
    money = 1000
    while money > 0:
        print('<<<<< GAME STARTS! >>>>>')
        choices = ['big', 'small']
        your_choice = input('big or small : ')

        if your_choice in choices:
            money_bet = input('How much do you want bet ? ({}-{})'.format(1, money))
            if 0 < int(money_bet) < money:
                money_bet = int(money_bet)
            else:
                print('Your money is not enought to bet! will all in:{}'.format(money))
                money_bet = money
            points = roll_dice()
            total = sum(points)
            youWin = your_choice == roll_result(total)
            if youWin:
                print('The points are:', points, 'You win ! ')
                money = money + money_bet
                print('You gained {} ,you have {} now !'.format(money_bet, money))
            else:
                print('The points are:', points, 'You lose ! ')
                money = money - money_bet
                print('You lose {} ,you have {} now !'.format(money_bet, money))
        elif your_choice == 'exit':
            money = 0
        else:
            print('Invalid Words')
            start_game()
    print('Game Over !')


start_game()