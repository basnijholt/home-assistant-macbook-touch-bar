import json
from pathlib import Path

from requests import get

from secret import url, token

headers = {
    "Authorization": f"Bearer {token}",
    "content-type": "application/json",
}

this_folder = Path(__file__).resolve().parent


def entity(entity_id):
    response_raw = get(f"{url}/api/states/{entity_id}", headers=headers)
    return json.loads(response_raw.text)
