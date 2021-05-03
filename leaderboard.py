leaderboard = 'leaderboard.txt'

def getTopX(x = 3):
    file = open(leaderboard, 'r')
    content = file.readlines()

    topX = [player.strip() for player in content]
    if(x == 'all'):
        return topX
    return topX[:x]

def addItemToLeaderboard(playerName, playerScore):
    file = open(leaderboard, 'r')
    content = file.readlines()

    scores = [int((player.strip()).split('-')[1]) for player in content]

    high = len(scores)
    low = 0

    while low < high:
        mid = (low + high) // 2
        if(playerScore > scores[mid]):
            high = mid
        else:
            low = mid + 1


    content.insert(low , playerName + ' - ' + str(playerScore) + '\n')
    content = ''.join(content)

    file = open(leaderboard, 'w')
    file.write(content)

def removeItemFromLeaderboard(playerName, index):
    file = open(leaderboard, 'r')
    content = file.readlines()

    allPlayerEntrys = [entry for entry in content if entry.split(' - ')[0] == playerName]

    removed = allPlayerEntrys.pop(index - 1)

    content.remove(removed)
    content = ''.join(content)

    file = open(leaderboard, 'w')
    file.write(content)
