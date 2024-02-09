data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

from rich import print as rprint
data = [{'cards': cards, 'bid': int(bid)} for hand in data.splitlines() for cards, bid in [hand.split()]]
# rprint(data)

CARDS = 'AKQJT98765432'
BASE = 20
CARDS_DICT = {card: idx + 1 for idx, card in enumerate(CARDS[::-1])}
CARD_TYPE_COUNTS = [(5, 1), (4, 2), (3, 2), (3, 3), (2, 3), (2, 4), (1, 5)]
CARD_TYPE_DICTS = {counts: 10**(6 * idx) for idx, counts in enumerate(CARD_TYPE_COUNTS)}

def hand_face_value(hand):
    value = 0
    for idx, card in enumerate(hand):
        value *= BASE
        value += CARDS_DICT[card]
    return value

def hand_type_value(hand):
    max_appearance = max([hand.count(i) for i in set(hand)])
    return CARD_TYPE_DICTS[(len(set(hand)), max_appearance)]

def hand_value(hand):
    return hand_face_value(hand) * hand_type_value(hand)

def hand_ordering(hand_bid):
    return hand_value(hand_bid['cards'])

sorted_data = sorted(data, key=hand_ordering)
total_won = 0
for idx, hand_info in enumerate(sorted_data):
    total_won += (idx + 1) * hand_info['bid']
print(total_won)

types = ['high', 'pair', '2pair', '3kind', 'full', '4kind', '5kind']
sorted_by_type = {types[i]: [] for i in range(7)}

from math import log10
for hand in sorted_data:
    idx = int(log10(hand_type_value(hand['cards'])) // 6)
    sorted_by_type[types[idx]].append(hand['cards'])
# print(sorted_by_type)