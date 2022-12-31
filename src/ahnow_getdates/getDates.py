'''
Created on Dec 29, 2022

@author: billw
'''

from datetime import datetime, timedelta
import copy

class DatesInRange:
    """
    get all dates from a start date to end date inclusive
    
    :param startDate: The beginning date (YYYY-MM-DD).
    :type startDate: str
    
    :param endDate: The end date (YYYY-MM-DD)
    :type endDate: str
    """     
        
    def __init__(self, startDate, endDate):
        self.startDate = startDate
        self.endDate = endDate
        
        
    def getDatesInRange(self):
        dateFormat = "%Y-%m-%d"
        dateStart = datetime.strptime(self.startDate,dateFormat)
        dateEnd = datetime.strptime(self.endDate, dateFormat)
        extractDate = copy.copy(dateStart)
        extractDate = extractDate - timedelta(days=1)
        diffDays = (dateEnd - extractDate).days
        for i in range(0,diffDays):
            extractDate = extractDate + timedelta(days=1)
            yield extractDate.strftime(dateFormat)
