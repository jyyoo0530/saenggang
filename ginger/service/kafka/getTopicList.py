from confluent_kafka.admin import AdminClient
from ginger.configuration import kafka_configuration

kafcon = kafka_configuration

conf = {'bootstrap.servers': kafcon.bootstrapServers}
admin = AdminClient(conf)

topicList = admin.list_topics().topics
print(topicList)
