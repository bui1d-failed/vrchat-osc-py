import time
from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)
eye_closed_amount = 0.1
rate = 0.0001
cooldown1 = 0.5
cooldown2 = 5
while True:

    while eye_closed_amount <= 1.0:
        client.send_message("/tracking/eye/EyesClosedAmount", eye_closed_amount)
        eye_closed_amount += rate

    time.sleep(cooldown1)
    while eye_closed_amount > 0.1:
        client.send_message("/tracking/eye/EyesClosedAmount", eye_closed_amount)
        eye_closed_amount -= rate
    time.sleep(cooldown2)
