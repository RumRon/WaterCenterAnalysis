from datetime import datetime
import pandas as pd

def main():

    #read file
    file = r'C:\Users\jrach\Documents\ArcGIS\Projects\TAB2\Analysis\0126CSO\Daily\NE_CSO.xlsx'###
    data = pd.read_excel(file)

    #convert date time to date(year,month,day)
    data["Date"] = data["Datetime [EST\EDT]"].dt.date

    # use date to sum up daily volume for each CSO outfall
    data = data.groupby(['Date']).sum()

    #check
    #print(data)

    #write the output excel file
    name = "output.xlsx"###
    data.to_excel(name)
    pirnt("Excel file created sucessfully")

main()
