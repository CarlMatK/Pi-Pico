import network
from time import sleep
ssid = "TP-Link_7228"
password = "91340863"
import json

def Telemetry():    
    sta_if = network.WLAN(network.STA_IF)
    print(sta_if.active())

    ap_if = network.WLAN(network.AP_IF)
    print(ap_if.active())

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    networks = wlan.scan()
    # Print Wi-Fi networks
    print("Available WiFi Networks:")
    for network_info in networks:
        print(network_info)
    
    
def conn_to(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    print("Connecting to... ",ssid)
    wlan.connect(ssid, password)
    conn_timeout = 30
    while conn_timeout > 0:
        if wlan.status() >= 3:
            break
        conn_timeout -= 1
        print('Waiting for Wi-Fi connection...')
        sleep(1)
        # Check if connection is successful
    if wlan.status() != 3:
        raise RuntimeError('Failed to establish a network connection')
    else:
        print('Connection successful!')
        network_info = wlan.ifconfig()
        print('IP address:', network_info[0])
        
   

#http://ip:3000/ metodo get -> texto
#http://ip:3000/atmos/send/readings metodo post
#enviar json
        
    
def upload_data():
     # 1. Crea un diccionario de Python (corresponde a un objeto JSON)
    datos_sensor = {
        "timestamp": "2024-06-01  20:30:00", #!Not Null
        "battery_level": 1000,  #!Not Null
        "wind_speed_kmh": 33.5,
        "wind_direction_deg": 90,
        "rainfall": 1.0,
        "uv_index": 8.0,
        "temperature_c": 30.0,
        "humidity": 80,
        
    }

    # 2. Serializa el diccionario a un string JSON
    objeto_json = json.dumps(datos_sensor)

    print(objeto_json)