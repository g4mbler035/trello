import json

from models.card import Card
from models.list import List
from trelloapi.trello_api import TrelloAPI
from models.board import Board
def main():

    trelloapi = TrelloAPI("8eb49dc2edac940d34abefa9c42c2b08", "ATTA32e8d1ccec9186eb0176fd97a2411f40d3fcfd9b2ed643c29dd0d302c926e17728FF51B8")

    boards_list = trelloapi.get_api_call("organizations","6489550fc20357debf4c8d65", "boards")

    if isinstance(boards_list, list):
        for board in boards_list:
            b = Board.from_json(json.dumps(board))
            if b.id:
                lists = trelloapi.get_api_call("boards", b.id, "lists")
                if isinstance(lists, list):
                    for llist in lists:
                        l = List.from_json(json.dumps(llist))
                        if(l.id):
                            print(l.id)
                            cards = trelloapi.get_api_call("lists", l.id, "cards")
                            # print(cards)
                            if isinstance(cards, list):
                                for card in cards:
                                    c = Card.from_json(json.dumps(card))
                                    print(c.id + ", " + c.name + ", " + c.desc)
                        else:
                            print("List ID is not valid")
            else:
                print("Board ID is not valid")

    print("Continued...")
if __name__ == '__main__':
    main()
