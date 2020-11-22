from kafka import KafkaProducer
import random
import json
from json import dumps
from datetime import datetime



bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
# topicName = 'my-topic-three'
topicName = 'my-topic-msg05'

# producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

# configuração do kafka
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

# producer.send(topicName, b'Hello World!')
# Call the producer.send method with a producer-record
print("Ctrl+c to Stop")
total = 0
while True:
    total += 1
    # print(random.randint(1,999))
    print(total)
    # producer.send('topicName', str(random.randint(1,999)).encode())
    data_e_hora_completa = datetime.now()
    data_string = data_e_hora_completa.strftime('%Y-%m-%d %H:%M:%S')
    msg = 'hello world com flush e group'
    dados = {"msg": msg, "horario": data_string, "total": total}
    # producer.send(topicName, b'Hello World!')
    print(dados)
    producer.send(topicName, value=dados)
    if total == 1000:
        producer.flush()
        break
