import ssl
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print(f"Connected: {str(rc)}")
    client.subscribe("topic/test")


def on_message(client, userdata, msg):
    print(f"{msg.topic} {str(msg.payload)}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(ca_certs="ca.crt",
               certfile="client.crt",
               keyfile="client.key",
               cert_reqs=ssl.CERT_REQUIRED,
               tls_version=ssl.PROTOCOL_TLSv1_2)

client.connect("localhost", 8883, 60)

client.loop_forever()
