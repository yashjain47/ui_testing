import softest
import logging
from openpyxl import workbook, load_workbook
import csv

class Utils(softest.TestCase):
    def assertListItemText(self,list,value):

        for stop in list:
            print("The Text is : ",stop.text)
            # assert stop.text == value
            
            '''This is soft Assertions'''
            self.soft_assert(self.assertEqual, stop.text ,value)
            if stop.text == value:
                print("Test Passed")
            else:
                print("Test Failed")

        self.assert_all()

    def custom_logger(loglevel=logging.DEBUG):
        
        # create logger.
        logger = logging.getLogger(__name__) 
        logger.setLevel(logging.DEBUG)

        # create console handler(ch) or file handler(fh) and set the log level.
        fh = logging.FileHandler("automation.log",mode="a")

        # create formatter - how you wants your logs to be formatted.
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s ',datefmt='%d/%m/%Y %I:%M:%S %p')

        # add formater to console or file hanlder. 
        fh.setFormatter(formatter)

        # add console handler to the logger.
        logger.addHandler(fh)
        return logger        
        

    def read_data_from_excel(file_name,sheet):

        datalist = []

        wb = load_workbook(filename=file_name)
        sh = wb[sheet]

        row_ct = sh.max_row
        col_ct = sh.max_column

        for i in range(2,row_ct+1):
            row = []
            for j in range(1,col_ct+1):
                row.append(sh.cell(row = i,column = j).value)
                print(sh.cell(row = i,column = j).value,end=' ')
            datalist.append(row)
            print('\n')

        return datalist


    def read_data_from_csv(file_name):

        datalist = []

        # open csv file
        with open(file=file_name,mode='r') as csvdata:
            reader = csv.reader(csvdata)

            # skip header
            next(reader)

            # add csv rows to datalist
            for rows in reader:
                datalist.append(rows)
                print("rows : ",rows)

        return datalist

        