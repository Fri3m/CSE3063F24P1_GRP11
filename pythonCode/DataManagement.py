import json
import os
import random
from json import JSONEncoder

from Classroom import Classroom
from Course import CourseInformation, CourseRequirements, CourseSection, Course
from Day import Day, SectionTime

from Department import DepartmentID, Department
from Faculty import FacultyID, Faculty
from User import Lecturer, Advisor, DepartmentScheduler, StudentsAffairs, DepartmentHead

from pythonCode.UserInformation import UserInformation
from pythonCode.Student import StudentID, Student
from pythonCode.Transcript import Transcript
import logging

from pythonCode.Logger import setup_logger

logger = setup_logger("DataManagement")


class DataManagement:

    def __init__(self):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        pass

    def __main__(self):
        # Yıldırım

        engineering = generateFaculty(1, "Engineering")
        self.createOrChangeFaculty(engineering)

        science = generateFaculty(2, "Science")
        self.createOrChangeFaculty(science)

        computerEngineering = generateDepartment(150, "Computer Engineering", engineering)
        self.createOrChangeDepartment(computerEngineering)

        mechanicalEngineering = generateDepartment(151, "Mechanical Engineering", engineering)
        self.createOrChangeDepartment(mechanicalEngineering)

        electricalEngineering = generateDepartment(152, "Electrical Engineering", engineering)
        self.createOrChangeDepartment(electricalEngineering)

        biology = generateDepartment(153, "Biology", science)
        self.createOrChangeDepartment(biology)

        chemistry = generateDepartment(154, "Chemistry", science)
        self.createOrChangeDepartment(chemistry)

        advisor = generateRandomAdvisor(computerEngineering)

        lecturer = generateRandomLecturer(computerEngineering)
        lecturer2 = generateRandomLecturer(computerEngineering)
        lecturer3 = generateRandomLecturer(computerEngineering)
        lecturer4 = generateRandomLecturer(computerEngineering)
        lecturer5 = generateRandomLecturer(computerEngineering)
        lecturer6 = generateRandomLecturer(computerEngineering)
        lecturer7 = generateRandomLecturer(computerEngineering)
        lecturer8 = generateRandomLecturer(computerEngineering)
        lecturer9 = generateRandomLecturer(computerEngineering)
        lecturer10 = generateRandomLecturer(computerEngineering)
        lecturer11 = generateRandomLecturer(computerEngineering)

        self.createOrChangeLecturer(advisor)
        self.createOrChangeLecturer(lecturer)
        self.createOrChangeLecturer(lecturer2)
        self.createOrChangeLecturer(lecturer3)
        self.createOrChangeLecturer(lecturer4)
        self.createOrChangeLecturer(lecturer5)
        self.createOrChangeLecturer(lecturer6)
        self.createOrChangeLecturer(lecturer7)
        self.createOrChangeLecturer(lecturer8)
        self.createOrChangeLecturer(lecturer9)
        self.createOrChangeLecturer(lecturer10)
        self.createOrChangeLecturer(lecturer11)

        lecturersForSections = []
        lecturersForSections.append(lecturer)
        lecturersForSections.append(lecturer)
        lecturersForSections.append(lecturer)
        days = []
        days.append(Day.Monday)
        days.append(Day.Monday)
        days.append(Day.Wednesday)
        sectionTimes = []
        sectionTimes.append(SectionTime.First)
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Fifth)

        o_cr = generateClassroom("CS10", 70)
        o_cr1 = generateClassroom("CS11", 50)
        self.createOrChangeClassroom(o_cr)
        self.createOrChangeClassroom(o_cr1)

        o_course1 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr,o_cr,o_cr1], "Introduction to Computer Engineering","CS1200", list(), 1, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course1)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer2)
        lecturersForSections.append(lecturer2)
        lecturersForSections.append(lecturer2)
        days.clear()
        days.append(Day.Tuesday)
        days.append(Day.Tuesday)
        days.append(Day.Thursday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.Fourth)
        sectionTimes.append(SectionTime.First)


        o_cr2 = generateClassroom("CS12", 60)
        o_cr3 = generateClassroom("CS13", 60)
        self.createOrChangeClassroom(o_cr2)
        self.createOrChangeClassroom(o_cr3)



        o_course2 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr,o_cr,o_cr3], "Introduction to Algorithms","CS1201", list(), 1, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course2)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer3)
        lecturersForSections.append(lecturer3)
        days.clear()
        days.append(Day.Tuesday)
        days.append(Day.Friday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Sixth)

        o_cr3 = generateClassroom("CS13", 50)
        self.createOrChangeClassroom(o_cr3)

        o_course3 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr1,o_cr3], "Linear Algebra for Computer Engineering","MATH256", list(), 1, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course3)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer2)
        lecturersForSections.append(lecturer2)
        lecturersForSections.append(lecturer2)
        days.clear()
        days.append(Day.Monday)
        days.append(Day.Monday)
        days.append(Day.Tuesday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Fifth)
        sectionTimes.append(SectionTime.Sixth)
        sectionTimes.append(SectionTime.Third)

        prerequisites = []
        prerequisites.append(o_course1.getCourseInformation())

        o_cr4 = generateClassroom("CS14", 80)
        self.createOrChangeClassroom(o_cr4)

        o_course4 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr,o_cr,o_cr4], "Data Structures","CS2225", prerequisites, 2, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course4)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer3)
        lecturersForSections.append(lecturer3)
        days.clear()
        days.append(Day.Wednesday)
        days.append(Day.Friday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.First)

        o_cr5 = generateClassroom("CS15", 40)
        self.createOrChangeClassroom(o_cr5)

        o_course5 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr1,o_cr3], "Differential Equations","MATH205", list(), 2, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course5)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer4)
        lecturersForSections.append(lecturer4)
        lecturersForSections.append(lecturer4)
        days.clear()
        days.append(Day.Thursday)
        days.append(Day.Thursday)
        days.append(Day.Friday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Sixth)
        sectionTimes.append(SectionTime.Seventh)
        sectionTimes.append(SectionTime.Fourth)

        o_cr5 = generateClassroom("CS15", 70)
        self.createOrChangeClassroom(o_cr5)

        o_course6 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr5,o_cr5,o_cr4], "Systems Programming","CS2138", list(), 2, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course6)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer5)
        lecturersForSections.append(lecturer5)
        lecturersForSections.append(lecturer5)
        days.clear()
        days.append(Day.Monday)
        days.append(Day.Monday)
        days.append(Day.Friday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.First)
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.First)

        prerequisites1 = []
        prerequisites1.append(o_course4.getCourseInformation())

        o_cr6 = generateClassroom("CS16", 75)
        self.createOrChangeClassroom(o_cr6)

        o_course7 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr6,o_cr6,o_cr6], "Database Systems","CS3125", prerequisites1, 3, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course7)



