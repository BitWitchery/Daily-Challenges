def medici_family(relation_name, relation_role):
    # Define a dictionary mapping names to their roles
    medici_roles = {
        "Giovanni di Bicci de' Medici": "founder",
        "Lorenzo de' Medici": "patron",
        "Cosimo de' Medici": "politician",
        "Piero di Cosimo de' Medici": "banker"
    }

    # Check if the given name exists and the role matches
    if relation_name in medici_roles and medici_roles[relation_name] == relation_role:
        return True
    return False