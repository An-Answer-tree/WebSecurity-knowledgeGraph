from neo4j import GraphDatabase
import json
from function import *

uri = "neo4j://127.0.0.1:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "12345678"))

# import event name(aka title)
title_list = []
json_list = json.load('./data_after_ner_ssid.json')
print(json_list[0])

# 在Neo4j数据库中创建节点
# with driver.session() as session:
#     session.write_transaction(create_event_nodes, title_list)

driver.close()  # close the driver object