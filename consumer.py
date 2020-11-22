from kafka import KafkaConsumer
topicname = 'my-topic-msg05'
brokers = ['localhost:9091','localhost:9092','localhost:9093']
# consumer = KafkaConsumer(topicname, bootstrap_servers=['localhost:9091','localhost:9092','localhost:9093'])
consumer = KafkaConsumer(topicname, group_id = 'group1', bootstrap_servers = brokers)
# consumer = KafkaConsumer(topicname, bootstrap_servers = brokers)

for message in consumer:
    print (message.value)
