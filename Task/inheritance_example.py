import logging as lg
lg.basicConfig(filename='inheritance_task_file', level=lg.DEBUG, format='%(asctime)s %(message)s')
class ineuro:
    def __init__(self, course_name, course_no, coding_background):
        self.course_name = course_name
        self.course_no = course_no
        self.coding_background = coding_background

    def ineuron1(self):
        lg.info('first program')
        try:
            if self.course_name=='fsds':
                print('okay choose from following')
        except Exception as e:
            lg.error('No such course no')

class internship(ineuro):
    def __init__(self,course_name,course_no,coding_background):
        super().__init__(course_name,course_no,coding_background)

    def intern_eligible(self):
        try:
            if self.coding_background=='freshers':
                print('elgible for internship')
            else:
                print('Not eligible for internship')
        except Exception as e:
            lg.error('their is some mistake')

class jobs(internship):
    def __init__(self,intership_experience,coding_background):
        super().__init__(self,intership_experience,coding_background)
        self.intership_experience=intership_experience
        print('Welcome to job portal')

    def Eligible(self):
        print(f'intership_experience-{self.intership_experience}')
        try:
            if self.intership_experience>=1:
                print('Yes!! you are eligible for job')
            else:
                print('Not eligible for job ')
        except Exception as e:
            lg.info('something when wrong')



# 2nd Example
class oneneuron:

    def __init__(self,course_name,course_domain,course_duration):
        self.course_name=course_name
        self.course_domain=course_domain
        self.course_duration=course_duration

    def ineuron2(self):
        try:
            if self.course_name=='fsds' or self.course_name=='web development' or self.course_name=='blockchain':
                print('Course is available')
            else:
                print('course Not available')
        except Exception as e:
            lg.error('There is some mistake',e)
            lg.info('Second program ended')

class intership1(oneneuron):
    def __init__(self,course_duration,internship_duration):
        self.course_duration=course_duration
        self.internship_duration=internship_duration

    def Availability(self):
        try:
            a=int(input('For how many months you want intership'))
            if self.internship_duration<=a and self.course_duration==12:
                print('Intership available')
            else:
                print('Intership not available')
        except:
            lg.error('There is some mistake')


class affialtes:
    def __init__(self,student_of_ineuron,batch):
        self.student_of_ineuron=student_of_ineuron
        self.batch=batch

    def capable(self):
        try:
            if self.student_of_ineuron=='yes':
                print('capable of affiliating')
            else:
                print('Not capable for affiliating')
        except:
            lg.error('There is some error')
#


#3 example

class intership3:
    def __init__(self, field , expertise):
        self.field = field
        self.expertise = expertise

    def eligible_criteria(self):
        try:
            if self.field == 'IT':
                print('Intership for your field available')
            else:
                print('Intership for your field not available')
        except:
            lg.error('something when wrong')
class jobs2:
    def __init__(self,intership_experience,project_status):
        self.intership_experience=intership_experience
        self.project_status=project_status

    def selection(self):
        try:
            if self.intership_experience>2 and self.project_status=='Done':
                print('Eligible for job')
            else:
                print('Not eligible for job')
        except Exception as e:
            lg.error('something when wrong',e)

class selction_for_mnc(intership3,jobs2):
    def __init__(self,field,expertise,intership_experience,project_status):
        intership3.__init__(self,field,expertise)
        jobs2.__init__(self,intership_experience,project_status)
    def mnc(self):
        try:
            if self.intership_experience>4 and self.field=='IT':
                print('You are selected in mnc')
            else:
                print('you are not selected in mnc')
        except:
            lg.error('something is wrong')
#


# Example 4
class assignment:
    def __init__(self,video_status_in, quizes_per):
        self.video_status_in=video_status_in
        self.quizes_per=quizes_per
    def Ass_vid_completion_status(self):
        try:
            if self.video_status_in =='75%' and self.quizes_per=='75%':
                print('All Assignment and videos 75% completed')
            else:
                print('Assignment or video 75% not done')
        except:
            lg.error('something when wrong')

class intership4:
    def __init__(self,status):
        self.status = status

    def intership_status(self):
        try:
            if self.status=='Done':
                print('intership done')
            else:
                print('intership not done')
        except:
            lg.error('something went wrong')