# cr = generateClassroom("aa",20)
# dm.createOrChangeClassroom(cr)
#
# course = generateCourse([lec], [Day.Friday], [SectionTime.Fifth], [cr], "test", "TT101", list(), 1, dep.get_facultyID(), dep.getDepartmentID())
# dm.createOrChangeCourse(course)

        # Yusuf
        # **************************************************** Faculties ****************************************************
        # new Faculty "Business"
        business = generateFaculty(3, "Business")
        self.createOrChangeFaculty(business)

#         # new Faculty "Science"
#         Science = generateFaculty(2, "Science")
#         self.createOrChangeFaculty(Science)

        # **************************************************** Departments ****************************************************
        # new Department "Business" in Faculty "Business"
        businessDepartment = generateDepartment(301, "Business", business)
        self.createOrChangeDepartment(businessDepartment)

#       # New Department "Biology" in Faculty "Science"
#        Biology = generateDepartment(201, "Biology", Science)
#        self.createOrChangeDepartment(Biology)
#        # New Department "Chemistry" in Faculty "Science"
#        Chemistry = generateDepartment(202, "Chemistry", Science)
#        elf.createOrChangeDepartment(Chemistry)
        # **************************************************** Classrooms ****************************************************

        # New Classrooms Business Faculty
        classroom301 = generateClassroom("B301", 60)
        classroom302 = generateClassroom("B302", 75)

        self.createOrChangeClassroom(classroom301)
        self.createOrChangeClassroom(classroom302)

        # New Classrooms Science Faculty
        classroom201 = generateClassroom("S201", 80)
        classroom202 = generateClassroom("S202", 75)
        classroom203 = generateClassroom("S203", 55)
        classroom204 = generateClassroom("S204", 60)
        classroom205 = generateClassroom("S205", 55)

        self.createOrChangeClassroom(classroom201)
        self.createOrChangeClassroom(classroom202)
        self.createOrChangeClassroom(classroom203)
        self.createOrChangeClassroom(classroom204)
        self.createOrChangeClassroom(classroom205)

        # **************************************************** Advisors and Lecturers ****************************************************
        # new Advisors and Lecturers for Business Department
        advisor301 = generateRandomAdvisor(businessDepartment)
        lecturer301 = generateRandomLecturer(businessDepartment)
        lecturer302 = generateRandomLecturer(businessDepartment)
        lecturer303 = generateRandomLecturer(businessDepartment)

        self.createOrChangeAdvisor(advisor301)
        self.createOrChangeLecturer(lecturer301)
        self.createOrChangeLecturer(lecturer302)
        self.createOrChangeLecturer(lecturer303)

        # New Advisors and Lecturers for Biology Department

        advisor201 = generateRandomAdvisor(biology)
        lecturer201 = generateRandomLecturer(biology)
        lecturer202 = generateRandomLecturer(biology)
        lecturer203 = generateRandomLecturer(biology)
        lecturer204 = generateRandomLecturer(biology)

        self.createOrChangeAdvisor(advisor201)
        self.createOrChangeLecturer(lecturer201)
        self.createOrChangeLecturer(lecturer202)
        self.createOrChangeLecturer(lecturer203)
        self.createOrChangeLecturer(lecturer204)

        # New Advisors and Lecturers for Chemistry Department

        advisor211 = generateRandomAdvisor(chemistry)
        lecturer211 = generateRandomLecturer(chemistry)
        lecturer212 = generateRandomLecturer(chemistry)
        lecturer213 = generateRandomLecturer(chemistry)
        lecturer214 = generateRandomLecturer(chemistry)

        self.createOrChangeAdvisor(advisor211)
        self.createOrChangeLecturer(lecturer211)
        self.createOrChangeLecturer(lecturer212)
        self.createOrChangeLecturer(lecturer213)
        self.createOrChangeLecturer(lecturer214)

        # **************************************************** Courses ****************************************************

        # Course1 for Business Department
        lecturerForSections = []
        lecturersForSections.append(lecturer301)
        lecturersForSections.append(lecturer301)
        lecturersForSections.append(lecturer301)
        days = []
        days.append(Day.Monday)
        days.append(Day.Monday)
        days.append(Day.Thursday)
        sectionTimes = []
        sectionTimes.append(SectionTime.First)
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Fifth)
        course301 = generateCourse(lecturersForSections, days, sectionTimes, [classroom301, classroom301, classroom302], "Principles of Microeconomics", "EC101", list(), 1, businessDepartment.get_facultyID(), businessDepartment.getDepartmentID())
        self.createOrChangeCourse(course301)

        # Course2 for Business Department
        lecturersForSections.clear()
        lecturersForSections.append(lecturer302)
        lecturersForSections.append(lecturer302)
        lecturersForSections.append(lecturer302)
        lecturersForSections.append(lecturer302)

        days.clear()
        days.append(Day.Tuesday)
        days.append(Day.Tuesday)
        days.append(Day.Wednesday)
        days.append(Day.Wednesday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.First)
        sectionTimes.append(SectionTime.Second)
        prerequisites = []
        prerequisites.append(course301.getCourseInformation())
        course302 = generateCourse(lecturersForSections, days, sectionTimes, [classroom302, classroom302, classroom301, classroom301], "Microeconomics", "EC203", prerequisites, 2, businessDepartment.get_facultyID(), businessDepartment.getDepartmentID())
        self.createOrChangeCourse(course302)

        # Course3 for Business Department
        lecturerForSections.clear()
        lecturersForSections.append(lecturer301)
        lecturersForSections.append(lecturer301)
        lecturersForSections.append(lecturer301)
        lecturersForSections.append(lecturer301)
        days.clear()
        days.append(Day.Monday)
        days.append(Day.Tuesday)
        days.append(Day.Tuesday)
        days.append(Day.Friday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Fifth)
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.Fourth)
        sectionTimes.append(SectionTime.First)
        prerequisites.clear()
        course303 = generateCourse(lecturersForSections, days, sectionTimes, [classroom301, classroom301, classroom301, classroom302], "Financial Management", "FM311", prerequisites, 3, businessDepartment.get_facultyID(), businessDepartment.getDepartmentID())
        self.createOrChangeCourse(course303)

        # Course4 for Business Department
        lecturerForSections.clear()
        lecturersForSections.append(lecturer303)
        lecturersForSections.append(lecturer303)
        lecturersForSections.append(lecturer303)
        days.clear()
        days.append(Day.Wednesday)
        days.append(Day.Wednesday)
        days.append(Day.Wednesday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.Fourth)
        prerequisites.clear()
        course304 = generateCourse(lecturersForSections, days, sectionTimes,
                                   [classroom302, classroom302, classroom302], "Strategic Management",
                                   "AD401", prerequisites, 4, businessDepartment.get_facultyID(),
                                   businessDepartment.getDepartmentID())
        self.createOrChangeLecturer(course304)
        # ********************************************************************************************************************
        # Course1 for Biology Department
        lecturerForSections.clear()
        lecturersForSections.append(lecturer201)
        lecturersForSections.append(lecturer201)
        lecturersForSections.append(lecturer201)
        days.clear()
        days.append(Day.Tuesday)
        days.append(Day.Tuesday)
        days.append(Day.Friday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.First)
        prerequisites.clear()
        course201 = generateCourse(lecturersForSections, days, sectionTimes,
                                   [classroom201, classroom201, classroom205], "General Biology",
                                   "BYL1011", prerequisites, 1, biology.get_facultyID(),
                                   biology.getDepartmentID())
        self.createOrChangeCourse(course201)

        # Course2 for Biology Department
        lecturerForSections.clear()
        lecturersForSections.append(lecturer202)
        lecturersForSections.append(lecturer202)
        lecturersForSections.append(lecturer202)
        lecturersForSections.append(lecturer202)

        days.clear()
        days.append(Day.Wednesday)
        days.append(Day.Thursday)
        days.append(Day.Thursday)
        days.append(Day.Friday)

        sectionTimes.clear()
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.First)
        prerequisites.clear()
        course202 = generateCourse(lecturersForSections, days, sectionTimes,
                                   [classroom202, classroom204, classroom204, classroom202], "History of Biology",
                                   "BYL2031", prerequisites, 2, biology.get_facultyID(),
                                   biology.getDepartmentID())
        self.createOrChangeCourse(course202)

        # Course3 for Biology Department
        lecturerForSections.clear()
        lecturersForSections.append(lecturer203)
        lecturersForSections.append(lecturer203)
        lecturersForSections.append(lecturer203)
        days.clear()
        days.append(Day.Tuesday)
        days.append(Day.Tuesday)
        days.append(Day.Thursday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.First)
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Fourth)
        prerequisites.clear()
        prerequisites.append(course201.getCourseInformation())
        course203 = generateCourse(lecturersForSections, days, sectionTimes,
                                   [classroom203, classroom203, classroom201], "Micro Biology",
                                   "BYL3042", prerequisites, 3, biology.get_facultyID(),
                                   biology.getDepartmentID())
        self.createOrChangeCourse(course203)

        # Course4 for Biology Department
        lecturerForSections.clear()
        lecturersForSections.append(lecturer204)
        lecturersForSections.append(lecturer204)
        lecturersForSections.append(lecturer204)
        days.clear()
        days.append(Day.Monday)
        days.append(Day.Monday)
        days.append(Day.Monday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.Fourth)
        prerequisites.clear()
        prerequisites.append(course201.getCourseInformation())
        course204 = generateCourse(lecturersForSections, days, sectionTimes,
                                   [classroom201, classroom201, classroom201], "Human Anatomy",
                                   "BYL4011", prerequisites, 4, biology.get_facultyID(),
                                   biology.getDepartmentID())
        self.createOrChangeCourse(course204)
        #********************************************************************************************************************
        # Course1 for Chemistry Department
        lecturerForSections.clear()
        lecturersForSections.append(lecturer211)
        lecturersForSections.append(lecturer211)
        lecturersForSections.append(lecturer211)
        lecturersForSections.append(lecturer211)
        days.clear()
        days.append(Day.Monday)
        days.append(Day.Monday)
        days.append(Day.Friday)
        days.append(Day.Friday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.Fourth)
        prerequisites.clear()
        course211 = generateCourse(lecturersForSections, days, sectionTimes,
                                   [classroom202, classroom202, classroom203, classroom203], "General Chemistry",
                                   "CHM1135", prerequisites, 1, chemistry.get_facultyID(),
                                   chemistry.getDepartmentID())
        self.createOrChangeCourse(course211)
        # Course2 for Chemistry Department
        lecturerForSections.clear()
        lecturersForSections.append(lecturer212)
        lecturersForSections.append(lecturer212)
        lecturersForSections.append(lecturer212)
        lecturersForSections.append(lecturer212)
        days.clear()
        days.append(Day.Tuesday)
        days.append(Day.Tuesday)
        days.append(Day.Wednesday)
        days.append(Day.Thursday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Second)
        prerequisites.clear()
        prerequisites.append(course211.getCourseInformation())
        course212 = generateCourse(lecturersForSections, days, sectionTimes,
                                   [classroom205, classroom205, classroom204, classroom203], "Analytical Chemistry",
                                   "CHM2023", prerequisites, 2, chemistry.get_facultyID(),
                                   chemistry.getDepartmentID())
        self.createOrChangeCourse(course212)

        # Course3 for Chemistry Department
        lecturerForSections.clear()
        lecturersForSections.append(lecturer213)
        lecturersForSections.append(lecturer213)
        lecturersForSections.append(lecturer213)
        days.clear()
        days.append(Day.Tuesday)
        days.append(Day.Tuesday)
        days.append(Day.Wednesday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.Second)
        prerequisites.clear()

        course213 = generateCourse(lecturersForSections, days, sectionTimes,
                                   [classroom204, classroom204, classroom202], "Industrial Analysis",
                                   "CHM3042", prerequisites, 3, chemistry.get_facultyID(),
                                   chemistry.getDepartmentID())
        self.createOrChangeCourse(course213)

        # Course4 for Chemistry Department
        lecturerForSections.clear()
        lecturersForSections.append(lecturer214)
        lecturersForSections.append(lecturer214)
        lecturersForSections.append(lecturer214)
        lecturersForSections.append(lecturer214)
        days.clear()
        days.append(Day.Tuesday)
        days.append(Day.Wednesday)
        days.append(Day.Wednesday)
        days.append(Day.Friday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.First)
        prerequisites.clear()
        prerequisites.append(course213.getCourseInformation())
        course214 = generateCourse(lecturersForSections, days, sectionTimes,
                                   [classroom205, classroom205, classroom204, classroom203], "Biochemistry",
                                   "CHM4011", prerequisites, 4, chemistry.get_facultyID(),
                                   chemistry.getDepartmentID())
        self.createOrChangeCourse(course214)

        #*****************************************************Students***************************************************************
        # for example: student306 is for 6th student in Business Department, student204 is for 4th student in Biology Department, student213 is for 3rd student in Chemistry Department

        student301 = generateRandomStudent(businessDepartment, 2021, 2, advisor301.get_staffId())
        student302 = generateRandomStudent(businessDepartment, 2024, 15, advisor301.get_staffId())
        student303 = generateRandomStudent(businessDepartment, 2023, 66, advisor301.get_staffId())
        student304 = generateRandomStudent(businessDepartment, 2022, 58, advisor301.get_staffId())
        student305 = generateRandomStudent(businessDepartment, 2021, 24, advisor301.get_staffId())
        student306 = generateRandomStudent(businessDepartment, 2023, 13, advisor301.get_staffId())

        student201 = generateRandomStudent(biology, 2022, 75, advisor201.get_staffId())
        student202 = generateRandomStudent(biology, 2022, 53, advisor201.get_staffId())
        student203 = generateRandomStudent(biology, 2024, 34, advisor201.get_staffId())
        student204 = generateRandomStudent(biology, 2021, 3, advisor201.get_staffId())
        student205 = generateRandomStudent(biology, 2023, 27, advisor201.get_staffId())
        student206 = generateRandomStudent(biology, 2024, 11, advisor201.get_staffId())

        student211 = generateRandomStudent(chemistry, 2021, 37, advisor211.get_staffId())
        student212 = generateRandomStudent(chemistry, 2022, 29, advisor211.get_staffId())
        student213 = generateRandomStudent(chemistry, 2024, 1, advisor211.get_staffId())
        student214 = generateRandomStudent(chemistry, 2024, 25, advisor211.get_staffId())
        student215 = generateRandomStudent(chemistry, 2024, 45, advisor211.get_staffId())
        student216 = generateRandomStudent(chemistry, 2023, 8, advisor211.get_staffId())

        #Add students taken courses to the system
        student301.getTranscript().addTakemCourse(course301.getCourseInformation(), 90, 54)
        student301.getTranscript().addTakemCourse(course301.getCourseInformation(), 80, 65)
        student301.getTranscript().addTakemCourse(course301.getCourseInformation(), 70, 75)

        student303.getTranscript().addTakemCourse(course301.getCourseInformation(), 90, 64)

        student304.getTranscript().addTakemCourse(course301.getCourseInformation(), 93, 74)
        student304.getTranscript().addTakemCourse(course301.getCourseInformation(), 85, 65)

        student305.getTranscript().addTakemCourse(course301.getCourseInformation(), 75, 70)
        student305.getTranscript().addTakemCourse(course301.getCourseInformation(), 65, 85)
        student305.getTranscript().addTakemCourse(course301.getCourseInformation(), 75, 75)

        student306.getTranscript().addTakemCourse(course301.getCourseInformation(), 85, 75)

        student306.getTranscript().addTakenCourse(course301.getCourseInformation(), 85, 75)

        student201.getTranscript().addTakenCourse(course201.getCourseInformation(), 85, 75)
        student201.getTranscript().addTakenCourse(course202.getCourseInformation(), 90, 85)

        student202.getTranscript().addTakenCourse(course201.getCourseInformation(), 68, 75)
        student202.getTranscript().addTakenCourse(course202.getCourseInformation(), 88, 72)

        student204.getTranscript().addTakenCourse(course201.getCourseInformation(), 65, 85)
        student204.getTranscript().addTakenCourse(course202.getCourseInformation(), 75, 850)
        student204.getTranscript().addTakenCourse(course203.getCourseInformation(), 55, 10)

        student205.getTranscript().addTakenCourse(course201.getCourseInformation(), 75, 85)

        student211.getTranscript().addTakenCourse(course211.getCourseInformation(), 38, 90)
        student211.getTranscript().addTakenCourse(course212.getCourseInformation(), 45, 85)
        student211.getTranscript().addTakenCourse(course213.getCourseInformation(), 85, 75)

        student212.getTranscript().addTakenCourse(course211.getCourseInformation(), 75, 85)
        student212.getTranscript().addTakenCourse(course212.getCourseInformation(), 55, 80)

        student216.getTranscript().addTakenCourse(course211.getCourseInformation(), 70, 85)

        #Add students to the system
        self.createOrChangeStudent(student301)
        self.createOrChangeStudent(student302)
        self.createOrChangeStudent(student303)
        self.createOrChangeStudent(student304)
        self.createOrChangeStudent(student305)
        self.createOrChangeStudent(student306)

        self.createOrChangeStudent(student201)
        self.createOrChangeStudent(student202)
        self.createOrChangeStudent(student203)
        self.createOrChangeStudent(student204)
        self.createOrChangeStudent(student205)
        self.createOrChangeStudent(student206)

        self.createOrChangeStudent(student211)
        self.createOrChangeStudent(student212)
        self.createOrChangeStudent(student213)
        self.createOrChangeStudent(student214)
        self.createOrChangeStudent(student215)
        self.createOrChangeStudent(student216)

        #********************************************************* DepartmentSchedulers and Student Affairs******************************************************
        departmentScheduler301 = generateRandomDepartmentScheduler(businessDepartment)
        departmentScheduler201 = generateRandomDepartmentScheduler(biology)
        departmentScheduler211 = generateRandomDepartmentScheduler(chemistry)

        self.createOrChangeDepartmentScheduler(departmentScheduler301)
        self.createOrChangeDepartmentScheduler(departmentScheduler201)
        self.createOrChangeDepartmentScheduler(departmentScheduler211)

        studentAffairs301 = generateRandomStudentsAffairs(businessDepartment)
        studentAffairs201 = generateRandomStudentsAffairs(biology)
        studentAffairs211 = generateRandomStudentsAffairs(chemistry)

        self.createOrChangeStudentsAffairs(studentAffairs301)
        self.createOrChangeStudentsAffairs(studentAffairs201)
        self.createOrChangeStudentsAffairs(studentAffairs211)



        #berkan





        # dataManagement.createOrChangeFaculty(Engineering)
        self.createOrChangeFaculty(engineering) # surası nolcak peki

        # createOrChange öyle kullanılmıyo




        MechanicalEngineering = generateDepartment(101,"Mechanical Engineering")
        self.createOrChangeDepartment(MechanicalEngineering)



        bAdvisor = generateRandomAdvisor(MechanicalEngineering)
        self.createOrChangeAdvisor(bAdvisor)

        #yukarıdakilere bakarak yap ömerle kendim nasıl isimlendirdiysem öyle yapıyorum java koduna bakarak
        #tüm variable isimlerinin başına b_ eklersen daha iyi olur diğerleriyle karışmaz ok şuanda yanlış mı yapıyorum
        #yukarıda faculty de engineering'in e si büyüktü onların küçük olması lazım
        #variableların ismi küçük harfle başlasın ok
        bLecturer1 =generateRandomLecturer(MechanicalEngineering)
        bLecturer2 =generateRandomLecturer(MechanicalEngineering)
        bLecturer3 =generateRandomLecturer(MechanicalEngineering)
        bLecturer4 =generateRandomLecturer(MechanicalEngineering)
        bLecturer5 =generateRandomLecturer(MechanicalEngineering)

        self.createOrChangeLecturer(bLecturer1)
        self.createOrChangeLecturer(bLecturer2)
        self.createOrChangeLecturer(bLecturer3)
        self.createOrChangeLecturer(bLecturer4)
        self.createOrChangeLecturer(bLecturer5)

        lecturers_for_sections = []
        lecturers_for_sections.append(bLecturer1)
        lecturers_for_sections.append(bLecturer1)

        days =[]
        days.append(Day.Friday)
        days.append(Day.Thursday)

        section_times = []
        section_times.append(SectionTime.Fourth)
        section_times.append(SectionTime.First)

        prerequisites =[]

        bcr1 = generateClassroom("MEZ01", 60)

        clasrooms = []
        clasrooms.append(bcr1)
        clasrooms.append(bcr1)

        Thermodynamics = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Thermodynamics",
            "MATH101",
            prerequisites,
            1,
            MechanicalEngineering.get_facultyID(),
            MechanicalEngineering.getDepartmentID()
        )
        self.createOrChangeCourse(Thermodynamics)


        lecturers_for_sections = []
        lecturers_for_sections.append(bLecturer1)
        lecturers_for_sections.append(bLecturer1)


        days = []
        days.append(Day.Thursday)
        days.append(Day.Wednesday)

        section_times = []
        section_times.append(SectionTime.First)
        section_times.append(SectionTime.Third)

        bcr1 = generateClassroom("MEZ01", 60)

        clasrooms = []
        clasrooms.append(bcr1)
        clasrooms.append(bcr1)

        b_prerequisites2 = []
        MaterialScience = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Material Sci.",
            "MSE272",b_prerequisites2,
            2,
            MechanicalEngineering.get_facultyID(),
            MechanicalEngineering.getDepartmentID()
        )
        self.createOrChangeCourse(MaterialScience)


        lecturers_for_sections = []
        lecturers_for_sections.append(bLecturer3)
        lecturers_for_sections.append(bLecturer3)
        lecturers_for_sections.append(bLecturer3)


        days = []
        days.append(Day.Thursday)
        days.append(Day.Monday)
        days.append(Day.Friday)


        section_times = []
        section_times.append(SectionTime.Fourth)
        section_times.append(SectionTime.Second)
        section_times.append(SectionTime.Second)

        bcr1 = generateClassroom("MEZ01", 60)

        clasrooms = []
        clasrooms.append(bcr1)
        clasrooms.append(bcr1)

        prerequisites = []
        prerequisites.append(MaterialScience.getCourseInformation())


        StrengthOfMaterials = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Strength of Mat.",
            "ME271",
            prerequisites,
            3,
            MechanicalEngineering.get_facultyID(),
            MechanicalEngineering.getDepartmentID()
        )
        self.createOrChangeCourse(StrengthOfMaterials)


        lecturers_for_sections = []
        lecturers_for_sections.append(bLecturer4)
        lecturers_for_sections.append(bLecturer5)

        days = []
        days.append(Day.Tuesday)
        days.append(Day.Wednesday)

        section_times = []
        section_times.append(SectionTime.First)
        section_times.append(SectionTime.Third)

        prerequisites = []

        FluidMechanics = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            "Fluid Mechanics",
            "ME361",
            prerequisites,
            3,
            MechanicalEngineering.get_facultyID(),
            MechanicalEngineering.getDepartmentID()
        )

        self.createOrChangeCourse(FluidMechanics)


























        pass

    def saveToJson(self, obj):

        file_name = ""
        logger.info(f"Saving {type(obj).__name__} to JSON")
        users = ("Student", "Lecturer", "Advisor", "Admin", "DepartmentScheduler", "StudentsAffairs", "DepartmentHead")
        if type(obj).__name__ in users:
            file_name = obj.getUserInformation().get_UNIVERSITY_EMAIL()
            logger.info(f"Saving {type(obj).__name__} with university email: {file_name}")
        elif type(obj).__name__ == "Department":
            file_name = obj.getDepartmentID().getDepartmentName()
            logger.info(f"Saving {type(obj).__name__} with department name: {file_name}")
        elif type(obj).__name__ == "Faculty":
            file_name = obj.getFacultyID().getFacultyName()
            logger.info(f"Saving {type(obj).__name__} with faculty name: {file_name}")
        elif type(obj).__name__ == "Course":
            file_name = obj.getCourseName()
            logger.info(f"Saving {type(obj).__name__} with course name: {file_name}")
        elif type(obj).__name__ == "Classroom":
            file_name = obj.get_classroom_name()
            logger.info(f"Saving {type(obj).__name__} with classroom name: {file_name}")
        file_path = f"../{type(obj).__name__}s/{file_name}.json"
        self.__saveToJson(obj, file_path)

    def __saveToJson(self, obj, file_path_and_name):
        # Extract the directory path from the file path
        directory = os.path.dirname(file_path_and_name)

        # Create the directory if it doesn't exist
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"Created directory: {directory}")

        # Open the file and write JSON data
        with open(file_path_and_name, "w") as file:
            json.dump(obj, file, indent=4, cls=customEncoder)
            logger.info(f"Saved {type(obj).__name__} to JSON")

    def loadFromJson(self, file_path_and_name):
        # Extract the directory path from the file path
        if not os.path.exists(file_path_and_name):
            logger.error(f"File doesn't exist: {file_path_and_name}")
            return None

        # Open the file and read JSON data
        with open(file_path_and_name, "r") as file:
            obj = json.load(file)
            logger.info(f"Loaded {type(obj).__name__} from JSON")
            return obj
        pass

    def deleteJsonFile(self, file_path_and_name):
        # Extract the directory path from the file path
        directory = os.path.dirname(file_path_and_name)

        # Return None if the directory doesn't exist
        if directory and not os.path.exists(directory):
            logger.error(f"Directory doesn't exist: {directory}")
            return

        os.remove(file_path_and_name)
        logger.info(f"Deleted file: {file_path_and_name}")

    def getAllJsons(self, folder_path):
        allObjects = []
        if not os.path.exists(folder_path):
            logger.info(f"There is no path such {folder_path}")
            return
        logger.info(f"Getting all JSON files from {folder_path}")
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and file_path.endswith(".json"):
                allObjects.append(self.loadFromJson(file_path))

        logger.info(f"Got all JSON files from {folder_path}")
        return allObjects

    def getAllStudents(self):
        absolute_path = os.path.abspath("../Students")
        datas = self.getAllJsons(absolute_path)
        s_list = list()

        for data in datas:
            s_list.append(Student.from_dict(data))

        return s_list

    def createOrChangeStudent(self, student):
        self.saveToJson(student)

    def getStudent(self, university_email):
        data = self.loadFromJson(f"../Students/{university_email}.json")
        return Student.from_dict(data)

    def removeStudent(self, university_email):
        self.deleteJsonFile(f"../Students/{university_email}.json")

    def getAllLecturers(self):
        absolute_path = os.path.abspath("../Lecturers")
        datas = self.getAllJsons(absolute_path)

        lecturers = list()
        for data in datas:
            lecturers.append(Lecturer.from_dict(data))

        return lecturers

    def createOrChangeLecturer(self, lecturer):
        self.saveToJson(lecturer)

    def getLecturer(self, university_email):
        data = self.loadFromJson(f"../Lecturers/{university_email}.json")
        return Lecturer.from_dict(data)

    def removeLecturer(self, university_email):
        self.deleteJsonFile(f"../Lecturers/{university_email}.json")

    def getAllCourses(self):
        absolute_path = os.path.abspath("../Courses")
        datas = self.getAllJsons(absolute_path)
        c_list = list()

        for data in datas:
            c_list.append(Course.from_dict(data))

        return c_list

    def createOrChangeCourse(self, course):
        self.saveToJson(course)

    def getCourse(self, course_name):
        data = self.loadFromJson(f"../Courses/{course_name}.json")
        return Course.from_dict(data)

    def removeCourse(self, course_name):
        self.deleteJsonFile(f"../Courses/{course_name}.json")

    def getAllAdvisors(self):
        absolute_path = os.path.abspath("../Advisors")
        datas = self.getAllJsons(absolute_path)
        advisors = list()
        for data in datas:
            advisors.append(Advisor.from_dict(data))
        return advisors

    def createOrChangeAdvisor(self, advisor):
        self.saveToJson(advisor)

    def getAdvisor(self, university_email):
        data = self.loadFromJson(f"../Advisors/{university_email}.json")
        return Advisor.from_dict(data)

    def removeAdvisor(self, university_email):
        self.deleteJsonFile(f"../Advisors/{university_email}.json")

    def getAllFaculties(self):
        absolute_path = os.path.abspath("../Facultys")
        datas = self.getAllJsons(absolute_path)
        f_list = list()

        for data in datas:
            f_list.append(data)
        return f_list

    def createOrChangeFaculty(self, faculty):
        self.saveToJson(faculty)

    def getFaculty(self, faculty_name):
        data = self.loadFromJson(f"../Faculties/{faculty_name}.json")
        return Faculty.from_dict(data)

    def removeFaculty(self, faculty_name):
        self.deleteJsonFile(f"../Faculties/{faculty_name}.json")

    def getAllDepartments(self):
        absolute_path = os.path.abspath("../Departments")
        datas = self.getAllJsons(absolute_path)
        d_list = list()

        for data in datas:
            d_list.append(Department.from_dict(data))
        return d_list

    def createOrChangeDepartment(self, department):
        self.saveToJson(department)

    def getDepartment(self, department_name):
        data = self.loadFromJson(f"../Departments/{department_name}.json")
        return Department.from_dict(data)

    def removeDepartment(self, department_name):
        self.deleteJsonFile(f"../Departments/{department_name}.json")

    def getAllDepartmentHeads(self):
        absolute_path = os.path.abspath("../DepartmentHeads")
        datas = self.getAllJsons(absolute_path)
        dh_list = list()
        for data in datas:
            dh_list.append(DepartmentHead.from_dict(data))
        return dh_list

    def createOrChangeDepartmentHead(self, departmentHead):
        self.saveToJson(departmentHead)

    def getDepartmentHead(self, university_email):
        return self.loadFromJson(f"../DepartmentHeads/{university_email}.json")

    def removeDepartmentHead(self, university_email):
        self.deleteJsonFile(f"../DepartmentHeads/{university_email}.json")

    def getAllDepartmentSchedulers(self):
        absolute_path = os.path.abspath("../DepartmentSchedulers")
        datas = self.getAllJsons(absolute_path)
        dss = list()
        for data in datas:
            dss.append(DepartmentScheduler.from_dict(data))
        return dss

    def createOrChangeDepartmentScheduler(self, departmentScheduler):
        self.saveToJson(departmentScheduler)

    def getDepartmentScheduler(self, university_email):
        data = self.loadFromJson(f"../DepartmentSchedulers/{university_email}.json")
        return DepartmentScheduler.from_dict(data)

    def removeDepartmentScheduler(self, university_email):
        self.deleteJsonFile(f"../DepartmentSchedulers/{university_email}.json")

    def getAllStudentsAffairs(self):
        absolute_path = os.path.abspath("../StudentsAffairss")
        datas = self.getAllJsons(absolute_path)
        sas = list()
        for data in datas:
            sas.append(StudentsAffairs.from_dict(data))
        return sas

    def createOrChangeStudentsAffairs(self, studentsAffairs):
        self.saveToJson(studentsAffairs)

    def getStudentsAffairs(self, university_email):
        data = self.loadFromJson(f"../StudentsAffairs/{university_email}.json")
        return StudentsAffairs.from_dict(data)

    def removeStudentsAffairs(self, university_email):
        self.deleteJsonFile(f"../StudentsAffairs/{university_email}.json")

    def getAllClassrooms(self):
        absolute_path = os.path.abspath("../Classrooms")
        datas = self.getAllJsons(absolute_path)
        classrooms = list()
        for data in datas:
            classrooms.append(Classroom.from_dict(data))
        return classrooms

    def createOrChangeClassroom(self, classroom):
        self.saveToJson(classroom)

    def getClassroom(self, classroom_name):
        data = self.loadFromJson(f"../Classrooms/{classroom_name}.json")
        return Classroom.from_dict(data)

    def removeClassroom(self, classroom_name):
        self.deleteJsonFile(f"../Classrooms/{classroom_name}.json")


