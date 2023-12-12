cards = {
    'A' : 12,
    'K' : 11,
    'Q' : 10,
    'J' : 9,
    'T' : 8,
    '9' : 7,
    '8' : 6,
    '7' : 5,
    '6' : 4,
    '5' : 3,
    '4' : 2,
    '3' : 1,
    '2' : 0,
}

def handValue(hand):
    apperences =[]
    for key in cards:
        apperences.append(hand.count(key))
    apperences.sort(reverse=True)
    print(apperences)
    if apperences[0] == 5:
        return 7
    if apperences[0] == 4:
        return 6
    if apperences[0] == 3 and apperences[1] == 2:
        return 5
    if apperences[0] == 3:
        return 4
    if apperences[0] == 2 and apperences[1] == 2:
        return 3
    if apperences[0] == 2:
        return 2
    else:
        return 1

def highCard(handA, handB):
    for char in handA:
        if cards[char] > cards[handB[0]]:
            return 0
        elif cards[char] < cards[handB[0]]:
            return 1

def compareHands(handA, handB):
    handA_value = handValue(handA)
    handB_value = handValue(handB)
    if handA_value == handB_value:
        if highCard(handA, handB) == 0:
            hands[handA][1] += 1
        else:
            hands[handB][1] += 1
    elif handA_value > handB_value:
        hands[handA][1] += 1
    else:
        hands[handB][1] += 1

with open('07/example.txt','r') as f:
    lines = f.readlines()
    hands = {}
    for line in lines:
        line = line.strip().split(' ')
        hands[line[0]] = [line[1], 0]

for hand in hands:
    for hand2 in hands:
        if hand != hand2:
            compareHands(hand, hand2)
for hand in hands:
    for hand2 in hands:
        if hand != hand2 and hands[hand][1] == hands[hand2][1]:
            compareHands(hand, hand2)

hands = sorted(hands.items(), key=lambda x: x[1][1])
hands_count = len(hands)
for i in range (1, hands_count+1):
    print(f"{i} * {int(hands[i-1][1][0])}")

print(hands)