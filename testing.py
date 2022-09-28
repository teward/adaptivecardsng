from adaptivecardsng.elements import TextBlock
from adaptivecardsng.cards import AdaptiveCard
from adaptivecardsng.helpers import TeamsAdaptiveMessage

from datetime import date

from adaptivecardsng.enums import FontWeight, FontSize, FontType

if __name__ == "__main__":
    card = AdaptiveCard()
    card.body = [
        TextBlock(text=f'{date.today().strftime("%m/%d/%Y")} '
                       f'Wifi Password Updated:',
                  font_weight=FontWeight.bolder, font_size=FontSize.large, wrap=False),
        TextBlock(text=f'I AM THE VERY MODEL OF A MODERN MAJOR GENERAL.',
                  font_size=FontSize.large, font_type=FontType.monospace, wrap=True)
    ]

    message = TeamsAdaptiveMessage(card)
    print(message.as_json())