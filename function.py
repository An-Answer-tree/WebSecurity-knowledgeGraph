import pandas as pd

def create_event_nodes(tx, event_names, features):
    for index, name in enumerate(event_names):
        tx.run("""
               CREATE (:Event {title: $title, sid: $sid, attacker: $attacker, victim: $victim, purpose: $purpose, extent_of_damage: $extent_of_damage, tools: $tools, time: $time, place: $place, number_of_victims: $number_of_victims, compromised_data: $compromised_data, number_of_data: $number_of_data, topic: $topic});
               
               """,
               title = name,
               sid = index,
               attacker = features.iloc[index]['attacker'],
               victim = features.iloc[index]['victim'],
               purpose = features.iloc[index]['purpose'],
               extent_of_damage = features.iloc[index]['extent_of_damage'],
               tools = features.iloc[index]['tools'],
               time = features.iloc[index]['time'],
               place = features.iloc[index]['place'],
               number_of_victims = features.iloc[index]['number_of_victims'],
               compromised_data = features.iloc[index]['compromised_data'],
               number_of_data = features.iloc[index]['number_of_data'],
               topic = features.iloc[index]['topic']
        )
        

def clear_all_nodes(tx):
    tx.run("MATCH (n) DETACH DELETE n")

def connect_related_nodes(tx, matrix_size, matrix):
    for i in range(matrix_size):
        for j in range(i + 1, matrix_size):  # 只处理上三角部分
            if matrix[i][j] == 1:  # 如果节点i和节点j相关
                tx.run(
                    """
                    MATCH (a:Event {sid: $sid_a}), (b:Event {sid: $sid_b})
                    MERGE (a)<-[r:RELATED]->(b)
                    SET r.label = 'RELATED'
                    """,
                    sid_a=i,
                    sid_b=j,
                )