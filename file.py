'''
文件系统
'''
import csv
import pandas as pd
from sort import sort_byscore_des,sort_byscore_asc,binsearch
#保存
#save_file1：写入学生信息，save_file2：写入文件头，save_file3:写入具体信息
def save_file1(filepath,class_list):
    with open(filepath,'a+',newline="") as f:
        writer=csv.writer(f)
        writer.writerow(class_list)

def save_file2(filepath,class_list):
    with open(filepath,'w',newline="") as f:
        writer=csv.writer(f)
        writer.writerow(class_list)

def save_file3(filepath,stu_list):
    with open(filepath, 'a+', newline="") as f:
        writer = csv.writer(f)
        for i in range(len(stu_list)):
            writer.writerow(stu_list[i])

#读取并加载到列表中
def read_file(filepath)->list:
    res=[]
    with open(filepath,'r',newline="") as f:
        reader=csv.reader(f)
        headers=next(reader)
        for row in reader:
            res.append(row)
        for i in range(len(res)):
            res[i][1]=eval(res[i][1])
            res[i][4]=eval(res[i][4])
    return headers,res
#显示学生信息
def load_data(filepath):
    with open(filepath, 'r', newline="") as f:
        data=pd.read_csv(f)
        print(data)

