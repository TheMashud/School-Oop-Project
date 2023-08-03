from School import School, ClassRoom, Subject
from Persons import Student, Teacher
def main():
    school = School('Madrasatu At Tahjib', 'Halisohor')

    eight = ClassRoom("eight")
    school.add_classroom(eight)
    nine = ClassRoom("nine")
    school.add_classroom(nine)
    ten = ClassRoom("ten")
    school.add_classroom(ten)

#add students
    alvee = Student('Mejbar rehamn', eight)
    school.student_admission(alvee)
    shareef = Student('Sharif rehman', eight)
    school.student_admission(shareef)

    nishad = Student('nishad rehamn', eight)
    school.student_admission(nishad)

    #subjects
    physics_teacher = Teacher('Mashudul hoque')
    physics = Subject('physics',physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Mahmuda Akter')
    chemistry = Subject('chemistry',chemistry_teacher)
    eight.add_subject(chemistry)
    
    biology_teacher = Teacher('Ifti seikh')
    biology = Subject('biology',biology_teacher)
    eight.add_subject(biology)

    eight.take_semester_final()
   




    print(school)


if __name__ == '__main__':
    main()