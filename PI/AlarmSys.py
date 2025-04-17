from gpiozero import LED, Button as GpioButton
from SevenSeg import SevenSeg
import requests
import time


adresse = "192.168.2.56/dashboard/orcl"
api_url = f"http://{adresse}/api.php"

seven_seg = SevenSeg(16, 12, 7, 26, 19, 20, 21, 18, False)

# LED alarm
led_alarm = LED(6)

# Alarm Zones
zone1 = GpioButton(22)
zone2 = GpioButton(23)
zone3 = GpioButton(9)
zone4 = GpioButton(11)
btnActivate = GpioButton(17)
btnDeactivate = GpioButton(27)
btn_reset = GpioButton(0) # to change after


systemStatus = 0
changement_local = False

def launch_sys_local():
    global changement_local, systemStatus
    changement_local = True
    seven_seg.cout_up()
    led_alarm.on()
    requests.put(f"{api_url}/etat/update")
    systemStatus = 1
    time.sleep(0.5)

def shutdown_sys_local():
    global changement_local, systemStatus
    changement_local = True
    seven_seg.cout_down()
    led_alarm.off()
    requests.put(f"{api_url}/etat/update")
    systemStatus = 0
    time.sleep(0.5)


def launch_sys():
    seven_seg.cout_up()
    led_alarm.on()

def shutdown_sys():
    seven_seg.cout_down()
    led_alarm.off()


def reset_sys():
    led_alarm.off()

# Zone 1
def zone1_onclick():
    if systemStatus == 1:
        seven_seg.show1()
        led_alarm.blink()
        requests.put(f"{api_url}/zones/1")

# Zone 2
def zone2_onclick():
    if systemStatus == 1:
        seven_seg.show2()
        led_alarm.blink()
        requests.put(f"{api_url}/zones/2")

# Zone 3
def zone3_onclick():
    if systemStatus == 1:
        seven_seg.show3()
        led_alarm.blink()
        requests.put(f"{api_url}/zones/3")

# Zone 4
def zone4_onclick():
    if systemStatus == 1:
        seven_seg.show4()
        led_alarm.blink()
        requests.put(f"{api_url}/zones/4")

zone1.when_pressed = zone1_onclick
zone2.when_pressed = zone2_onclick
zone3.when_pressed = zone3_onclick
zone4.when_pressed = zone4_onclick
btn_reset.when_pressed = reset_sys
btnActivate.when_pressed = launch_sys_local
btnDeactivate.when_pressed = shutdown_sys_local

try:
    response = requests.get(f"{api_url}/etat")
    etat = response.json()["etat"]
    systemStatus = int(etat)
    if systemStatus == 0:
        seven_seg.show0()
    else:
        seven_seg.showA()
except Exception as e:
    print("Erreur lors de l'initialisation :", e)

# Boucle principale
while True:
    try:
        response = requests.get(f"{api_url}/etat")
        etat = int(response.json()["etat"])

        if etat != systemStatus:
            if not changement_local:
                if etat == 1:
                    launch_sys()
                else:
                    shutdown_sys()
            systemStatus = etat
            changement_local = False

        time.sleep(1)

    except Exception as e:
        print("Erreur de connexion :", e)


