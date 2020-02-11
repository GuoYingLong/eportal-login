# -*- coding: utf-8 -*-
import requests, time, json,sys

# 认证服务器访问的IP地址
IP = 'http://10.200.200.248'

params = (
     ('method', 'login'),
)

# 登录
def login(username, password):
    
    # 设置表格数据
    data = {
        'userId': username,
        'password': password,
        'service': '',
        'queryString': 'wlanuserip=d3f94b58e944bac825d41e10028c6ed5&wlanacname=f0a84436888c6c46f8767008165e7980&ssid=&nasip=21aea9e1c34fe0bfecaa6d4544af21c6&snmpagentip=&mac=92077bdf24107b48b3372f446e0cafe9&t=wireless-v2&url=709db9dc9ce334aa024775e22fb74a232056518a7aae8aa6&apmac=&nasid=f0a84436888c6c46f8767008165e7980&vid=d468ea41e905d091&port=f1492fa065990d34&nasportid=5b9da5b08a53a540a2f7a2b77b704e7de708bfac0f0f136217662997cd7aedea',
        'operatorPwd': '',
        'operatorUserId': '',
        'validcode': '',
        'passwordEncrypt': 'false'
    }

    while True:
        try:
            response = requests.post(IP + '/eportal/InterFace.do', params=params, data=data)
            if response.status_code == 200:  #判断返回http状态码200为成功
                response.encoding = 'UTF-8'  #修改编码格式为UTF-8
                result = json.loads(response.text)
                if 'success' in result['result']:
                    # print(response.text)
                    print("校园网登入成功！",result['message'])
                    break
                elif '密码不匹配,请输入正确的密码!' in result['message']:
                    print("密码错误！请重新尝试")
                    break
                elif '用户不存在' in result['message']:
                    print("用户不存在！请重新尝试")
                    break
                else:
                    print("登录失败", result['message'])
                    time.sleep(3)
            else:
                print("提交请求失败！")
                time.sleep(3)
        except Exception as e:
            print("正在尝试重连......", e)
            time.sleep(3)

if __name__ == '__main__':
	#认证
    username = input("用户名:")
    password = input("密码:")

    #封装成exe文件后，外部传递参数
    # username = sys.argv[1]
    # password = sys.argv[2]
    login(username,password)
