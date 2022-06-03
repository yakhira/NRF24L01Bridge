import logging
import libs.nrf24 as nrf24
import RPi.GPIO as GPIO
import spidev

def start_listening(ce_pin):
    logging.info("Start listening NRF24 network")

    GPIO.setmode(GPIO.BCM)
    pipes = [[0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]
    radio = nrf24.NRF24(GPIO, spidev.SpiDev())
    radio.begin(0, ce_pin)
    radio.setPayloadSize(32)
    radio.setChannel(0x76)
    radio.setDataRate(nrf24.NRF24.BR_1MBPS)
    radio.setPALevel(nrf24.NRF24.PA_MIN)
    radio.setAutoAck(True)
    radio.enableDynamicPayloads()
    radio.enableAckPayload()
    radio.openReadingPipe(1, pipes[0])
    radio.printDetails()
    radio.startListening()
    GPIO.cleanup()
    return radio

def send_message(message, ce_pin):
    logging.info("Stop listening NRF24 network")
    GPIO.setmode(GPIO.BCM)
    pipes = [[0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]
    radio = nrf24.NRF24(GPIO, spidev.SpiDev())
    radio.begin(0, ce_pin)
    radio.setPayloadSize(32)
    radio.setChannel(0x76)
    radio.setDataRate(nrf24.NRF24.BR_1MBPS)
    radio.setPALevel(nrf24.NRF24.PA_MIN)
    radio.setAutoAck(True)
    radio.enableDynamicPayloads()
    radio.enableAckPayload()
    radio.openReadingPipe(1, pipes[0])
    radio.printDetails()
    radio.stopListening()
    radio.write(message)
    GPIO.cleanup()

    logging.info(f"Sent message via NRF24: {message}")
    return start_listening(ce_pin)