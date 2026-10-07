import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    numChars = int(sys.stdin.readline().rstrip())
    msg = sys.stdin.readline().rstrip()
    j = 0
    while j<numChars:
        token = msg[j:j+3]
        rToken = token[::-1]
        if rToken in msg[j+3:]:
            k = msg.find(rToken)
            secret = msg[j+3:k]
            for letter in token:
                secret = secret.replace(letter*2, letter)
            print(secret)
            j = k+3
        else:
            j += 1 