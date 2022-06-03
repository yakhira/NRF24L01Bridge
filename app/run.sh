#!/usr/bin/env bashio
set +u

CONFIG_PATH=/data/options.json

export MISO_PIN=$(jq --raw-output ".mosi_pin" $CONFIG_PATH)
export MOSI_PIN=$(jq --raw-output ".miso_pin" $CONFIG_PATH)
export SCLK_PIN=$(jq --raw-output ".sclk_pin" $CONFIG_PATH)
export CN_PIN=$(jq --raw-output ".cn_pin" $CONFIG_PATH)
export CSN_PIN=$(jq --raw-output ".csn_pin" $CONFIG_PATH)
export MQTT_TOPIC=$(jq --raw-output ".mqtt_topic" $CONFIG_PATH)
export MQTT_HOST=$(bashio::services mqtt "host")
export MQTT_USER=$(bashio::services mqtt "username")
export MQTT_PASSWORD=$(bashio::services mqtt "password")

exec /usr/bin/python3 $APPDIR/main.py