def respond(alert):
    if alert['severity'] == 'high':
        return "quarantine_host"
    return "log_only"