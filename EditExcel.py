from openpyxl import load_workbook

class runExcel():
    def __init__(self, city):
        self.wb = load_workbook('result.xlsx')
        cityList = {'sjz':'石家庄', 'ts':'唐山'}
        self.sheet = self.wb[cityList[city]]

    def readExcel(self):
        print(self.sheet['A1'].value)

    def writeExcel(self,idate,col_num):
        row_init = 2
        print('All:', len(idate))
        for val in range(len(idate)):
            self.sheet.cell(row_init, col_num).value = idate[val].strip()
            # print(val, idate[val])
            row_init += 1
        self.wb.save('result.xlsx')

    def parseData(self):
        pass

    def dataDeduplication(self):
        pass

    def run_main(self):
        ll = list('aa'*50)
        print(ll)

if __name__ == "__main__":
    myrunning = runExcel()
    myrunning.run_main()