#vim: set fileencoding:utf-8

__author__ = 'Jack'
import os
import sys
import shutil
import zipfile


#空文件 便于写入此空文件到apk包中作为channel文件
src_empty_file = 'info/info.txt'
f = open(src_empty_file, 'a')
f.close()

#获取渠道列表
channel_file = 'info/channels.txt'
f = open(channel_file)
lines = f.readlines();
f.close()

#获取所有APK文件
# python3 : os.listdir()即可，这里使用兼容Python2的os.listdir('.')
apk_path = os.listdir(".")
src_apks = []
for file in apk_path:
    if os.path.isfile(file):
		# 分割文件名与后缀
        file_path, file_extension = os.path.splitext(file)
        if file_extension == '.apk':
            src_apks.append(file)

#遍历渠道号并写入apk
for src_apk in src_apks:
    src_apk_file_name = os.path.basename(src_apk)
	#扩展名为apk
    src_apk_name, src_apk_extension = os.path.splitext(src_apk)
	#最终生成的多渠道apk的名称
    output_dir = 'output_' + src_apk_name + '/'
	#目录不存在则创建
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for line in lines:
		# 获取当前渠道号，因为从渠道文件中获得带有\n,所有strip一下
        target_channel = line.strip()
		#拼接对应渠道号的apk
        target_apk = output_dir + src_apk_name + "-" + target_channel + src_apk_extension
		#复制源apk到目标apk中
        shutil.copy(src_apk,  target_apk)
		#压缩
        zipped = zipfile.ZipFile(target_apk, 'a', zipfile.ZIP_DEFLATED)
		#初始化渠道信息
        empty_channel_file = "META-INF/channel_{channel}".format(channel=target_channel)
		#写入渠道信息
        zipped.write(src_empty_file, empty_channel_file)
		#关闭zip流
        zipped.close()