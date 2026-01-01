import time
from pythonosc import udp_client
import random

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)
cooldown = 0.5

while True:
    x,y,z = random.uniform(0, 360), random.uniform(0, 360),random.uniform(0, 360)
    client.send_message("/tracking/eye/CenterVec", [x, y, z])

    pitch,yaw = random.uniform(0,360),random.uniform(-360,360)
    client.send_message("/tracking/eye/CenterPitchYaw", [pitch, yaw])

    time.sleep(cooldown)
