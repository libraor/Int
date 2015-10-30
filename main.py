x = raw_input("欠款时间（格式2015/1/1）：")
y = raw_input("还款时间（格式2015/1/1）：")
z = input("欠款金额：")

#将输入时间转化为时间戳
import time
x = time.strptime(x, "%Y/%m/%d")
x = int(time.mktime(x))
y = time.strptime(y, "%Y/%m/%d")
y = int(time.mktime(y))

#计算欠款天数
day = (y-x)/3600/24

#计算欠款利率
lilv = 0.06/360

#计算欠款利息
lixi = day*lilv*z


#将计算过程导出到excel

