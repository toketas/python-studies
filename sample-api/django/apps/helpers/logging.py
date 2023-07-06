import logging
import json_log_formatter

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

formatter = json_log_formatter.JSONFormatter()

json_handler = logging.StreamHandler()
json_handler.setFormatter(formatter)
json_handler.setLevel(logging.INFO)

log.addHandler(json_handler)
log.propagate = False
