import config
import time
import logging
import logging.config
import utils.mqtt as _mqtt
import utils.radio as _radio
import threading

logging.basicConfig(level=logging.INFO)

radio = _radio.start_listening(config.CE_PIN)

def radio_loop():
    while True: 
        while not radio.available(0):
            time.sleep(1/100)

        receivedMessage = []
        message = ""

        radio.read(receivedMessage, radio.getDynamicPayloadSize())

        for n in receivedMessage:
            if(n>=32 and n<=126):
                message+=chr(n)
        
        if message:
            logging.info(f"Receved message via NRF24: {message}")

            if config.MQTT_ENABLE:
                _mqtt.mqtt_publish(
                    config.MQTT_HOST,
                    config.MQTT_USER,
                    config.MQTT_PASS,
                    config.MQTT_TOPIC,
                    message
                )
        
        time.sleep(1)

def mqtt_loop():
    while True: 
        message = _mqtt.mqtt_subscribe(
            config.MQTT_HOST,
            config.MQTT_USER,
            config.MQTT_PASS,
            config.MQTT_TOPIC
        )
        radio = _radio.send_message(message, config.CE_PIN)

radio_listening = threading.Thread(target=mqtt_loop)
radio_listening.start()

radio_loop()
