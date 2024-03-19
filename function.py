def create_event_nodes(tx, event_names):
    for name in event_names:
        tx.run("CREATE (:Event {name: $name})", name=name)

