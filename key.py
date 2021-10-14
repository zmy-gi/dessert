'''
dict = {"k1":"v1","k2":"v2","k3":"v3"}
for i in dict:
   print(i)
for a,b in dict.items():
   print(a)
for a, b in dict.items():
   print(b)
for j in dict:
   print(dict[j])
dict["k4"]="v4"
print(dict)
'''
info = {
    '苹果':32.8,
    '香蕉': 22,
    '葡萄': 15.5
}
#print('苹果：',info['苹果'])
for i in info:
    print(i,info[i])
aa={'草莓':6.5,'橘子':3.6,'樱桃':10.6}
info.update(aa)
print(info)

buy = {
    '小明': {
        'fruits': {'苹果':4, '草莓':13, '香蕉':10},
        'money':{'苹果':32.8,'草莓':6.5,'香蕉': 22,}
    },
    '小刚': {
        'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
        'money': {'葡萄': 15.5,'橘子':3.6,'樱桃':10.6}
    }
}

print(buy["小明"]["fruits"]["苹果"]+buy["小明"]['fruits']["草莓"]+buy["小明"]["fruits"]["香蕉"])
print(buy["小刚"]["fruits"]["葡萄"]+buy["小刚"]['fruits']["橘子"]+buy["小刚"]["fruits"]["樱桃"])
a=['21','3','56','9','10','3']
b=a.count('10')
print(b)

from collections import Counter
arr=[1,5,3,9,4,56,3,4,9,1,2,87,56,1,9,1,]
def counter(arr):
    return Counter(arr)
print(counter(arr))

