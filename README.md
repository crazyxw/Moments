#### Setup1: 运行前先连接手机,打开开发者模式
#### Setup2: 在打开appium
#### Setup3: 设置用户名密码, 这里使用的是QQ登陆
```
# deviceName请根据自身手机进行设置
# 如果不想每次都登陆,请修改desired_caps为:
       desired_caps = {
          "platformName": "Android",
          "deviceName": "MI_5s_Plus",
          "appPackage": "com.tencent.mm",
          "appActivity": ".ui.LauncherUI",
          "noReset": True,
            }
# 然后把run方法里的login模块注释掉即可
```
##### TODO：去重&存储
