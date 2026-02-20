from utils import load_config
from networking import connect_wifi, get_public_ip_info, get_weather
from display import init_display, show_message, show_coords, show_weather
import time

REFRESH = 600  # 10 minut

def main():
    # LCD
    init_display()

    # Config
    config = load_config()

    # WiFi
    show_message("Connecting...")
    wlan = connect_wifi(config["wifi_ssid"], config["wifi_password"])

    if not wlan.isconnected():
        show_message("WiFi failed")
        time.sleep(3)
    else:
        show_message("Connected")
        time.sleep(1)

    # IP geolokace
    try:
        ip = get_public_ip_info()
        lat = ip["lat"]
        lon = ip["lon"]
        show_coords(lat, lon)
        time.sleep(3)
    except:
        show_message("IP error")
        lat = 50.087
        lon = 14.421
        time.sleep(2)

    # Hlavní smyčka
    while True:
        try:
            if not wlan.isconnected():
                show_message("Reconnecting")
                wlan = connect_wifi(config["wifi_ssid"], config["wifi_password"])

            weather = get_weather(lat, lon, config["owm_api_key"])
            show_weather(weather)

        except Exception as e:
            show_message("API error")
            print("Chyba:", e)

        time.sleep(REFRESH)


main()