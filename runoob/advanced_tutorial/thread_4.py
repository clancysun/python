#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: thread_4.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 19:16:22
############################

import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Staring " + self.name)
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完全
for t in threads:
    t.join()
print("Exiting Main Thread")
