mnhd = ['123','132','435','437','125','890']

try:
    phone = int(input("请输入手机号码:"))

    if len(str(phone)) != 11 :
        print("长度不符合")
        exit(0)

    for i in mnhd:
        if i == str(phone)[0:3]:
            break
        else:
            print("不包含模拟字段")
            exit(0)

except ValueError:
    print("请输入数字")
else:
    print("手机号码正确")