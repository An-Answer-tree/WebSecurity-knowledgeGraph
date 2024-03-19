def create_event_nodes(tx, event_names):
    for name in event_names:
        tx.run("CREATE (:Event {name: $name})", name=name)

def clear_all_nodes(tx):
    tx.run("MATCH (n) DETACH DELETE n")

def connect_related_nodes(tx, matrix_size, matrix):
    for i in range(matrix_size):
        for j in range(i + 1, matrix_size):  # 只处理上三角部分
            if matrix[i][j] == 1:  # 如果节点i和节点j相关
                tx.run(
                    """
                    MATCH (a:Event {identity: $identity_a}), (b:Event {identity: $identity_b})
                    MERGE (a)-[r:RELATED]-(b)
                    SET r.label = '相关'
                    """,
                    identity_a=i,
                    identity_b=j,
                )