import libs.nrf24 as nrf24
import RPi.GPIO as GPIO
import spidev
import time
import config

def radio_setup():
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    radio = nrf24.NRF24(GPIO, spidev.SpiDev())
    radio.begin(0, config.CE_PIN)
    time.sleep(3)

    radio.setRetries(15, 15)
    radio.setChannel(config.RADIO_CHANNEL)
    radio.setDataRate(nrf24.NRF24.BR_1MBPS)
    radio.setPALevel(nrf24.NRF24.PA_MIN)
    radio.setPayloadSize(8)
    radio.openReadingPipe(1, config.READ_PIPE)
    radio.openWritingPipe(config.WRITE_PIPE)
    radio.startListening()
    radio.printDetails()
    return radio