names = ["Ali", "Fatma", "Zeynep", "Ahmet", "Ayse", "Mehmet", "Emine", "Hasan", "Huseyin", "Elif", "Mustafa",
         "Sibel", "Burak", "Busra", "Omer", "Halime", "Murat", "Gizem", "Eren", "Esra", "Yusuf", "Melis", "Can",
         "Hatice", "Oguz", "Rabia", "Kerem", "Derya", "Furkan", "Sevgi", "Kadir", "Selin", "Ibrahim", "Tugce",
         "Cem", "Pelin", "Baris", "Leyla", "Serkan", "Sule", "Deniz", "Cansu", "Hakan", "Damla", "Merve", "Tolga",
         "Ezgi", "Volkan", "Dilara", "Uğur", "Selma", "Ece", "Adem", "Zeynep", "Burcu", "Ozan", "Cemile",
         "Yasemin", "Alper", "Duygu", "Serdar", "Gul", "Okan", "Seda", "Bora", "Nurgul", "Cagri", "Seyma",
         "Dogukan", "Gulsah", "Tuna", "Hande", "Gokhan", "Berna", "Caner", "Bahar", "Arda", "Necla", "Batuhan",
         "Hilal", "Atakan", "Tulay", "Cengiz", "Berke", "Perihan", "Ece", "Tayfun", "Ceyda", "Emirhan", "Gonca",
         "Erdem", "Ayla", "Tamer", "Isil", "Havva", "Sevda", "Gokce", "Alime"]
