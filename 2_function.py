# 函数
# print() 是一个放入对象就能将结果打印的函数
# input() 是一个可以让用户输入信息的函数
# len() 是一个可以测量对象长度的函数
# int() 是一个可以将字符串类型的数字转化成整数类型的函数
# abs()     dict()   help()     min()       setatt()
# all()     dir()    hex()      next()      slice()
# any()     divmod() id()       object()    sorted()
# ascii()   enumerate() input() oct()       staticmethod()
# bin()     eval()   int()      open()      str()
# bool()    exec()   ininstance()   ord()   sum()
# bytearray()   filter()    issubclass()    pow()   super()
# bytes()   float()  iter()     print()     tuple()
# callable()    format() len()  property()  type()
# chr()     frozenset() list()  range()     vars()
# compile() globals() map()     reversed()  _import_()
# complex() hasattr()   max()   round()
# delattr() hash()    memoryview()  set()

# 定义函数 关键字def 函数名（自己取） 参数2个（可选） 冒号：一定不能少
#        此处有缩进 关键字return 结果
def function():
    return 'something'


print(function())


# 摄氏度转换公式
def fahrenheit_converter(C):
    fahrenheit = C * 9 / 5 + 32
    return str(fahrenheit) + '°F'


lyric_length = len('I Cry Out For Magic!')
print('歌词长度为：' + str(lyric_length))

C2F = fahrenheit_converter(35)
print('35°转换为华氏度为：' + C2F)


# 重量转化器函数
def weight_coverter(weight_g):
    weight_kg = float(weight_g) / 1000
    return weight_kg


w_g = input('请输入以“g”为单位的数字：')
w_kg = weight_coverter(w_g)
print('输入的: ' + w_g + 'g 转换后为： ' + str(w_kg) + "kg")


# 标准答案
def g2kg(g):
    return str(g / 1000) + 'kg'


print(g2kg(200345))

import math


# 求直角三角形斜边长的函数 math.sqrt 求平方根 pow(x,y):x的y次方
def right_triangle_third_side(side_a, side_b):
    third_side = math.sqrt(float(side_a) * float(side_a) + pow(float(side_b), 2))
    return third_side


side_a = input('请输入直角边a的长度：')
side_b = input('请输入直角边b的长度：')
third_side = right_triangle_third_side(side_a, side_b)
print('直角边长为：' + str(side_a) + '、' + str(side_b) + ' 的三角形斜边长为：' + str(third_side))


# 标准答案
def Pythagorean_theorem(a, b):
    return 'The right triangle third side\'s length is:{}'.format((a ** 2 + b ** 2) ** (1 / 2))


# 等价于a的平方与b的平方和的1/2次方
print(Pythagorean_theorem(3, 4))


# 传递参数与参数类型
# 位置参数 (positional argument)
# 关键词参数 （keyword argument)
def trapezoid_area(base_up, base_down, height):
    return 1 / 2 * (base_up + base_down) * height


# 位置参数传入
print(trapezoid_area(1, 2, 3))
# 关键词参数传入
print(trapezoid_area(base_up=4, base_down=5, height=6))
# 参数反序传入
print(trapezoid_area(height=6, base_down=5, base_up=4))
# 正序传入，正确
print(trapezoid_area(4, 5, height=6))

# 参数的命名和变量的命名, 注意位置参数的传入，与变量的命名无关系
# 函数中定义的参数在调用时缺一不可
base_up = 1
base_down = 2
height = 3
print(trapezoid_area(height, base_down, base_up))


def flashlight(battery1, battery2):
    return 'Light!'


nanfu1 = 600
nanfu2 = 600
print(flashlight(nanfu1, nanfu2))

print('   *', ' *  *', '*  *  *', '  |  ')
# 神奇的默认参数 sep='\n' 表示换行分隔符
print('    *', '  *   *', ' *  *  *', '    |    ', sep='\n')


# 参数设定默认值
def trapezoid_area_default(base_up, base_down, height=3):
    return 1 / 2 * (base_up + base_down) * height


print(trapezoid_area_default(1, 2))
print(trapezoid_area_default(1, 2, height=15))
# request.get(url, headers = header) 这个是在请求网站时header，可填可不填
# img.save(img_new, img_format, quality = 100) 在给图片加水印的时候默认的水印质量是100

# 敏感词过滤器
# 打开文件操作
file = open('E://Python/Code/GitPython/ReadWriteFiles/file.txt', 'w')
file.write('\nHello Python!')


# 文件操作函数
def text_creat(name, msg):
    desktop_path = 'E://Python/Code/GitPython/ReadWriteFiles/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('信息写入完毕！')


text_creat('HellPython', 'Hello Python ! \nI have write the message to file!')


# 敏感字替换函数
def text_filter(word, censored_word='lame', changed_word='Awesome'):
    return word.replace(censored_word, changed_word)


print(text_filter('Python is lame!'))


# 实现函数的合并
def consored_text_creat(name, msg):
    clean_msg = text_filter(msg)
    text_creat(name, clean_msg)


consored_text_creat('Try', 'lame!lame!lame!')