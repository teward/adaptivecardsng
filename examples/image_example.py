from adaptivecardsng.elements import Image, ImageSize
from adaptivecardsng.elements import TextBlock
from adaptivecardsng.containers import Container
from adaptivecardsng.cards import AdaptiveCard

card = AdaptiveCard()

card.body = [
    Container(items=[
        TextBlock(text="This image is at: [https://adaptivecards.io/content/cats/1.png]"
                       "(https://adaptivecards.io/content/cats/1.png)"),
        Image(url=f"https://adaptivecards.io/content/cats/1.png",
              alt_text="Catto", size=ImageSize.small)
        ])
]

print(str(card))

