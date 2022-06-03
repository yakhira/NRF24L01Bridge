import logging
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe


def mqtt_subscribe(host, user, password, topic):
    message = subscribe.simple(
        topic,
        hostname=host,
        auth={
            "username": user,
            "password": password
        }
    )
    logging.info(f"Receved message from MQTT: {message.payload.decode()}")
    return message.payload.decode()

def mqtt_publish(host, user, password, topic, message):
    logging.info(f"Publish message {message} to topic {topic}")
    publish.single(
        topic,
        message,
        hostname=host,
        auth={
            'username': user,
            'password': password
        }
    )
    logging.info(f"Sent message via MQTT: {message}")