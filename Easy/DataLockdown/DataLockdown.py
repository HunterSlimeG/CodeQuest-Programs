import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    links = int(sys.stdin.readline().rstrip())
    review = []
    for link in range(links):
        line = sys.stdin.readline().rstrip().split(" ")
        url = line[0]
        size = int(line[1])

        if not url.endswith(".lmco.com") and not ".lmco.com/" in url and size > 1000:
            review.append(" ".join(line))
    print("\n".join(review))