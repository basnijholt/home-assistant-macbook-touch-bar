import json
from pathlib import Path

from requests import get, post

from secret import url, token

headers = {
    "Authorization": f"Bearer {token}",
    "content-type": "application/json",
}

this_folder = Path(__file__).resolve().parent
icon_folder = this_folder.parent / "icons"


def entity(entity_id):
    response_raw = get(f"{url}/api/states/{entity_id}", headers=headers)
    return json.loads(response_raw.text)


def service(domain, service, entity_id, **data):
    data = dict(data, entity_id=entity_id)
    response_raw = post(
        f"{url}/api/services/{domain}/{service}",
        headers=headers,
        data=json.dumps(data),
    )
    return response_raw
