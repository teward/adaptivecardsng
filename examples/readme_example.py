from adaptivecardsng.elements import TextBlock, FontType, FontSize, FontWeight
from adaptivecardsng.containers import Container, ColumnSet, Column
from adaptivecardsng.cards import AdaptiveCard
from adaptivecardsng.messages.teams import TeamsAdaptiveMessage

card = AdaptiveCard()
card.body = [
    Container(items=[
        TextBlock(text=f'Adaptive Cards Example',
                  font_weight=FontWeight.bolder, font_size=FontSize.large, wrap=True),
        ColumnSet(columns=[
            Column(width='stretch',
                   items=[
                       TextBlock(text="author", font_weight=FontWeight.bolder, wrap=True),
                       TextBlock(text='version', font_weight=FontWeight.bolder, wrap=True)
                   ]),
            Column(width='stretch',
                   items=[
                       TextBlock(text="Thomas Ward", wrap=True),
                       TextBlock(text="0.0.0-alpha.0", wrap=True,
                                 font_type=FontType.monospace)
                   ])
        ])
    ]),
    TextBlock(text="more information available at "
                   "(the GitHub Repository for adaptivecardsng)"
                   "[https://github.com/teward/adaptivecardsng]",
              subtle=True, wrap=True, font_size=FontSize.small)
]

message = TeamsAdaptiveMessage(card)

print(str(message))
