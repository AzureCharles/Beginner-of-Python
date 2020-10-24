#这个文件是关于while和for循环的练习
length = int(input("请指定需要的二进制位数\n"))
bin_numbers = []
for number in range(1,length+1):
    number = 2**number
    bin_numbers.append(number)
    #制造一个长度为length的二进制数表
print("\n其对应基表为：\n")
print(bin_numbers)
    #打表
    
bin_type=[] 
    #存储二进制形式
bin_numbers = sorted(bin_numbers,reverse=True)

test_number = int(input("\n请输入需要转化的十进制数：\n"))

for order in range(0,len(bin_numbers)):
    rank = test_number/bin_numbers[order]
    bin_type.append(int(rank))
    test_number = test_number%bin_numbers[order]
print("\n对应二进制形式为：\n")
print(bin_type)
    #用列表显示10位的二进制数

active = True
while active:
    message = input("\n你希望删除基表吗？(Y/N)\n")
    if message == 'Y':

        while bin_numbers:
            bin_numbers.pop()
        print("删除成功！\n")
        active = False
    #显示删表过程，不要输出空表
