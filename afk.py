import asyncio
import time
import threading
from pythonosc import udp_client

enabled = True
autojump = True
autowalk = True
autospin = True
autochat = True
afk_message = "has been AFK for: "

start_time = time.time()
client = udp_client.SimpleUDPClient("127.0.0.1", 9000)
client.send_message("/input/Jump", 0)

client.send_message("/input/LookHorizontal", autospin and 1 or False)
client.send_message("/input/Vertical", autowalk and 1 or False)


async def autoJump():
    while enabled and autojump:
        client.send_message("/input/Jump", 0)
        await asyncio.sleep(0.1)
        client.send_message("/input/Jump", 1)
        await asyncio.sleep(0.1)

async def autoChat():
    while enabled and autochat:
        elapsed = int(time.time() - start_time)
        hour = elapsed // 3600
        minute = (elapsed % 3600) // 60
        second = elapsed % 60

        chat_msg = f"{afk_message} {hour} (H) {minute} (M) {second} (S)"
        client.send_message("/chatbox/input", [chat_msg, True, False])
        await asyncio.sleep(3)

async def main():
    await asyncio.gather(autoJump(), autoChat())

def run_loop():
    asyncio.run(main())

if __name__ == "__main__":
    loop_thread = threading.Thread(target=run_loop, daemon=True)
    loop_thread.start()

    try:
        input("Press ENTER to quit...")
    finally:
        enabled = False
        client.send_message("/input/LookHorizontal", False)
        client.send_message("/input/Vertical", False)
        client.send_message("/chatbox/input", [" ", True, False])
        client.send_message("/input/Jump", 0)
        quit()
