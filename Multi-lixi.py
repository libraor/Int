
def lixi(x,y,z):
        
        #������ʱ��ת��Ϊʱ���
        import time
        import datetime
        x = time.strptime(x, "%Y/%m/%d")
        x = int(time.mktime(x))
        y = time.strptime(y, "%Y/%m/%d")
        y = int(time.mktime(y))


        '''
        �����б�
        lilv1��Ϣ�䶯��
        lilv2������������
        lilv3��������һ������
        lilv4һ����������
        lilv5������������
        lilv6������������
        '''
        lilv1 = [7780,8535,8592,9131,9312,9617,9731,10157,10310,10408,10567,10752,11739,12720,13266,13379,13590,13652,13715,13747,13771,13868,14138,14161,14182,14210,14236,14902,14969,15014,15070,15162,15499,15527,16396,16495,16566,16614,16673,16732]
        lilv2 = [8.10 ,8.82 ,9.00 ,9.00 ,10.08 ,9.72 ,9.18 ,7.65 ,7.02 ,6.57 ,6.12 ,5.58 ,5.04 ,5.22 ,5.40 ,5.58 ,5.67 ,5.85 ,6.03 ,6.21 ,6.48 ,6.57 ,6.21 ,6.12 ,6.03 ,5.04 ,4.86 ,5.10 ,5.35 ,5.60 ,5.85 ,6.10 ,5.85 ,5.60 ,5.60 ,5.35 ,5.10 ,4.85 ,4.60 ,4.35 ]
        lilv3 = [8.64 ,9.36 ,10.98 ,10.98 ,12.06 ,10.98 ,10.08 ,8.64 ,7.92 ,6.93 ,6.39 ,5.85 ,5.31 ,5.58 ,5.85 ,6.12 ,6.39 ,6.57 ,6.84 ,7.02 ,7.29 ,7.47 ,7.20 ,6.93 ,6.66 ,5.58 ,5.31 ,5.56 ,5.81 ,6.06 ,6.31 ,6.56 ,6.31 ,6.00 ,5.60 ,5.35 ,5.10 ,4.85 ,4.6,4.35]
        lilv4 = [9.00 ,10.80 ,12.24 ,12.96 ,13.50 ,13.14 ,10.98 ,9.36 ,9.00 ,7.11 ,6.66 ,5.94 ,5.49 ,5.76 ,6.03 ,6.30 ,6.57 ,6.75 ,7.02 ,7.20 ,7.47 ,7.56 ,7.29 ,7.02 ,6.75 ,5.67 ,5.40 ,5.60 ,5.85 ,6.10 ,6.40 ,6.65 ,6.40 ,6.15 ,6.00 ,5.75 ,5.50 ,5.25 ,5.00 ,4.75]
        lilv5 = [9.54 ,12.06 ,13.86 ,14.58 ,15.12 ,14.94 ,11.70 ,9.90 ,9.72 ,7.65 ,7.20 ,6.03 ,5.58 ,5.85 ,6.12 ,6.48 ,6.75 ,6.93 ,7.20 ,7.38 ,7.65 ,7.74 ,7.56 ,7.29 ,7.02 ,5.94 ,5.76 ,5.96 ,6.22 ,6.45 ,6.65 ,6.90 ,6.65 ,6.40 ,6.00 ,5.75 ,5.50 ,5.25 ,5.00 ,4.75]
        lilv6 = [9.72 ,12.24 ,14.04 ,14.76 ,15.30 ,15.12 ,12.42 ,10.53 ,10.35 ,8.01 ,7.56 ,6.21 ,5.76 ,6.12 ,6.39 ,6.84 ,7.11 ,7.20 ,7.38 ,7.56 ,7.83 ,7.83 ,7.74 ,7.47 ,7.20 ,6.12 ,5.94 ,6.14 ,6.40 ,6.60 ,6.80 ,7.05 ,6.80 ,6.55 ,6.15 ,5.90 ,5.65 ,5.40 ,5.40 ,4.90]


        #ȷ�ϼ�Ϣ�ڼ�
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

        #����Ƿ������,��ȷ����������ˮƽ,�����¼�Ϊ180�죬һ���Ϊ360��
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

        '''����Ƿ����Ϣ
        lilv[i-1]/100/360 �м�1Ϊ���õ���ǰ����
        lilv1[i]-(x/3600/24)-1 �м�1Ϊ�ۼ�����
        (y/3600/24)-lilv1[j]+1 �м�1Ϊ��������
        day2 Ϊ��Ϣ���ڲ�ֵ
        dateArray = datetime.datetime.utcfromtimestamp(x+28800) �м�28800Ϊ����Ϊ����ʱ��
        date1Ϊ��Ϣ��ʼʱ��
        date2Ϊ��Ϣ��ֹʱ��
        '''
        #lixi = day*lilv*z 
        lixi =0
        lixiall = 0 #�ֶ���Ϣ�ϼ�
        global lixiall2 #ȫ����Ϣ�ϼ�
        if (y-x)/3600/24 < lilv1[i]-lilv1[j]: #�жϼ�Ϣ�ڼ��Ƿ�����Ϣ�䶯
            day2 = (y-x)/3600/24
        else:
            day2 = lilv1[i]-(x/3600/24)-1
        #print y-x
        #print lilv1[i]-lilv1[j]
        #print lixiall

        while lilv1[i] < lilv1[j]:
                lixi = day2*lilv[i-1]/100/360*z
                lixiall = lixiall + lixi
                if day2 == lilv1[i]-(x/3600/24)-1:
                        date1 = datetime.datetime.utcfromtimestamp(x+28800)
                        dateout1 = date1.strftime("%Y��%m��%d��")
                        date2 = datetime.datetime.utcfromtimestamp(lilv1[i]*24*3600)
                        dateout2 = date2.strftime("%Y��%m��%d��")
                else:
                        date1 = datetime.datetime.utcfromtimestamp(lilv1[i-1]*24*3600)
                        dateout1 = date1.strftime("%Y��%m��%d��")
                        date2 = datetime.datetime.utcfromtimestamp(lilv1[i]*24*3600)
                        dateout2 = date2.strftime("%Y��%m��%d��")
                result = [dateout1,dateout2,day2,'�� * ��Ϣ', lilv[i-1],'% =', lixi] #�����txt
                for k in range(0,7): 
                        result[k] = str(result[k])
                str1 = " "
                str1 = str1.join(result)
                print str1
                print "---------------------------------------------------------------"
                f = open("��Ϣ.txt",'a')
                f.write(str1+'\n')
                f.write("---------------------------------------------------------------"+"\n")
                f.close()
                if i == len(lilv)-1:
                        lixi = ((y/3600/24)-lilv1[j]+1)*lilv[j]/100/360*z
                        lixiall = lixiall + lixi
                        date1 = datetime.datetime.utcfromtimestamp(lilv1[j]*24*3600)
                        dateout1 = date1.strftime("%Y��%m��%d��")
                        date2 = datetime.datetime.utcfromtimestamp(y+28800)
                        dateout2 = date2.strftime("%Y��%m��%d��")
                        result = [dateout1,dateout2,(y/3600/24)-lilv1[j]+1,'�� * ��Ϣ',lilv[j],'% =', lixi] #�����txt
                        for k in range(0,7): 
                                result[k] = str(result[k])
                        str1 = " "
                        str1 = str1.join(result)
                        print str1
                        print "---------------------------------------------------------------"
                        f = open("��Ϣ.txt",'a')
                        f.write(str1+'\n')
                        f.write("---------------------------------------------------------------"+"\n")
                        f.close()
                        break
                i+=1
                day2 = lilv1[i]-lilv1[i-1]
        else:
                if (y-x)/3600/24 < lilv1[i]-lilv1[j]:
                    lixi = day2*lilv[j]/100/360*z
                    lixiall = lixiall + lixi
                    date1 = datetime.datetime.utcfromtimestamp(x+28800)
                    dateout1 = date1.strftime("%Y��%m��%d��")
                    date2 = datetime.datetime.utcfromtimestamp(y+28800)
                    dateout2 = date2.strftime("%Y��%m��%d��")
                    result = [dateout1,dateout2,day2,'�� * ��Ϣ',lilv[j],'% =', lixi] #�����txt
                    for k in range(0,7): 
                            result[k] = str(result[k])
                    str1 = " "
                    str1 = str1.join(result)
                    print str1
                    print "---------------------------------------------------------------"
                    f = open("��Ϣ.txt",'a')
                    f.write(str1+'\n')
                    f.write("---------------------------------------------------------------"+"\n")
                    f.close()


                else:

                    lixi = ((y/3600/24)-lilv1[j]+1)*lilv[j]/100/360*z
                    lixiall = lixiall + lixi
                    date1 = datetime.datetime.utcfromtimestamp(lilv1[j]*24*3600)
                    dateout1 = date1.strftime("%Y��%m��%d��")
                    date2 = datetime.datetime.utcfromtimestamp(y+28800)
                    dateout2 = date2.strftime("%Y��%m��%d��")
                    result = [dateout1,dateout2,(y/3600/24)-lilv1[j]+1,'�� * ��Ϣ',lilv[j],'% =', lixi] #�����txt
                    for k in range(0,7): 
                            result[k] = str(result[k])
                    str1 = " "
                    str1 = str1.join(result)
                    print str1
                    print "---------------------------------------------------------------"
                    f = open("��Ϣ.txt",'a')
                    f.write(str1+'\n')
                    f.write("---------------------------------------------------------------"+"\n")
                    f.close()

        result = ['�ֶα���',z,'�ֶ���Ϣ�ϼƣ�',lixiall]  #�����txt
        result[1] = str(result[1])
        result[3] = str(result[3])
        str1 = " "
        str1 = str1.join(result)
        print str1
        print "---------------------------------------------------------------"
        f = open("��Ϣ.txt",'a')
        f.write(str1+'\n')
        f.write("---------------------------------------------------------------"+"\n")
        f.close()
        lixiall2 = lixiall2 + lixiall

        return

