from PyQt5.QtCore import Qt 

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout,  
                                QVBoxLayout, QLabel, QGroupBox, QRadioButton, QButtonGroup) 
from random import shuffle 
from random import randint 
count = 0
class Question:
    def __init__(self, question, right_answer, wrong1 , wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Real name Neil Josten is: ', 'Nathaniel ', 'Stefan', 'Alex', 'Neil'))
questions_list.append(Question('What number does Andrew Joseph minyard play under?', '03', '10', '05', '11'))
questions_list.append(Question('Who was andrews best friend?', 'Rene', 'Kevin', 'Aaron', 'Nicky'))
questions_list.append(Question('What position does Neil play in?', 'striker', 'defender', ' goalkeeper', 'midfielder'))
questions_list.append(Question('What Andrew loved in the first book?', 'ice cream', 'chocolate', 'knives', '-'))


app = QApplication([]) 
window = QWidget() 
window.setWindowTitle('Memory Cards') 
  
btn_OK = QPushButton('to answer') 
lb_Question = QLabel('In what year was Moscow founded?') 
  
RadioGroupBox = QGroupBox('Answer options') 
rbtn_1 = QRadioButton('1905') 
rbtn_2 = QRadioButton('1906') 
rbtn_3 = QRadioButton('1907') 
rbtn_4 = QRadioButton('1908') 
  
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1) 
RadioGroup.addButton(rbtn_2) 
RadioGroup.addButton(rbtn_3) 
RadioGroup.addButton(rbtn_4) 
  
layout_ans1 = QHBoxLayout() 
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout() 
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2) 
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4) 
layout_ans1.addLayout(layout_ans2) 
layout_ans1.addLayout(layout_ans3) 
  
RadioGroupBox.setLayout(layout_ans1) 
  ###
AnsGroupBox = QGroupBox('Test result') 
lb_Result = QLabel('Are you right or wrong?') 
lb_Correct = QLabel('the answer will be here') 
  
layout_res = QVBoxLayout() 
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop)) 
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2) 
AnsGroupBox.setLayout(layout_res) 
  
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
  
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) 
layout_line2.addWidget(RadioGroupBox) 
layout_line2.addWidget(AnsGroupBox)   
AnsGroupBox.hide() 
  
layout_line3.addStretch(1) 
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1) 
  
layout_card = QVBoxLayout() 
  
layout_card.addLayout(layout_line1, stretch=2) 
layout_card.addLayout(layout_line2, stretch=8) 
layout_card.addStretch(1) 
layout_card.addLayout(layout_line3, stretch=1) 
layout_card.addStretch(1) 
layout_card.setSpacing(5) 
  
window.setLayout(layout_card) 
  
def show_result(): 
    RadioGroupBox.hide() 
    AnsGroupBox.show() 
    btn_OK.setText('next question') 
  
def show_question(): 
    RadioGroupBox.show() 
    AnsGroupBox.hide() 
    btn_OK.setText('to answer') 
    RadioGroup.setExclusive(False) #
    rbtn_1.setChecked(False) 
    rbtn_2.setChecked(False) 
    rbtn_3.setChecked(False) 
    rbtn_4.setChecked(False) 
    RadioGroup.setExclusive(True) #
  
def test(): 
    if 'to answer' == btn_OK.text(): 
        show_result() 
    else: 
        show_question() 
  
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] 
def ask(q: Question): 
    shuffle(answers) 
    answers[0].setText(q.right_answer) 
    answers[1].setText(q.wrong1) 
    answers[2].setText(q.wrong2) 
    answers[3].setText(q.wrong3) 
    lb_Question.setText(q.question) 
    lb_Correct.setText(q.right_answer) 
    show_question() 
  
def show_correct(res): 
    lb_Result.setText(res) 
    show_result() 
  
def check_answer(): 
    if answers[0].isChecked(): 
        show_correct('right!') 
        count =+ 1
    else: 
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked(): 
            show_correct('wrong!') 
  
def next_question():
    window.cur_question = randint(0,len(questions_list)-1)

    if window.cur_question == len(questions_list):
        window.cur_question = 0
    q = questions_list[window.cur_question]
    questions_list.remove(q)
    ask(q)

def click_ok():
    if btn_OK.text() == 'to answer':
        check_answer()
    else:
        next_question()
window.score = 0
window.total = 0
btn_OK.clicked.connect(click_ok)
window.cur_question = -1
next_question
window.resize(400,300)
window.show() 
app.exec_()
print('Процент правильных ответов:',5 / count * 100)