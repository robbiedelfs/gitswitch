import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
	print("Subprocess called.")
	subprocess.call(["php", "mailtest.php", "shell=True"])
        time.sleep(0.2)
