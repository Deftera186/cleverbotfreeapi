![cleverbotfreeapi](https://www.cleverbot.com/images/cleverbot254x114.jpg)

# cleverbotfreeapi
Simple unofficial package to interact with the same API that the Cleverbot website uses for free.

![Downloads](https://pepy.tech/badge/cleverbotfreeapi) ![PyPI](https://img.shields.io/pypi/v/cleverbotfreeapi) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cleverbotfreeapi) ![PyPI - License](https://img.shields.io/pypi/l/cleverbotfreeapi)
## Installation
```pip
pip install cleverbotfreeapi
```
## Usage
```python
import cleverbotfreeapi

# Without context or session
cleverbotfreeapi.cleverbot("Hello.")

# With context, without session
# Please note that context should include messages sent to Cleverbot as well as the responses
cleverbotfreeapi.cleverbot("Bad.", ["hi.", "How are you?"])

# Without context, with session
cleverbotfreeapi.cleverbot("Hi.", session="Deftera")
cleverbotfreeapi.cleverbot("Fine :)", session="Deftera")

# With context and session
# An ongoing conversation with the first question as "How are you?"
cleverbotfreeapi.cleverbot(input(">>"), ["hi.", "How are you?"], "How are you?")
while True:
  print(cleverbotfreeapi.cleverbot(input(">>"), session="How are you?"))
```
