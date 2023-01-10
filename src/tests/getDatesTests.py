'''
Created on Dec 30, 2022

@author: billw
'''

import unittest
import GetDatesPackage.getDates as dates

class GetDatesTestCase(unittest.TestCase):
    
    def setUp(self):
        self.reportStartDate = "2022-12-25"
        self.reportEndDate = "2023-01-01"
        self.reportDates = dates.DatesInRange(self.reportStartDate, self.reportEndDate)                  

    def test_range(self):
        testDates = []
        for testDate in self.reportDates.getDatesInRange():
            testDates.append(testDate)
        self.assertEqual(self.reportStartDate, testDates[0],"Incorrect start date in range")
        self.assertEqual(self.reportEndDate, testDates[-1], "Incorrect end date")
        
        
if __name__ == '__main__':
    unittest.main()
            
            
            