surnames = ["Yilmaz", "Kaya", "Demir", "Celik", "Sahin", "Arslan", "Aydin", "Eren", "Ozturk", "Yildiz", "Aslan",
            "Keskin", "Polat", "Dogan", "Koc", "Gunes", "Aksoy", "Karaca", "Uzun", "Kilic", "Tas", "Candan",
            "Erdogan", "Gul", "Yalcin", "Balci", "Kaplan", "Can", "Durmaz", "Cetin", "Turkmen", "Simsek", "Duman",
            "Sari", "Saglam", "Ucar", "Kurt", "Ozdemir", "Isik", "Ersoy", "Soylu", "Korkmaz", "Bulut", "Kavak",
            "Turan", "Altun", "Ozkan", "Kara", "Gunduz", "Ates", "Yucel", "Erdem", "Keser", "Celikkan", "Toprak",
            "Yalman", "Ari", "Bayrak", "Deniz", "Durak", "Gultekin", "Orhan", "Aktas", "Sezer", "Pala", "Karatas",
            "Aksu", "Goksel", "Bozkurt", "Yuksel", "Albayrak", "Ozen", "Seker", "Erol", "Akcay", "Ozdem", "Arman",
            "Karahan", "Tunc", "Oztan", "Batur", "Tokgoz", "Acar", "Ergin", "Ulu", "Uz", "Altay", "Soydan",
            "Koroglu", "Torun", "Akbas", "Kalayci", "Koksal", "Tuna", "Akin", "Guler", "Erkan", "Gokce"]
