import requests
from dataclasses import dataclass
@dataclass
class TrelloAPI:
    api_key : str = ""
    api_token : str = ""

    def get_api_call(self, resource_type, resource_id, resource_path):
        api_url = f"https://api.trello.com/1/{resource_type}/{resource_id}/{resource_path}"

        header = {
            "Accept": "application/json"
        }
        query = {
            'key': self.api_key,
            'token': self.api_token
        }

        try:
            response = requests.request(
                "GET",
                api_url,
                headers=header,
                params=query
            )
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(e)

        if response.status_code == 200:
            try:
                resp_dict = response.json()
            except requests.JSONDecodeError:
                print('Response could not be serialized')
        else:
            return False


        return response.json()