import requests
import hashlib
import re

cookies = None


def cleverbot(stimulus, context=[]):
    global cookies
    _context = context[:]
    if (cookies is None):
        req = requests.get("https://www.cleverbot.com/")
        cookies = {
            'XVIS': re.search(
                r"\w+(?=;)",
                req.headers["Set-cookie"]).group()}
    payload = f"stimulus={requests.utils.requote_uri(stimulus + '.')}&"

    reverseContext = list(reversed(_context))

    for i in range(len(_context)):
        payload += f"vText{i + 2}={requests.utils.requote_uri(reverseContext[i])}&"

    payload += "cb_settings_scripting=no&islearning=1&icognoid=wsf&icognocheck="

    payload += hashlib.md5(payload[7:33].encode()).hexdigest()

    req = requests.post(
        "https://www.cleverbot.com/webservicemin?uc=UseOfficialCleverbotAPI",
        cookies=cookies,
        data=payload)
    return requests.utils.unquote(req.headers["CBOUTPUT"])


if __name__ == "__main__":
    context = []
    while True:
        message = input(">> ")
        response = cleverbot(message, context)
        context.append(message + ".")
        context.append(response)
        print(response)
