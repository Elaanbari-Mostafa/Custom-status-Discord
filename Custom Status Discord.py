from pypresence import Presence
import time 

start = int(time.time())
client_id = "id client here"
RPC = Presence(client_id)
RPC.connect()

while True:
    RPC.update(
        large_image = "Name of image",
        small_image = "Name of image",
        large_text = "hover text",
        small_text = "hover text",
        state = "state",
        start = start,
        pid = 1,
        details = "details",
        buttons = [ { "label":"Name of first Button","url":"url here" } ,
                    { "label":"Name of second Button","url":"url here" } ]
    )
    time.sleep(50)
    #print("start")
