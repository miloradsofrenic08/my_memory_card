from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QPushButton, QLabel, QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout
from random import shuffle, randint

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("Kako se zove najveca planina?","Himalaji","alpi","majevica","Jahorina"))
question_list.append(Question("Koji je glavni grad Francuske?","Pariz","Bijeljina","Monako","Milano"))
question_list.append(Question("Ko je napisao roman na drini cuprija","Ivo Andric","Mesa Selimovic","Djura Jaksic","Desanka Maksimovic"))
question_list.append(Question("Kad je poceo prvi svijetski rat","28.7.1914","28.6.1914","23.7.1914","25.1914"))
question_list.append(Question("Ko je ubio sultana murata","Milos Obilic","knez Lazar","Oto fon Bizmark","Fernando Magelan"))
question_list.append(Question("Gdje su se srbi povlacili u prvom svijetskom rati","na krf","na kosovo","u solun","u skoplje"))
question_list.append(Question("kad je poslan ultimatum srbiji","23.7.1914","25.7.1914","28.6.1914","28.7.1914"))
question_list.append(Question("Kad je nastala prva jugoslavija","1.12.1918","12.7.1918","17.9.1919","11.11.1918"))
question_list.append(Question("Ko je ubio sultana murata","Milos Obilic","knez Lazar","Oto fon Bizmark","Fernando Magelan"))
question_list.append(Question("kad je poceo prvi svijetski rat","28.7.1914","28.6.1914","23.7.1914","25.1914"))




app = QApplication([])
my_win = QWidget()


question = QLabel("Which nationality does not exist?")
ans_button = QPushButton("Answer")
Group_Box = QGroupBox("Answer options")
rbtn_1 = QRadioButton("Enets")
rbtn_2 = QRadioButton("Smurfs")
rbtn_3 = QRadioButton("Chulyms")
rbtn_4 = QRadioButton("Aleuts")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()

layout_2.addWidget(rbtn_1)
layout_2.addWidget(rbtn_2)
layout_3.addWidget(rbtn_3)
layout_3.addWidget(rbtn_4)

layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)
Group_Box.setLayout(layout_1)

AnsGrupBox = QGroupBox("Test result")
lb_Result = QLabel("True/False")
lb_Correct = QLabel("Tacan odgovor ce biti ovde!")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct,alignment=Qt.AlignHCenter,stretch=2)

AnsGrupBox.setLayout(layout_res)


layout_line_1 = QHBoxLayout()
layout_line_2 = QHBoxLayout()
layout_line_3 = QHBoxLayout()
layout_line_4 = QVBoxLayout()
layout_line_1.addWidget(question, alignment = (Qt.AlignHCenter|Qt.AlignVCenter))
layout_line_2.addWidget(Group_Box)
layout_line_2.addWidget(AnsGrupBox)
AnsGrupBox.hide() 
layout_line_3.addStretch(3)
layout_line_3.addWidget(ans_button, stretch = 2)
layout_line_3.addStretch(3)
layout_line_4.addLayout(layout_line_1)
layout_line_4.addLayout(layout_line_2)
layout_line_4.addLayout(layout_line_3)

def show_result():
    Group_Box.hide()
    AnsGrupBox.show()
    ans_button.setText("Next question")

def show_question():
    AnsGrupBox.hide()
    Group_Box.show()
    ans_button.setText("Answer")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct("Znam to!")
        my_win.score +=1
        print("Statistika \n - Ukupno pitanja: ", my_win.total, "\n - Tacnih odgovora:", my_win.score)
        print("Postotak: ", (my_win.score/my_win.total)*100, "%")

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Netacno !")
            print("Postotak: ", (my_win.score/my_win.total)*100, "%")
            

def next_question():
    my_win.total +=1
    print("Statistika \n - Ukupno pitanja: ", my_win.total, "\n - Tacnih odgovora:", my_win.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_OK ():
    if ans_button.text() == "Answer":
        check_answer()
    else:
        next_question()




my_win.setLayout(layout_line_4)


ans_button.clicked.connect(click_OK)
my_win.total = 0 
my_win.score = 0
next_question()


my_win.show()
app.exec_()

