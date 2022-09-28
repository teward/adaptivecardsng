# adaptivecardsng - Python Library for Easy Building of AdaptiveCards Object JSON

## What is/are Adaptive Cards?
Per the documentation at https://adaptivecards.io (a Microsoft website), Adaptive Cards 
are best described as follows:

  > Adaptive Cards are platform-agnostic snippets of UI, authored in JSON, 
  > that apps and services can openly exchange. When delivered to a specific 
  > app, the JSON is transformed into native UI that automatically adapts to 
  > its surroundings. It helps design and integrate light-weight UI for all 
  > major platforms and frameworks.

This is heavily useful in automated bot response applications, etc. including those 
built upon and working with Microsoft Teams and the Microsoft bot frameworks.

## Aren't there several Adaptive Cards frameworks already for Python?

Okay, you got us - this is Yet Another Implementation of Adaptive Cards (AC for short below).

However, the only Python libraries I could find for Adaptive Cards that were 'developer 
friendly' were either Cisco's outdated repository for Adaptive Cards support, or `adaptivecards` 
on PyPI which has not been updated since AC version 1.2.  This set of code functions - 
adaptivecardsng - is a Python Object-Oriented design of AC development and creation, and 
follows the spec at https://adaptivecards.io/explorer/ as closely as it can for the current release.

## Which Adaptive Cards spec version is this library written for?

As of right now while you're reading this document, this library is written to be AC 1.5 compliant.

It also includes a number of additional things that are not available in other versions, such as 
the specific schemas and Enums that are defined within the AC spec as actual Enums and object types 
here so that you can more easily choose options without having to remember all the strings. This 
also makes sure that you don't have any type of unrecognized arguments in the JSON when sending it 
off to endpoints.

## So, this is entirely Python, right?  No extra dependencies?

Yep, fully written in Python.  Of course, it's got a minimum support of Python 