#!/usr/bin/env bashio
set +u

CONFIG_PATH=/data/options.json

export CN_PIN=$(jq --raw-output ".cn_pin" $CONFIG_PATH)
export CSN_PIN=$(jq --raw-output ".csn_pin" $CONFIG_PATH)

export MQTT_READ_TOPIC=$(jq --raw-output ".mqtt_read_topic" $CONFIG_PATH)
export MQTT_WRITE_TOPIC=$(jq --raw-output ".mqtt_write_topic" $CONFIG_PATH)
export MQTT_HOST=$(bashio::services mqtt "host")
export MQTT_USER=$(bashio::services mqtt "username")
export MQTT_PASSWORD=$(bashio::services mqtt "password")

export READ_PIPE=$(jq --raw-output ".read_pipe" $CONFIG_PATH)
export WRITE_PIPE=$(jq --raw-output ".write_pipe" $CONFIG_PATH)
export RADIO_CHANNEL=$(jq --raw-output ".radio_channel" $CONFIG_PATH)

exec /usr/bin/python3 $APPDIR/main.py