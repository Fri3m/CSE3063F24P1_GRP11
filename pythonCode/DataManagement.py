import json
import os
import random
from json import JSONEncoder

from Classroom import Classroom
from Course import CourseInformation, CourseRequirements, CourseSection, Course, TakenCourse
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

        o_course1 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr, o_cr, o_cr1],
                                   "Introduction to Computer Engineering", "CS1200", list(), 1,
                                   computerEngineering.get_facultyID(), computerEngineering.getDepartmentID())
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

        o_course2 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr, o_cr, o_cr3],
                                   "Introduction to Algorithms", "CS1201", list(), 1,
                                   computerEngineering.get_facultyID(), computerEngineering.getDepartmentID())
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

        o_course3 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr1, o_cr3],
                                   "Linear Algebra for Computer Engineering", "MATH256", list(), 1,
                                   computerEngineering.get_facultyID(), computerEngineering.getDepartmentID())
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

        o_course4 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr, o_cr, o_cr4], "Data Structures",
                                   "CS2225", prerequisites, 2, computerEngineering.get_facultyID(),
                                   computerEngineering.getDepartmentID())
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

        o_course5 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr1, o_cr3], "Differential Equations",
                                   "MATH205", list(), 2, computerEngineering.get_facultyID(),
                                   computerEngineering.getDepartmentID())
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

        o_course6 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr5, o_cr5, o_cr4],
                                   "Systems Programming", "CS2138", list(), 2, computerEngineering.get_facultyID(),
                                   computerEngineering.getDepartmentID())
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

        o_course7 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr6, o_cr6, o_cr6], "Database Systems",
                                   "CS3125", prerequisites1, 3, computerEngineering.get_facultyID(),
                                   computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course7)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer6)
        lecturersForSections.append(lecturer6)
        lecturersForSections.append(lecturer6)
        days.clear()
        days.append(Day.Tuesday)
        days.append(Day.Wednesday)
        days.append(Day.Wednesday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Seventh)
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Third)

        prerequisites2 = []
        prerequisites2.append(o_course7.getCourseInformation())

        o_course8 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr6, o_cr5, o_cr5],
                                   "Software Engineering", "CS3044", prerequisites2, 3,
                                   computerEngineering.get_facultyID(), computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course8)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer)
        lecturersForSections.append(lecturer)
        days.clear()
        days.append(Day.Thursday)
        days.append(Day.Friday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.Fifth)

        o_course9 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr, o_cr1], "Digital Logic Design",
                                   "CS3215", list(), 3, computerEngineering.get_facultyID(),
                                   computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course9)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer7)
        lecturersForSections.append(lecturer7)
        lecturersForSections.append(lecturer7)
        days.clear()
        days.append(Day.Monday)
        days.append(Day.Wednesday)
        days.append(Day.Wednesday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.First)
        sectionTimes.append(SectionTime.First)
        sectionTimes.append(SectionTime.Second)

        o_cr7 = generateClassroom("CS17", 60)
        self.createOrChangeClassroom(o_cr7)

        o_course10 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr7, o_cr7, o_cr7],
                                    "Computer Networks", "CS4074", list(), 4, computerEngineering.get_facultyID(),
                                    computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course10)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer6)
        lecturersForSections.append(lecturer6)
        lecturersForSections.append(lecturer6)
        days.clear()
        days.append(Day.Tuesday)
        days.append(Day.Friday)
        days.append(Day.Friday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Third)
        sectionTimes.append(SectionTime.First)
        sectionTimes.append(SectionTime.Second)

        prerequisites3 = []
        prerequisites3.append(o_course3.getCourseInformation())

        o_cr8 = generateClassroom("CS18", 70)
        self.createOrChangeClassroom(o_cr8)

        o_course11 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr7, o_cr8, o_cr8],
                                    "Introduction to Machine Learning", "CS4288", prerequisites3, 4,
                                    computerEngineering.get_facultyID(), computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course11)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer7)
        lecturersForSections.append(lecturer7)
        days.clear()
        days.append(Day.Thursday)
        days.append(Day.Thursday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Fifth)
        sectionTimes.append(SectionTime.Sixth)

        o_course12 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr8, o_cr8], "Cloud Computing",
                                    "CS4012", list(), 4, computerEngineering.get_facultyID(),
                                    computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course12)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer8)
        lecturersForSections.append(lecturer8)
        days.clear()
        days.append(Day.Wednesday)
        days.append(Day.Friday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Fifth)
        sectionTimes.append(SectionTime.Sixth)

        o_course13 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr5, o_cr5], "Mechatronics", "ME3022",
                                    list(), 4, computerEngineering.get_facultyID(),
                                    computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course13)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer9)
        lecturersForSections.append(lecturer9)
        days.clear()
        days.append(Day.Monday)
        days.append(Day.Monday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Third)

        o_course14 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr3, o_cr3],
                                    "Planning and Management of Research", "BIOE4072", list(), 4,
                                    computerEngineering.get_facultyID(), computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course14)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer10)
        lecturersForSections.append(lecturer10)
        days.clear()
        days.append(Day.Tuesday)
        days.append(Day.Tuesday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Fifth)
        sectionTimes.append(SectionTime.Sixth)

        o_cr9 = generateClassroom("CS19", 40)
        self.createOrChangeClassroom(o_cr9)

        o_course15 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr9, o_cr9], "Financial Engineering",
                                    "CHE4068", list(), 4, computerEngineering.get_facultyID(),
                                    computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course15)

        lecturersForSections.clear()
        lecturersForSections.append(lecturer11)
        lecturersForSections.append(lecturer11)
        days.clear()
        days.append(Day.Tuesday)
        days.append(Day.Thursday)
        sectionTimes.clear()
        sectionTimes.append(SectionTime.Second)
        sectionTimes.append(SectionTime.Fourth)

        o_course16 = generateCourse(lecturersForSections, days, sectionTimes, [o_cr9, o_cr9],
                                    "Introduction to Image Processing", "EE4062", list(), 4,
                                    computerEngineering.get_facultyID(), computerEngineering.getDepartmentID())
        self.createOrChangeCourse(o_course16)

        o_st1 = generateRandomStudent(computerEngineering, 2021, 3, advisor.get_staffId())
        o_st2 = generateRandomStudent(computerEngineering, 2021, 70, advisor.get_staffId())
        o_st3 = generateRandomStudent(computerEngineering, 2022, 15, advisor.get_staffId())
        o_st4 = generateRandomStudent(computerEngineering, 2022, 32, advisor.get_staffId())
        o_st5 = generateRandomStudent(computerEngineering, 2023, 25, advisor.get_staffId())
        o_st6 = generateRandomStudent(computerEngineering, 2023, 23, advisor.get_staffId())
        o_st7 = generateRandomStudent(computerEngineering, 2024, 60, advisor.get_staffId())
        o_st8 = generateRandomStudent(computerEngineering, 2024, 45, advisor.get_staffId())

        self.createOrChangeStudent(o_st1)
        self.createOrChangeStudent(o_st2)
        self.createOrChangeStudent(o_st3)
        self.createOrChangeStudent(o_st4)

        takenCourse = TakenCourse(o_course1.getCourseInformation(), 90, 54)
        takenCourse1 = TakenCourse(o_course2.getCourseInformation(), 70, 35)
        takenCourse2 = TakenCourse(o_course3.getCourseInformation(), 20, 100)
        takenCourse3 = TakenCourse(o_course4.getCourseInformation(), 85, 50)
        takenCourse4 = TakenCourse(o_course5.getCourseInformation(), 75, 40)
        takenCourse5 = TakenCourse(o_course6.getCourseInformation(), 95, 55)
        takenCourse6 = TakenCourse(o_course7.getCourseInformation(), 90, 50)
        takenCourse7 = TakenCourse(o_course8.getCourseInformation(), 85, 45)
        takenCourse8 = TakenCourse(o_course9.getCourseInformation(), 30, 90)

        o_st1.getTranscript().addTakenCourse(takenCourse)
        o_st1.getTranscript().addTakenCourse(takenCourse1)
        o_st1.getTranscript().addTakenCourse(takenCourse2)
        o_st1.getTranscript().addTakenCourse(takenCourse3)
        o_st1.getTranscript().addTakenCourse(takenCourse4)
        o_st1.getTranscript().addTakenCourse(takenCourse5)
        o_st1.getTranscript().addTakenCourse(takenCourse6)
        o_st1.getTranscript().addTakenCourse(takenCourse7)
        o_st1.getTranscript().addTakenCourse(takenCourse8)
        self.createOrChangeStudent(o_st1)

        takenCourse9 = TakenCourse(o_course1.getCourseInformation(), 50, 50)
        takenCourse10 = TakenCourse(o_course2.getCourseInformation(), 70, 70)
        takenCourse11 = TakenCourse(o_course3.getCourseInformation(), 100, 65)
        takenCourse12 = TakenCourse(o_course4.getCourseInformation(), 85, 50)
        takenCourse13 = TakenCourse(o_course5.getCourseInformation(), 75, 40)
        takenCourse14 = TakenCourse(o_course6.getCourseInformation(), 50, 80)
        takenCourse15 = TakenCourse(o_course7.getCourseInformation(), 40, 80)
        takenCourse17 = TakenCourse(o_course9.getCourseInformation(), 60, 85)

        o_st2.getTranscript().addTakenCourse(takenCourse9)
        o_st2.getTranscript().addTakenCourse(takenCourse10)
        o_st2.getTranscript().addTakenCourse(takenCourse11)
        o_st2.getTranscript().addTakenCourse(takenCourse12)
        o_st2.getTranscript().addTakenCourse(takenCourse13)
        o_st2.getTranscript().addTakenCourse(takenCourse14)
        o_st2.getTranscript().addTakenCourse(takenCourse15)
        o_st2.getTranscript().addTakenCourse(takenCourse17)
        self.createOrChangeStudent(o_st2)

        takenCourse18 = TakenCourse(o_course1.getCourseInformation(), 100, 95)
        takenCourse19 = TakenCourse(o_course2.getCourseInformation(), 97, 93)
        takenCourse20 = TakenCourse(o_course3.getCourseInformation(), 55, 65)
        takenCourse22 = TakenCourse(o_course5.getCourseInformation(), 75, 40)
        takenCourse23 = TakenCourse(o_course6.getCourseInformation(), 67, 50)

        o_st3.getTranscript().addTakenCourse(takenCourse18)
        o_st3.getTranscript().addTakenCourse(takenCourse19)
        o_st3.getTranscript().addTakenCourse(takenCourse20)
        o_st3.getTranscript().addTakenCourse(takenCourse22)
        o_st3.getTranscript().addTakenCourse(takenCourse23)
        self.createOrChangeStudent(o_st3)

        takenCourse24 = TakenCourse(o_course1.getCourseInformation(), 70, 95)
        takenCourse25 = TakenCourse(o_course2.getCourseInformation(), 90, 60)
        takenCourse26 = TakenCourse(o_course3.getCourseInformation(), 60, 70)
        takenCourse27 = TakenCourse(o_course4.getCourseInformation(), 90, 40)
        takenCourse28 = TakenCourse(o_course5.getCourseInformation(), 85, 50)
        takenCourse29 = TakenCourse(o_course6.getCourseInformation(), 55, 75)

        o_st4.getTranscript().addTakenCourse(takenCourse24)
        o_st4.getTranscript().addTakenCourse(takenCourse25)
        o_st4.getTranscript().addTakenCourse(takenCourse26)
        o_st4.getTranscript().addTakenCourse(takenCourse27)
        o_st4.getTranscript().addTakenCourse(takenCourse28)
        o_st4.getTranscript().addTakenCourse(takenCourse29)
        self.createOrChangeStudent(o_st4)

        takenCourse30 = TakenCourse(o_course1.getCourseInformation(), 90, 65)
        takenCourse31 = TakenCourse(o_course2.getCourseInformation(), 75, 50)
        takenCourse32 = TakenCourse(o_course3.getCourseInformation(), 50, 85)

        o_st5.getTranscript().addTakenCourse(takenCourse30)
        o_st5.getTranscript().addTakenCourse(takenCourse31)
        o_st5.getTranscript().addTakenCourse(takenCourse32)
        self.createOrChangeStudent(o_st5)

        takenCourse33 = TakenCourse(o_course1.getCourseInformation(), 50, 85)
        takenCourse34 = TakenCourse(o_course2.getCourseInformation(), 90, 55)
        takenCourse35 = TakenCourse(o_course3.getCourseInformation(), 90, 70)

        o_st6.getTranscript().addTakenCourse(takenCourse33)
        o_st6.getTranscript().addTakenCourse(takenCourse34)
        o_st6.getTranscript().addTakenCourse(takenCourse35)
        self.createOrChangeStudent(o_st6)

        self.createOrChangeStudent(o_st7)
        self.createOrChangeStudent(o_st8)

        departmentScheduler = generateRandomDepartmentScheduler(computerEngineering)
        self.createOrChangeDepartmentScheduler(departmentScheduler)

        departmentHead = generateRandomDepartmentHead(computerEngineering)
        self.createOrChangeDepartmentHead(departmentHead)

        studentsAffairs = generateRandomStudentsAffairs(computerEngineering)
        self.createOrChangeStudentsAffairs(studentsAffairs)

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
        lecturersForSections = []
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
        lecturersForSections.clear()
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
        lecturersForSections.clear()
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
        lecturersForSections.clear()
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
        lecturersForSections.clear()
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
        lecturersForSections.clear()
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
        lecturersForSections.clear()
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
        lecturersForSections.clear()
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
        lecturersForSections.clear()
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
        lecturersForSections.clear()
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
        lecturersForSections.clear()
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

        student301.getTranscript().addTakenCourse(TakenCourse(course301.getCourseInformation(), 90, 54))
        student301.getTranscript().addTakenCourse(TakenCourse(course301.getCourseInformation(), 80, 65))
        student301.getTranscript().addTakenCourse(TakenCourse(course301.getCourseInformation(), 70, 75))

        student303.getTranscript().addTakenCourse(TakenCourse(course301.getCourseInformation(), 90, 64))

        student304.getTranscript().addTakenCourse(TakenCourse(course301.getCourseInformation(), 93, 74))
        student304.getTranscript().addTakenCourse(TakenCourse(course301.getCourseInformation(), 85, 65))

        student305.getTranscript().addTakenCourse(TakenCourse(course301.getCourseInformation(), 75, 70))
        student305.getTranscript().addTakenCourse(TakenCourse(course301.getCourseInformation(), 65, 85))
        student305.getTranscript().addTakenCourse(TakenCourse(course301.getCourseInformation(), 75, 75))

        student306.getTranscript().addTakenCourse(TakenCourse(course301.getCourseInformation(), 85, 75))

        student306.getTranscript().addTakenCourse(TakenCourse(course301.getCourseInformation(), 85, 75))

        student201.getTranscript().addTakenCourse(TakenCourse(course201.getCourseInformation(), 85, 75))
        student201.getTranscript().addTakenCourse(TakenCourse(course202.getCourseInformation(), 90, 85))

        student202.getTranscript().addTakenCourse(TakenCourse(course201.getCourseInformation(), 68, 75))
        student202.getTranscript().addTakenCourse(TakenCourse(course202.getCourseInformation(), 88, 72))

        student204.getTranscript().addTakenCourse(TakenCourse(course201.getCourseInformation(), 65, 85))
        student204.getTranscript().addTakenCourse(TakenCourse(course202.getCourseInformation(), 75, 850))
        student204.getTranscript().addTakenCourse(TakenCourse(course203.getCourseInformation(), 55, 10))

        student205.getTranscript().addTakenCourse(TakenCourse(course201.getCourseInformation(), 75, 85))

        student211.getTranscript().addTakenCourse(TakenCourse(course211.getCourseInformation(), 38, 90))
        student211.getTranscript().addTakenCourse(TakenCourse(course212.getCourseInformation(), 45, 85))
        student211.getTranscript().addTakenCourse(TakenCourse(course213.getCourseInformation(), 85, 75))

        student212.getTranscript().addTakenCourse(TakenCourse(course211.getCourseInformation(), 75, 85))
        student212.getTranscript().addTakenCourse(TakenCourse(course212.getCourseInformation(), 55, 80))

        student216.getTranscript().addTakenCourse(TakenCourse(course211.getCourseInformation(), 70, 85))

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




        MechanicalEngineering = generateDepartment(101,"Mechanical Engineering",engineering)
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

        clasrooms.clear()
        clasrooms.append(bcr1)
        clasrooms.append(bcr1)

        prerequisites = []

        FluidMechanics = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Fluid Mechanics",
            "ME361",
            prerequisites,
            3,
            MechanicalEngineering.get_facultyID(),
            MechanicalEngineering.getDepartmentID()
        )

        self.createOrChangeCourse(FluidMechanics)
        #berkan

        self.createOrChangeFaculty(engineering)

        MechanicalEngineering = generateDepartment(101, "Mechanical Engineering",engineering)
        self.createOrChangeDepartment(MechanicalEngineering)

        bAdvisor = generateRandomAdvisor(MechanicalEngineering)
        self.createOrChangeAdvisor(bAdvisor)

        bLecturer1 = generateRandomLecturer(MechanicalEngineering)
        bLecturer2 = generateRandomLecturer(MechanicalEngineering)
        bLecturer3 = generateRandomLecturer(MechanicalEngineering)
        bLecturer4 = generateRandomLecturer(MechanicalEngineering)
        bLecturer5 = generateRandomLecturer(MechanicalEngineering)

        self.createOrChangeLecturer(bLecturer1)
        self.createOrChangeLecturer(bLecturer2)
        self.createOrChangeLecturer(bLecturer3)
        self.createOrChangeLecturer(bLecturer4)
        self.createOrChangeLecturer(bLecturer5)

        lecturers_for_sections = []
        lecturers_for_sections.append(bLecturer1)
        lecturers_for_sections.append(bLecturer1)

        days = []
        days.append(Day.Friday)
        days.append(Day.Thursday)

        section_times = []
        section_times.append(SectionTime.Fourth)
        section_times.append(SectionTime.First)

        prerequisites = []

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

        bcr2 = generateClassroom("MEZ02", 60)

        clasrooms = []
        clasrooms.append(bcr2)
        clasrooms.append(bcr2)

        b_prerequisites2 = []
        MaterialScience = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Material Sci.",
            "MSE272", b_prerequisites2,
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

        bcr3 = generateClassroom("MEZ02", 60)

        clasrooms = []
        clasrooms.append(bcr3)
        clasrooms.append(bcr3)
        clasrooms.append(bcr3)

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

        bcr4 = generateClassroom("MEZ01", 60)

        clasrooms = []
        clasrooms.append(bcr4)
        clasrooms.append(bcr4)

        prerequisites = []

        FluidMechanics = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Fluid Mechanics",
            "ME361",
            prerequisites,
            3,
            MechanicalEngineering.get_facultyID(),
            MechanicalEngineering.getDepartmentID()
        )

        self.createOrChangeCourse(FluidMechanics)

        lecturers_for_sections = []
        lecturers_for_sections.append(bLecturer5)
        lecturers_for_sections.append(bLecturer5)
        lecturers_for_sections.append(bLecturer1)

        days = []
        days.append(Day.Thursday)
        days.append(Day.Monday)
        days.append(Day.Tuesday)

        section_times = []
        section_times.append(SectionTime.Second)
        section_times.append(SectionTime.Second)
        section_times.append(SectionTime.Fourth)

        bcr5 = generateClassroom("MEZ03", 60)

        clasrooms = []
        clasrooms.append(bcr5)
        clasrooms.append(bcr5)
        clasrooms.append(bcr5)

        prerequisites = []

        HeatTransfer = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Heat Transfer",
            "ME471",
            prerequisites,
            4,
            MechanicalEngineering.get_facultyID(),
            MechanicalEngineering.getDepartmentID()
        )

        self.createOrChangeCourse(HeatTransfer)

        bStudent2021_2 = generateRandomStudent(MechanicalEngineering, 2021, 4, bAdvisor.get_staffId())
        bStudent2021_2.getTranscript().addTakenCourse(TakenCourse(Thermodynamics.getCourseInformation(), 90, 85))
        bStudent2021_2.getTranscript().addTakenCourse(TakenCourse(MaterialScience.getCourseInformation(), 88, 72))
        bStudent2021_2.getTranscript().addTakenCourse(TakenCourse(StrengthOfMaterials.getCourseInformation(), 75, 85))
        bStudent2021_2.getTranscript().addTakenCourse(TakenCourse(FluidMechanics.getCourseInformation(), 55, 100))
        self.createOrChangeStudent(bStudent2021_2)

        bStudent2022_1 = generateRandomStudent(MechanicalEngineering, 2022, 3, bAdvisor.get_staffId())
        bStudent2022_1.getTranscript().addTakenCourse(TakenCourse(Thermodynamics.getCourseInformation(), 67, 80))
        bStudent2022_1.getTranscript().addTakenCourse(TakenCourse(MaterialScience.getCourseInformation(), 74, 69))
        self.createOrChangeStudent(bStudent2022_1)

        bStudent2023_2 = generateRandomStudent(MechanicalEngineering, 2023, 2, bAdvisor.get_staffId())
        self.createOrChangeStudent(bStudent2023_2)
        bStudent2022_1.getTranscript().addTakenCourse(TakenCourse(Thermodynamics.getCourseInformation(), 31, 90))

        bStudent2024_2 = generateRandomStudent(MechanicalEngineering, 2024, 1, bAdvisor.get_staffId())
        self.createOrChangeStudent(bStudent2024_2)
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #

        IndustrialEngineering = generateDepartment(101, "Industrial Engineering", engineering)
        self.createOrChangeDepartment(IndustrialEngineering)

        ieLecturer1 = generateRandomLecturer(IndustrialEngineering)
        self.createOrChangeLecturer(ieLecturer1)

        ieLecturer2 = generateRandomLecturer(IndustrialEngineering)
        self.createOrChangeLecturer(ieLecturer2)

        ieLecturer3 = generateRandomLecturer(IndustrialEngineering)
        self.createOrChangeLecturer(ieLecturer3)

        ieLecturer4 = generateRandomLecturer(IndustrialEngineering)
        self.createOrChangeLecturer(ieLecturer4)

        bbAdvisor = generateRandomAdvisor(IndustrialEngineering)
        self.createOrChangeAdvisor(bbAdvisor)

        lecturers_for_sections = []
        lecturers_for_sections.append(ieLecturer1)
        lecturers_for_sections.append(ieLecturer1)
        lecturers_for_sections.append(ieLecturer1)

        days = []
        days.append(Day.Wednesday)
        days.append(Day.Monday)
        days.append(Day.Friday)

        section_times = []
        section_times.append(SectionTime.Third)
        section_times.append(SectionTime.Fourth)
        section_times.append(SectionTime.Fourth)

        bcr6 = generateClassroom("IEZ01", 60)

        clasrooms = []
        clasrooms.append(bcr6)
        clasrooms.append(bcr6)
        clasrooms.append(bcr6)

        prerequisites = []

        OperationsResearch = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Operations Research",
            "IE3003",
            prerequisites,
            3,
            IndustrialEngineering.get_facultyID(),
            IndustrialEngineering.getDepartmentID()
        )

        self.createOrChangeCourse(OperationsResearch)

        lecturers_for_sections = []
        lecturers_for_sections.append(ieLecturer2)
        lecturers_for_sections.append(ieLecturer2)
        lecturers_for_sections.append(ieLecturer4)

        days = []
        days.append(Day.Wednesday)
        days.append(Day.Friday)
        days.append(Day.Monday)

        section_times = []
        section_times.append(SectionTime.First)
        section_times.append(SectionTime.Second)
        section_times.append(SectionTime.Third)

        bcr7 = generateClassroom("IEZ02", 60)

        clasrooms = []
        clasrooms.append(bcr7)
        clasrooms.append(bcr7)
        clasrooms.append(bcr7)

        prerequisites = []

        Probability = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Probability",
            "IE2151",
            prerequisites,
            2,
            IndustrialEngineering.get_facultyID(),
            IndustrialEngineering.getDepartmentID()
        )

        self.createOrChangeCourse(Probability)

        lecturers_for_sections = []
        lecturers_for_sections.append(ieLecturer3)
        lecturers_for_sections.append(ieLecturer3)
        lecturers_for_sections.append(ieLecturer3)

        days = []
        days.append(Day.Wednesday)
        days.append(Day.Monday)
        days.append(Day.Tuesday)

        section_times = []
        section_times.append(SectionTime.Fourth)
        section_times.append(SectionTime.Fourth)
        section_times.append(SectionTime.Third)

        bcr8 = generateClassroom("IEZ03", 60)

        clasrooms = []
        clasrooms.append(bcr8)
        clasrooms.append(bcr8)
        clasrooms.append(bcr8)

        prerequisites = []
        prerequisites.append(Probability.getCourseInformation())

        Simulation = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Simulation",
            "IE3064",
            prerequisites,
            3,
            IndustrialEngineering.get_facultyID(),
            IndustrialEngineering.getDepartmentID()
        )

        self.createOrChangeCourse(Simulation)

        lecturers_for_sections = []
        lecturers_for_sections.append(ieLecturer4)
        lecturers_for_sections.append(ieLecturer4)

        days = []
        days.append(Day.Friday)
        days.append(Day.Wednesday)

        section_times = []
        section_times.append(SectionTime.Third)
        section_times.append(SectionTime.Third)

        bcr9 = generateClassroom("IEZ02", 60)

        clasrooms = []
        clasrooms.append(bcr9)
        clasrooms.append(bcr9)

        prerequisites = []

        TurkishLanguage = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Turkish Language",
            "TRD121",
            prerequisites,
            1,
            IndustrialEngineering.get_facultyID(),
            IndustrialEngineering.getDepartmentID()
        )

        self.createOrChangeCourse(TurkishLanguage)

        ieStudent2021_1 = generateRandomStudent(IndustrialEngineering, 2021, 101,
                                                bbAdvisor.get_staffId())
        ieStudent2021_1.getTranscript().addTakenCourse(TakenCourse(OperationsResearch.getCourseInformation(), 90, 85))
        ieStudent2021_1.getTranscript().addTakenCourse(TakenCourse(Probability.getCourseInformation(), 88, 72))
        ieStudent2021_1.getTranscript().addTakenCourse(TakenCourse(Simulation.getCourseInformation(), 75, 85))
        ieStudent2021_1.getTranscript().addTakenCourse(TakenCourse(TurkishLanguage.getCourseInformation(), 55, 100))
        self.createOrChangeStudent(ieStudent2021_1)

        ieStudent2022_2 = generateRandomStudent(IndustrialEngineering, 2022, 47, bbAdvisor.get_staffId())
        ieStudent2022_2.getTranscript().addTakenCourse(TakenCourse(OperationsResearch.getCourseInformation(), 67, 80))
        ieStudent2022_2.getTranscript().addTakenCourse(TakenCourse(Probability.getCourseInformation(), 74, 69))
        self.createOrChangeStudent(ieStudent2022_2)

        ieStudent2023_1 = generateRandomStudent(IndustrialEngineering, 2023, 33, bbAdvisor.get_staffId())
        ieStudent2023_1.getTranscript().addTakenCourse(TakenCourse(OperationsResearch.getCourseInformation(), 31, 90))
        self.createOrChangeStudent(ieStudent2023_1)

        ieStudent2024_1 = generateRandomStudent(IndustrialEngineering, 2024, 26, bbAdvisor.get_staffId())
        self.createOrChangeStudent(ieStudent2024_1)
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #

        ElectricalEngineering = generateDepartment(101, "Electrical Engineering", engineering)
        self.createOrChangeDepartment(ElectricalEngineering)

        eeLecturer1 = generateRandomLecturer(ElectricalEngineering)
        self.createOrChangeLecturer(eeLecturer1)

        eeLecturer2 = generateRandomLecturer(ElectricalEngineering)
        self.createOrChangeLecturer(eeLecturer2)

        bbbAdvisor = generateRandomAdvisor(ElectricalEngineering)
        self.createOrChangeAdvisor(bbbAdvisor)

        lecturers_for_sections = []
        lecturers_for_sections.append(eeLecturer1)
        lecturers_for_sections.append(eeLecturer1)
        lecturers_for_sections.append(eeLecturer1)

        days = []
        days.append(Day.Friday)
        days.append(Day.Tuesday)
        days.append(Day.Thursday)

        section_times = []
        section_times.append(SectionTime.Second)
        section_times.append(SectionTime.Second)
        section_times.append(SectionTime.Fourth)

        bcr10 = generateClassroom("EEZ01", 60)

        clasrooms = []
        clasrooms.append(bcr10)
        clasrooms.append(bcr10)
        clasrooms.append(bcr10)

        prerequisites = []

        PhysicsI = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Physics I",
            "PHYS1101",
            prerequisites,
            1,
            ElectricalEngineering.get_facultyID(),
            ElectricalEngineering.getDepartmentID()
        )

        self.createOrChangeCourse(PhysicsI)

        lecturers_for_sections = []
        lecturers_for_sections.append(eeLecturer2)
        lecturers_for_sections.append(eeLecturer2)

        days = []
        days.append(Day.Wednesday)
        days.append(Day.Thursday)

        section_times = []
        section_times.append(SectionTime.Fourth)
        section_times.append(SectionTime.Second)

        bcr11 = generateClassroom("EEZ02", 60)

        clasrooms = []
        clasrooms.append(bcr11)
        clasrooms.append(bcr11)

        prerequisites = []

        DigitalDesign = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Digital Design",
            "EE2003",
            prerequisites,
            2,
            ElectricalEngineering.get_facultyID(),
            ElectricalEngineering.getDepartmentID()
        )

        self.createOrChangeCourse(DigitalDesign)

        lecturers_for_sections = []
        lecturers_for_sections.append(eeLecturer1)
        lecturers_for_sections.append(eeLecturer1)

        days = []
        days.append(Day.Thursday)
        days.append(Day.Monday)

        section_times = []
        section_times.append(SectionTime.Third)
        section_times.append(SectionTime.Third)

        bcr12 = generateClassroom("EEZ01", 60)

        clasrooms = []
        clasrooms.append(bcr12)
        clasrooms.append(bcr12)

        prerequisites = []

        CommunicationSystems = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Communication Systems",
            "EE3082",
            prerequisites,
            3,
            ElectricalEngineering.get_facultyID(),
            ElectricalEngineering.getDepartmentID()
        )

        self.createOrChangeCourse(CommunicationSystems)

        lecturers_for_sections = []
        lecturers_for_sections.append(eeLecturer2)
        lecturers_for_sections.append(eeLecturer1)

        days = []
        days.append(Day.Wednesday)
        days.append(Day.Friday)

        section_times = []
        section_times.append(SectionTime.Third)
        section_times.append(SectionTime.Third)

        bcr13 = generateClassroom("EEZ01", 60)

        clasrooms = []
        clasrooms.append(bcr13)
        clasrooms.append(bcr13)

        prerequisites = []
        prerequisites.append(DigitalDesign.getCourseInformation())

        ElectromagneticWaves = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Electromagnetic Waves",
            "EE4051",
            prerequisites,
            4,
            ElectricalEngineering.get_facultyID(),
            ElectricalEngineering.getDepartmentID()
        )

        self.createOrChangeCourse(ElectromagneticWaves)

        lecturers_for_sections = []
        lecturers_for_sections.append(eeLecturer1)
        lecturers_for_sections.append(eeLecturer1)

        days = []
        days.append(Day.Wednesday)
        days.append(Day.Tuesday)

        section_times = []
        section_times.append(SectionTime.Seventh)
        section_times.append(SectionTime.Ninth)

        bcr14 = generateClassroom("EEZ01", 60)

        clasrooms = []
        clasrooms.append(bcr14)
        clasrooms.append(bcr14)

        prerequisites = []

        SignalsAndSystems = generateCourse(
            lecturers_for_sections,
            days,
            section_times,
            clasrooms,
            "Signals and Systems",
            "EE3061",
            prerequisites,
            3,
            ElectricalEngineering.get_facultyID(),
            ElectricalEngineering.getDepartmentID()
        )

        self.createOrChangeCourse(SignalsAndSystems)

        eeStudent2021 = generateRandomStudent(ElectricalEngineering, 2021, 4, bbbAdvisor.get_staffId())
        eeStudent2021.getTranscript().addTakenCourse(TakenCourse(PhysicsI.getCourseInformation(), 90, 85))
        eeStudent2021.getTranscript().addTakenCourse(TakenCourse(DigitalDesign.getCourseInformation(), 88, 72))
        eeStudent2021.getTranscript().addTakenCourse(TakenCourse(CommunicationSystems.getCourseInformation(), 75, 85))
        eeStudent2021.getTranscript().addTakenCourse(TakenCourse(SignalsAndSystems.getCourseInformation(), 55, 100))
        self.createOrChangeStudent(eeStudent2021)

        eeStudent2022_2 = generateRandomStudent(ElectricalEngineering, 2022, 3, bbbAdvisor.get_staffId())
        eeStudent2022_2.getTranscript().addTakenCourse(TakenCourse(PhysicsI.getCourseInformation(), 67, 80))
        eeStudent2022_2.getTranscript().addTakenCourse(TakenCourse(DigitalDesign.getCourseInformation(), 74, 69))
        self.createOrChangeStudent(eeStudent2022_2)

        eeStudent2023_1 = generateRandomStudent(ElectricalEngineering, 2023, 2, bbbAdvisor.get_staffId())
        eeStudent2023_1.getTranscript().addTakenCourse(TakenCourse(PhysicsI.getCourseInformation(), 31, 90))
        self.createOrChangeStudent(eeStudent2023_1)

        eeStudent2024_2 = generateRandomStudent(ElectricalEngineering, 2024, 1, bbbAdvisor.get_staffId())
        self.createOrChangeStudent(eeStudent2024_2)

























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
        data = self.loadFromJson(f"../Facultys/{faculty_name}.json")
        print(faculty_name)
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
         "Ezgi", "Volkan", "Dilara", "Ugur", "Selma", "Ece", "Adem", "Zeynep", "Burcu", "Ozan", "Cemile",
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


def generateUniversityEmail(name, surname):
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
    universityEmail = generateUniversityEmail(firstName, lastName)
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

#if __name__ == "__main__":
#    dm = DataManagement()
#    dm.__main__()
