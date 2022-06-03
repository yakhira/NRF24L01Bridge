import os

SUPERVISOR_TOKEN = os.getenv('SUPERVISOR_TOKEN')
HASSIO_TOKEN = os.getenv('HASSIO_TOKEN')
SUPERVISOR_API = 'http://supervisor/core/api'

MISO_PIN = int(os.getenv('MISO_PIN', 9))
MOSI_PIN = int(os.getenv('MOSI_PIN', 10))
SCLK_PIN = int(os.getenv('SCLK_PIN', 11))
CE_PIN = int(os.getenv('CE_PIN', 25))
CSN_PIN = int(os.getenv('CSN_PIN', 8))

MQTT_TOPIC = os.getenv('MQTT_TOPIC')
MQTT_HOST = os.getenv('MQTT_HOST')
MQTT_USER = os.getenv('MQTT_USER')
MQTT_PASS = os.getenv('MQTT_PASSWORD')

MQTT_ENABLE = True if MQTT_TOPIC and MQTT_HOST and MQTT_USER and MQTT_PASS else False
