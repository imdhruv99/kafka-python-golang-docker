from confluent_kafka import Producer
import log_generator
import time

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def produce_logs(producer, topic):
    log = log_generator.generate_log()
    producer.produce(topic, key="key", value=log, callback=delivery_report)
    producer.poll(1)
    time.sleep(1)

if __name__ == "__main__":
    producer = Producer({
        'bootstrap.servers': 'localhost:9091,localhost:9092,localhost:9093',
        'security.protocol': 'PLAINTEXT'
    })
    while True:
        produce_logs(producer, 'logs')