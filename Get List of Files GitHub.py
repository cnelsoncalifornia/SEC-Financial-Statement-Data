# This code obtains a list of all the json files that are downloaded from bulk data on the SEC website.
# Visit https://www.sec.gov/edgar/sec-api-documentation
# Download companyfacts.zip at the bottom of the page.
# Extract the json files from companyfacts.zip and place them in their own folder.  
# Put the path to that folder in 'path here' below.
# Created by cnelsoncalifornia and first made available on github June 2, 2022.




import os
import pandas as pd

path = r'path here'

list_of_files = []
for root,dirs,files in os.walk(path):
    for file in files:
        list_of_files.append(os.path.join(root,file))

listdf=pd.DataFrame(list_of_files)

listdf.to_excel("List of files.xlsx")

