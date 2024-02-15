from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import GiftEvent
import serial
import time

client: TikTokLiveClient = TikTokLiveClient(
    unique_id="Your-Tiktok-Username", **(
        {
            "enable_detailed_gifts": True
        }
    )
)

ser = serial.Serial('COM3', 9600)

def dispense_portion():
    ser.write(b'd')
    time.sleep(5)
ser.open()

coinsspent = 0
foodportions = 0

@client.on("gift")
async def on_gift(event : GiftEvent):
    global coinsspent, foodportions
    coinsspent += event.gift.info.diamond_count
    foodportions = coinsspent//100
    coinsspent = coinsspent%100
    if foodportions > 0:
        for i in range(foodportions):
            dispense_portion()

if __name__ == '__main__':
    client.run()
