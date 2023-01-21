'''
定义学生类、老师类基于Person
'''
from sort import sort_byscore_des,sort_byscore_asc,binsearch
from file import save_file1,save_file2,save_file3,read_file,load_data
from abc import ABCMeta,ABC,abstractmethod

class Person(object,metaclass=ABCMeta):#父类：Person
    def __init__(self,name:str,age:int,sex:str):
        self.name=name #属性：姓名
        self.age=age   #属性：年龄
        self.sex=sex   #属性：性别

class Student(Person):#学生类
    count=0
    def __init__(self,name,age,sex,id:str,score:int):
        Student.count+=1    #实现学生计数
        self.id=id  #属性：学号
        self.__score=score  #私有属性：成绩
        super(Student,self).__init__(name, age, sex)#super方法调用父类初始化
    #实现对score读写
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        self.__score=value

    #学生自己查询成绩
    def stu_search(self):
        flag=0
        id=input('请输入学号：')
        a=read_file(filepath)
        res=a[1]#得到文件内容
        for i in range(len(res)):
            if res[i][3]==id:
                print(f'您的成绩为：{res[i][4]}')
                flag=1
                break
        if flag==0:
            print('您的学号有误，请重新输入！')

class Studentoperate():#接口:定义操作方法(抽象)
    #录入学生信息
    def input_student(self):
        pass
    #修改学生信息
    def change_sthdent(self):
        pass
    #删除学生信息
    def delete_student(self):
         pass
    #查询学生信息
        #通过姓名查询
    def tea_search_byname(self):
        pass
        #通过分数查询
    def tea_search_byscore(self):
        pass
    #排序
        #按成绩由高到低排序并保存
    def sortbyscore_des_save(self):
        a=read_file(filepath)
        headers=a[0]
        res=a[1]
        res=sort_byscore_des(res)
        save_file2(filepath2, headers)
        save_file3(filepath2, res)
        print('排序已完成！')
        #按成绩由低到高排序并保存
    def sortbyscore_asc_save(self):
        a=read_file(filepath)
        headers=a[0]
        res=a[1]
        res=sort_byscore_asc(res)
        save_file2(filepath3, headers)
        save_file3(filepath3, res)
        print('排序已完成！')

    #显示所有学生信息
    def show_allstudent(self):
        print('a:按成绩降序显示')
        print('b:按成绩升序显示')
        str=input('请输入a或b:')
        if str=='a':
            load_data(filepath2)
        elif str=='b':
            load_data(filepath3)

class Teacher(Person,Studentoperate):#老师类
    def __init__(self,name,age,sex,title:str):
        self.title=title    #属性：职称
        super(Teacher,self).__init__(name,age,sex)
    #录入学生信息
    def input_student(self):
        name=input('姓名：')
        age=eval(input('年龄：'))
        sex=input('性别：')
        id=input('学号：')
        score=eval(input('成绩：'))
        save_file1(filepath, [name, age, sex, id, score])
        print('信息已录入！')
    #修改学生信息
    def change_student(self):
        flag=0
        name1 = input('需要修改学生的姓名：')
        score = eval(input('请输入成绩：'))
        b=read_file(filepath)
        headers=b[0]
        res=b[1]
        for i in range(len(res)):
            if res[i][0]==name1:
                res[i][4]=score
                flag=1
                break
        if flag==0:
            print('该生信息不存在！')
        else:
            save_file2(filepath,headers)
            save_file3(filepath, res)
            print('信息以修改！')

    #删除学生信息
    def delete_student(self):
        name2=input('需要删除信息的学生姓名：')
        flag=0
        c=read_file(filepath)
        headers=c[0]
        res=c[1]
        for j in range(len(res)):
            if res[j][0]==name2:
                # res.pop(j)
                del res[j]
                flag=1
                break
        if flag==0:
            print('系统未找到该生信息！')
        else:
            save_file2(filepath, headers)
            save_file3(filepath, res)
            print('该生信息以删除！')

    #查询学生信息
        #通过姓名查询
    def tea_search_byname(self):
        name3=input('请输入学生姓名：')
        flag = 0
        d = read_file(filepath)
        headers = d[0]
        res = d[1]
        for j in range(len(res)):
             if res[j][0] == name3:
                # print(f'{headers[0]}:{res[j][0]},{headers[1]}:{res[j][1]},{headers[2]}:{res[j][2]},{headers[3]}:{res[j][3]},{headers[4]}:{res[j][4]}')
                for u in range(len(headers)):
                    print(headers[u],end='  ')
                print('\n')
                for v in range(5):
                        print(res[j][v],end='   ')
                print('\n')
                flag = 1
                break
        if flag == 0:
            print('系统未找到该生信息！')
        #通过分数查询:二分查找
    def tea_search_byscore(self):
        score=int(input('请输入分数：'))
        flag = 0
        e=read_file(filepath3)
        headers = e[0]
        res = e[1]
        index=binsearch(res,score) #二分查找
        print(f'分数为{score}的学生信息为：')
        print(f'{headers[0]}:{res[index][0]};{headers[1]}:{res[index][1]};{headers[2]}:{res[index][2]};{headers[3]}:{res[index][3]}')

