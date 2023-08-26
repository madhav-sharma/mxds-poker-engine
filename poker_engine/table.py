import logging
from datetime import datetime

from .player import Player


class Table:
    """
    A class to represent a poker table.
    """
    def __init__(self):
        self.start_time = datetime.utcnow()
        self.players = []
        self.dealer = None
        self.deck = None

    def add_player(self, player: Player) -> bool:
        """
        Add a player to the table.
        """
        logging.info(f"Adding player {player} to table")
        if player in self.players:
            return False
        self.players.append(player)

