import pandas as pd
import math

def create_event_nodes(tx, event_names, features):
    for index, name in enumerate(event_names):
        attacker = features[index][0]
        victim = features[index][1]
        purpose = features[index][2]
        extent_of_damage = features[index][3]
        tools = features[index][4]
        time = features[index][5]
        place = features[index][6]
        number_of_victims = features[index][7]
        compromised_data = features[index][8]
        number_of_data = features[index][9]
        topic = features[index][11]

        # 检查属性是否不为空，如果不为空则创建节点和关系
        if attacker:
            tx.run("CREATE (:Attacker {attacker: $attacker, fid: $fid})", attacker=attacker, fid=index)
        if victim:
            tx.run("CREATE (:Victim {victim: $victim, fid: $fid})", victim=victim, fid=index)
        if purpose:
            tx.run("CREATE (:Purpose {purpose: $purpose, fid: $fid})", purpose=purpose, fid=index)
        if extent_of_damage:
            tx.run("CREATE (:Extent_of_damage {extent_of_damage: $extent_of_damage, fid: $fid})", extent_of_damage=extent_of_damage, fid=index)
        if tools:
            tx.run("CREATE (:Tools {tools: $tools, fid: $fid})", tools=tools, fid=index)
        if time:
            tx.run("CREATE (:Time {time: $time, fid: $fid})", time=time, fid=index)
        if place:
            tx.run("CREATE (:Place {place: $place, fid: $fid})", place=place, fid=index)
        if number_of_victims:
            tx.run("CREATE (:Number_of_victims {number_of_victims: $number_of_victims, fid: $fid})", number_of_victims=number_of_victims, fid=index)
        if compromised_data:
            tx.run("CREATE (:Compromised_data {compromised_data: $compromised_data, fid: $fid})", compromised_data=compromised_data, fid=index)
        if number_of_data:
            tx.run("CREATE (:Number_of_data {number_of_data: $number_of_data, fid: $fid})", number_of_data=number_of_data, fid=index)
        if topic:
            tx.run("CREATE (:Topic {topic: $topic, fid: $fid})", topic=topic, fid=index)
        
        # 创建事件节点
        tx.run("CREATE (:Event {title: $title, sid: $sid})", title=name, sid=index)

        # 建立事件节点与其他节点之间的关系
        if attacker:
            tx.run("MATCH (a:Event {sid: $sid}), (b:Attacker {fid: $fid}) MERGE (a)-[:HAS_ATTACKER]->(b)", sid=index, fid=index)
        if victim:
            tx.run("MATCH (a:Event {sid: $sid}), (b:Victim {fid: $fid}) MERGE (a)-[:HAS_VICTIM]->(b)", sid=index, fid=index)
        if purpose:
            tx.run("MATCH (a:Event {sid: $sid}), (b:Purpose {fid: $fid}) MERGE (a)-[:HAS_PURPOSE]->(b)", sid=index, fid=index)
        if extent_of_damage:
            tx.run("MATCH (a:Event {sid: $sid}), (b:Extent_of_damage {fid: $fid}) MERGE (a)-[:HAS_EXTENT_OF_DAMAGE]->(b)", sid=index, fid=index)
        if tools:
            tx.run("MATCH (a:Event {sid: $sid}), (b:Tools {fid: $fid}) MERGE (a)-[:USES_TOOLS]->(b)", sid=index, fid=index)
        if time:
            tx.run("MATCH (a:Event {sid: $sid}), (b:Time {fid: $fid}) MERGE (a)-[:OCCURS_AT_TIME]->(b)", sid=index, fid=index)
        if place:
            tx.run("MATCH (a:Event {sid: $sid}), (b:Place {fid: $fid}) MERGE (a)-[:OCCURS_AT_PLACE]->(b)", sid=index, fid=index)
        if number_of_victims:
            tx.run("MATCH (a:Event {sid: $sid}), (b:Number_of_victims {fid: $fid}) MERGE (a)-[:HAS_NUMBER_OF_VICTIMS]->(b)", sid=index, fid=index)
        if compromised_data:
            tx.run("MATCH (a:Event {sid: $sid}), (b:Compromised_data {fid: $fid}) MERGE (a)-[:HAS_COMPROMISED_DATA]->(b)", sid=index, fid=index)
        if number_of_data:
            tx.run("MATCH (a:Event {sid: $sid}), (b:Number_of_data {fid: $fid}) MERGE (a)-[:HAS_NUMBER_OF_DATA]->(b)", sid=index, fid=index)
        if topic:
            tx.run("MATCH (a:Event {sid: $sid}), (b:Topic {fid: $fid}) MERGE (a)-[:RELATES_TO_TOPIC]->(b)", sid=index, fid=index)

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