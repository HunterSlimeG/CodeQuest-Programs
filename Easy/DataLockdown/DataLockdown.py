
cases = int(input())
for caseNum in range(cases):
    links = int(input())
    review = []
    for link in range(links):
        line = input().split(" ")
        url = line[0]
        size = int(line[1])

        if not url.endswith(".lmco.com") and not ".lmco.com/" in url and size > 1000:
            review.append(" ".join(line))
    print("\n".join(review))