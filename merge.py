from PyQt5 import QtCore, QtGui, QtWidgets

import pickle

import os

import pandas as pd


def login(UserName, Password):

    UserPass = pickle.load(open('UserPass','rb'))

    if UserName not in list(UserPass.keys()):
        return 'Username does not exits!'

    elif UserName in list(UserPass.keys()) and Password != UserPass[UserName]['Password']:
        return 'Password is Wrong!'

    else:
        return True



def SignUp(UserName, Password, ID):

    UserPass = pickle.load(open('UserPass','rb'))
    UserPass[UserName] = {"Password" : Password, "ID" : ID}

    pickle.dump(UserPass, open('UserPass','wb'))




def reset_pass(UserName, ID):
    UserPass = pickle.load(open('UserPass','rb'))

    if  UserPass[UserName]["ID"] == ID:
        return  UserPass[UserName]["Password"]






class home(object):

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()





    def setupUihome(self):
        MainWindow = self.MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signin = QtWidgets.QToolButton(self.centralwidget)
        self.signin.setGeometry(QtCore.QRect(190, 230, 441, 111))
        self.signin.setObjectName("signin")
        self.signUp = QtWidgets.QPushButton(self.centralwidget)
        self.signUp.setGeometry(QtCore.QRect(190, 60, 441, 121))
        self.signUp.setMouseTracking(False)
        self.signUp.setCheckable(False)
        self.signUp.setObjectName("signUp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUiHome(MainWindow)
        self.signUp.clicked.connect(self.setupUiSignUp)
        self.signin.clicked.connect(self.setupUiLoginPan)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)







    def retranslateUiHome(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.signin.setText(_translate("MainWindow", "I already have an account."))
        self.signUp.setText(_translate("MainWindow", "I don’t have any account and I want to register."))







    def setupUiLoginPan(self):
        MainWindow = self.MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(275, 140, 250, 60))
        self.Password.setAutoFillBackground(True)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.Useraame = QtWidgets.QLineEdit(self.centralwidget)
        self.Useraame.setGeometry(QtCore.QRect(275, 30, 250, 61))
        self.Useraame.setInputMask("")
        self.Useraame.setText("")
        self.Useraame.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.Useraame.setObjectName("Useraame")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(270, 230, 100, 51))
        self.login.setDefault(False)
        self.login.setObjectName("login")
        self.logger = QtWidgets.QTextBrowser(self.centralwidget)
        self.logger.setGeometry(QtCore.QRect(40, 340, 700, 192))
        self.logger.setFrameShape(QtWidgets.QFrame.Box)
        self.logger.setObjectName("logger")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(120, 150, 131, 41))
        self.password_label.setObjectName("password_label")
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(120, 40, 121, 41))
        self.user_label.setObjectName("user_label")
        self.forget = QtWidgets.QPushButton(self.centralwidget)
        self.forget.setGeometry(QtCore.QRect(560, 150, 180, 40))
        self.forget.setDefault(False)
        self.forget.setObjectName("forget")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(370, 230, 100, 51))
        self.back.setDefault(False)
        self.back.setObjectName("back")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUiLogin(MainWindow)
        
        def temp_login():
            b1 = login(self.Useraame.text(), self.Password.text())
            if b1 == True:
                self.setupUiQuizlist()
            else:
                self.logger.setText("<h1>" + b1 + "<\h1>")


        self.login.clicked.connect(temp_login)
        self.back.clicked.connect(self.setupUihome)
        self.forget.clicked.connect(self.setupUiFroget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)







    def retranslateUiLogin(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Password.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.Useraame.setPlaceholderText(_translate("MainWindow", "USERNAME"))
        self.login.setText(_translate("MainWindow", "login"))
        self.password_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Password :</span></p></body></html>"))
        self.user_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Username :</span></p></body></html>"))
        self.forget.setText(_translate("MainWindow", "Forget Password"))
        self.back.setText(_translate("MainWindow", "Back"))





    def setupUiSignUp(self):
        MainWindow = self.MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(275, 140, 250, 61))
        self.Password.setAutoFillBackground(True)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.Useraame = QtWidgets.QLineEdit(self.centralwidget)
        self.Useraame.setGeometry(QtCore.QRect(275, 30, 250, 61))
        self.Useraame.setInputMask("")
        self.Useraame.setText("")
        self.Useraame.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.Useraame.setObjectName("Useraame")
        self.SignUp = QtWidgets.QPushButton(self.centralwidget)
        self.SignUp.setGeometry(QtCore.QRect(330, 380, 100, 51))
        self.SignUp.setDefault(False)
        self.SignUp.setObjectName("SignUp")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(120, 150, 131, 41))
        self.password_label.setObjectName("password_label")
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(120, 40, 121, 41))
        self.user_label.setObjectName("user_label")
        self.password_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.password_label_2.setGeometry(QtCore.QRect(110, 270, 131, 41))
        self.password_label_2.setObjectName("password_label_2")
        self.ID_Number = QtWidgets.QLineEdit(self.centralwidget)
        self.ID_Number.setGeometry(QtCore.QRect(275, 260, 250, 61))
        self.ID_Number.setAutoFillBackground(True)
        self.ID_Number.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ID_Number.setObjectName("ID_Number")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(440, 380, 100, 51))
        self.back.setDefault(False)
        self.back.setObjectName("back")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUiSignUp(MainWindow)


        def temp_signUp_and_back_to_home():
            SignUp(self.Useraame.text(), self.Password.text(),self.ID_Number.text())
            self.setupUiLoginPan()


        self.SignUp.clicked.connect(temp_signUp_and_back_to_home)
        self.back.clicked.connect(self.setupUihome)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUiSignUp(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Password.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.Useraame.setPlaceholderText(_translate("MainWindow", "USERNAME"))
        self.SignUp.setText(_translate("MainWindow", "SignUp"))
        self.password_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Password :</span></p></body></html>"))
        self.user_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Username :</span></p></body></html>"))
        self.password_label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">ID Number :</span></p></body></html>"))
        self.ID_Number.setPlaceholderText(_translate("MainWindow", "ID NUMBER"))
        self.back.setText(_translate("MainWindow", "Back"))





    def setupUiFroget(self):
        MainWindow = self.MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IDNum = QtWidgets.QLineEdit(self.centralwidget)
        self.IDNum.setGeometry(QtCore.QRect(275, 140, 250, 60))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.IDNum.setFont(font)
        self.IDNum.setAutoFillBackground(True)
        self.IDNum.setText("")
        self.IDNum.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.IDNum.setAlignment(QtCore.Qt.AlignCenter)
        self.IDNum.setObjectName("IDNum")
        self.Useraame = QtWidgets.QLineEdit(self.centralwidget)
        self.Useraame.setGeometry(QtCore.QRect(275, 30, 250, 61))
        self.Useraame.setInputMask("")
        self.Useraame.setText("")
        self.Useraame.setAlignment(QtCore.Qt.AlignCenter)
        self.Useraame.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.Useraame.setObjectName("Useraame")
        self.showPass = QtWidgets.QPushButton(self.centralwidget)
        self.showPass.setGeometry(QtCore.QRect(300, 230, 200, 51))
        self.showPass.setDefault(False)
        self.showPass.setObjectName("showPass")
        self.logger = QtWidgets.QTextBrowser(self.centralwidget)
        self.logger.setGeometry(QtCore.QRect(40, 340, 700, 192))
        self.logger.setFrameShape(QtWidgets.QFrame.Box)
        self.logger.setObjectName("logger")
        self.ID_label = QtWidgets.QLabel(self.centralwidget)
        self.ID_label.setGeometry(QtCore.QRect(120, 150, 131, 41))
        self.ID_label.setObjectName("ID_label")
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(120, 40, 121, 41))
        self.user_label.setObjectName("user_label")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(350, 285, 100, 51))
        self.back.setDefault(False)
        self.back.setObjectName("back")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUiForget(MainWindow)


        def temp_froget_pass():
            passWord = reset_pass(self.Useraame.text(), self.IDNum.text())
            self.logger.setText('Your Password is :' + "<h1>" + passWord + "<\h1>")


        self.showPass.clicked.connect(temp_froget_pass)
        self.back.clicked.connect(self.setupUiLoginPan)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUiForget(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.IDNum.setPlaceholderText(_translate("MainWindow", "ID NUMBER"))
        self.Useraame.setPlaceholderText(_translate("MainWindow", "USERNAME"))
        self.showPass.setText(_translate("MainWindow", "Show Password"))
        self.ID_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">ID Number :</span></p></body></html>"))
        self.user_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Username :</span></p></body></html>"))
        self.back.setText(_translate("MainWindow", "Back"))


    def setupUiQuizlist(self):
        MainWindow = self.MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(400, 200, 320, 61))
        self.start.setObjectName("start")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(60, 200, 320, 61))
        self.back.setObjectName("back")
        self.quizlist = QtWidgets.QComboBox(self.centralwidget)
        self.quizlist.setGeometry(QtCore.QRect(190, 120, 381, 31))
        self.quizlist.setObjectName("quizlist")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 320, 681, 192))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        Quiz_list = os.listdir(path='Quizes')

        for i in range(len(Quiz_list)):
            self.quizlist.addItem(Quiz_list[i])

        self.chosen_file = Quiz_list[0]


        def temp_choose():
            self.chosen_file = Quiz_list[self.quizlist.currentIndex()]
            print(self.chosen_file)
            self.textBrowser.setText("<h1>{} is Choosen! </h1>".format(self.chosen_file))



        self.retranslateUiQiuzlist(MainWindow)
        self.back.clicked.connect(self.setupUiLoginPan)
        self.start.clicked.connect(self.setupUiQuestionPan)
        self.quizlist.activated['QString'].connect(temp_choose)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUiQiuzlist(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "Start Quiz"))
        self.back.setText(_translate("MainWindow", "Back"))



    def setupUiQuestionPan(self):
        MainWindow = self.MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 110, 700, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.op1 = QtWidgets.QPushButton(self.centralwidget)
        self.op1.setGeometry(QtCore.QRect(80, 270, 120, 61))
        self.op1.setObjectName("op1")
        self.op2 = QtWidgets.QPushButton(self.centralwidget)
        self.op2.setGeometry(QtCore.QRect(250, 270, 120, 61))
        self.op2.setObjectName("op2")
        self.po3 = QtWidgets.QPushButton(self.centralwidget)
        self.po3.setGeometry(QtCore.QRect(420, 270, 120, 61))
        self.po3.setObjectName("po3")
        self.op4 = QtWidgets.QPushButton(self.centralwidget)
        self.op4.setGeometry(QtCore.QRect(590, 270, 120, 61))
        self.op4.setObjectName("op4")
        self.Qustion_label = QtWidgets.QLabel(self.centralwidget)
        self.Qustion_label.setGeometry(QtCore.QRect(50, 30, 300, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Qustion_label.setFont(font)
        self.Qustion_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Qustion_label.setObjectName("Qustion_label")
        self.previous = QtWidgets.QPushButton(self.centralwidget)
        self.previous.setGeometry(QtCore.QRect(80, 440, 300, 51))
        self.previous.setObjectName("previous")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(410, 440, 300, 51))
        self.next.setObjectName("next")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        _translate = QtCore.QCoreApplication.translate

        df = pd.read_csv('./Quizes/' + self.chosen_file)
        self.df = df
        
        self.answers = {}
        for i in range(df.shape[0]):
            self.answers[i] = None

        

        self.Question_index = 0

        def Que():
            index = self.Question_index 
            if self.Question_index == 0:
                self.previous.setText('Back')
                self.next.setText('Next')

            elif self.Question_index + 1 == df.shape[0]:
                self.next.setText('Finish !')
            else:
                self.previous.setText('Previous Question')
                self.next.setText('Next')

            self.Qustion_label.setText("Question {} out of {}:".format(str(index + 1), str(df.shape[0])))
            self.op4.setText('4. {}'.format(df['4'][index]))
            self.po3.setText('3. {}'.format(df['3'][index]))
            self.op2.setText('2. {}'.format(df['2'][index]))
            self.op1.setText('1. {}'.format(df['1'][index]))
            self.textBrowser.setText('<h1>' + df['Question'][index] + '<\h1> <br>' +'\n your Answer is : {}'.format(self.answers[index]))

        Que()

        def Next():
            if self.Question_index + 1 != df.shape[0]:
                self.Question_index += 1
                Que()
            elif self.Question_index + 1 == df.shape[0]:
                self.setupUiResultPan()

        def previous():
            if self.Question_index == 0:
                self.setupUiQuizlist()
            else:    
                self.Question_index -= 1 
                Que()
                
            


        def option(choice):
            self.answers[self.Question_index ] = choice
            self.textBrowser.setText('<h1>' + df['Question'][self.Question_index] + '<\h1> <br>' +'\n your Answer is : {}'.format(self.answers[self.Question_index ]))

        self.op1.clicked.connect(lambda x : option(1))
        self.op2.clicked.connect(lambda x : option(2))
        self.op4.clicked.connect(lambda x : option(4))
        self.po3.clicked.connect(lambda x : option(3))
        self.previous.clicked.connect(previous)
        self.next.clicked.connect(Next)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.retranslateUiQuestionPan(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUiQuestionPan(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.op1.setText(_translate("MainWindow", "PushButton"))
        #self.op2.setText(_translate("MainWindow", "PushButton"))
        #self.po3.setText(_translate("MainWindow", "PushButton"))
        #self.op4.setText(_translate("MainWindow", "PushButton"))
        #self.Qustion_label.setText(_translate("MainWindow", "Qustion"))
        #self.previous.setText(_translate("MainWindow", "Previous Question"))
        #self.next.setText(_translate("MainWindow", "Next Question"))




    def setupUiResultPan(self):
        MainWindow = self.MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 773)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Questions_result = QtWidgets.QTableWidget(self.centralwidget)
        self.Questions_result.setGeometry(QtCore.QRect(20, 10, 861, 461))
        self.Questions_result.setObjectName("Questions_result")

        self.Questions_result.setColumnCount(4)
        self.Questions_result.setRowCount(self.df.shape[0] + 1)

        self.Questions_result.horizontalHeader().setStretchLastSection(True) 

        self.Questions_result.setItem(0, 0, QtWidgets.QTableWidgetItem("Question"))
        self.Questions_result.setItem(0, 1, QtWidgets.QTableWidgetItem("your Answer"))
        self.Questions_result.setItem(0, 2, QtWidgets.QTableWidgetItem("Correct Answer"))
        self.Questions_result.setItem(0, 3, QtWidgets.QTableWidgetItem("Status"))


        header = self.Questions_result.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        count_correct = 0
        count_not_answered = 0
        count_InCorrect = 0

        for i in range(0, self.df.shape[0]):
            self.Questions_result.setItem(i+1, 0, QtWidgets.QTableWidgetItem(self.df['Question'][i]))
            
            if self.answers[i] == None:
                self.Questions_result.setItem(i+1, 1, QtWidgets.QTableWidgetItem("--"))
            else:
                self.Questions_result.setItem(i+1, 1, QtWidgets.QTableWidgetItem(self.df[str(self.answers[i])][i]))
            
            self.Questions_result.setItem(i+1, 2, QtWidgets.QTableWidgetItem(self.df[str(self.df['answer'][i])][i]))

            if self.answers[i] == self.df['answer'][i]:
                count_correct += 1
                self.Questions_result.setItem(i+1, 3, QtWidgets.QTableWidgetItem('Correct'))#.setBackground(QtGui.QBrush(QtGui.QColor(38, 255, 0))))
                self.Questions_result.item(i+1, 3).setBackground(QtGui.QColor(38,255,0))

            elif self.answers[i] == None:
                count_not_answered += 1
                self.Questions_result.setItem(i+1, 3, QtWidgets.QTableWidgetItem(' Not Answered' ))#.setBackground(QtGui.QBrush(QtGui.QColor(255, 255, 0))))
                self.Questions_result.item(i+1, 3).setBackground(QtGui.QColor(255,255,0))
            else:
                count_InCorrect += 1
                self.Questions_result.setItem(i+1, 3, QtWidgets.QTableWidgetItem('InCorrect'))#.setBackground(QtGui.QBrush(QtGui.QColor(255, 55, 0))))
                self.Questions_result.item(i+1, 3).setBackground(QtGui.QColor(255,55,0))

        self.signout = QtWidgets.QPushButton(self.centralwidget)
        self.signout.setGeometry(QtCore.QRect(470, 650, 411, 61))
        self.signout.setObjectName("signout")

        self.NewQuiz = QtWidgets.QPushButton(self.centralwidget)
        self.NewQuiz.setGeometry(QtCore.QRect(20, 650, 411, 61))
        self.NewQuiz.setObjectName("NewQuiz")

        self.total_results = QtWidgets.QTableWidget(self.centralwidget)
        self.total_results.setGeometry(QtCore.QRect(20, 490, 861, 131))
        self.total_results.setObjectName("total_results")
        self.total_results.setColumnCount(5)
        self.total_results.setRowCount(2)

        self.total_results.setItem(0, 0, QtWidgets.QTableWidgetItem('Total'))
        self.total_results.setItem(0, 1, QtWidgets.QTableWidgetItem('Correct'))
        self.total_results.setItem(0, 2, QtWidgets.QTableWidgetItem("Not Answered"))
        self.total_results.setItem(0, 3, QtWidgets.QTableWidgetItem('InCorrect'))
        self.total_results.setItem(1, 4, QtWidgets.QTableWidgetItem('Score'))
        self.total_results.setItem(1, 0, QtWidgets.QTableWidgetItem(str(self.df.shape[0])))
        self.total_results.setItem(1, 1, QtWidgets.QTableWidgetItem(str(count_correct)))
        self.total_results.setItem(1, 2, QtWidgets.QTableWidgetItem(str(count_not_answered)))
        self.total_results.setItem(1, 3, QtWidgets.QTableWidgetItem(str(count_InCorrect)))
        self.total_results.setItem(1, 4, QtWidgets.QTableWidgetItem(str(count_correct/self.df.shape[0])))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUiResultPan(MainWindow)
        self.signout.clicked.connect(self.setupUihome)
        self.NewQuiz.clicked.connect(self.setupUiQuizlist)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        header1 = self.total_results.horizontalHeader()       
        header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def retranslateUiResultPan(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.signout.setText(_translate("MainWindow", "Sign Out"))
        self.NewQuiz.setText(_translate("MainWindow", "Start New Quiz"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = home()
    ui.setupUihome()
    ui.MainWindow.show()
    sys.exit(app.exec_())