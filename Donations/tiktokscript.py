
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import GiftEvent

client: TikTokLiveClient = TikTokLiveClient(
    unique_id="Your-Tiktok-Username", **(
        {
            "enable_detailed_gifts": True
        }
    )
)

coinsspent = 0
foodportions = 0

@client.on("gift")
async def on_gift(event : GiftEvent):
    global coinsspent, foodportions
    coinsspent += event.gift.info.diamond_count
    print(f"coinsspent: {coinsspent}")
    foodportions = coinsspent//100
    coinsspent = coinsspent%100
    if foodportions > 0:
        print(f"dropping spent {foodportions} portions")

if __name__ == '__main__':
    client.run()