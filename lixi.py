
def lixi(x,y,z):
        
        #将输入时间转化为时间戳
        import time
        import datetime
        x = time.strptime(x, "%Y/%m/%d")
        x = int(time.mktime(x))
        y = time.strptime(y, "%Y/%m/%d")
        y = int(time.mktime(y))


        '''
        利率列表
        lilv1利息变动日
        lilv2六个月内利率
        lilv3六个月至一年利率
        lilv4一至三年利率
        lilv5三至五年利率
        lilv6五年以上利率
        '''
        lilv1 = [7780,8535,8592,9131,9312,9617,9731,10157,10310,10408,10567,10752,11739,12720,13266,13379,13590,13652,13715,13747,13771,13868,14138,14161,14182,14210,14236,14902,14969,15014,15070,15162,15499,15527,16396,16495,16566,16614,16673,16732]
        lilv2 = [8.10 ,8.82 ,9.00 ,9.00 ,10.08 ,9.72 ,9.18 ,7.65 ,7.02 ,6.57 ,6.12 ,5.58 ,5.04 ,5.22 ,5.40 ,5.58 ,5.67 ,5.85 ,6.03 ,6.21 ,6.48 ,6.57 ,6.21 ,6.12 ,6.03 ,5.04 ,4.86 ,5.10 ,5.35 ,5.60 ,5.85 ,6.10 ,5.85 ,5.60 ,5.60 ,5.35 ,5.10 ,4.85 ,4.60 ,4.35 ]
        lilv3 = [8.64 ,9.36 ,10.98 ,10.98 ,12.06 ,10.98 ,10.08 ,8.64 ,7.92 ,6.93 ,6.39 ,5.85 ,5.31 ,5.58 ,5.85 ,6.12 ,6.39 ,6.57 ,6.84 ,7.02 ,7.29 ,7.47 ,7.20 ,6.93 ,6.66 ,5.58 ,5.31 ,5.56 ,5.81 ,6.06 ,6.31 ,6.56 ,6.31 ,6.00 ,5.60 ,5.35 ,5.10 ,4.85 ,4.6,4.35]
        lilv4 = [9.00 ,10.80 ,12.24 ,12.96 ,13.50 ,13.14 ,10.98 ,9.36 ,9.00 ,7.11 ,6.66 ,5.94 ,5.49 ,5.76 ,6.03 ,6.30 ,6.57 ,6.75 ,7.02 ,7.20 ,7.47 ,7.56 ,7.29 ,7.02 ,6.75 ,5.67 ,5.40 ,5.60 ,5.85 ,6.10 ,6.40 ,6.65 ,6.40 ,6.15 ,6.00 ,5.75 ,5.50 ,5.25 ,5.00 ,4.75]
        lilv5 = [9.54 ,12.06 ,13.86 ,14.58 ,15.12 ,14.94 ,11.70 ,9.90 ,9.72 ,7.65 ,7.20 ,6.03 ,5.58 ,5.85 ,6.12 ,6.48 ,6.75 ,6.93 ,7.20 ,7.38 ,7.65 ,7.74 ,7.56 ,7.29 ,7.02 ,5.94 ,5.76 ,5.96 ,6.22 ,6.45 ,6.65 ,6.90 ,6.65 ,6.40 ,6.00 ,5.75 ,5.50 ,5.25 ,5.00 ,4.75]
        lilv6 = [9.72 ,12.24 ,14.04 ,14.76 ,15.30 ,15.12 ,12.42 ,10.53 ,10.35 ,8.01 ,7.56 ,6.21 ,5.76 ,6.12 ,6.39 ,6.84 ,7.11 ,7.20 ,7.38 ,7.56 ,7.83 ,7.83 ,7.74 ,7.47 ,7.20 ,6.12 ,5.94 ,6.14 ,6.40 ,6.60 ,6.80 ,7.05 ,6.80 ,6.55 ,6.15 ,5.90 ,5.65 ,5.40 ,5.40 ,4.90]


        #确认计息期间
        i = 0
        while x >=lilv1[i]*24*3600: 
        	i+=1
        j = -1
        while y <=lilv1[j]*24*3600:
        	j-=1

        #print x
        #print y
        #print lilv1[0]*24*3600
        #print i
        #print j
        #print lilv1[i:j+1]

        #计算欠款天数,并确定适用利率水平,六个月记为180天，一年记为360天
        day = (y-x)/3600/24
        #print day

        if day<=180:
                lilv=lilv2
        elif day>180 and day<=360:
               lilv=lilv3
        elif day>360 and day<=1080:
                lilv=lilv4
        elif day>1080 and day<=1800:
                lilv=lilv5
        else:
               lilv=lilv6

        #print lilv[:]
        #print lilv1[i]
        #print lilv1[j]

        '''计算欠款利息
        lilv[i-1]/100/360 中减1为适用调整前利率
        lilv1[i]-(x/3600/24)-1 中减1为扣减天数
        (y/3600/24)-lilv1[j]+1 中加1为补足天数
        day2 为计息日期差值
        dateArray = datetime.datetime.utcfromtimestamp(x+28800) 中加28800为调整为北京时间
        date1为计息起始时间
        date2为计息截止时间
        '''
        #lixi = day*lilv*z 
        lixi =0
        lixiall = 0 #分段利息合计
        global lixiall2 #全局利息合计
        day2 = lilv1[i]-(x/3600/24)-1
        #print lixiall

        while lilv1[i] <= lilv1[j]:
                lixi = day2*lilv[i-1]/100/360*z
                lixiall = lixiall + lixi
                if day2 == lilv1[i]-(x/3600/24)-1:
                        date1 = datetime.datetime.utcfromtimestamp(x+28800)
                        dateout1 = date1.strftime("%Y年%m月%d日")
                        date2 = datetime.datetime.utcfromtimestamp(lilv1[i]*24*3600)
                        dateout2 = date2.strftime("%Y年%m月%d日")
                else:
                        date1 = datetime.datetime.utcfromtimestamp(lilv1[i-1]*24*3600)
                        dateout1 = date1.strftime("%Y年%m月%d日")
                        date2 = datetime.datetime.utcfromtimestamp(lilv1[i]*24*3600)
                        dateout2 = date2.strftime("%Y年%m月%d日")
                print dateout1,dateout2,day2,'天 * 年息', lilv[i-1],'% =', lixi
                if i == len(lilv)-1:
                        lixi = ((y/3600/24)-lilv1[j]+1)*lilv[j]/100/360*z
                        lixiall = lixiall + lixi
                        date1 = datetime.datetime.utcfromtimestamp(lilv1[j]*24*3600)
                        dateout1 = date1.strftime("%Y年%m月%d日")
                        date2 = datetime.datetime.utcfromtimestamp(y+28800)
                        dateout2 = date2.strftime("%Y年%m月%d日")
                        print dateout1,dateout2,(y/3600/24)-lilv1[j]+1,'天 * 年息',lilv[j],'% =', lixi
                        break
                i+=1
                day2 = lilv1[i]-lilv1[i-1]
        else:
                lixi = ((y/3600/24)-lilv1[j]+1)*lilv[j]/100/360*z
                lixiall = lixiall + lixi
                print (y/3600/24)-lilv1[j]+1,'天 * 年息',lilv[j],'% =', lixi

        print '分段利息合计：',lixiall
        lixiall2 = lixiall2 + lixiall

        return


        #将计算过程导出到txt

lixiall2 = 0 #全局变量
ss = 1
#ss = input("分段数：")
i = 0
while ss > i :
        x = "2014/1/1"
        #x = raw_input("欠款时间（格式2015/1/1）：")
        y = "2015/11/1"
        #y = raw_input("还款时间（格式2015/1/1）：")
        z = 10000
        #z = input("欠款金额：")
        lixi(x,y,z)
        i+=1

print '利息总计：',lixiall2
