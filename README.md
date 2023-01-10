# GetDates

Utility to produce all dates in a range

#Installation
pip install getDates


#Get started
How to get all dates from start date to end date inclusive:

import getDates

# Instantiate a getDates object
            reportDates = getDates.DatesInRange("2022-12-1", "2022-12-25')                  


# Call the getDatesInRange method
            for gaDate in reportDates.getDatesInRange():
              print(gaDate)
              
              
