print("====================================================")
print("|                                                   |")
print("|                     12月份衣服销售数据               |")
print("|  日期       服装名称      价格    库存数量    销售量    |")
print("|  1号        羽绒服      253.6    500         10     |")
print("|  2号        牛仔裤      86.3     600         60     |")
print("|  3号         风衣       96.8     335         43     |")
print("|  4号         皮草       135.9    855         63     |")
print("|  5号         T血        65.8     632         63     |")
print("|  6号         衬衫       49.3      562         120    |")
print("|  7号        牛仔裤       86.3      600        72      |")
print("|  8号         羽绒服       253.6     500       69      |")
print("|  9号         牛仔裤       86.3      600       63      |")
print("|  10号         衬衫        49.3      562      45      |")
print("|  11号         皮草        135.9    855       75       |")
print("|  12号         风衣        96.8      335        52     |")
print("|  13号         衬衫      49.3        562       16      |")
print("|  14号         皮草       135.9      855       69      |")
print("|  15号         牛仔裤      86.3      600        54     |")
print("|  16号         羽绒服      253.6     500        28     |")
print("|  17号         风衣         96.8      335        98    |")
print("|  18号         牛仔裤     86.3      600          87     |")
print("|  19号         皮草       135.9      855        45      |")
print("|  20号         衬衫       49.3      562          78     |")
print("|  21号         羽绒服      253.6      500       85      |")
print("|  22号         皮草       135.9       855       65     |")
print("|  23号         T血        65.8     632         63     |")
print("|  24号         风衣        96.8      335        52     |")
print("|  25号         牛仔裤      86.3      600        54     |")
print("|  26号         皮草       135.9      855        45      |")
print("|  27号        牛仔裤       86.3      600        72      |")
print("|  28号          T血        86.3      600       63      |")
print("|  29号         羽绒服      253.6     500        28     |")
print("|  30号         皮草        135.9    855       75       |")
num=(253.6*220+86.3*462+96.8*245+135.9*437+65.8*189+49.3*259)
print(type(int(num)))
print("总销售额:",num)
num1=round((1812/30))
print("平均每日销售数量:",num1,)
a=(220/1812*100)
b=round(a,2)
print("羽绒服月销售占比:",b,"%")
a1=(462/1812*100)
b1=round(a1,2)
print("牛仔裤月销售占比:",b1,"%")
a2=(245/1812*100)
b2=round(a2,2)
print("风衣月销售占比:",b2,"%")
a3=(437/1812*100)
b3=round(a3,2)
print("皮草月销售占比:",b3,"%")
a4=(189/1812*100)
b4=round(a4,2)
print("T恤月销售占比:",b4,"%")
a5=(259/1812*100)
b5=round(a5,2)
print("衬衫月销售占比:",b5,"%")