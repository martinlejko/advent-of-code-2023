cards = {
    'A' : 12,
    'K' : 11,
    'Q' : 10,
    'T' : 9,
    '9' : 8,
    '8' : 7,
    '7' : 6,
    '6' : 5,
    '5' : 4,
    '4' : 3,
    '3' : 2,
    '2' : 1,
    'J' : 0,
}

def handValue(hand):
    apperences =[]
    joker_count = 0
    for key in cards:
        if key == 'J':
            joker_count = hand.count(key)
        else:
            apperences.append(hand.count(key))
    apperences.sort(reverse=True)
    value = 0

    if apperences[0] == 5:
        if value < 7:
            value = 7
    if apperences[0] == 4:
        if value < 6:
            value = 6
    if apperences[0] == 3 and apperences[1] == 2:
        if value < 5:
            value = 5
    if apperences[0] == 3:
        if value < 4: 
            value = 4
    if apperences[0] == 2 and apperences[1] == 2:
        if value < 3:
            value = 3
    if apperences[0] == 2:
        if value < 2:
            value = 2
    if joker_count == 5:
        if value < 7:
            value = 7
    if joker_count == 4:
        if value < 7:
            value = 7
    if joker_count == 3 and apperences[0] == 2:
        if value < 7:
            value = 7
    if joker_count == 3 and apperences[0] == 1:
        if value < 6:
            value = 6
    if joker_count == 2 and apperences[0] == 3:
        if value < 7:
            value = 7
    if joker_count == 2 and apperences[0] == 2:
        if value < 6:
            value = 6
    if joker_count == 2 and apperences[0] == 1:
        if value < 4:
            value = 4
    if joker_count == 1 and apperences[0] == 4:
        if value < 7:
            value = 7
    if joker_count == 1 and apperences[0] == 3:
        if value < 6:
            value = 6
    if joker_count == 1 and apperences[0] == 2 and apperences[1] == 2:
        if value < 5:
            value = 5
    if joker_count == 1 and apperences[0] == 2:
        if value < 4:
            value = 4
    if joker_count == 1 and apperences[0] == 1:
        if value < 2:
            value = 2
    else:
        if value < 1:
            value = 1
    evals.add((hand,value))
    return int(value)

def highCard(handA, handB):
    for i in range(0,len(handA)):
        if cards[handA[i]] > cards[handB[i]]:
            return 0
        elif cards[handA[i]] < cards[handB[i]]:
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
 
with open('07/input2.txt','r') as f:
    evals = set()
    lines = f.readlines()
    hands = {}
    sum = 0
    
    for line in lines:
        line = line.strip().split(' ')
        hands[line[0]] = [line[1], 0]

    for hand in hands:
        for hand2 in hands:
            if hand != hand2:
                compareHands(hand, hand2)
    hands = sorted(hands.items(), key=lambda x: x[1][1])
    hands_count = len(hands)

    for i in range (1, hands_count+1):
        # print(f"{i} * {int(hands[i-1][1][0])}")
        sum += i*int(hands[i-1][1][0])
    
    print(f"Sum: {sum}")