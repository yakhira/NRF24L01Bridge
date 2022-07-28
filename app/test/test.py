import json
import config
import time
import logging
import logging.config
import utils.radio as _radio


logging.config.dictConfig(config.DEFAULT_LOGGING)

radio = _radio.radio_setup()

# def radio_loop():
#     while True: 
#         while not radio.available(0):
#             time.sleep(1/100)

#         receivedMessage = []
#         message = ""

#         radio.read(receivedMessage, radio.getDynamicPayloadSize())

#         if receivedMessage: 
#             logging.info(receivedMessage)

#         for n in receivedMessage:
#             if(n>=32 and n<=126):
#                 message+=chr(n)
        
#         if message:
#             logging.info(
#                 f"Received message from address 0x{''.join('%02x'%pipe for pipe in config.READ_PIPE)} (NRF24): {message}."
#             )        
#         time.sleep(1)

# radio_loop()

while True:
    radio.write("TEST MESSAGE")
    time.sleep(1)