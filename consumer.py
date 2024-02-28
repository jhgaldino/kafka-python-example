from confluent_kafka import Consumer, KafkaException

def create_consumer():
    conf = {'bootstrap.servers': 'localhost:9092', 'group.id': 'mygroup', 'auto.offset.reset': 'earliest'}
    consumer = Consumer(conf)

    try:
        consumer.subscribe(['logs'])

        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            else:
                print('Received message: {}'.format(msg.value().decode('utf-8')))

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    create_consumer()