print "----------------------------"
print "������Ϣ������ v1.20"
print "���ߣ���Ң �㽭������ʦ������"
print "Email:linyao@foxmail.com"
print "���ʱ䶯������2015��10��24��"
print "----------------------------"
f = open("��Ϣ.txt",'w')
f.write("-------------------------"+"\n")
f.write("������Ϣ����������ʣ� v1.20"+"\n")
f.write("���ߣ���Ң �㽭������ʦ������"+"\n")
f.write("Email:linyao@foxmail.com"+"\n")
f.write("���ʱ䶯������2015��10��24��"+"\n")
f.write("-------------------------"+"\n")
f.write("---------------------------------------------------------------"+"\n")
f.write("��������        ��������      ��Ϣ����    ��Ϣ��׼     ��Ϣ"+"\n")
f.write("---------------------------------------------------------------"+"\n")
f.close()

lixiall2 = 0.0 #ȫ�ֱ���
#ss = 1
ss = input("�ֶ�����")
i = 0
zz = 0.0 #����ͳ�Ʊ���
while ss > i :
        #x = "2012/9/5"
        x = raw_input("�������ڣ���ʽ2015/1/1����")
        #y = "2014/8/15"
        y = raw_input("�������ڣ���ʽ2015/1/1����")
        #z = 10000.0
        z = input("Ƿ���")
        zz = zz + z
        lixi(x,y,z)
        i+=1

result = ['�����ܼ�',zz,'��Ϣ�ܼƣ�',lixiall2] #�����txt
result[1] = str(result[1])
result[3] = str(result[3])
str1 = " "
str1 = str1.join(result)
print str1
print "---------------------------------------------------------------"
f = open("��Ϣ.txt",'a')
f.write(str1+'\n')
f.write("---------------------------------------------------------------"+"\n")
f.close()
