import requests
import re
import itertools

startChallenge = 2329  # The highest Strava challenge number as of April 23, 2021.
failCount = 0

for i in itertools.count(start=startChallenge):
    link = f"https://www.strava.com/challenges/{i}"
    pageText = requests.get(link).text
    title = re.search('<\W*title\W*(.*)</title', pageText, re.IGNORECASE)  # Get the title from the page.

    if title.group(1) == "Challenges - Strava" and failCount >= 5:  # If we've run into 5 fails in a row, assume we hit the end
        break
    elif title.group(1) == "Challenges - Strava":  # If we get this title, some challenge doesn't exist.
        failCount += 1
    else:
        printString = title.group(1).replace(" - Strava Challenges", "") + f" ({link})"
        print(printString)

print("That's all, folks.")
