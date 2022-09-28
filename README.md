## adaptivecardsng - Python Library for Easy Building of Adaptive Cards Object JSON
**This project is licensed under GPL 3.0 and later**

### What are Adaptive Cards?
Per the documentation at https://adaptivecards.io (a Microsoft website), Adaptive Cards 
are best described as follows:

  > Adaptive Cards are platform-agnostic snippets of UI, authored in JSON, 
  > that apps and services can openly exchange. When delivered to a specific 
  > app, the JSON is transformed into native UI that automatically adapts to 
  > its surroundings. It helps design and integrate light-weight UI for all 
  > major platforms and frameworks.

This is heavily useful in automated bot response applications, etc. including those 
built upon and working with Microsoft Teams and the Microsoft bot frameworks.

This way, you can use Python object-oriented programming to easily generate the JSON for objects 
and cards without ever having to touch the JSON underneath.

### Aren't there several Adaptive Cards frameworks already for Python?

Okay, you got us - this is Yet Another Implementation of Adaptive Cards (AC for short below).

However, the only Python libraries I could find for Adaptive Cards that were 'developer 
friendly' were either Cisco's outdated repository for Adaptive Cards support, or `adaptivecards` 
on PyPI which has not been updated since AC version 1.2.  This set of code functions - 
adaptivecardsng - is a Python Object-Oriented design of AC development and creation, and 
follows the spec at https://adaptivecards.io/explorer/ as closely as it can for the current release.

### Which Adaptive Cards spec version is this library written for?

As of right now while you're reading this document, this library is written to be AC 1.5 compliant.

It also includes a number of additional things that are not available in other versions, such as 
the specific schemas and Enums that are defined within the AC spec as actual Enums and object types 
here so that you can more easily choose options without having to remember all the strings. This 
also makes sure that you don't have any type of unrecognized arguments in the JSON when sending it 
off to endpoints.

### So, this is entirely Python, right?  No extra dependencies?

Yep, fully written in Python.  Specifically, Python 3, with support for Python 3.7 and newer.

Don't ask for older Python versions, please, because we use certain type definitions and type
hinting that don't work with older versions of Python before 3.7.  This is due to what the Python 
versions of `__future__` support and older than 3.7 does not support the type annotations we use 
for type hinting, and we have that there intentionally.

### Usage

There are some differences between this library and `adaptivecards`, there are some distinct 
differences.

Because a code sample is more useful to understand, we'll write one here (this is also in the file 
`examples/readme_example.py`):

```python
from adaptivecardsng.elements import TextBlock, FontType, FontSize, FontWeight
from adaptivecardsng.containers import Container, ColumnSet, Column
from adaptivecardsng.cards import AdaptiveCard

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
                   "[https://github.com/teward/adaptivecardsng]"
                   "(https://github.com/teward/adaptivecardsng)",
              subtle=True, wrap=True, font_size=FontSize.small)
]

print(str(card))
```

This generates this output:

```json
{
  "$schema": "https://adaptivecards.io/schemas/adaptive-card.json",
  "body": [
    {
      "items": [
        {
          "size": "large",
          "style": "default",
          "text": "Adaptive Cards Example",
          "type": "TextBlock",
          "weight": "bolder",
          "wrap": true
        },
        {
          "columns": [
            {
              "items": [
                {
                  "style": "default",
                  "text": "author",
                  "type": "TextBlock",
                  "weight": "bolder",
                  "wrap": true
                },
                {
                  "style": "default",
                  "text": "version",
                  "type": "TextBlock",
                  "weight": "bolder",
                  "wrap": true
                }
              ],
              "width": "stretch"
            },
            {
              "items": [
                {
                  "style": "default",
                  "text": "Thomas Ward",
                  "type": "TextBlock",
                  "wrap": true
                },
                {
                  "fontType": "monospace",
                  "style": "default",
                  "text": "0.0.0-alpha.0",
                  "type": "TextBlock",
                  "wrap": true
                }
              ],
              "width": "stretch"
            }
          ],
          "type": "ColumnSet"
        }
      ],
      "type": "Container"
    },
    {
      "isSubtle": true,
      "size": "small",
      "style": "default",
      "text": "more information available at [https://github.com/teward/adaptivecardsng](https://github.com/teward/adaptivecardsng)",
      "type": "TextBlock",
      "wrap": true
    }
  ],
  "type": "AdaptiveCard",
  "version": "1.5"
}
```

And that in turn, when rendered in Teams after properly being transmitted and formatted as a 
Teams-compatible message looks something like this:

![adaptivecardsng_teams_rendering](https://user-images.githubusercontent.com/327952/192674758-8cbfd8be-7b5d-430c-a63f-8a369bb1e657.png)


<!--
### Installation

While you can always download this from GitHub and run the installer, we actually do have this 
uploaded to PyPI.  So you can install it with code as simple as:

    python3 -m pip install adaptivecardsng

# We don't have installation instructions yet because this is in devel.
-->

