import android 

droid = android.Android()

droid.ttsSpeak('今天教你如何在平板上向github上传代码。')
droid.ttsSpeak('前提是你已经有github账户，如果没有可以访问其镜像网站注册账户。')
print('github的镜像网站：https://bgithub.xyz/')

droid.ttsSpeak('1.在应用商店搜索aidlux,并安装')

droid.ttsSpeak('2.进入aidlux打开终端，使用apt-get install git命令安装Git')
print("apt-get install git")

droid.ttsSpeak('3.国内直接访问github速度慢，需要使用如下命令给Git配置一个镜像网站')
print('git config --global url."https://bgithub.xyz/".insteadOf "https://github.com/"')

droid.ttsSpeak('4.配置你github的用户名和邮箱账户')
print('git config --global user.name "你的用户名"')
print('git config --global user.email "你的邮箱"')

droid.ttsSpeak('5.配置你github的用户名和邮箱账户')