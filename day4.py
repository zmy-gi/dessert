
names={"姓名0":"曹操","年龄1":56,"性别":"男","编号1":"106","任职公司1":"IBM","薪资1":500,"部门编号1":"50","姓名1":
            {"姓名2":"大乔",'年龄2':19,"性别":"女","编号2":"230","任职公司2":"微软","薪资2":501,"部门编号2":"60","姓名3":
                {"姓名4":"小乔",'年龄3':19,"性别":"女","编号3":"210","任职公司3":"Oracle","薪资3":600,"部门编号3":"60","姓名5":
                    {"姓名6":"小李",'年龄4':45,"性别":"男","编号4":"230","任职公司4":"Tencent","薪资4":700,"部门编号4":"10"}}}
       }
#print(names)

#print((names["薪资"]+names["姓名1"]["薪资"]+names["姓名1"]["姓名3"]["薪资"]+names["姓名1"]["姓名3"]["姓名5"]["薪资"])/4)
#每个人的平均薪资
#num=int(input("平均薪资：")
#print((names["年龄"]+names["姓名1"]["年龄"]+names["姓名1"]["姓名3"]["年龄"]+names["姓名1"]["姓名3"]["姓名5"]["年龄"])/4)
#平均年龄

'''
#刘备，45，男，220，alibaba，500,30
print(dict)
aa={"姓名7":"小李",'年龄5':45,"性别5":"男","编号5":"230","任职公司5":"Tencent","薪资5":700,"部门编号5":"10"}
names.update(aa)
#or
names["姓名7"]="刘备"
names["年龄7"]=45
names["性别5"]="男"
names["编号5"]="220"
names["任职公司5"]="alibab"
names["薪资5"]=500
names["部门编号5"]="30"    #添加数据
print(names)
'''
name = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
i=0
j=0
for a in range(len(name)):
  if  name[a][2]=="男":
    i+=1
  else:
    j+=1
print("男生人数为{},女生人数为{}".format(i,j))

l=0
m=0
n=0
for x in range(4):
    if name[x][6]=="50":
        l+=1
    elif name[x][6]=="60":
        m+=1
    else:
        n+=1
print("50部门的人数为{},60部门的人数为{},10部门的人数为{}".format(l,m,n))


'''

[罗恩, 23 ,35 ,44]
[哈利 ,60, 77 ,68 ,88, 90]
[赫敏, 97 ,99 ,89 ,91, 95, 90]
[马尔福 ,100, 85 ,90]
求每个人的总成绩？

'''

dict={"姓名":"罗恩","1":23,"2":35,"3":44,"姓名1":
        {"姓名2":"哈利","1":60,"2":77,"3":68,"4":88,"5":90,"姓名3":
           {"姓名4":"赫敏","1":97,"2":99,"3":89,"4":91,"5":95,"6":90,"姓名5":
               {"姓名6":"马尔福","1":100,"2":85,"3":95}}}}
a=dict["1"]+dict["2"]+dict["3"]
print("罗恩的总成绩为：",a)
b=dict["姓名1"]["1"]+dict["姓名1"]["2"]+dict["姓名1"]["3"]+dict["姓名1"]["4"]+dict["姓名1"]["5"]
print("哈利的总成绩为：",b)
c=dict["姓名1"]["姓名3"]["1"]+dict["姓名1"]["姓名3"]["2"]+dict["姓名1"]["姓名3"]["3"]+dict["姓名1"]["姓名3"]["4"]+dict["姓名1"]["姓名3"]["5"]+dict["姓名1"]["姓名3"]["6"]
print("赫敏的总成绩为：",c)
d=dict["姓名1"]["姓名3"]["姓名5"]["1"]+dict["姓名1"]["姓名3"]["姓名5"]["2"]+dict["姓名1"]["姓名3"]["姓名5"]["3"]
print("马尔福的总成绩为：",d)


num=int(input("请输入一个数："))
while num!=0:
    print(num%10)
    num=num//10

    # a=[5,2,4,7,9,1,3,5,4,0,6,1,3] 冒泡排序
    a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3, ]
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)