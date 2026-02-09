import json
from datetime import datetime


def log_audit(query, context, response):

    log_entry = {
        "timestamp": str(datetime.utcnow()),
        "query": query,
        "context_used": context,
        "response": response
    }

    with open("audit_log.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
