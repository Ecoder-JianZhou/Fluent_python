# container data sequence: list, tuple, collections.deque, that can save different tyles data
# list comprehension and generator expression

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)  # [36, 162, 163, 165, 8364, 164]

symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)    # [36, 162, 163, 165, 8364, 164]

# 用列表推导和map/filter组合来创建同样的表单
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii) # [162, 163, 165, 8364, 164]
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii) # [162, 163, 165, 8364, 164]

# 示例2-4 使用列表推导计算笛卡儿积
print("示例2-4 使用列表推导计算笛卡儿积")
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'),
#  ('white', 'M'), ('white', 'L')]

for color in colors:
    for size in sizes:
        print((color, size))

# ('black', 'S')
# ('black', 'M')
# ('black', 'L')
# ('white', 'S')
# ('white', 'M')
# ('white', 'L')

tshirts = [(color, size) for size in sizes
                         for color in colors]
print(tshirts)
# [('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'),
#  ('black', 'L'), ('white', 'L')]

print("用生成器表达式初始化元组和数组: 生成器表达式的语法跟列表推导差不多，只不过把方括号换成圆括号而已")
symbols = '$¢£¥€¤'
print(tuple(ord(symbol) for symbol in symbols))
# (36, 162, 163, 165, 8364, 164)
import array
print(array.array('I', (ord(symbol) for symbol in symbols)))
# array('I', [36, 162, 163, 165, 8364, 164])

print("使用生成器表达式计算笛卡儿积")
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s%s'%(c, s) for c in colors for s in sizes):
    print(tshirt)

# black S
# black M
# black L
# white S
# white M
# white L