cities = ["Adana", "Adiyaman", "Afyonkarahisar", "Agri", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan",
          "Artvin", "Aydin", "Balikesir", "Bartin", "Batman", "Bayburt", "Bilecik", "Bingol", "Bitlis", "Bolu",
          "Burdur", "Bursa", "Canakkale", "Cankiri", "Corum", "Denizli", "Diyarbakir", "Duzce", "Edirne", "Elazig",
          "Erzincan", "Erzurum", "Eskisehir", "Gaziantep", "Giresun", "Gumushane", "Hakkari", "Hatay", "Igdir",
          "Isparta", "Istanbul", "Izmir", "Kahramanmaras", "Karabuk", "Karaman", "Kars", "Kastamonu", "Kayseri",
          "Kirikkale", "Kirklareli", "Kirsehir", "Kilis", "Kocaeli", "Konya", "Kutahya", "Malatya", "Manisa",
          "Mardin", "Mersin", "Mugla", "Mus", "Nevsehir", "Nigde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun",
          "Sanliurfa", "Siirt", "Sinop", "Sirnak", "Sivas", "Tekirdag", "Tokat", "Trabzon", "Tunceli", "Usak",
          "Van", "Yalova", "Yozgat", "Zonguldak"]


def __getRandomName():
    ___name = random.choice(names)
    logger.info(f"Getting random name: {___name}")
    return ___name


