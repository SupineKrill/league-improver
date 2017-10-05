import regex as re
import requests


class LoLAPI:

    def __init__(self):
        self.api_key = self.get_api() 
        self.name_regex = re.compile(r'[^0-9._ a-zA-Z\p{L}]+$')
        self.region = "na1"
        self.basic_url = f"https://{self.region}.api.riotgames.com"

    def get_api(self):
        """Loads api key from text file."""
        try:
            with open("api_key.txt","r") as api_file:
                return api_file.readline().strip()
        except FileNotFoundError as e:
            raise e

    def real_name(self, name):
        """Confirms summoner name is a valid name. Returns boolean"""
        try:
            self.name_regex.search(name).group()
            return False
        except AttributeError as e:
            return True

    def request_json(self, url, return_json=True):
        """Return JSON from requested URL"""
        try:
            if return_json:
                return requests.get(f"{self.basic_url}{url}?api_key={self.api_key}").json()
            else:
                return requests.get(f"{self.basic_url}{url}?api_key={self.api_key}")
        except Exception as e:
            raise e

    def get_summoner_id(self,summoner_name, return_json=True):
        """Get a summoner by account id. Return JSON"""
        if self.real_name(summoner_name):
            return self.request_json(f"/lol/summoner/v3/summoners/by-name/{summoner_name}")

    def get_ranked_games(self, account_id, return_json=True):
        """Takes account ID. Returns JSON of all ranked games played"""
        return self.request_json(f"/lol/match/v3/matchlists/by-account/{account_id}", False) 

if __name__ == '__main__':
    test = LoLAPI()
    self_id = test.get_summoner_id("SupineKrill")["accountId"]
    print(self_id)