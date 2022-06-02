# Use this code to create a dataframe containing reported net income for periods running Jan 1 through Dec 31 and then export it to a CSV file.
# This code may be modified to get other financial statement data and/or other reporting periods.
# Tags those companies that have 2021 (the latest year available as of this writing) and 2009, which is the earliest year for which the data seem to be decent.
# Requires a list of the names and paths of each file for each company.
# Created by cnelsoncalifornia and first made available on github June 1, 2022.



# WARNING: This code is likely to exclude data from many companies.  This should only be considered a preliminary code.  
# See the readme file for more details.


import json
import pandas as pd


file_list = pd.read_excel('List of files.xlsx') # Gets list of all files containing SEC company data.  One file per company.


num_companies=len(file_list.index)


i = 0
data = pd.DataFrame()
d1 = pd.DataFrame()
for i in range(num_companies):      #  There may be a long wait. Replace range(num_companies) with range(100) to test the code. 
    with open(file_list['File Addresses'][i], 'r') as json_file:
        company = (json.load(json_file))
    co_num=file_list['File Addresses'][i][-15:-5]  # This gives the company's identifying CIK code.
   
    try:
        d1 = pd.DataFrame(company['facts']['us-gaap']['NetIncomeLoss']['units']['USD'])  
                        # NetIncomeLoss can be replaced with other accounting numbers.
        d1= d1[d1['form']=='10-K']  # Gets only data from annual reports.  Excludes quarterly reports.
        d1= d1.drop_duplicates(subset = ['start'], keep = 'last',ignore_index = True) 
                        # Drops rows with duplicate start dates.  Keep the last one.
    
        # Drops quarterly data.  This is necessary since quarterly data might appear in annual reports.
        is_year = []
        has_2021 = False
        has_2009 = False
        for j in range(len(d1)):
            month = [int(d1['start'][j][5]),int(d1['start'][j][6])]
            end_month = [int(d1['end'][j][5]),int(d1['end'][j][6])]
            month_match = (month[1]==end_month[1]+1)|((month[0]==0) & (month[1]==1) & (end_month[0]==1) & (end_month[1]==2))
            year = [int(d1['start'][j][2]),int(d1['start'][j][3])]
            end_year = [int(d1['end'][j][2]),int(d1['end'][j][3])] 
            year_match = ((year[0]==end_year[0])&(year[1]==end_year[1]))
            is_year.append(month_match&year_match)
            if((year[0]==2)&(year[1]==1)):
               has_2021 = True
            if((year[0]==0)&(year[1]==9)):
               has_2009 = True
        d1.insert(loc=0,column='is_year',value=is_year)
        d1 = d1[d1['is_year']==True]  #Drops values that aren't annual or that don't start Jan 1.
        if(len(d1)<5):
            continue
        
        d1.insert(0,"has 2021",has_2021)
        d1.insert(1,"has 2009",has_2009)
    
        d1.insert(0,"CIK",co_num) # Insert column that has the CIK (Company code) number.
        d1.rename(columns={'val':'NetIncome'},inplace=True) 
                    # Rename val as Net Income.  inplace=True means makes changes to original datafile.

        data = data.append(d1)
        
    except:
        continue
   

# Export to CSV file.
data.to_csv("SEC Earnings Data CSV.csv")




