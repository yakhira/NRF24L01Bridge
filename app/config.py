import os

SUPERVISOR_TOKEN = os.getenv('SUPERVISOR_TOKEN')
HASSIO_TOKEN = os.getenv('HASSIO_TOKEN')
SUPERVISOR_API = 'http://supervisor/core/api'

CE_PIN = int(os.getenv('CE_PIN', 25))
CSN_PIN = int(os.getenv('CSN_PIN', 8))

MQTT_READ_TOPIC = os.getenv('MQTT_READ_TOPIC')
MQTT_WRITE_TOPIC = os.getenv('MQTT_WRITE_TOPIC')
MQTT_HOST = os.getenv('MQTT_HOST')
MQTT_USER = os.getenv('MQTT_USER')
MQTT_PASS = os.getenv('MQTT_PASSWORD')

READ_PIPE = os.getenv('READ_PIPE', '0xe7e7e7e7e7').replace('0x', '')
WRITE_PIPE = os.getenv('WRITE_PIPE', '0xc2c2c2c2c2').replace('0x', '')
RADIO_CHANNEL = ord(
    bytes.fromhex(
        os.getenv(
            'RADIO_CHANNEL',
            '0x76'
        ).replace('0x', '')
    )
)

READ_PIPE = [
    ord(bytes.fromhex(READ_PIPE[i:i+2]))
    for i in range(0, len(READ_PIPE), 2)
]

WRITE_PIPE = [
    ord(bytes.fromhex(WRITE_PIPE[i:i+2]))
    for i in range(0, len(WRITE_PIPE), 2)
]

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(module)s: [%(levelname)s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }
}
