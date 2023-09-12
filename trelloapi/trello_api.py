import requests

class APIBase:
    api_key: str
    api_token: str

    def __init__(self, api_key, api_token):
        self.api_key = api_key
        self.api_token = api_token

class TrelloAPI(APIBase):

    base_url: str = "https://api.trello.com"
    api_version: str = "1"

    def get_api_call(self, type_req, resource_type, resource_id, resource_path):
        api_url = f"{self.base_url}/{self.api_version}/{resource_type}/{resource_id}/{resource_path}"

        header = {
            "Accept": "application/json"
        }
        query = {
            'key': self.api_key,
            'token': self.api_token
        }

        try:
            response = requests.request(
                type_req,
                api_url,
                headers=header,
                params=query
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Http Error: ", e)
        except requests.exceptions.ConnectionError as e:
            print("Connection error: ", e)
        except requests.exceptions.Timeout as e:
            print("Timeout Error: ", e)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

        if response.status_code == 200:
            try:
                resp_dict = response.json()
            except requests.JSONDecodeError:
                print('Response could not be serialized')
        else:
            return False


        return resp_dict