class StudentView:
    def __init__(self):
        self.tch=Teacher('张老师',55,'男','教授')
        self.stu=Student('张三',20,'男','001',100)
    def __display__(self):
        print('-'*100)
        print('*'*25,'学生信息管理系统','*'*25)
        print('''
            |       (1)添加学生信息           |
            |       (2)修改学生信息           |
            |       (3)删除学生信息           |
            |       (4)通过姓名查询学生信息     |
            |       (5)通过分数查询学生信息     |
            |       (6)按成绩由高到低排序、并保存|
            |       (7)按成绩由低到高排序、并保存|
            |       (8)查看所有学生信息        |
            |       (e)退出系统               |
                 ''')

    def diaplay_student(self):
        print('-'*100)
        print('*'*25,'成绩查询系统','*'*25)
        print('''
        1:查询成绩
        2：退出
        ''')

    def main(self):
        while True:
            #选择功能
            num = input('请选择功能：')
            if num == '1':
                self.tch.input_student()
            elif num == '2':
                self.tch.change_student()
            elif num == '3':
                self.tch.delete_student()
            elif num == '4':
                self.tch.tea_search_byname()
            elif num == '5':
                self.tch.tea_search_byscore()
            elif num == '6':
                self.tch.sortbyscore_des_save()
            elif num == '7':
                self.tch.sortbyscore_asc_save()
            elif num == '8':
                self.tch.show_allstudent()
            elif num == 'e':
                exit()

    def main_stu(self):
        while True:
            num=input('请选择功能：')
            #选择功能
            if num=='1':
                self.stu.stu_search()
            elif num=='2':
                exit()
class Login:
    usn=None
    psd=None

    def is_validate_student(self) -> bool:
            if self.usn=='admin' and self.psd=='0001':
                return True
            else:
                return False

    def is_validate_teacher(self) -> bool:
            if self.usn=='admin' and self.psd=='123456':
                return True
            else:
                return False

if __name__ == '__main__':
    filepath='D:\learning app\PythonProject\manage system\student.csv'
    filepath2='D:\learning app\PythonProject\manage system\student_des.csv'
    filepath3='D:\learning app\PythonProject\manage system\student_asc.csv'
    stu=StudentView()
    login=Login()
    usn=input('请输入用户名：')
    psd=input('请输入密码：')
    login.usn=usn
    login.psd=psd
    print('s代表学生|t代表老师')
    pd=input('请输入s或t:')
    if pd=='s':
        if login.is_validate_student() is True:
            stu.diaplay_student()
            stu.main_stu()
        else:
            print('用户名或密码错误，请重新输入！')
    elif pd=='t':
        if login.is_validate_teacher() is True:
            stu.__display__()
            stu.main()
        else:
            print('用户名或密码错误，请重新输入！')

    # stu.diaplay_student()
    # stu.main_stu()
    # stu.__display__()
    # stu.main()
