import json
import os
import time

import requests


HUE_USERNAME = os.environ.get("HUE_USERNAME")
HUE_URL = os.environ.get("HUE_URL")
URL = f"{HUE_URL}/api/{HUE_USERNAME}"


def update_light(light, hue, bri, sat):
    return requests.put(f"{URL}/lights/{light}/state", data=json.dumps({
        "hue": hue,
        "on": True,
        "bri": bri,
        "sat": sat,
    }))


def party1(light_ids):
    hue = 0
    while True:
        yield [(i, hue, 254, 254) for i in light_ids]
        hue += 5000
        hue %= 65000


def main():
    res = requests.get(f"{URL}/lights")
    light_ids = res.json().keys()

    for updates in party1(light_ids):
        for update in updates:
            update_light(*update)
        time.sleep(0.2)


if __name__ == "__main__":
    main()
