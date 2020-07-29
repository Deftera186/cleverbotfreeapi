![cleverbotfreeapi](https://www.cleverbot.com/images/cleverbot254x114.jpg)

# cleverbotfreeapi
Simple unofficial package to interact with the same API that the Cleverbot website uses for free.
This package is based on the package that was written in node.js: https://www.npmjs.com/package/cleverbot-free
## Installation
```pip
pip install cleverbotfreeapi
```
## Usage
```python
import cleverbotfreeapi

# Without context
cleverbotfreeapi.cleverbot("Hello")

# With context
# Please note that context should include messages sent to Cleverbot as well as the responses
cleverbotfreeapi.cleverbot("Bad", ["hi.", "How are you?"])
```