
x = raw_input("欠款时间（格式2015/1/1）：")
y = raw_input("还款时间（格式2015/1/1）：")
z = input("欠款金额：")

#将输入时间转化为时间戳
import time
x = time.strptime(x, "%Y/%m/%d")
x = int(time.mktime(x))
y = time.strptime(y, "%Y/%m/%d")
y = int(time.mktime(y))


#利率列表 lilv1利息变动日 lilv2六个月内利率 lilv3六个月至一年利率 lilv4一至三年利率 lilv5三至五年利率 lilv6五年以上利率
lilv1 = [33349,34104,34161,34700,34881,35186,35300,35726,35879,35977,36136,36321,37308,38289,38835,38948,39159,39221,39284,39316,39340,39437,39707,39730,39751,39779,39805,40471,40538,40583,40639,40731,41068,41096,41965,42064,42135,42183,42242,42301]
lilv2 = [8.10 ,8.82 ,9.00 ,9.00 ,10.08 ,9.72 ,9.18 ,7.65 ,7.02 ,6.57 ,6.12 ,5.58 ,5.04 ,5.22 ,5.40 ,5.58 ,5.67 ,5.85 ,6.03 ,6.21 ,6.48 ,6.57 ,6.21 ,6.12 ,6.03 ,5.04 ,4.86 ,5.10 ,5.35 ,5.60 ,5.85 ,6.10 ,5.85 ,5.60 ,5.60 ,5.35 ,5.10 ,4.85 ,4.60 ,4.35 ]
lilv3 = [8.64 ,9.36 ,10.98 ,10.98 ,12.06 ,10.98 ,10.08 ,8.64 ,7.92 ,6.93 ,6.39 ,5.85 ,5.31 ,5.58 ,5.85 ,6.12 ,6.39 ,6.57 ,6.84 ,7.02 ,7.29 ,7.47 ,7.20 ,6.93 ,6.66 ,5.58 ,5.31 ,5.56 ,5.81 ,6.06 ,6.31 ,6.56 ,6.31 ,6.00 ,5.60 ,5.35 ,5.10 ,4.85 ,4.6,4.35]
lilv4 = [9.00 ,10.80 ,12.24 ,12.96 ,13.50 ,13.14 ,10.98 ,9.36 ,9.00 ,7.11 ,6.66 ,5.94 ,5.49 ,5.76 ,6.03 ,6.30 ,6.57 ,6.75 ,7.02 ,7.20 ,7.47 ,7.56 ,7.29 ,7.02 ,6.75 ,5.67 ,5.40 ,5.60 ,5.85 ,6.10 ,6.40 ,6.65 ,6.40 ,6.15 ,6.00 ,5.75 ,5.50 ,5.25 ,5.00 ,4.75]
lilv5 = [9.54 ,12.06 ,13.86 ,14.58 ,15.12 ,14.94 ,11.70 ,9.90 ,9.72 ,7.65 ,7.20 ,6.03 ,5.58 ,5.85 ,6.12 ,6.48 ,6.75 ,6.93 ,7.20 ,7.38 ,7.65 ,7.74 ,7.56 ,7.29 ,7.02 ,5.94 ,5.76 ,5.96 ,6.22 ,6.45 ,6.65 ,6.90 ,6.65 ,6.40 ,6.00 ,5.75 ,5.50 ,5.25 ,5.00 ,4.75]
lilv6 = [9.72 ,12.24 ,14.04 ,14.76 ,15.30 ,15.12 ,12.42 ,10.53 ,10.35 ,8.01 ,7.56 ,6.21 ,5.76 ,6.12 ,6.39 ,6.84 ,7.11 ,7.20 ,7.38 ,7.56 ,7.83 ,7.83 ,7.74 ,7.47 ,7.20 ,6.12 ,5.94 ,6.14 ,6.40 ,6.60 ,6.80 ,7.05 ,6.80 ,6.55 ,6.15 ,5.90 ,5.65 ,5.40 ,5.40 ,4.90]


#确认计息期间 25569为调整excel时间与时间戳起算点差异
i = 0
while x >=(lilv1[i]-25569)*24*3600: 
	i+=1
j = -1
while y <=(lilv1[j]-25569)*24*3600:
	j-=1

'''print x
print (lilv1[0]-25569)*24*3600
print i
print j
print lilv1[i:j+1]
'''

#计算欠款天数,并确定适用利率水平
day = (y-x)/3600/24
if day<=180:
        lilv=lilv2
elif day>180&&day<=360:
        lilv=lilv3
elif day>360&&day<=1080:
        lilv=lilv4
elif day>1080&&day<=1800:
        lilv=lilv5
else:
        lilv=lilv6



#计算欠款利息
#lixi = day*lilv*z


#将计算过程导出到excel

