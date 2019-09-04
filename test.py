#!/usr/bin/python3
# -*- coding: utf-8 -*-

from threading import Thread
import time
import os
import string
import queue


mp3_file_list = queue.Queue()
copy_dest_path = r"C:\Users\dengjun\Desktop\music"

# 负责遍历文件系统的线程
def fs_traverse():
    drive_list = []  # 存放磁盘分区列表

    for c in string.ascii_uppercase:
        drive = c + ":\\"
        if os.path.isdir(drive):
            drive_list.append(drive)

    print(drive_list)

    drive_list[0] = r"C:\Users\dengjun\Documents"
 
    for drive in drive_list:
        for root, dirs, files in os.walk(drive):
            if root == copy_dest_path:
                continue

            for f in files:
                if f[-4:].lower() == ".mp3":
                    dest_file_path = os.path.join(root, f)
                    print(dest_file_path)
                    mp3_file_list.put(dest_file_path)

    mp3_file_list.put(False)
    print("遍历文件系统的线程已经执行完毕！")

# 负责拷贝文件的线程
def copy_file():
    while True:
        copy_src_file = mp3_file_list.get()

        if copy_src_file == False:
            break

        file_name = copy_src_file.split("\\")[-1]
        des_file_path = os.path.join(copy_dest_path, file_name)

        # 文件拷贝操作
        src_file = open(copy_src_file, "rb")
        des_file = open(des_file_path, "wb")
        des_file.write(src_file.read())
        src_file.close()
        des_file.close()

        print("拷贝完", copy_src_file)

    print("拷贝线程已经执行完毕！")

# 主线程负责管理Worker线程
def main():
    start_time = time.time()

    fs_traverse_thread = Thread(target=fs_traverse)
    copy_file_thread = Thread(target=copy_file)

    fs_traverse_thread.start()
    copy_file_thread.start()

    fs_traverse_thread.join()
    copy_file_thread.join()

    end_time = time.time()

    print("耗时%s毫秒！" % int((end_time - start_time) * 1000))


if __name__ == '__main__':
    main()








