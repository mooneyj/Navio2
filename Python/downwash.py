import sys
import time

import navio.pwm
import navio.util
import navio.adc

navio.util.check_apm()


PWM_OUTPUT = 0
SERVO_MIN = 1.000 #ms
SERVO_MAX = 1.150 #ms
SERVO_ABSMAX = 1.150 #ms


adc = navio.adc.ADC()
results = [0] * 3 #3col array, for airspeed, throttle position & time. #adc.channel_count 

#Function sets throttle pos and records over timeperiod tau
def setthr(thr,tau,result)


with navio.pwm.PWM(PWM_OUTPUT) as pwm:
    pwm.set_period(50)
    pwm.enable()

    #First initialise the ESC...
    
    
    #Then cycle through throttle positions whilst recording airspeed.
    while (True):
        #First initialise the ESC...
        pwm.set_duty_cycle(SERVO_MIN)
        time.sleep(1)
        pwm.set_duty_cycle(SERVO_ABSMAX)
        time.sleep(1)
        
        #Then perform experiment... 
        #Update duty cycle & record data at 50sps (max possible due to pwm freq).
        s = ''
        for i in range (0, adc.channel_count):
            results[i] = adc.read(i)
            s += 'A{0}: {1:6.4f}V '.format(i, results[i] / 1000)
        print(s)
        time.sleep(0.5)
