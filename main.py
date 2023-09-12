import json

from models.card import Card
from models.list import List
from trelloapi.trello_api import TrelloAPI
from models.board import Board
from dotenv import load_dotenv

import os
def main():
    load_dotenv()

    api_key = os.getenv("API_KEY")
    api_token = os.getenv("API_TOKEN")
    resource_id = os.getenv("RESOURCE_ID")

    trelloapi = TrelloAPI(api_key, api_token)

    boards_list = trelloapi.get_api_call("GET", "organizations", resource_id, "boards")

    if not isinstance(boards_list, list):
        return False

    for board in boards_list:
        b = Board.from_json(json.dumps(board))
        if not b.id:
            return False
        lists = trelloapi.get_api_call("GET","boards", b.id, "lists")
        if not isinstance(lists, list):
            return False
        for llist in lists:
            l = List.from_json(json.dumps(llist))
            if not l.id:
                return False
            cards = trelloapi.get_api_call("GET","lists", l.id, "cards")
            if not isinstance(cards, list):
                return False
            for card in cards:
                c = Card.from_json(json.dumps(card))
                print(c.id + ", " + c.name + ", " + c.desc)

    print("Continued...")

if __name__ == '__main__':
    main()