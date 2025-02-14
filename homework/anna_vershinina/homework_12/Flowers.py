class Flower:
    leaves = True

    def __init__(
        self,
        name,
        lifespan_in_days,
        color,
        price,
        stem,
    ):
        self.name = name
        self.lifespan_in_days = lifespan_in_days
        self.color = color
        self.price = price
        self.stem = stem

    def __str__(self):
        return str(
            self.__dict__
        )  # This function allows to see objects like a dictionary


class Succulent(Flower):
    petals_type = "Only green leaves"
    color = "green"

    def __init__(self, name, lifespan_in_days, price, stem):
        super().__init__(
            name,
            lifespan_in_days,
            Succulent.color,
            price,
            stem,
        )

    def __str__(self):
        return str(self.__dict__)


class Rose(Flower):
    thorns = True

    def __init__(
        self,
        name,
        lifespan_in_days,
        color,
        price,
        stem,
    ):
        super().__init__(
            name,
            lifespan_in_days,
            color,
            price,
            stem,
        )

    def __str__(self):
        return str(self.__dict__)


class Bouquet:

    def __init__(self):
        self.flowers = (
            []
        )  # attribute - a variable which belongs to the object

    def add_flower(self, flower):  # adds passed flower object to a list
        self.flowers.append(flower)

    def when_withers(self):
        total_lifespan = sum(
            flower.lifespan_in_days for flower in self.flowers
        )
        bouquet_lifespan = total_lifespan / len(self.flowers)
        return bouquet_lifespan

    def sort_bouquet(self, criterion):
        self.flowers.sort(key=lambda flower: getattr(flower, criterion))

    def bouquet_flower_search(self, criterion, value):
        search_result = []
        """search_criterion = ['price', 'lifespan_in_days', 'color', 'stem']"""

        for flower in self.flowers:
            if criterion == "price" and flower.price == value:
                search_result.append(flower)
            elif (
                criterion == "lifespan_in_days"
                and flower.lifespan_in_days == value
            ):
                search_result.append(flower)
            elif criterion == "color" and flower.color == value:
                search_result.append(flower)
            elif criterion == "stem" and flower.stem == value:
                search_result.append(flower)

        if search_result:
            return "\n".join(str(flower) for flower in search_result)
        else:
            return "Nothing was found"

    def __str__(self):
        output_str = "\n".join(str(flower) for flower in self.flowers)
        return output_str


white_rose = Rose("White Rose", 5, "white", 50, 40)
chamomile = Flower("Chamomile", 3, "yellow", 10, 20)
hydrangea = Flower("Ajisai", 10, "purple", 30, 5)
beautiful_succulent = Succulent("Swamp Grace", 15, 10, 3)
red_rose = Rose("Red Rose", 4, "red", 60, 37)

bouquet1 = Bouquet()
bouquet1.add_flower(white_rose)
bouquet1.add_flower(beautiful_succulent)
bouquet1.add_flower(hydrangea)
bouquet1.add_flower(chamomile)

print(bouquet1)
lifespan_bouquet_1 = round(bouquet1.when_withers())
print(f"Bouquet will be fresh for {lifespan_bouquet_1} days")

bouquet1.sort_bouquet("lifespan_in_days")
print(f"The sorted list: \n{bouquet1}")

search_result = bouquet1.bouquet_flower_search("price", 10)
print(f"The search result is: \n{search_result}")
