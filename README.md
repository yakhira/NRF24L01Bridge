# Home Assistant Add-on: NRF24L01Bridge

This addon tested with Raspberry PI 3

## Installation

Follow these steps to get the add-on installed on your system:

1. Uncomment dtparam=spi=on in /mnt/boot/config.txt and reboot.
2. Navigate in your Home Assistant frontend to **Supervisor** -> **Add-on Store**.
3. Find the "MRF24L01 Bridge" add-on and click it.
4. Click on the "INSTALL" button.

## How to use

The add-on has a couple of options available. To get the add-on running:

1. Start the add-on.
2. Have some patience and wait a couple of minutes.
3. Check the add-on log output to see the result.


If you have old NRF24L01Bridge settings available, remove this old integration and restart Home Assistant to see the new one.

## Configuration

Add-on configuration:

```yaml
"CE": 25,
"CSN": 8,
"MQTT_READ_TOPIC": "nrf24/read",
"MQTT_WRITE_TOPIC": "nrf24/write",
"READ_PIPE": "0xe7e7e7e7e7", 
"WRITE_PIPE": "0xc2c2c2c2c2", 
"RADIO_CHANNEL": 118
```

MQTT_READ_TOPIC - topic to recieve message via NRF24

MQTT_WRITE_TOPIC - topic to send message via NRF24

RX address: 0xe7e7e7e7e7

TX address: 0xc2c2c2c2c2

RADIO_CHANNEL: 118 (0x76)

## Example MQTT message

```json
{
    "address": "0xc2c2c2c2c2",
    "message": "test"
}
```

## Connection

![](Rpi_nrf24l01.png)