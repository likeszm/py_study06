#循环学习记录

"""
收获:
锻炼了对字符串的处理
"""

#while循环
"""
condition = True
while condition :
    temp = input("输入0结束循环:")
    if temp == '0' :
        condition = False
        
"""

#for循环多用于迭代
"""
list1 = [1,2.1,'3.0','test',['h',8,9.0]]
tuple1 = (1, 23, 3.0 ,'4', 'hello')
str1 = "hello world"

for i in list1 :
    print(f"list1 = {i}")

for i in tuple1 :
    print(f"tuple1 = {i}")

for i in str1 :
    print(f"str1 = {i}")
"""

#rang方法
"""
for i in range(10) :
    print(f"n = {i}")

for i in range(5,11) :
    print(f"j = {i}")

for i in range(5,11,2) :
    print(f"k = {i}")
"""

#enumerate方法
"""
list2 = [1,2.0,'h','hello']
tuple2 = (2,3.0,'4',"hello ")
str2 = "hello world"

for index,i in enumerate(list2) :
    print(f"[{index}] = {i}")

for index,i in enumerate(tuple2) :
    print(f"[{index}] = {i}")

for index,i in enumerate(str2) :
    print(f"[{index}] = {i}")
"""

#break
"""
while True :
    if '0' == input("输入0退出:") :
        break
"""

#continue
"""
while True :
    var = input()
    if var == '0' :
        break
    elif var == '1' :
        continue
    print("0退出 1取消下次提示 : ")
"""

#列表推导式
"""
list1 = [1,2,3,4,5,6]
list2 = [num**3 for num in list1]
print(list2)
"""

#题目

ageTable = '''
    诸葛亮, 28
    刘备, 48
    刘琦, 25
    赵云, 32
    张飞, 43
    关羽, 45
'''

"""
print("年龄大于30：")
for str in ageTable.splitlines() :
    if str != '' :
        temp = str.split(',')
        name = temp[0]
        age = temp[-1]
        if int(age) > 30 :
            print(f"{name:<5}的年龄是{age}")

print("年龄小于等于30：")
for str in ageTable.splitlines() :
    if str != '' :
        temp = str.split(',')
        name = temp[0]
        age = temp[-1]
        if int(age) <= 30 :
            print(f"{name:<5}的年龄是{age}")
"""

#题目
"""
list_test = [["剪刀", "石头"], ["布", "剪刀"], ["剪刀", "剪刀"]]

count,count_a,count_b = 0,0,0
for temp in list_test :
    a,b = temp[0],temp[-1]
    if ((a == "剪刀") and (b == "布")) or ((a == "石头") and (b == "剪刀")) or ((a == "布") and (b == "石头")) :
        count_a+=1
    elif not a == b :
        count_b+=1
    else :
        count+=1

count = int(count) + int(count_a) + int(count_b)
print(f"共计比赛{count}次")
print(f"A赢了{count_a}次，B赢了{count_b}次!")
"""