class Aprroval(assignment,intership4):
    def __init__(self,video_status_in, quizes_per,status):
        assignment.__init__(self,video_status_in, quizes_per)
        intership4.__init__(self,status)

    def final_approval(self):
        try:
            if self.video_status_in=='75%' and self.quizes_per=='75%' and self.intership_status=='Done':
                print('congo!! you are finally selected in final job round')
            else:
                print('Intership or assignment or video not done fully')
        except:
            lg.error('something went wrong')

obj3=Aprroval('75%','75%','Done')
obj3.final_approval()
obj3.intership_status()
#5 example single inheritance


class ineuron5:
    def __init__(self,certificate_status):
        self.certificate_status=certificate_status

    def passing(self):
        try:
            lg.info('5th program begins')
            if self.certificate_status=='pass':
                print('you are eligible to generate certificate')
            else:
                print('You are not eligible to generate certificate')
        except:
            lg.error('something when wrong')

class selection_for_job(ineuron5):
    def __init__(self,certificate_status):
        ineuron5.__init__(self,certificate_status)

    def job(self):
        try:
            if self.certificate_status=='Done':
                print('congo eligible for job')
            else:
                print('Not eligible ..complete the certificate')
        except:
            lg.error('something when wrong')




#6th program
class techneuron:
    try:
        def classes(self):
            print('Here you will get live link')
    except:
        lg.error('something went wrong')

class rec_classes(techneuron):
    try:
        def recording(self):
            print('Here you will get recorded videos')
    except:
        lg.error('something went wrong')

class live_rec_classes(rec_classes):
    try:
        def li_record(self):
            print('Here you will get recorded  and live videos')
    except:
        lg.error('something went wrong')


#7th program begins
class syllabus:
    def topics(self):
        try:
            print('This will show you the topics which will bbe covered')
        except:
             lg.error('something went wrong')

class Analystics:
    def your_result(self):
        try:
            print('This will show you the how much % of course you have completed')
        except:
             lg.error('something went wrong')

class overall(syllabus,Analystics):
    def final_status(self):
        try:
            print('This will show you final status')
        except:
            lg.error('something went wrong')


# 8th program
class ineuron():
    def ineuro(self):
        try:
            print('Yoa are in ineuron class')
        except:
            lg.error('There is some error')

class tech_ineuron(ineuron):
    def tech(self):
        try:
            print('Yoa are in tech ineuron class')
        except:
            lg.error('There is some error')



#10th project
class intershipp():
    def i_project(self):
        try:
            print('This all project belongs to ineuron')
        except:
            lg.error('There is some error')

class your_proj:
    def myself(self):
        try:
            print('This all project belongs to shahiraj')
        except:
            lg.error('There is some error')

class comb(intershipp,your_proj):
    def over_all(self):
        try:
            print('This combines both your ineuron and yours project')
        except:
            lg.error('There is some error')

obj1=ineuro('fsds','100','Experienced')
obj2=internship('fsds','555','Experienced')
obj2.ineuron1()
obj2.intern_eligible()
obj3=jobs(0 ,'freshers')
obj3.Eligible()
obj3.intern_eligible()



obj1=oneneuron('javascript','IT','1 year')
obj1.ineuron2()#
obj2=intership1(12,12)
obj2.Availability()
obj3=affialtes('yes',2018)
obj3.capable()



obj1=intership3('IT','data science')
obj1.eligible_criteria()
obj2=jobs2(6,'Done')
obj2.selection()
obj3=selction_for_mnc('IT','data science',5,'Done')
obj3.eligible_criteria()
obj3.selection()




obj3=Aprroval('75%','75%','Done')
obj3.final_approval()
obj3.intership_status()

obj1=selection_for_job('Done')
obj1.job()

obj3=live_rec_classes()
obj3.li_record()
obj3.recording()
obj3.classes()

obj1=overall()
obj1.final_status()
obj1.your_result()
obj1.topics()


obj1=tech_ineuron()
obj1.ineuro()
obj1.tech()


obj1=comb()
obj1.myself()
obj1.i_project()
obj1.over_all()


























