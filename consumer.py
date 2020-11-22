from kafka import KafkaConsumer
topicname = 'my-topic-msg02-sem-flush'
brokers = ['localhost:9091','localhost:9092','localhost:9093']
# consumer = KafkaConsumer(topicname, bootstrap_servers=['localhost:9091','localhost:9092','localhost:9093'])
consumer = KafkaConsumer(topicname, group_id = 'group1', bootstrap_servers = brokers)
# consumer = KafkaConsumer(topicname, group_id = 'group1', bootstrap_servers = brokers, auto_offset_reset = 'earliest')
# consumer = KafkaConsumer(topicname, bootstrap_servers = brokers)

for message in consumer:
    # print (type(message.value))
    print (message.value.decode("utf-8"))
