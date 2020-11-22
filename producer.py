from kafka import KafkaProducer
import random
import json
from json import dumps
from datetime import datetime



bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
# topicName = 'my-topic-three'
topicName = 'my-topic-msg02-sem-flush'

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
    # print(total)
    # producer.send('topicName', str(random.randint(1,999)).encode())
    data_e_hora_completa = datetime.now()
    data_string = data_e_hora_completa.strftime('%Y-%m-%d %H:%M:%S')
    msg = 'Olá pessoas, agora sem flush e com o consumer desligado!!!'
    dados = {"msg": str(msg), "horario": data_string, "total": total}
    # producer.send(topicName, b'Hello World!')
    print(dados)
    p = producer.send(topicName, value=dados)
    # print(dir(p))
    print(p.error_on_callbacks)
    if p.error_on_callbacks == 'FALSE':
        print('error')
        break
    if total == 10:
        break
# O flush deve ser chamado somente ao finalizar a aplicação
producer.flush()
