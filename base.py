import regex as re


class LoLAPI:

    def __init__(self):
        self.api_key = self.get_api() 
        self.name_regex = re.compile(r'[^0-9._ a-zA-Z\p{L}]+$')
    def get_api(self):
        try:
            with open("api_key.txt","r") as api_file:
                return api_file.readline().strip()
        except FileNotFoundError as e:
            raise e
    def name_test(self, name):
        try:
            self.name_regex.search(name).group()
            return False
        except AttributeError as e:
            return True

if __name__ == '__main__':
    test = LoLAPI()
    print(test.api_key)
    print(test.name_test("SupineKrill"))