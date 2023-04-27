def insertionSort(list, last):
    comparison = 0
    for current in range(1, last + 1):
        hold = list[current]
        walker = current - 1
        while walker >= 0 and list[walker] > hold:
            list[walker + 1] = list[walker]
            walker -= 1
            comparison += 1
        list[walker + 1] = hold
        print(list)
    comparison = comparison + last - 1
    print("Comparison times :", comparison)


def selectionSort(list, last):
    comparison = 0
    for current in range(last):
        smallest = current
        walker = current + 1
        while walker <= last:
            if list[walker] < list[smallest]:
                smallest = walker
            walker += 1
            comparison += 1
        list[current], list[smallest] = list[smallest], list[current]
        print(list)
    print("Comparison times :", comparison)

def bubbleSort(list, last):
    current = 0
    comparison = 0
    sorted = "false"
    while current <= last and sorted == "false":
        walker = last
        sorted = "true"
        while walker > current:
            if list[walker] < list[walker - 1]:
                sorted = "false"
                list[walker], list[walker - 1] = list[walker - 1], list[walker]
            walker -= 1
            comparison += 1
        current += 1
        print(list)
    print("Comparison times :", comparison)


def insertionCardSort(cards, last):
    comparison = 0
    for current in range(1, last + 1):
        hold = cards[current]
        walker = current - 1
        while walker >= 0 and cardValue(cards[walker]) > cardValue(hold):
            cards[walker + 1] = cards[walker]
            walker -= 1
            comparison += 1
        cards[walker + 1] = hold
        print(cards)
    comparison = comparison + last - 1
    print("Comparison times :", comparison)

def selectionCardSort(cards, last):
    comparison = 0
    for current in range(last):
        smallest = current
        walker = current + 1
        while walker <= last:
            if cardValue(cards[walker]) < cardValue(cards[smallest]):
                smallest = walker
            walker += 1
            comparison += 1
        cards[current], cards[smallest] = cards[smallest], cards[current]
        print(cards)
    print("Comparison times :", comparison)

def bubbleCardSort(cards, last):
    current = 0
    comparison = 0
    sorted = "false"
    while current <= last and sorted == "false":
        walker = last
        sorted = "true"
        while walker > current:
            if cardValue(cards[walker]) < cardValue(cards[walker - 1]):
                sorted = "false"
                cards[walker], cards[walker - 1] = cards[walker - 1], cards[walker]
            walker -= 1
            comparison += 1
        current += 1
        print(cards)
    print("Comparison times :", comparison)

def cardValue(card):
    num = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12, "A": 13}
    set_of_cards = {"♣": 0, "♦": 1, "♥": 2, "♠": 3}
    return ((num[card[:-1]], set_of_cards[card[-1]]))

        
# insertionSort([23, 78, 45, 8, 32, 56], 5)
# selectionSort([23, 78, 45, 8, 32, 56], 5)
# bubbleSort([23, 78, 45, 8, 32, 56], 5)
# insertionCardSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
# selectionCardSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
bubbleCardSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
# cardValue(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'])