def __getRandomSurname():
    ___surname = random.choice(surnames)
    logger.info(f"Getting random surname: {___surname}")
    return ___surname


def __getRandomCity():
    ___city = random.choice(cities)
    logger.info(f"Getting random city: {___city}")
    return ___city


def __generateEmail(name, surname):
    ___email = f"{str(name).lower()}{str(surname).lower()}{random.randint(0, 100)}@gmail.com"
    logger.info(f"Generated email: {___email}")
    return ___email


def __generateUniversityEmail(name, surname):
    ___unimail = f"{str(name).lower()}{str(surname).lower()}@marun.edu.tr"
    logger.info(f"Generated university email: {___unimail}")
    return ___unimail


def __generatePhoneNumber():
    phoneNumber = f"+90 5{random.randint(0, 9)}{random.randint(0, 9)} {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)} {random.randint(0, 9)}{random.randint(0, 9)} {random.randint(0, 9)}{random.randint(0, 9)}"
    logger.info(f"Generated phone number: {phoneNumber}")
    return phoneNumber


def __generatePassword(name, city, phoneNumber):
    ___password = str(1234)
    logger.info(f"Generated password: {___password}")
    return ___password


def __generateRandomUserInformation():
    logger.info("Generating random user information")
    firstName = __getRandomName()
    lastName = __getRandomSurname()
    city = __getRandomCity()
    phoneNumber = __generatePhoneNumber()
    email = __generateEmail(firstName, lastName)
    universityEmail = __generateUniversityEmail(firstName, lastName)
    password = __generatePassword(firstName, city, phoneNumber)
    ui = UserInformation(firstName, lastName, password, universityEmail, email, city, phoneNumber)
    logger.info(
        f"Generated random user information: {firstName} {lastName} {city} {phoneNumber} {email} {universityEmail}")
    return ui


