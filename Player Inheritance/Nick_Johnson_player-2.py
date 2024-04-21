class Player:
    def __init__(self, name: str, position: str):
        if name == "":
            raise ValueError("name cannot be empty.")
        else:
            self.__name = name

        if position == "":
            raise ValueError("position cannot be empty.")
        else:
            self.__position = position

    @property  # read-only
    def name(self):
        return self.__name

    @property  # read-only
    def position(self):
        return self.__position

    def getStats(self) -> str:
        return "Player Name: " + self.__name + " Position: " + self.__position


class Pitcher(Player):
    def __init__(self, name: str, wins: int, loss: int):
        super().__init__(name, "Pitcher")  # init name and position from super

        if wins < 0:
            raise ValueError("wins cannot be negative.")
        else:
            self.wins = wins

        if loss < 0:
            raise ValueError("loss cannot be negative.")
        else:
            self.loss = loss

    # override super
    def getStats(self) -> str:
        return (
            super().getStats()
            + " "
            + str(self.wins)
            + "-"
            + str(self.loss)
            + " win-loss"
        )


class Batter(Player):
    def __init__(self, name: str, position: str, at_bats: int, hits: int):
        super().__init__(name, position)

        if at_bats < 0:
            raise ValueError("at_Bats cannot be negative.")
        else:
            self.at_bats = at_bats

        if hits < 0:
            raise ValueError("hits cannot be negative.")
        else:
            self.hits = hits

    @property  # read-only
    def average(self):
        return round(self.hits / self.at_bats, 3)

    # override super
    def getStats(self) -> str:
        # needs error checking for 0 at_bat -- not part of spec
        # needs error checking for hits > at_bat -- not part of spec
        return super().getStats() + " Stats: Batting Avg: " + str(self.average)
