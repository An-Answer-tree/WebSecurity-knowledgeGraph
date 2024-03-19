def create_event_nodes(tx, event_names):
    for index, name in enumerate(event_names):
        tx.run("CREATE (:Event {name: $name, ssid: $ssid})", name=name, ssid = index)

def clear_all_nodes(tx):
    tx.run("MATCH (n) DETACH DELETE n")

def connect_related_nodes(tx, matrix_size, matrix):
    for i in range(matrix_size):
        for j in range(i + 1, matrix_size):  # 只处理上三角部分
            if matrix[i][j] == 1:  # 如果节点i和节点j相关
                tx.run(
                     """
                    MATCH (a:Event {ssid: $ssid_a}), (b:Event {ssid: $ssid_b})
                    MERGE (a)-[r:RELATED]-(b)
                    SET r.label = 'RELATED'
                    """,
                    ssid_a=i,
                    ssid_b=j,
                )