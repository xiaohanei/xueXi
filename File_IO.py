import csv
class File_IO():
    def read_txt(self,file_name):
        txt_file = open(file_name).readlines()
        return txt_file

    def read_csv(self,file_name):
        csv_file = csv.reader(open(file_name))
        return csv_file

    def write_csv(self,file_name,data):
        out = open(file_name,'a')
        csv_write = csv.writer(out)
        csv_write.writerow(data)



if __name__ == '__main__':
   # test_txt = File_IO().read_txt('/Users/mac/Desktop/pythonProject/xueXi/test_file/test.txt')
    #print(test_txt)
    #File_IO().write_csv('/Users/mac/Desktop/pythonProject/xueXi/test_file/test.csv',['李六','南昌','19'])
    test_csv = File_IO().read_txt('/Users/mac/Desktop/pythonProject/xueXi/test_file/test.csv')
    print(test_csv)
    # for line in test_txt:
    #     print(line.split(','))