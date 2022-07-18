#Example no1
import logging as lg
lg.basicConfig(filename='polymorphism and overriding_file', level=lg.DEBUG, format='%(asctime)s %(message)s')

class ineuron:
    def intership(self):
        lg.error('1st program begins')
        try:
            print('You are in intership class')
        except:
            lg.error('something when wrong')

class job:
    def intership(self):
        try:
            print('you are in job class who have done intership')
        except:
            lg.error('something when wrong')
            lg.info('first program ended')

def placement(a)  :
    a.intership()

i=ineuron()
j=job()
placement(i)
placement(j)

# #Example 2
class techneuron:
    def __init__(self,name,current_status,age):
        self.name=name
        self.current_status=current_status
        self.age=age

    def info(self):
        lg.info('2nd program begins')
        try:
            if self.age>40:
                print('Sorry!! you are not Eligible')
            else:
                print('Eligible')
        except:
            lg.error('something went wrong')



class kidneuron(techneuron):
    def __init__(self,name,current_status,age):
        techneuron.__init__(self,name,current_status,age)
    def info(self):
        try:
            if self.age<15:
                print('you are eligible')
            else:
                print('you are not eligible')
        except:
            lg.error('something when wrong')
            lg.info('second proogram ended')

def com(a):
    a.info()

c=techneuron('sai','job',58)
d=kidneuron('tai','job',10)
com(c)
com(d)

#3 program
class ineuron1:
    def __init__(self,videos_completed):
        self.videos_completed=videos_completed

    def live_comp(self):
        lg.info('3rd program begins')
        try:
            if self.videos_completed>'75%':
                print('You have completed 75% of live video')
            else:
                print('Not completed 75% live video')
        except:
            lg.error('something went wrong')
            lg.info('1st  parent block exceuted')

class kindineuron2(ineuron1):
    def __init__(self, videos_completed):
        ineuron1.__init__(self,videos_completed)

    def live_comp(self):
        try:
            if self.videos_completed >= '75%':
                print('You have completed 75% of live video')
            else:
                print('Not completed 75% live video')
        except:
            lg.error('something went wrong')
def completion(z):
    z.live_comp()

a=ineuron1('65%')
b=kindineuron2('80%')
completion(a)
completion(b)

#4 program
class ineuron1:
    def __init__(self,hackthon_name):
        self.hackthon_name=hackthon_name

    def challenge(self):
        lg.info('4th program begins')
        try:
            if self.hackthon_name=='Data analystic ':
                print('You are in data analytic hackthon')
            else:
                print('oops!!This is data analystic hackthon ')
        except:
            lg.error('something went wrong')

class ineuron2(ineuron1):
    def __init__(self, hackthon_name):
        ineuron1.__init__(self,hackthon_name)

    def challenge(self):
        try:
            if self.hackthon_name=='blockchain':
                print('you are in blockchain hackthon')
            else:
                print('oops!!you are  in blockchain hackthon')
        except:
            lg.error('something went wrong')
def complition(z):
    z.challenge()

a=ineuron1('java')
b=ineuron2('blockchain')
complition(a)
complition(b)

#5
class oneneuron:

    def price(self):
        lg.info('5th program begins')
        try:
            a=int(input('Enter your budget for ineuron'))
            if a<=18000 and a>=4000:
                print('Course is in your budget')
            else:
                print('Your budget is higher than course price')
        except:
            lg.error('something went wrong')

class techneuron:

    def price(self):
        try:
            a = int(input('Enter your budget for ineuron'))
            if a<=11000 and a>=4000:
                print('Course is in your budget')
            else:
                print('Your budget is higher than course price')
        except:
            lg.error('something went wrong')
def prices(z):
    z.price()

a=oneneuron()
b=techneuron()
prices(a)
prices(b)

#6th program

class oneneuron:
    def course(self):
        lg.error('6th program begins')
        try:
            print('Welcome to one neuron')
        except:
            lg.error('something when wrong')

class techneuron:
    def course(self):
        try:
            print('Welcome to techneuron')
        except:
            lg.error('something when wrong')
            lg.info('6th program ended')

def flatform(a)  :
    a.course()

i=oneneuron()
j=techneuron()
flatform(i)
flatform(j)

#7th program begins
class Digital_marketing:
    def intership(self):
        lg.error('7th program begins')
        try:
            a=int(input('For how many months you want intership'))
            print('Congrats!!you are one step ahead for digital marketing intership..Let you know soon')
        except:
            lg.error('something when wrong')

class Tech:
    def intership(self):
        try:
            a = int(input('For how many months you want intership'))
            print('Congrats!!you are one step ahead for Tech intership..Let you know soon')
        except:
            lg.error('something when wrong')
            lg.info('7th program ended')

def status(a)  :
    a.intership()

i=Digital_marketing()
j=Tech()
status(i)
status(j)

#8th program

class oneneuron_enrollment:
    def __init__(self,name,email_id,phn_no):
        self.name=name
        self.email_id=email_id
        self.phn_no=phn_no

    def welcome(self):
        lg.info('8th program begins')
        try:
            if type(self.phn_no)==int and len(str(self.phn_no))==10 :
                pass
            else:
                print('phone number is invalid')
        except:
            lg.error('something when wrong')


class tech_neuron_enrollment(oneneuron_enrollment):
    def __init__(self,name,email_id,phn_no):

        oneneuron_enrollment.__init__(self,name,email_id,phn_no)

    def welcome(self):
        try:
            if type(self.phn_no) ==int and  len(str(self.phn_no))==10 :
                pass
            else:
                print('phone number is invalid')

        except:
            lg.error('something when wrong')

def enroll(phn_no):
    # name.welcome()
    # email_id.welcome()
    phn_no.welcome()

i=oneneuron_enrollment('sairaj','dafe@gmail.com','96s44811466')
j=tech_neuron_enrollment('manu','manu@gmail.com','7412589634')
enroll(i)
enroll(j)

#9th program
class ineuron:
    def Assignment(self):
        lg.error('9th program begins')
        try:
            print('Ineuron Assignment done')
        except:
            lg.error('something when wrong')

class oneneuron:
    def Assignment(self):
        try:
            print('One neuron Assignment done')
        except:
            lg.error('something when wrong')
            lg.info('9th program ended')

def check(a):
    a.Assignment()

i=ineuron()
j=oneneuron()
check(i)
check(j)

# 10th program begin
class Tech:
    def __init__(self,graduation,skill_set,curr_ctc):
        self.graduation=graduation
        self.skill_set=skill_set
        self.curr_ctc=curr_ctc
    def Skill(self):
        lg.error('10th program begins')
        try:
            if self.graduation=='B.tech' and self.graduation=='B.E':
                if self.skill_set=='SQL' and self.skill_set=='python':
                    if int(self.curr_ctc)<=7:
                        print('elgible for job')
                    else:
                        print('Not eligible for job')
        except:
            lg.error('something went wrong')

class oneneuron(Tech):
    def __init__(self, graduation, skill_set, curr_ctc):
        Tech.__init__(self, graduation, skill_set, curr_ctc)
    def Skill(self):
        try:
            if self.graduation=='12th' or self.graduation=='dropout':
                print(self.graduation)
                if self.skill_set=='SEO' or self.skill_set=='google adv':
                    print(self.skill_set)
                    if self.curr_ctc<=7:
                        print('elgible for job')
                    else:
                        print('Not eligible for job')

        except:

            lg.error('something when wrong')
            lg.info('9th program ended')

def check(a):
    a.Skill()

i=Tech('B.Tech','SQL',5)
j=oneneuron('Dropout'.lower(),'google adv',6)
check(i)
check(j)

