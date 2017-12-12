# AndroidMultiChannelBuild
Kit support generating multi-channel apk （Android多渠道打包工具）  


1、删除原先友盟中的设置（若没有忽略此步，跳转第2步）： 
<meta-data android:name="UMENG_CHANNEL" android:value="${channel}"/>

2、添加ChannelUtils类到项目中。只需在程序启动时的Activity中调用此接口设置渠道：
//友盟统计
String channel = ChannelUtils.getChannel(this);
AnalyticsConfig.setChannel(channel);
 
 
3、具体使用步骤：
(1)将想要批量打包的apk文件拷贝到PythonTool目录下（与py同级），运行py脚本即可打包完成。（生成的渠道apk包在output_** 目录下）
(2)你可以粘贴下面的渠道到channel.txt中保持它在windows端的可读性。

channel.txt在info目录下：   
DOSPY  
WANDOUJIA  
COOLAPK  
360  
YINGYONGBAO  
91  
XIAOMI  
HUAWEI  
GFAN  
BAIDU  
ANZHI  
AndroidChannelBuild.py是多渠道打包的脚本


4、执行命令 python AndroidChannelBuild.py  生成多渠道包；

