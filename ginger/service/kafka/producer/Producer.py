from confluent_kafka import Producer
import socket


def send_message():
    def acked(err, msg):
        if err is not None:
            print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            print("Message produced: %s" % (str(msg)))

    conf = {
        'bootstrap.servers': "ginger9.io:9092",
        # 'auto.offset.reset': 'smallest',
        # 'security.protocol': 'PLAINTEXT',
        # 'sasl.mechanism': 'PLAIN',
        # 'sasl.username' : '',
        # 'sasl.password' : '',
        'client.id': socket.gethostname()
    }
    producer = Producer(conf)
    producer.produce(topic="test", key="key", value="ttttteeeeesssssttttt")
    producer.flush()


send_message()