def generateFaculty(facultyID, facultyName):
    logger.info("Generating faculty")
    ___fac = Faculty(FacultyID(facultyID, facultyName))
    logger.info(f"Generated faculty: {facultyID} {facultyName}")
    return ___fac


def generateDepartment(departmentID, departmentName, faculty):
    logger.info("Generating department")
    ___dep = Department(DepartmentID(departmentID, departmentName), faculty.getFacultyID())
    faculty.addDepartment(___dep)
    logger.info(f"Generated department: {departmentID} {departmentName}")
    return ___dep


def generateRandomLecturer(department):
    logger.info("Generating random lecturer")
    userInformation = __generateRandomUserInformation()
    ___lec = Lecturer(userInformation)
    logger.info(f"Generated random lecturer: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___lec


def generateRandomAdvisor(department):
    logger.info("Generating random advisor")
    userInformation = __generateRandomUserInformation()
    ___adv = Advisor(userInformation)
    logger.info(f"Generated random advisor: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___adv


def generateRandomStudent(department, entranceDate, entranceRank, advisorID):
    logger.info("Generating random student")
    userInformation = __generateRandomUserInformation()
    studentID = StudentID(department.getDepartmentID(), entranceDate, entranceRank, department.get_facultyID())
    transcript = Transcript(studentID)
    return Student(userInformation, studentID, transcript, advisorID, 2025 - entranceDate)


def generateNonRandomStudent(userInformation, department, entrance_date, entrance_rank, advisor_id):
    logger.info("Generating non-random student")
    studentID = StudentID(department.getDepartmentID(), entrance_date, entrance_rank, department.get_facultyID())
    transcript = Transcript(studentID)
    ___stu = Student(userInformation, studentID, transcript, advisor_id, 2025 - entrance_date)
    logger.info(f"Generated non-random student: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___stu


def generateCourseInformation(courseName, courseCode):
    logger.info("Generating course information")
    ___courseInfo = CourseInformation(courseName, courseCode)
    logger.info(f"Generated course information: {courseName} {courseCode}")
    return ___courseInfo


def generateCourseRequirements(prerequisiteCourses, minimumCurrentClass, facultyID, departmentID):
    logger.info("Generating course requirements")
    ___courseReq = CourseRequirements(prerequisiteCourses, minimumCurrentClass, facultyID, departmentID)
    logger.info(f"Generated course requirements: {prerequisiteCourses} {minimumCurrentClass}")
    return ___courseReq


def generateCourse(lecturerForSections, days, sectionTimes, classRooms, courseName, courseCode, prerequisiteCourses,
                   minimumCurrentClass, facultyID, departmentID):
    logger.info("Generating course")
    ___courseInfo = generateCourseInformation(courseName, courseCode)
    ___courseReq = generateCourseRequirements(prerequisiteCourses, minimumCurrentClass, facultyID, departmentID)
    courseSections = list()
    for i in range(len(lecturerForSections)):
        ___courseSec = CourseSection(days[i], sectionTimes[i], lecturerForSections[i], classRooms[i])
        courseSections.append(___courseSec)
    ___course = Course(___courseInfo, ___courseReq, courseSections)
    logger.info(f"Generated course: {courseName} {courseCode}")
    return ___course


def generateRandomDepartmentScheduler(department):
    logger.info("Generating random department scheduler")
    userInformation = __generateRandomUserInformation()
    ___depSched = DepartmentScheduler(userInformation)
    logger.info(
        f"Generated random department scheduler: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___depSched


def generateRandomDepartmentHead(department):
    logger.info("Generating random department head")
    userInformation = __generateRandomUserInformation()
    ___depHead = DepartmentHead(userInformation)
    logger.info(
        f"Generated random department head: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___depHead


def generateRandomStudentsAffairs(department):
    logger.info("Generating random students affairs")
    userInformation = __generateRandomUserInformation()
    ___stuAff = StudentsAffairs(userInformation)
    logger.info(
        f"Generated random students affairs: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___stuAff


def generateClassroom(classroomName, capacity):
    logger.info("Generating classroom")
    ___classroom = Classroom(classroomName, capacity)
    logger.info(f"Generated classroom: {classroomName} {capacity}")
    return ___classroom


class customEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

dm = DataManagement()
# fac = generateFaculty(15,"eng")
# dm.createOrChangeFaculty(fac)
#
# dep = generateDepartment(150, "comp eng",fac )
# dm.createOrChangeDepartment(dep)
#
# ad = generateRandomAdvisor(dep)
#
# dm.createOrChangeAdvisor(ad)
#
# stu = generateRandomStudent(dep,2022,1,ad.get_staffId())
# dm.createOrChangeStudent(stu)
#
# lec = generateRandomLecturer(dep)
# dm.createOrChangeLecturer(lec)
#
# sa = generateRandomStudentsAffairs(dep)
# dm.createOrChangeStudentsAffairs(sa)
#
# dsch = generateRandomDepartmentScheduler(dep)
# dm.createOrChangeDepartmentScheduler(dsch)
#
# dh = generateRandomDepartmentHead(dep)
# dm.createOrChangeDepartmentHead(dh)
#
# cr = generateClassroom("aa",20)
# dm.createOrChangeClassroom(cr)
#
# course = generateCourse([lec], [Day.Friday], [SectionTime.Fifth], [cr], "test", "TT101", list(), 1, dep.get_facultyID(), dep.getDepartmentID())
# dm.createOrChangeCourse(course)
#
# course1 = generateCourse([lec], [Day.Friday], [SectionTime.Fifth], [cr], "test2", "TT102", list(), 1, dep.get_facultyID(), dep.getDepartmentID())
# dm.createOrChangeCourse(course1)

# Yusuf
# **************************************************** Faculties ****************************************************
# new Faculty "Business"
Business = generateFaculty(3, "Business")
dm.createOrChangeFaculty(Business)
# new Faculty "Science"
Science = generateFaculty(2, "Science")
dm.createOrChangeFaculty(Science)

#**************************************************** Departments ****************************************************
# new Department "Business" in Faculty "Business"
BusinessDepartment = generateDepartment(301, "Business", Business)
dm.createOrChangeDepartment(BusinessDepartment)
# New Department "Biology" in Faculty "Science"
Biology = generateDepartment(201, "Biology", Science)
dm.createOrChangeDepartment(Biology)
# New Department "Chemistry" in Faculty "Science"
Chemistry = generateDepartment(202, "Chemistry", Science)
dm.createOrChangeDepartment(Chemistry)

#**************************************************** Advisors and Lecturers ****************************************************
# new Advisors and Lecturers for Business Department
advisor301 = generateRandomAdvisor(BusinessDepartment)


