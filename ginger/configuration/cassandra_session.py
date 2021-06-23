from cassandra.cluster import Cluster, PlainTextAuthProvider

# credential=PlainTextAuthProvider(username='cassandra-cluster', password='cassandra')
#
# cluster: Cluster = Cluster(ips, protocol_version=2, auth_provider=credential)
cluster: Cluster = Cluster(['0.0.0.0'], port=9042)
session = cluster.connect()