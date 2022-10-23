# Grocery-Deals
After browsing online for ingrdients to cook pasta, I wondered which grocer offered them most affordably.
Driven by curiosity, I compared the product webpages of near equivalent items and noted where I found the cheapest option.
Keeping organized sparks joy, so I made a Google Spreadsheet to document my findings:
https://docs.google.com/spreadsheets/d/19FUu_ghsOdYvcTWcPXHH6B38UvputOzPQotog9w1dBY/edit?usp=sharing

I wanted a reference to see which grocer provided the most competitive price.
For example, a bundle of green onions costs $0.20 less on Weee! compared to Amazon Fresh.
With a bit of functional programming within Sheets, I automatically highlighted the cheapest vendor and returned its name in a separate column.

As a broke college student who restocks biweekly, I quickly realized manually updating my spreadsheet would be time consuming.
Instead of clicking links and overwriting prices, I used Python to automate the boring stuff.

Here is the process:

1. Make a Google Cloud project and enable Google Drive and Google Sheets API
https://pygsheets.readthedocs.io/en/staging/authorization.html

2. Create a service key, which generates a dummy email/ user who can access your drive, and save it as a JSON to your computer
https://developers.google.com/workspace/guides/create-credentials#service-account

3. Install libariaries to speed up development (pygsheets, bs4, requests_html, pandas)
https://github.com/nithinmurali/pygsheets

4. Divide and conquer: separate files contain scripts that interact with the Google Spreadsheet, obtain the price from a website, and store constants that faciliate the other operations

The result is a spreadsheet that updates its prices column everytime the script runs, which can be maintained on a consistent basis with Task Scheduler on Windows
