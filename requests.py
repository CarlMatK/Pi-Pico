import network

ssid = "red"
password = "pswd"

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
    
    
def conn_to():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    print("Connecting to... ",ssid)
    wlan.connect(ssid, password)
    conn_timeout = 10
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

def upload_data():
    print("Implement function")
    