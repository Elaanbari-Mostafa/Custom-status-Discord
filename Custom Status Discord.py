from pypresence import Presence
import time 

start = int(time.time())
client_id = ""
RPC = Presence(client_id)
RPC.connect()

while True:
    RPC.update(
        large_image = "algo",
        small_image = "programming",
        large_text = "ALGO TO THE MOON",
        small_text = "Programming",
        state = "Just thinking...",
        start = start,
        pid = 1,
        details = "I'm a Programmer and Coding is my life",
        buttons = [ { "label":"Algo in YouTube","url":"https://www.youtube.com/watch?v=mDNKfBQfkwA" } ,
                    { "label":"Algo in Discord","url":"https://discord.gg/y7usVZnG" } ]
    )
    time.sleep(50)
    #print("start")