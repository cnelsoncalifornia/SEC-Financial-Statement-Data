# SEC-Financial-Statement-Data
This code extracts financial statement data from annual and quarterly reports filed by US publicly traded corporations.

Warning!  This code is likely to exclude many data points that may be important to your results.  This should be considered preliminary only.  In order to include more data, you will need to modify the code given in SEC Data Extract GitHub.py (included).

Step 1: Visit https://www.sec.gov/edgar/sec-api-documentation  Download companyfacts.zip at the bottom of the page and extract the json files.  There should be one for each company.

Step 2: Use Get List of Files GitHub.py (included) to get a file that contains the paths of each of the json files.

Step 3: Identify the code for the financial statement data that you wish to obtain.  Options can be found on the file SEC Data Index.xlsx (included).  To access net income, for instance, use ['facts']['us-gaap']['NetIncomeLoss']['units']['USD'] in SEC Data Extract GitHub.py.

Step 4: Modify SEC Data Extract GitHub.py to output a CSV file that contains the financial statement data you are interested in obtaining.

The first version of these files was uploaded to GitHub on June 1-2, 2022 by cnelsoncalifornia.
