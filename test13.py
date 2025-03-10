#this program uses functions to calculate a students final grade and their mean score

name = input("Enter student's name: ")
adm = input("Enter the student's admission number: ")
score1 = float(input("Enter Mathematics score: "))
score2 = float(input("Enter English score: "))
score3 = float(input("Enter Science score: "))
score4 = float(input("Enter Social Studies score: "))
optional = input("What opional subject does the student take? ")
score5 = float(input("Enter "+optional+ " score: "))


def mean_marks():
    final_score = score1 + score2 + score3 + score4 + score5
    mean_score = final_score/ 5
    if mean_score >= 70:
        grade = 'A'
    elif mean_score >= 60 and mean_score < 70:
        grade = 'B'
    elif mean_score >= 50 and mean_score < 60:
        grade = 'C'
    elif mean_score >= 40 and mean_score < 50:
        grade = 'D'
    else: 
        grade = 'F'
    
    print("=" * 20)
    print("FINAL TRANSCRIPT")
    print("="* 20)
    print("Student's name: ",name)
    print("Student's admission number: ",adm)
    print("Mathematics: ",score1)
    print("English: ",score2)
    print("Science: ",score3)
    print("Social Studies: ",score4)
    print(optional,": ",score5)
    print("Total marks: ",final_score)
    print("Mean marks: ",mean_score)
    print("Final grade: ",grade)


mean_marks ()


