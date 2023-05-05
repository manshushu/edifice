import RPi.GPIO as GPIO
import time

# 设置GPIO模式为BCM编码模式，并关闭警告信息
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 风扇控制引脚的BCM编码
fan_pin = 4

# 温度阈值，超过这个温度就启动风扇
fan_threshold = 50

# 设置风扇控制引脚为输出模式
GPIO.setup(fan_pin, GPIO.OUT)

# 初始化风扇状态为关闭
GPIO.output(fan_pin, False)

# 定义读取温度的函数
def get_cpu_temperature():
    res = open('/sys/class/thermal/thermal_zone0/temp', 'r').readline()
    return float(res)/1000

# 定义调整风扇转速的函数
def set_fan_speed(speed):
    # 将速度的百分比转换为占空比
    duty_cycle = speed / 100.0
    # 根据占空比调整PWM信号的占空比
    pwm.ChangeDutyCycle(duty_cycle)

# 初始化PWM信号，控制风扇转速
pwm = GPIO.PWM(fan_pin, 100)
pwm.start(0)

try:
    while True:
        # 读取当前温度
        temperature = get_cpu_temperature()

        # 如果当前温度超过阈值，则启动风扇并逐步调整风扇转速
        if temperature > fan_threshold:
            GPIO.output(fan_pin, True)
            speed = min(100, int((temperature - fan_threshold) * 2))
            set_fan_speed(speed)

        # 如果当前温度低于阈值，则关闭风扇
        else:
            GPIO.output(fan_pin, False)
            set_fan_speed(0)

        # 每隔一秒钟读取一次温度
        time.sleep(1)

except KeyboardInterrupt:
    # 当用户按下Ctrl+C时，停止PWM信号和GPIO引脚
    pwm.stop()
    GPIO.cleanup()
