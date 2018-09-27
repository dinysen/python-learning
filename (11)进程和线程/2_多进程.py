#/usr/bin/env python3
#-*- coding:utf-8 -*-

#Unix/Linux系统的多进程创建，使用os.fork()方法
#由于windows系统上无法实现,所以只做记录

#跨平台的进程创建方法
from multiprocessing import Process,Pool
import os,time,random
def createProcess(name):
	print("Create a child process called %s (%s) " % (name,os.getpid()));

def long_task_proc(name):
	print("Run task %s(%s)" % (name,os.getpid()));
	start = time.time();
	time.sleep(random.random()*3);
	end = time.time();
	print("Task %s run %.2f seconds " % (name,end-start));

if __name__=="__main__":
#新创建一个进程
	print("Parent process is %s " % os.getpid());
#	p = Process(target=createProcess,args=("test",));
#	print("Child process will start");
#	p.start();
	#join()方法让上一个进程完成后处理下一件事情，常用语进程间的同步
#	p.join();
#	print("Child process end");
	
	#因为我的电脑是4核，所以第5个进程会等待某一个先前的进程结束后再启动
	p = Pool(4);
	for i in range(5):
		p.apply_async(long_task_proc,args=(i,));
	print("Waiting all processes done...");
	#close()的意思是进程池中不能增加其他进城了
	p.close();
	p.join();
	print("All subprocesses done...");
