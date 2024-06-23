# A-Level Maths and Further Maths Progress Tracker

This program allows you to update which section you are up to (e.g., '4.3') for the latest (as of 23/06/24) A-Level Maths and Further Maths textbooks (the compulsary 6, and further stats 1 and 2). 


- Calculates mean percentage completion of year 1, year 2, and total A-Level.
- Stores the most recent completed sections in json files for each textbook.
- Run using a clickable .bat file.

I made this to gameify my progress to help motivate me and to practice my python skills.


## Viewing Your Progress
### Example input
```
view_or_update = 'v'
textbook_choice = 'pm1'   ...   (a.k.a., pure maths 1)
```
### Example output:
```
  You have completed 8.89% of the PM1 textbook
  Your last completed section is 2.2

  Total A-Level completion = 1.11%
  Total Year 1 completion = 2.22%
  Total Year 2 completion = 0.00%
```

## Updating Your Progress
### Example input
```
view_or_update = 'u'
textbook_choice = 'pm1'
latest_section = '2.2'
```
### Example output
```
You have now completed 8.89% of the PM1 textbook
```
