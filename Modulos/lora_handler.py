
# Lora Consts, Callback, Init Object
   #*  PI PICO W PINOUT 
   #?  0   6  7  4  PINOUT GPIO
   #* CSN SCK TX RX  PINOUT PROTOCOL	

#Los numeros aqui representan gpiX (no pines reales)
# RFM95_CS = 0
# lora_cs_pin = Pin(RFM95_CS, Pin.OUT, value=1)
# 
# RFM95_RST = 28 
# RFM95_INT = 27 #(PIN DE INTERRUPCION)
# 
# RFM95_SPIBUS = SPIConfig.rp2_0 # (NSS SCK MOSI MISO)
# RF95_FREQ = 915.0
# RF95_POW = 10 # 5 A 23 (RECOMENDADO MIENTRAS MAS BAJO MEJOR)
# CLIENT_ADDRESS = 1
# SERVER_ADDRESS = 2
#  
# def on_get(payload):
#     print("From:", payload.header_from)
#     print("Received:", payload.message)
#     print("RSSI: {}; SNR: {}".format(payload.rssi, payload.snr))
# #
# lora = LoRa(RFM95_SPIBUS,
#             RFM95_INT,
#             SERVER_ADDRESS,
#             RFM95_CS,
#             reset_pin=RFM95_RST,
#             freq=RF95_FREQ,
#             tx_power=RF95_POW,
#             acks=True)
#  
# lora.on_recv = on_get
# lora.set_mode_rx()

