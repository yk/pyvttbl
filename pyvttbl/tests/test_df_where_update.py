

# Copyright (c) 2011, Roger Lew [see LICENSE.txt]
# This software is funded in part by NIH Grant P20 RR016454.

# Python 2 to 3 workarounds
import sys
if sys.version_info[0] == 2:
    _strobj = str
    _xrange = xrange
elif sys.version_info[0] == 3:
    _strobj = str
    _xrange = range
    
import unittest
import warnings
import os

import numpy as np

from pyvttbl import DataFrame
from pyvttbl.misc.support import *

class Test_where_update(unittest.TestCase):
    def test0(self):
        R = DataFrame([('SUBJECT', [1, 2]), ('TIMEOFDAY', ['T1', 'T1']), ('COURSE', ['C1', 'C2']), ('MODEL', ['M1', 'M1']), ('ERROR', [10, 10])])
        
        df=DataFrame()
        df.read_tbl('data/error~subjectXtimeofdayXcourseXmodel_MISSING.csv')
        df.where_update('ERROR = 10')
        self.assertEqual(repr(df),repr(R))
        
    def test1(self):
        R = DataFrame([('SUBJECT', [1, 2]), ('TIMEOFDAY', ['T1', 'T1']), ('COURSE', ['C1', 'C2']), ('MODEL', ['M1', 'M1']), ('ERROR', [10, 10])])
        
        df=DataFrame()
        df.read_tbl('data/error~subjectXtimeofdayXcourseXmodel_MISSING.csv')
        df.where_update(['ERROR = 10'])
        self.assertEqual(repr(df),repr(R))
        
    def test2(self):
        R = DataFrame([('SUBJECT', [1, 2]), ('TIMEOFDAY', ['T1', 'T1']), ('COURSE', ['C1', 'C2']), ('MODEL', ['M1', 'M1']), ('ERROR', [10, 10])])
        
        df=DataFrame()
        df.read_tbl('data/error~subjectXtimeofdayXcourseXmodel_MISSING.csv')
        df.where_update([('ERROR', '=', 10)])
        self.assertEqual(repr(df),repr(R))
        
    def test3(self):
        R = DataFrame([('SUBJECT', [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3]), ('TIMEOFDAY', ['T1', 'T1', 'T1', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T1', 'T1', 'T1', 'T2', 'T2', 'T2']), ('COURSE', ['C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1']), ('MODEL', ['M1', 'M2', 'M3', 'M1', 'M2', 'M3', 'M1', 'M2', 'M3', 'M1', 'M2', 'M3', 'M1', 'M2', 'M3']), ('ERROR', [10, 8, 6, 5, 4, 3, 4, 3, 3, 8, 7, 4, 4, 1, 2])])
        
        df=DataFrame()
        df.read_tbl('data/error~subjectXtimeofdayXcourseXmodel_MISSING.csv')
        df.where_update('COURSE = "C1" and TIMEOFDAY in ("T1", "T2")')
        self.assertEqual(repr(df),repr(R))
        
    def test5(self):
        R = DataFrame([('SUBJECT', [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3]), ('TIMEOFDAY', ['T1', 'T1', 'T1', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T1', 'T1', 'T1', 'T2', 'T2', 'T2']), ('COURSE', ['C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1']), ('MODEL', ['M1', 'M2', 'M3', 'M1', 'M2', 'M3', 'M1', 'M2', 'M3', 'M1', 'M2', 'M3', 'M1', 'M2', 'M3']), ('ERROR', [10, 8, 6, 5, 4, 3, 4, 3, 3, 8, 7, 4, 4, 1, 2])])
        
        df=DataFrame()
        df.read_tbl('data/error~subjectXtimeofdayXcourseXmodel_MISSING.csv')
        df.where_update(['COURSE = "C1"','TIMEOFDAY in ("T1", "T2")'])
        self.assertEqual(repr(df),repr(R))
        
    def test6(self):
        R = DataFrame([('SUBJECT', [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3]), ('TIMEOFDAY', ['T1', 'T1', 'T1', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T1', 'T1', 'T1', 'T2', 'T2', 'T2']), ('COURSE', ['C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1']), ('MODEL', ['M1', 'M2', 'M3', 'M1', 'M2', 'M3', 'M1', 'M2', 'M3', 'M1', 'M2', 'M3', 'M1', 'M2', 'M3']), ('ERROR', [10, 8, 6, 5, 4, 3, 4, 3, 3, 8, 7, 4, 4, 1, 2])])
        
        df=DataFrame()
        df.read_tbl('data/error~subjectXtimeofdayXcourseXmodel_MISSING.csv')
        df.where_update([('COURSE','=',['C1']),('TIMEOFDAY','in',["T1", "T2"])])
        self.assertEqual(repr(df),repr(R))
        
def suite():
    return unittest.TestSuite((
            unittest.makeSuite(Test_where_update)
                              ))

if __name__ == "__main__":
    # run tests
    runner = unittest.TextTestRunner()
    runner.run(suite())
