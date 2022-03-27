import pulsar
# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://192.168.2.232:6650')
# Subscribe to a topic and subscription
consumer = client.subscribe('C1-Topic', subscription_name='C1-sub')
# Display message received from producer
msg = consumer.receive()
decoded_msg=msg.data().decode()
#decoded_msg=("number_of_words",number_of_words)
index=int(decoded_msg)
try:
    while index>0:
        msg=consumer.receive()
        index=index-1;
        print('%s' % msg.data().decode().upper())
        # Acknowledge for receiving the message
        consumer.acknowledge(msg)
except:
    consumer.negative_acknowledge(msg)
# Destroy pulsar client
client.close()