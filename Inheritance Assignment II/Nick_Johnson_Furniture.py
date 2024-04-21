class Furniture:
    def __init__(self, weight: int):
        if weight <= 0:
            raise ValueError("Weight must be positive")
        else:
            self.__weight = weight

    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int) -> None:
        if weight <= 0:
            raise ValueError("Weight must be positive")
        else:
            self.__weight = weight

    def __str__(self) -> str:
        return "Item Weight: " + str(self.__weight)

    def __eq__(self, other: "Furniture") -> bool:
        return self.__weight == other.__weight

    def __ne__(self, other: "Furniture") -> bool:
        return self.__weight != other.__weight

    def __lt__(self, other: "Furniture") -> bool:
        return self.__weight < other.__weight

    def __le__(self, other: "Furniture") -> bool:
        return self.__weight <= other.__weight

    def __gt__(self, other: "Furniture") -> bool:
        return self.__weight > other.__weight

    def __ge__(self, other: "Furniture") -> bool:
        return self.__weight >= other.__weight


class Table(Furniture):
    def __init__(self, weight: int, wood: str):
        Furniture.__init__(self, weight)

        if not isinstance(wood, str):
            raise ValueError("Wood should be of type string")

        else:
            self.__wood = wood

    @property
    def wood(self) -> str:
        return self.__wood

    @wood.setter
    def wood(self, wood) -> None:
        if not isinstance(wood, str):
            raise ValueError("Wood should be of type string")

        else:
            self.__wood = wood

    def __str__(self) -> str:
        return "Table " + Furniture.__str__(self) + " Made of: " + self.wood


class Bed(Furniture):
    SIZES = ["Twin", "Full", "Queen", "King"]

    def __init__(self, weight: int, size: str):
        Furniture.__init__(self, weight)

        if size not in Bed.SIZES:
            raise ValueError("Size must be Twin, Full, Queen, or King")
        else:
            self.__size = size

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str) -> None:
        if size not in Bed.SIZES:
            raise ValueError("Size must be Twin, Full, Queen, or King")
        else:
            self.__size = size

    def __str__(self) -> str:
        return "Bed " + Furniture.__str__(self) + " Size: " + self.__size


class FurnitureGallery:
    def __init__(self):
        self.__furnList = []

    def addFurniture(self, item: Furniture) -> None:
        if isinstance(item, Furniture):
            self.__furnList.append(item)
        else:
            raise ValueError("Item must be an instance of the Furniture class")

    def __iter__(self):
        for item in self.__furnList:
            yield item

    def sort(self) -> list[Furniture]:
        for i in range(len(self.__furnList)):
            alr_sort = True

            for j in range(len(self.__furnList) - i - 1):
                if self.__furnList[j].weight > self.__furnList[j + 1].weight:
                    self.__furnList[j], self.__furnList[j + 1] = (
                        self.__furnList[j + 1],
                        self.__furnList[j],
                    )

                    alr_sort = False

            if alr_sort:
                break
