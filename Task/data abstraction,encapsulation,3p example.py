#example 1
import logging as lg
lg.basicConfig(filename='abs_enc_3p', level=lg.DEBUG, format='%(asctime)s %(message)s')

class ineuron:
    __students='enroll'

    def student(self):
        try:
            lg.info('1st program begins')
            print('status of student is', ineuron.__students)
            lg.info('first program ended')
        except:
            lg.error('Something when wrong')


#Example2

class ineuron1:
    def __init__(self,course_name,course_domain,__fees):
        self.course_name=course_name
        self.course_domain=course_domain
        self.__fees = __fees

    def show(self):
        lg.info('2nd program begins')
        try:
            if self.course_name=='fSDS' or self.course_name=='blockchain':
                print('select domain')
                if self.course_domain=='IT':
                    print('check the fees')
                    print('fees is',self.__fees)
            else:
                pass
        except Exception as e:
            lg.error('something is wrong')


# 3 program begins
class sub:
    def __init__(self,__code,_mode,intership):
        self.code=__code
        self.mode=_mode
        self.intership=intership

    def valid(self):
        lg.info('3th  program begins')
        try:
            a=str(input('Enter the code')).lower()
            if self.mode=='online'.lower():
                print('code is 101')
            elif self.mode=='offline'.lower():
                print('code is 555')
            else:
                print('You have inserted something wrong')
        except Exception as e:
            print(e)

class check_it(sub):
    def __init__(self, __code, _mode,intership):
        sub.__init__(self, __code, _mode, intership)
    def we(self):
        try:
            lg.info('3rd program begin')
            b=str(input('Enter the mode no')).lower()
            if self.code==101:
                print('Welcome to online classs')
            elif self.mode==555:
                print('Welcome to offline class')
            else:
                print('you enter something else..please check')
        except Exception as e:
            print(e)


#4 program brgins
class internship:
    def __init__(self,stipend,role,id_no):
        self.__stipend=stipend
        self._role=role
        self.id_no=id_no

    def eligible(self):
        a=int(input('Enter the no of years Experience'))
        try:
            lg.info('4th program begins')
            if a==0:
                print('Eligible for intership')
            else:
                print('Not eligible for intership')
        except Exception as e:
            # lg.error('something when wrong')
            print('e')

    def gh(self):
        return self.__stipend

class one_internship(internship):
    def __init__(self,stipend,role,id_no):
        internship.__init__(self,stipend,role,id_no)
    def stp(self):
        try:
            a=int(input('enter the stipend'))
            if self.gh()>=a:
                print('stipend is less than 10000')
            else:
                print('stipend is more than 10000')
                lg.info('4th program ended')
        except Exception as e:
            # lg.error('something went wrong')
            print(e)


#5th example begin
class ineuron:
    def __init__(self):
        self.__students='login'

    def student(self):
        try:
            lg.info('5th program begins')
            print('status of student is', self._ineuron__students)
        except:
            lg.error('Something when wrong')

    def stu_change(self,new_value):
        try:
            self.__students=new_value
        except:
            print('Something when wrong')

#
# obj=ineuron()
# obj.student()
# print(obj._ineuron__students)
#
# obj=ineuron1('fSDS','IT','7000')
# obj.show()
#
# obj=check_it(101,'online','yes')
# obj.we()
# obj.valid()
#
# obj=ineuron()
# obj.student()
# obj.stu_change('error')
# obj.student()



