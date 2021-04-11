# coding:utf-8
# Python程序：Hello World 第一个Python程序：Hello World！

print('Hello World! 你好，Python的世界！')

# 变量 标识符 赋值符 值
answer = 42

# print() 打印函数
print(answer)

# 文件操作 open() file.write()
file = open('E://Python/Code/Github_Pycharm_PythonStudy/ReadWriteFiles/file.txt', 'w')
file.write('Hello World!')

# 字符串 拼接字符串
what_he_does = ' plays'
his_instrument = ' guitar'
his_name = 'Robert Johnson'
artist_intro = his_name + what_he_does + his_instrument
print(artist_intro)

# 字符串转换为数值计算 强制类型转换 int()
num = 1
string = '1'
num2 = int(string)
print(num + num2)

# 字符串乘法 *
words = 'words ' * 3
print(words)

# 字符串长度 len()
word = 'a loooooong word'
num = 12
string = 'bang!'
total = string * (len(word) - num)  # 等价于字符串‘bang!'*4
print(total)

# 网址链接尾部倒数10个字符命名
url = 'http://www.stie.cn/lksdjforiurgldkjlkjlj1209dlkjf.jpg'
file_name = url[-10:]
print(file_name)

# 字符串的分片与索引
name = 'My name is Mike'
# 通过下标访问，从第一个字符从0开始向右编号
print(name[0])
# 通过INDEXING访问，从最后一个字符从-1开始向左编号
print(name[-6])
# 截取中间字符串，不包括冒号（：）右边的字符
print(name[11:15])
# 截取第X位之后的字符
print(name[5:])
# 截取第X位之前的字符，从0位开始，不包括X位
print(name[:5])

# 找出你朋友中的魔鬼 三种访问字符串字符方法：下标，区间，INDEXING,前后标省略的冒号
word = 'friends'
find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]
print(find_the_evil_in_your_friends)

# 字符串的方法 .replace()
phone_number = '139-8871-5536'
hiding_number = phone_number.replace(phone_number[:9], '*' * 9)
print(hiding_number)

# 模拟通讯录中的电话号码联想功能 .find()  str() len()
search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'
print(search + ' is at ' + str(num_a.find(search)) + ' to ' + str(num_a.find(search)
                                                                  + len(search)) + ' of num_a')
print(search + ' is at ' + str(num_b.find(search)) + ' to ' + str(num_b.find(search)
                                                                  + len(search)) + ' of num_b')

# 字符串格式化 .format()
print('{} a word she can get what she {} for.'.format('with', 'came'))
print('{preposition} a word she can get what she {verb} for.'.format(preposition='with', verb='came'))
print('{0} a word she can get what she {1} for.'.format('with', 'came'))

city = input("请输入城市的名称(pingyin)：")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
print(url)
