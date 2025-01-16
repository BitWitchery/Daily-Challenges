def medici_family(relation_name, relation_role):
    if relation_name == 'Giovanni di Bicci de\' Medici' and relation_role == 'founder':
        return True
    elif relation_name == 'Lorenzo de\' Medici' and relation_role == 'patron':
        return True
    elif relation_name == 'Cosimo de\' Medici' and relation_role == 'politician':
        return True
    elif relation_name == 'Piero di Cosimo de\' Medici' and relation_role == 'banker':
        return False
    else:
        return False