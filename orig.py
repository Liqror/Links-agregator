# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orig.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1132, 835)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pic/agregator-icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.userThemeFrame = QtWidgets.QFrame(self.centralwidget)
        self.userThemeFrame.setMinimumSize(QtCore.QSize(280, 0))
        self.userThemeFrame.setMaximumSize(QtCore.QSize(282, 16777215))
        self.userThemeFrame.setStyleSheet("background-color: rgb(42, 42, 68);")
        self.userThemeFrame.setObjectName("userThemeFrame")
        self.userThemeLayout = QtWidgets.QVBoxLayout(self.userThemeFrame)
        self.userThemeLayout.setObjectName("userThemeLayout")
        self.userFrame = QtWidgets.QFrame(self.userThemeFrame)
        self.userFrame.setEnabled(True)
        self.userFrame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.userFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userFrame.setObjectName("userFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.userFrame)
        self.verticalLayout_5.setContentsMargins(2, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.userWidget = QtWidgets.QWidget(self.userFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userWidget.sizePolicy().hasHeightForWidth())
        self.userWidget.setSizePolicy(sizePolicy)
        self.userWidget.setObjectName("userWidget")
        self.user = QtWidgets.QHBoxLayout(self.userWidget)
        self.user.setObjectName("user")
        self.userImage = QtWidgets.QLabel(self.userWidget)
        self.userImage.setMaximumSize(QtCore.QSize(60, 50))
        self.userImage.setStyleSheet("border-radius: 5px;")
        self.userImage.setText("")
        self.userImage.setPixmap(QtGui.QPixmap("Pic/rounded-userdog.png"))
        self.userImage.setScaledContents(True)
        self.userImage.setObjectName("userImage")
        self.user.addWidget(self.userImage)
        self.userName = QtWidgets.QLabel(self.userWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.userName.setFont(font)
        self.userName.setStyleSheet("color: rgb(255, 255, 255);")
        self.userName.setTextFormat(QtCore.Qt.AutoText)
        self.userName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.userName.setObjectName("userName")
        self.user.addWidget(self.userName)
        self.verticalLayout_5.addWidget(self.userWidget)
        self.newLinkButton = QtWidgets.QPushButton(self.userFrame)
        self.newLinkButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newLinkButton.setFont(font)
        self.newLinkButton.setStyleSheet("background: #5E5EEC;\n"
"border-radius: 12px;\n"
"color: rgb(255, 255, 255);")
        self.newLinkButton.setIconSize(QtCore.QSize(16, 16))
        self.newLinkButton.setObjectName("newLinkButton")
        self.verticalLayout_5.addWidget(self.newLinkButton)
        self.themeWidget = QtWidgets.QWidget(self.userFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.themeWidget.sizePolicy().hasHeightForWidth())
        self.themeWidget.setSizePolicy(sizePolicy)
        self.themeWidget.setMaximumSize(QtCore.QSize(262, 52))
        self.themeWidget.setObjectName("themeWidget")
        self.addNewTheme = QtWidgets.QHBoxLayout(self.themeWidget)
        self.addNewTheme.setContentsMargins(0, -1, 0, -1)
        self.addNewTheme.setObjectName("addNewTheme")
        self.themeLable = QtWidgets.QLabel(self.themeWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.themeLable.sizePolicy().hasHeightForWidth())
        self.themeLable.setSizePolicy(sizePolicy)
        self.themeLable.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.themeLable.setFont(font)
        self.themeLable.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.themeLable.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.themeLable.setStyleSheet("background: #5E5EEC;\n"
"border-radius: 12px;\n"
"color: rgb(255, 255, 255);")
        self.themeLable.setScaledContents(False)
        self.themeLable.setAlignment(QtCore.Qt.AlignCenter)
        self.themeLable.setObjectName("themeLable")
        self.addNewTheme.addWidget(self.themeLable)
        self.plus = QtWidgets.QPushButton(self.themeWidget)
        self.plus.setMaximumSize(QtCore.QSize(30, 30))
        self.plus.setStyleSheet("background: #5E5EEC;\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);")
        self.plus.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pic/???????????? ????????.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plus.setIcon(icon1)
        self.plus.setIconSize(QtCore.QSize(30, 30))
        self.plus.setObjectName("plus")
        self.addNewTheme.addWidget(self.plus)
        self.verticalLayout_5.addWidget(self.themeWidget)
        self.userThemeLayout.addWidget(self.userFrame)
        self.addThemeFrame = QtWidgets.QFrame(self.userThemeFrame)
        self.addThemeFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.addThemeFrame.setObjectName("addThemeFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.addThemeFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.addThemeFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background: #A2A2E8;\n"
"border-radius: 5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.horizontalFrame = QtWidgets.QFrame(self.addThemeFrame)
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cancelThemeButton = QtWidgets.QPushButton(self.horizontalFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancelThemeButton.setFont(font)
        self.cancelThemeButton.setStyleSheet("background: #5E5EEC;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.cancelThemeButton.setObjectName("cancelThemeButton")
        self.horizontalLayout_4.addWidget(self.cancelThemeButton)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.saveThemeButton = QtWidgets.QPushButton(self.horizontalFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saveThemeButton.setFont(font)
        self.saveThemeButton.setStyleSheet("background: #5E5EEC;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.saveThemeButton.setObjectName("saveThemeButton")
        self.horizontalLayout_4.addWidget(self.saveThemeButton)
        self.verticalLayout_3.addWidget(self.horizontalFrame)
        self.userThemeLayout.addWidget(self.addThemeFrame)
        self.themesLayout = QtWidgets.QVBoxLayout()
        self.themesLayout.setObjectName("themesLayout")
        self.userThemeLayout.addLayout(self.themesLayout)
        self.exitAccButton = QtWidgets.QPushButton(self.userThemeFrame)
        self.exitAccButton.setMinimumSize(QtCore.QSize(215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.exitAccButton.setFont(font)
        self.exitAccButton.setStyleSheet("background: #5E5EEC;\n"
"border-radius: 12px;\n"
"color: rgb(255, 255, 255);")
        self.exitAccButton.setObjectName("exitAccButton")
        self.userThemeLayout.addWidget(self.exitAccButton)
        self.horizontalLayout_3.addWidget(self.userThemeFrame)
        self.Frame = QtWidgets.QFrame(self.centralwidget)
        self.Frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Frame.setStyleSheet("background-color: rgb(162, 162, 232);")
        self.Frame.setObjectName("Frame")
        self.libraryLayout = QtWidgets.QVBoxLayout(self.Frame)
        self.libraryLayout.setObjectName("libraryLayout")
        self.nameFrame = QtWidgets.QFrame(self.Frame)
        self.nameFrame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.nameFrame.setObjectName("nameFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.nameFrame)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QPushButton(self.nameFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(40, 40))
        self.label.setStyleSheet("border-style: outset; \n"
"border-width: 0px;")
        self.label.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pic/?????????????? ?????????? ?????? ????????2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("Pic/?????????????? ?????????? ?????? ????????2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("Pic/?????????????? ?????????? ?????? ????????2.jpg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("Pic/?????????????? ?????????? ?????? ????????2.jpg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("Pic/?????????????? ?????????? ?????? ????????2.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("Pic/?????????????? ?????????? ?????? ????????2.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.label.setIcon(icon2)
        self.label.setIconSize(QtCore.QSize(40, 40))
        self.label.setFlat(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nameOfLayout = QtWidgets.QLabel(self.nameFrame)
        self.nameOfLayout.setMinimumSize(QtCore.QSize(400, 40))
        self.nameOfLayout.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.nameOfLayout.setFont(font)
        self.nameOfLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.nameOfLayout.setObjectName("nameOfLayout")
        self.horizontalLayout.addWidget(self.nameOfLayout)
        self.nothingLabel = QtWidgets.QLabel(self.nameFrame)
        self.nothingLabel.setMaximumSize(QtCore.QSize(45, 40))
        self.nothingLabel.setText("")
        self.nothingLabel.setObjectName("nothingLabel")
        self.horizontalLayout.addWidget(self.nothingLabel)
        self.deleteButton = QtWidgets.QPushButton(self.nameFrame)
        self.deleteButton.setMaximumSize(QtCore.QSize(45, 40))
        self.deleteButton.setStyleSheet("border-style: outset; \n"
"border-width: 0px;")
        self.deleteButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Pic/??????????????.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon3)
        self.deleteButton.setIconSize(QtCore.QSize(45, 38))
        self.deleteButton.setFlat(True)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.libraryLayout.addWidget(self.nameFrame)
        self.centralLayout = QtWidgets.QVBoxLayout()
        self.centralLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.centralLayout.setObjectName("centralLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setGeometry(QtCore.QRect(0, 0, 531, 741))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.descriptionLayout = QtWidgets.QVBoxLayout()
        self.descriptionLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.descriptionLayout.setObjectName("descriptionLayout")
        self.typeOfInfLayout = QtWidgets.QHBoxLayout()
        self.typeOfInfLayout.setObjectName("typeOfInfLayout")
        self.linkButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.linkButton.setFont(font)
        self.linkButton.setObjectName("linkButton")
        self.typeOfInfLayout.addWidget(self.linkButton)
        self.dockButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dockButton.setFont(font)
        self.dockButton.setObjectName("dockButton")
        self.typeOfInfLayout.addWidget(self.dockButton)
        self.imgButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.imgButton.setFont(font)
        self.imgButton.setObjectName("imgButton")
        self.typeOfInfLayout.addWidget(self.imgButton)
        self.descriptionLayout.addLayout(self.typeOfInfLayout)
        self.linkLineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.linkLineEdit.setFont(font)
        self.linkLineEdit.setStyleSheet("background: #5E5EEC;\n"
"border-radius: 5px;")
        self.linkLineEdit.setInputMask("")
        self.linkLineEdit.setText("")
        self.linkLineEdit.setMaxLength(32767)
        self.linkLineEdit.setObjectName("linkLineEdit")
        self.descriptionLayout.addWidget(self.linkLineEdit)
        self.themeComboBox = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.themeComboBox.setFont(font)
        self.themeComboBox.setStyleSheet("background: #5E5EEC;\n"
"border-radius: 5px;")
        self.themeComboBox.setObjectName("themeComboBox")
        self.themeComboBox.addItem("")
        self.descriptionLayout.addWidget(self.themeComboBox)
        self.tagsLineEdit = QtWidgets.QLineEdit(self.widget)
        self.tagsLineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagsLineEdit.sizePolicy().hasHeightForWidth())
        self.tagsLineEdit.setSizePolicy(sizePolicy)
        self.tagsLineEdit.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tagsLineEdit.setFont(font)
        self.tagsLineEdit.setStyleSheet("background: #5E5EEC;\n"
"border-radius: 5px;")
        self.tagsLineEdit.setObjectName("tagsLineEdit")
        self.descriptionLayout.addWidget(self.tagsLineEdit)
        self.descriptionTextEdit = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.descriptionTextEdit.setFont(font)
        self.descriptionTextEdit.setStyleSheet("background: #5E5EEC;\n"
"border-radius: 5px;")
        self.descriptionTextEdit.setDocumentTitle("")
        self.descriptionTextEdit.setObjectName("descriptionTextEdit")
        self.descriptionLayout.addWidget(self.descriptionTextEdit)
        self.buttonHorizontalLayout = QtWidgets.QHBoxLayout()
        self.buttonHorizontalLayout.setObjectName("buttonHorizontalLayout")
        self.backPushButton = QtWidgets.QPushButton(self.widget)
        self.backPushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.backPushButton.setFont(font)
        self.backPushButton.setStyleSheet("background-color: rgb(42, 42, 68); color: rgb(255, 255, 255);")
        self.backPushButton.setObjectName("backPushButton")
        self.buttonHorizontalLayout.addWidget(self.backPushButton)
        self.savePushButton = QtWidgets.QPushButton(self.widget)
        self.savePushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.savePushButton.setFont(font)
        self.savePushButton.setStyleSheet("background-color: rgb(42, 42, 68);color: rgb(255, 255, 255);")
        self.savePushButton.setObjectName("savePushButton")
        self.buttonHorizontalLayout.addWidget(self.savePushButton)
        self.descriptionLayout.addLayout(self.buttonHorizontalLayout)
        self.verticalLayout.addLayout(self.descriptionLayout)
        self.stackedWidget.addWidget(self.page_2)
        self.centralLayout.addWidget(self.stackedWidget)
        self.libraryLayout.addLayout(self.centralLayout)
        self.horizontalLayout_3.addWidget(self.Frame)
        self.searchFrame = QtWidgets.QFrame(self.centralwidget)
        self.searchFrame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.searchFrame.setStyleSheet("QWidget#searchFrame{ background-color: rgb(42, 42, 68);}")
        self.searchFrame.setObjectName("searchFrame")
        self.searchLayout = QtWidgets.QVBoxLayout(self.searchFrame)
        self.searchLayout.setObjectName("searchLayout")
        self.littleSearchLayout = QtWidgets.QHBoxLayout()
        self.littleSearchLayout.setObjectName("littleSearchLayout")
        self.searchImage = QtWidgets.QLabel(self.searchFrame)
        self.searchImage.setMinimumSize(QtCore.QSize(0, 0))
        self.searchImage.setMaximumSize(QtCore.QSize(45, 35))
        self.searchImage.setText("")
        self.searchImage.setPixmap(QtGui.QPixmap("Pic/????????.jpg"))
        self.searchImage.setScaledContents(True)
        self.searchImage.setObjectName("searchImage")
        self.littleSearchLayout.addWidget(self.searchImage)
        self.generalSearch = QtWidgets.QLineEdit(self.searchFrame)
        self.generalSearch.setMinimumSize(QtCore.QSize(220, 0))
        self.generalSearch.setMaximumSize(QtCore.QSize(195, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.generalSearch.setFont(font)
        self.generalSearch.setStyleSheet("QLineEdit {\n"
"background: #A2A2E8;\n"
"border-radius: 10px;\n"
"}")
        self.generalSearch.setText("")
        self.generalSearch.setObjectName("generalSearch")
        self.littleSearchLayout.addWidget(self.generalSearch)
        self.searchLayout.addLayout(self.littleSearchLayout)
        self.resourceType = QtWidgets.QComboBox(self.searchFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.resourceType.setFont(font)
        self.resourceType.setStyleSheet("QComboBox {\n"
"            background: #A2A2E8;\n"
"            border-radius: 10px;\n"
"            padding-left: 90px;\n"
"\n"
"        }\n"
"QComboBox QAbstractItemView {\n"
"            padding-left: 90px;\n"
"            background-color: rgb(162, 162, 232)\n"
"        }")
        self.resourceType.setObjectName("resourceType")
        self.resourceType.addItem("")
        self.resourceType.addItem("")
        self.resourceType.addItem("")
        self.resourceType.addItem("")
        self.searchLayout.addWidget(self.resourceType)
        self.themeSearch = QtWidgets.QLineEdit(self.searchFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.themeSearch.setFont(font)
        self.themeSearch.setStyleSheet("QLineEdit {\n"
"background: #A2A2E8;\n"
"border-radius: 10px;\n"
"}")
        self.themeSearch.setText("")
        self.themeSearch.setAlignment(QtCore.Qt.AlignCenter)
        self.themeSearch.setObjectName("themeSearch")
        self.searchLayout.addWidget(self.themeSearch)
        self.tagSearch = QtWidgets.QLineEdit(self.searchFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.tagSearch.setFont(font)
        self.tagSearch.setStyleSheet("background: #A2A2E8;\n"
"border-radius: 10px;")
        self.tagSearch.setText("")
        self.tagSearch.setAlignment(QtCore.Qt.AlignCenter)
        self.tagSearch.setObjectName("tagSearch")
        self.searchLayout.addWidget(self.tagSearch)
        self.descriptionSearch = QtWidgets.QLineEdit(self.searchFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.descriptionSearch.setFont(font)
        self.descriptionSearch.setStyleSheet("background: #A2A2E8;\n"
"border-radius: 10px;")
        self.descriptionSearch.setText("")
        self.descriptionSearch.setAlignment(QtCore.Qt.AlignCenter)
        self.descriptionSearch.setObjectName("descriptionSearch")
        self.searchLayout.addWidget(self.descriptionSearch)
        self.sourceSearch = QtWidgets.QLineEdit(self.searchFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sourceSearch.setFont(font)
        self.sourceSearch.setStyleSheet("background: #A2A2E8;\n"
"border-radius: 10px;")
        self.sourceSearch.setText("")
        self.sourceSearch.setAlignment(QtCore.Qt.AlignCenter)
        self.sourceSearch.setObjectName("sourceSearch")
        self.searchLayout.addWidget(self.sourceSearch)
        self.dateSearch = QtWidgets.QDateEdit(self.searchFrame)
        self.dateSearch.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.dateSearch.setFont(font)
        self.dateSearch.setStyleSheet("background: #A2A2E8;\n"
"border-radius: 10px;\n"
"")
        self.dateSearch.setObjectName("dateSearch")
        self.searchLayout.addWidget(self.dateSearch)
        self.applyButton = QtWidgets.QPushButton(self.searchFrame)
        self.applyButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.applyButton.setFont(font)
        self.applyButton.setStyleSheet("background: #5E5EEC;\n"
"border-radius: 12px;\n"
"color: rgb(255, 255, 255);")
        self.applyButton.setObjectName("applyButton")
        self.searchLayout.addWidget(self.applyButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.searchLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.searchFrame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: #5E5EEC;\n"
"border-radius: 12px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.searchLayout.addWidget(self.pushButton)
        self.horizontalLayout_3.addWidget(self.searchFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.userName.setText(_translate("MainWindow", "Kitten"))
        self.newLinkButton.setText(_translate("MainWindow", "?????????? ????????????"))
        self.themeLable.setText(_translate("MainWindow", "????????"))
        self.cancelThemeButton.setText(_translate("MainWindow", "????????????"))
        self.saveThemeButton.setText(_translate("MainWindow", "??????????????????"))
        self.exitAccButton.setText(_translate("MainWindow", "?????????? ???? ????????????????"))
        self.nameOfLayout.setText(_translate("MainWindow", "?????? ????????????????????"))
        self.linkButton.setText(_translate("MainWindow", "????????????"))
        self.dockButton.setText(_translate("MainWindow", "????????????????"))
        self.imgButton.setText(_translate("MainWindow", "??????????????????????"))
        self.linkLineEdit.setPlaceholderText(_translate("MainWindow", "????????????..."))
        self.themeComboBox.setCurrentText(_translate("MainWindow", "????????..."))
        self.themeComboBox.setItemText(0, _translate("MainWindow", "????????..."))
        self.tagsLineEdit.setPlaceholderText(_translate("MainWindow", "????????..."))
        self.descriptionTextEdit.setPlaceholderText(_translate("MainWindow", "????????????????..."))
        self.backPushButton.setText(_translate("MainWindow", "??????????"))
        self.savePushButton.setText(_translate("MainWindow", "??????????????????"))
        self.generalSearch.setPlaceholderText(_translate("MainWindow", "??????????"))
        self.resourceType.setCurrentText(_translate("MainWindow", "?????? ??????????????"))
        self.resourceType.setItemText(0, _translate("MainWindow", "?????? ??????????????"))
        self.resourceType.setItemText(1, _translate("MainWindow", "????????????"))
        self.resourceType.setItemText(2, _translate("MainWindow", "????????????????"))
        self.resourceType.setItemText(3, _translate("MainWindow", "??????????????????????"))
        self.themeSearch.setPlaceholderText(_translate("MainWindow", "????????"))
        self.tagSearch.setPlaceholderText(_translate("MainWindow", "????????"))
        self.descriptionSearch.setPlaceholderText(_translate("MainWindow", "????????????????"))
        self.sourceSearch.setPlaceholderText(_translate("MainWindow", "????????????????"))
        self.applyButton.setText(_translate("MainWindow", "??????????????????"))
        self.pushButton.setText(_translate("MainWindow", "???????????????? ??????????"))
