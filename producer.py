import string
import pulsar
# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://192.168.2.232:6650')
# Create a producer on the topic that consumer can subscribe to
producer = client.create_producer('C1-Topic')
#do split operation by space
splitted_sentence='Welcome to Data Engineering Course!'.split(" ")
number_of_words=len(splitted_sentence)
# Send each word to topic
producer.send(str(number_of_words).encode('utf-8'))
print("sending to broker....")
for word in splitted_sentence:
    print(word)
    producer.send((word).encode('utf-8'))
print("completed....")
# Destroy pulsar client
client.close()
