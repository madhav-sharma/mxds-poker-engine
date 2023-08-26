class Player:
    """
    A class to represent a poker player.
    """
    def __init__(self, name: str, account_id: str):
        self.name = name
        self.account_id = account_id

    def __eq__(self, other):
        return self.account_id == other.account_id

    def __str__(self):
        return f"Player: {self.name} ({self.account_id})"

