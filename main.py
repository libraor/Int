x = raw_input("Ƿ��ʱ�䣨��ʽ2015/1/1����")
y = raw_input("����ʱ�䣨��ʽ2015/1/1����")
z = input("Ƿ���")

#������ʱ��ת��Ϊʱ���
import time
x = time.strptime(x, "%Y/%m/%d")
x = int(time.mktime(x))
y = time.strptime(y, "%Y/%m/%d")
y = int(time.mktime(y))

#����Ƿ������
day = (y-x)/3600/24

#����Ƿ������
lilv = 0.06/360

#����Ƿ����Ϣ
lixi = day*lilv*z


#��������̵�����excel

