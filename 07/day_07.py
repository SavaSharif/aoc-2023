import itertools
from typing import List
from common.utils import read_file


def p1(input: List[str]) -> int:
    card_ranks = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'] # A is the strongest, 2 is the weakest
    hands = [tuple(line.split()) for line in input]
    patterns = [
        five_of_a_kind,
        four_of_a_kind,
        full_house,
        three_of_a_kind,
        two_pairs,
        one_pair,
        high_card
    ]

    def custom_sort_key(item):
        value_1 = next(i for i, pattern in enumerate(patterns) if pattern(item[0]))
        
        value_2 = card_ranks.index(item[0][0])
        value_3 = card_ranks.index(item[0][1])
        value_4 = card_ranks.index(item[0][2])
        value_5 = card_ranks.index(item[0][3])
        value_6 = card_ranks.index(item[0][4])

        return (value_1, value_2, value_3, value_4, value_5, value_6)


    hands.sort(key=custom_sort_key, reverse=True)


    total_winnings = sum((i+1) * int(bet) for i, (_, bet) in enumerate(hands))
    return total_winnings


def p2(input: List[str]) -> int:
    card_ranks = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    hands = [tuple(line.split()) for line in input]

    patterns = [
        five_of_a_kind,
        four_of_a_kind,
        full_house,
        three_of_a_kind,
        two_pairs,
        one_pair,
        high_card
    ]
    
    new_hands = hands.copy()
    for i, (hand, bet) in enumerate(hands):
    #    check whether it contains a joker
        if "J" in hand:
            possible_hands = []
            # joker can be any card, so we need to check all possible hands and find the best one
            for card in card_ranks:
                new_hand = hand.replace("J", card)
                possible_hands.append((new_hand, bet))
            # check all possible hands and find the best one
            possible_hands.sort(key=lambda x: (next(i for i, pattern in enumerate(patterns) if pattern(x[0])), card_ranks.index(x[0][0]), card_ranks.index(x[0][1]), card_ranks.index(x[0][2]), card_ranks.index(x[0][3]), card_ranks.index(x[0][4])))
            new_hands[i] = possible_hands[0]

    # combine both into a new list that looks like: old_hand, new_hand, bet
    hands = list(zip(hands, new_hands))

    # sort hands by pattern, then by card rank
    # the first element of the tuple is the old hand, the second element is the new hand, we want to pattern match on the new hand, but sort by the old hand
    hands.sort(
        key=lambda x: (
            next(i for i, pattern in enumerate(patterns) if pattern(x[1][0])),
            card_ranks.index(x[0][0][0]),
            card_ranks.index(x[0][0][1]),
            card_ranks.index(x[0][0][2]),
            card_ranks.index(x[0][0][3]),
            card_ranks.index(x[0][0][4])
        ),
        reverse=True
    )

    # remove the new hand from the tuple
    hands = [(new_cards, new_bet) for (old_cards, old_bet), (new_cards, new_bet) in hands]

    
    total_winnings = sum((i+1) * int(bet) for i, (_, bet) in enumerate(hands))
    return total_winnings


def five_of_a_kind(cards: List[str]) -> bool:
    return len(set(cards)) == 1

def four_of_a_kind(cards: List[str]) -> bool:
    return len(set(cards)) == 2 and any(cards.count(card) == 4 for card in set(cards))

def full_house(cards: List[str]) -> bool:
    return len(set(cards)) == 2 and any(cards.count(card) in (2, 3) for card in set(cards))

def three_of_a_kind(cards: List[str]) -> bool:
    return len(set(cards)) == 3 and any(cards.count(card) == 3 for card in set(cards))

def two_pairs(cards: List[str]) -> bool:
    return len(set(cards)) == 3 and sum(cards.count(card) == 2 for card in set(cards)) == 2

def one_pair(cards: List[str]) -> bool:
    return len(set(cards)) == 4 and any(cards.count(card) == 2 for card in set(cards))

def high_card(cards: List[str]) -> bool:
    return len(set(cards)) == 5

if __name__ == "__main__":
    input_data = read_file("07/input.txt")
    result = p1(input_data)
    result = p2(input_data)

    print(result)
