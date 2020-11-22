# kafka-tutorial

A full tutorial for deploying a Kafka cluster with Python producers and consumers.

https://medium.com/better-programming/a-simple-apache-kafka-cluster-with-docker-kafdrop-and-python-cf45ab99e2b9


# docker-compose
## dicas de docker-compose para não esquecer

Executar o docker-compose utilizando no de arquivo diferente de docker-compose.yml
Use o "-d" para executar as saidas de console em background


```
docker-compose -f arquivo.yml up -d
```
## discas de python

comando pip:

```
pip freeze
pip install -r requeriments.txt
pip freeze > requeriments.txt
```

Programa gerador de nomes (BR) em python para ajudar a criar transações fakes

```
pip install fordev

python
>>> from fordev.generator import people
>>> p = people(sex='M', age=25, state='SP')
>>> print(p)
```

## problemas com powershell

Powershell impedindo de abrir o virtual venv do python. executei o comando abaixo para resolver.

```
Set-ExecutionPolicy RemoteSigned

```
O vscode executou internamente o comando: 


```
 & e:/Arquivos/devops/kafka/tutorial/EntendendoKafka/venv/Scripts/Activate.ps1
```

## onde eu parei:

1. entendi que posso testar se o producer teve sucesso no envio de uma msg para o broker
2. o producer.flush só deve ser feito qual a aplicação é encerrada
3. O consumer, mesmo que desligado, consegue tratar as mensagem de onde parou.
4. parei os conatiners com docker-compose down

## Problemas para resolver:

1. Preciso resolver a situação de decode da mensagem. O Kafka está ignorando o parametro utf-8 criado do producer. a msg também poder ser verificada no kafdrop

Exemplo:
```
{"msg": "Ol\u00e1 pessoas, agora sem flush e com o consumer desligado!!!", "horario": "2020-11-22 15:21:28", "total": 6}
```

## dicas GIT

Não esquecer de rodar, para novos diretórios, os comandos:

```
git config --global user.email "msilva1610@gmail.com"
git config --global user.name "msilva1610"
```