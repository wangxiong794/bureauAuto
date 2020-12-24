# coding=utf-8
# 计算劳务费税费
# 应纳税所得额 = 劳务报酬（少于4000元）-800元
# 应纳税所得额 = 劳务报酬（超过4000元）*（1-20%）
# 应纳税额 = 应纳所得税额 * 使用税率 - 速算扣除数
# 应纳税所得额（0<X≤20000）时，使用税率20%，速算扣除数0元
# 应纳税所得额（20000<X≤50000）时，使用税率30%，速算扣除数2000元
# 应纳税所得额（50000<X）时，使用税率40%，速算扣除数7000元

def frontFee1():
    # 输入税前金额，算出税费和税后金额
    frontFee = input("请输入税前金额：")
    try:
        frontFee = float(frontFee)
        if 0 < frontFee <= 800:
            return 0, frontFee
        elif 800 < frontFee < 4000:
            return (frontFee - 800) * 0.2, frontFee - (frontFee - 800) * 0.2
        elif frontFee >= 4000:
            money = frontFee * 0.8
            if money <= 20000:
                return round(money * 0.2, 2), round(frontFee - money * 0.2, 2)
            elif 20000 < money <= 50000:
                return round(money * 0.3 - 2000, 2), round(frontFee - money * 0.3 - 2000, 2)
            elif money > 50000:
                return round(money * 0.4 - 7000, 2), round(frontFee - money * 0.4 - 7000, 2)
        else:
            print("税前金额无效")
    except:
        print("税前金额无效")


a = frontFee1()
print("税费为 %s 元，税后金额为 %s 元" % a)
