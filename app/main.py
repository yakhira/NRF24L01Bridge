import json
import config
import time
import logging
import logging.config
import utils.mqtt as _mqtt
import utils.radio as _radio
import threading


logging.config.dictConfig(config.DEFAULT_LOGGING)

radio = _radio.radio_setup()

def radio_loop():
    while True: 
        while not radio.available(0):
            time.sleep(1/100)

        receivedMessage = []
        message = ""

        radio.read(receivedMessage, radio.getDynamicPayloadSize())

        if receivedMessage: 
            logging.info(receivedMessage)

        for n in receivedMessage:
            if(n>=32 and n<=126):
                message+=chr(n)
        
        if message:
            logging.info(
                f"Received message from address 0x{''.join('%02x'%pipe for pipe in config.READ_PIPE)} (NRF24): {message}."
            )

            _mqtt.mqtt_publish(
                config.MQTT_HOST,
                config.MQTT_USER,
                config.MQTT_PASS,
                config.MQTT_READ_TOPIC,
                message
            )
        
        time.sleep(1)

def mqtt_loop():
    while True:
        message = _mqtt.mqtt_subscribe(
            config.MQTT_HOST,
            config.MQTT_USER,
            config.MQTT_PASS,
            config.MQTT_WRITE_TOPIC
        )

        try:
            address = config.WRITE_PIPE

            json_message = json.loads(message)

            if type(json_message) == dict:
                if 'address' in json_message:
                    address = [
                        ord(bytes.fromhex(json_message['address'][i:i+2]))
                        for i in range(2, len(json_message['address']), 2)
                    ]
                    radio.openWritingPipe(address)
                if 'message' in json_message:
                    message = json_message['message']
        except json.JSONDecodeError:
            pass

        radio.stopListening()
        radio.write(message)
        logging.info(
            f"Sent message to 0x{''.join('%02x'%pipe for pipe in address)} (NRF24): {message}."
        )
        radio.startListening()

t_mqtt_loop = threading.Thread(target=mqtt_loop)
t_mqtt_loop.start()

radio_loop()