from cassandra.cluster import Cluster

cluster: Cluster = Cluster(['0.0.0.0'], port=9042)
session = cluster.connect('ginger9', wait_for_all_pools=True)
session.set_keyspace('ginger9')
