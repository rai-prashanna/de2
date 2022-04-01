import pulsar
# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://192.168.2.232:6650')
# Subscribe to a topic and subscription
consumer = client.subscribe('C1-Topic', subscription_name='C1-sub')
# Display message received from producer
msg = consumer.receive()
decoded_msg=msg.data().decode()
consumer.acknowledge(msg)
#decoded_msg=("number_of_words",number_of_words)
index=int(decoded_msg)
messages_list=[]
while index>0:
    msg=consumer.receive()
    index=index-1;
    messages_list.append(msg.data().decode().upper())
    consumer.acknowledge(msg)

print('%s' % " ".join(messages_list))
# Destroy pulsar client
client.close()