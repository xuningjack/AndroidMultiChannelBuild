__author__ = 'Jack'
import os
import sys
import shutil
import zipfile


# 空文件 便于写入此空文件到apk包中作为channel文件
src_empty_file = 'info/info.txt'
f = open(src_empty_file, 'a')
f.close()

# 获取渠道列表
channel_file = 'info/channels.txt'
f = open(channel_file)
lines = f.readlines();
f.close()

# 获取所有APK文件
apk_path = os.listdir()
src_apks = []
for file in apk_path:
    if os.path.isfile(file):
        file_path, file_extension = os.path.splitext(file)
        if file_extension == '.apk':
            src_apks.append(file)

# 遍历渠道号并写入apk

for src_apk in src_apks:
    src_apk_file_name = os.path.basename(src_apk)
    src_apk_name, src_apk_extension = os.path.splitext(src_apk)
    output_dir = 'output_' + src_apk_name + '/'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for line in lines:
        target_channel = line.strip()
        target_apk = output_dir + src_apk_name + "-" + target_channel + src_apk_extension
        shutil.copy(src_apk,  target_apk)
        zipped = zipfile.ZipFile(target_apk, 'a', zipfile.ZIP_DEFLATED)
        empty_channel_file = "META-INF/channel_{channel}".format(channel=target_channel)
        zipped.write(src_empty_file, empty_channel_file)
        zipped.close()


