import json
from pathlib import Path

import requests

from secret import token, url

headers = {
    "Authorization": f"Bearer {token}",
    "content-type": "application/json",
}

this_folder = Path(__file__).resolve().parent
icon_folder = this_folder.parent / "icons"


def entity(entity_id):
    try:
        response_raw = requests.get(f"{url}/api/states/{entity_id}", headers=headers)
        return json.loads(response_raw.text)
    except (requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
        return dict(state="unknown")


def service(domain, service, entity_id, **data):
    data = dict(data, entity_id=entity_id)
    response_raw = requests.post(
        f"{url}/api/services/{domain}/{service}",
        headers=headers,
        data=json.dumps(data),
    )
    return response_raw
