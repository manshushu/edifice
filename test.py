import multiprocessing
import math
import time

def calculate_prime(n):
    """
    计算质数的函数
    """
    primelist = []
    for num in range(2, n + 1):
        isprime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if (num % i) == 0:
                isprime = False
                break
        if isprime:
            primelist.append(num)
    return primelist

if __name__ == "__main__":
    processes = []
    num_processes = multiprocessing.cpu_count() # 获取本机的CPU数量
    print("Running on", num_processes, "cores")
    
    # 启动多个进程进行计算
    for i in range(num_processes):
        process = multiprocessing.Process(target=calculate_prime, args=(500000,))
        processes.append(process)
        process.start()
        
    # 让程序在后台运行指定时间（例如60秒）
    runtime = 60
    print("Program will run for {} seconds...".format(runtime))
    time.sleep(runtime)

    # 终止所有进程并退出程序
    print("Terminating all processes...")
    for process in processes:
        process.terminate()