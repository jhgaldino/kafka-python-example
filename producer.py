from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

p.produce('logs', 'Hello World!', callback=delivery_report)

# Wait for any outstanding messages to be delivered and reports to be received
p.flush()