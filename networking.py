import network
import urequests
import time

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        wlan.connect(ssid, password)
        timeout = 20
        while not wlan.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -= 1

    return wlan


def get_public_ip_info():
    r = urequests.get("http://ip-api.com/json/")
    data = r.json()
    r.close()

    if data.get("status") != "success":
        raise ValueError("IP API error")

    return data


def get_weather(lat, lon, api_key):
    url = (
        "https://api.openweathermap.org/data/2.5/weather?"
        "lat={}&lon={}&appid={}&units=metric"
    ).format(lat, lon, api_key)

    r = urequests.get(url)
    data = r.json()
    r.close()

    if data.get("cod") != 200:
        raise ValueError("Weather API error")

    return data