# Home Assistant Add-on: NRF24L01Bridge

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
"MOSI": 10,
"MISO": 9,
"SCLK": 11,
"CE": 25,
"CSN": 8
```

## Support

Got questions?

In case you've found a bug, please [open an issue on our GitHub][issue].
[issue] https://github.com/yakhira/NRF24L01Bridge