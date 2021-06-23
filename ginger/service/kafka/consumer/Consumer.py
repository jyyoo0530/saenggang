import sys

from confluent_kafka import Consumer, KafkaException, KafkaError

running =True
def get_message():
    consumer = Consumer({
        'bootstrap.servers': 'ginger9.io:9092',
        'group.id': 'test',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe(["test"])

    while running:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        else:
            print(msg.value())
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
            elif msg.error():
                raise KafkaException(msg.error())
    # consumer.close()

get_message()