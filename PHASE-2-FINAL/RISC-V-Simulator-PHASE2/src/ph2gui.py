from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
#import temp3
import pipelining
#import pipeline




class Ui_MainWindow1(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.inst_count = len(pipelining.instructions)
        self.inst_num = 1
        self.register_change = 0
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2000, 2000)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        layout = QtWidgets.QVBoxLayout(self.centralwidget) ##
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget) ##
        layout.addWidget(self.scrollArea) #
        self.scrollAreaWidgetContents = QtWidgets.QWidget() #
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 2200, 2200)) #
        self.scrollArea.setWidget(self.scrollAreaWidgetContents) #
        layout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents) #
        MainWindow.setCentralWidget(self.centralwidget) #
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setEnabled(True)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.scrollArea)
        
        self.Simulator = QtWidgets.QGroupBox(self.centralwidget)
        self.Simulator.setGeometry(QtCore.QRect(10, 0, 2000, 2000))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Simulator.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(24)
        self.Simulator.setFont(font)
        self.Simulator.setAutoFillBackground(True)
        self.Simulator.setStyleSheet("")
        self.Simulator.setAlignment(QtCore.Qt.AlignCenter)
        self.Simulator.setObjectName("Simulator")
        self.simulatorTable = QtWidgets.QTableWidget(self.Simulator)
        self.simulatorTable.setGeometry(QtCore.QRect(10, 110, 639, 841))
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.simulatorTable.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.simulatorTable.setFont(font)
        self.simulatorTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.simulatorTable.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.simulatorTable.setAcceptDrops(False)
        self.simulatorTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.simulatorTable.setAutoFillBackground(False)
        self.simulatorTable.setStyleSheet("font: 18pt \"Sitka Small\";\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.simulatorTable.setLineWidth(0)
        self.simulatorTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.simulatorTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.simulatorTable.setAlternatingRowColors(False)
        self.simulatorTable.setShowGrid(False)
        self.simulatorTable.setGridStyle(QtCore.Qt.NoPen)
        self.simulatorTable.setObjectName("simulatorTable")
        self.simulatorTable.setColumnCount(3)
        self.simulatorTable.setRowCount(self.inst_count)
        
        # for the headers
        for i in range(2): #num of Columns=2
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
            self.simulatorTable.setVerticalHeaderItem(i, item)
        
        for i in range(2): #num of ROws=2
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.simulatorTable.setHorizontalHeaderItem(i, item)
        
        
        #for the cells inside the table with address (i,j)
        
        for i in range(2):
            for j in range(2):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.simulatorTable.setItem(i, j, item)
                
        
        
        
        self.simulatorTable.horizontalHeader().setVisible(True)
        self.simulatorTable.horizontalHeader().setCascadingSectionResizes(False)
        self.simulatorTable.horizontalHeader().setDefaultSectionSize(290)
        self.simulatorTable.horizontalHeader().setHighlightSections(False)
        self.simulatorTable.horizontalHeader().setMinimumSectionSize(100)
        self.simulatorTable.verticalHeader().setVisible(True)
        self.simulatorTable.verticalHeader().setCascadingSectionResizes(True)
        self.simulatorTable.verticalHeader().setHighlightSections(True)
        self.simulatorTable.verticalHeader().setStretchLastSection(False)
        
        self.radioButton()
        
        self.registerTable = QtWidgets.QTableWidget(self.Simulator)
        self.registerTable.setGeometry(QtCore.QRect(660, 110, 360, 731))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.registerTable.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.registerTable.setFont(font)
        self.registerTable.setAlternatingRowColors(False)
        self.registerTable.setObjectName("registerTable")
        self.registerTable.setColumnCount(2)
        self.registerTable.setRowCount(31)
        
        
        self.registerTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.registerTable.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.registerTable.setAcceptDrops(False)
        self.registerTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.registerTable.setAutoFillBackground(False)
        self.registerTable.setLineWidth(0)
        self.registerTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.registerTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.registerTable.setAlternatingRowColors(False)
        self.registerTable.setShowGrid(False)
        self.registerTable.setGridStyle(QtCore.Qt.NoPen)
        
        self.registerTable.setVisible(True)
        
        
        for i in range(31):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.registerTable.setVerticalHeaderItem(i, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setHorizontalHeaderItem(1, item)
        
        for j in range(2):
            for i in range(31):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.registerTable.setItem(i, j, item)
            
        self.registerTable.horizontalHeader().setDefaultSectionSize(150)
        
        #Data Memory Table
        self.dataMem = QtWidgets.QTableWidget(self.Simulator)
        self.dataMem.setGeometry(QtCore.QRect(660, 110, 370, 751))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.dataMem.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.dataMem.setFont(font)
        self.dataMem.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.dataMem.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.dataMem.setObjectName("dataMem")
        
        self.dataMem.setVisible(False)
        
        
        self.dataMem.setColumnCount(2) # Number of columns in data memory table
        self.dataMem.setRowCount(1000) # Number of rows in data mem table
        item = QtWidgets.QTableWidgetItem()
        self.dataMem.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataMem.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataMem.setItem(0, 0, item)
        self.dataMem.horizontalHeader().setDefaultSectionSize(140)
        self.groupBox = QtWidgets.QGroupBox(self.Simulator)
        self.groupBox.setGeometry(QtCore.QRect(660, 860, 370, 91))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.groupBox.setVisible(True)
        
        self.radioButton2()
        
        # Stack memory table
        self.stackMem = QtWidgets.QTableWidget(self.Simulator)
        self.stackMem.setGeometry(QtCore.QRect(660, 110, 370, 751))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.stackMem.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.stackMem.setFont(font)
        self.stackMem.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.stackMem.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.stackMem.setObjectName("stackMem")
        
        self.stackMem.setVisible(False)
        
        
        self.stackMem.setColumnCount(2) # Number of columns in stack mem table
        self.stackMem.setRowCount(1000) # Number of rows in stack mem table
        item = QtWidgets.QTableWidgetItem()
        self.stackMem.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stackMem.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stackMem.setItem(0, 0, item)
        self.stackMem.horizontalHeader().setDefaultSectionSize(140)
        
        # Heap memory Table
        self.heapMem = QtWidgets.QTableWidget(self.Simulator)
        self.heapMem.setGeometry(QtCore.QRect(660, 110, 370, 751))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.heapMem.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.heapMem.setFont(font)
        self.heapMem.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.heapMem.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.heapMem.setObjectName("heapMem")
        
        self.heapMem.setVisible(False)
        
        
        self.heapMem.setColumnCount(2) # Number of columns in heap mem table
        self.heapMem.setRowCount(1000) # Number of rows in heap mem table
        item = QtWidgets.QTableWidgetItem()
        self.heapMem.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.heapMem.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.heapMem.setItem(0, 0, item)
        self.heapMem.horizontalHeader().setDefaultSectionSize(140)
        
        #Step Button
        self.stepBtn = QtWidgets.QPushButton(self.Simulator)
        self.stepBtn.setGeometry(QtCore.QRect(190, 60, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.stepBtn.setFont(font)
        self.stepBtn.setObjectName("stepBtn")
        self.stepBtn.setStyleSheet('QPushButton {background-color: #000000; color: #00aa00; border:3px solid green;}')
        
        # Exit but will be used as Run
        self.exitBtn = QtWidgets.QPushButton(self.Simulator)
        self.exitBtn.setGeometry(QtCore.QRect(370, 60, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.exitBtn.setFont(font)
        self.exitBtn.setObjectName("exitBtn")
        self.exitBtn.setStyleSheet('QPushButton {background-color: #000000; color: #00aa00; border:3px solid green;}')
        
        # Menu bar and Status bar not used
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1064, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # List Widget 1 to display 3, 4, 5
        self.listWidget = QtWidgets.QListWidget(self.Simulator)
        self.listWidget.setGeometry(QtCore.QRect(1050, 110, 600, 500))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.listWidget.setWordWrap(True)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        
        # List Widget 2 to display buffer/stat
        self.listWidget2 = QtWidgets.QListWidget(self.Simulator)
        self.listWidget2.setGeometry(QtCore.QRect(1050, 630, 400, 300))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.listWidget2.setWordWrap(True)
        self.listWidget2.setFont(font)
        self.listWidget2.setObjectName("listWidget2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget2.addItem(item)
        
        # List widget for the input (point 5)
        self.listWidget3 = QtWidgets.QListWidget(self.Simulator)
        self.listWidget3.setGeometry(QtCore.QRect(1470, 630, 400, 300))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.listWidget3.setWordWrap(True)
        self.listWidget3.setFont(font)
        self.listWidget3.setObjectName("listWidget3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget3.addItem(item)
        
        # Checkbox for data forwarding
        self.forwarding_box = QtWidgets.QCheckBox(self.Simulator)
        self.forwarding_box.setGeometry(QtCore.QRect(1700, 110, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.forwarding_box.setFont(font)
        self.forwarding_box.setObjectName("forwarding_box")
        
        # Checkbox for register print
        self.register_box = QtWidgets.QCheckBox(self.Simulator)
        self.register_box.setGeometry(QtCore.QRect(1700, 140, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.register_box.setFont(font)
        self.register_box.setObjectName("register_box")
        
        # Take input
        self.inputButton = QtWidgets.QPushButton(self.Simulator)
        self.inputButton.setGeometry(QtCore.QRect(1660, 190, 210, 30))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.inputButton.setFont(font)
        self.inputButton.setObjectName("inputButton")
        self.inputButton.setStyleSheet('QPushButton {background-color: #000000; color: #00aa00; border:3px solid green;}')
        
        #self.simulatorTable.selectRow(0) # Highlighting the very first instruction
        
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.stepBtn.clicked.connect(self.step_clicked) #call step clicked
        self.exitBtn.clicked.connect(self.run_clicked) # Run clicked
        self.forwarding_box.stateChanged.connect(self.forwarding_checked) # Forwarding Checked
        self.register_box.stateChanged.connect(self.register_checked) # Forwarding Checked
        self.inputButton.clicked.connect(self.take_input) # When taking input
#-----------------------------------------------------------------------------------------------

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Simulator.setTitle(_translate("MainWindow", "SIMULATOR"))
        
        #
        #Put Number of instructions here in for loop
        #
        for i in range(2): 
            item = self.simulatorTable.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", str(i+1)))
            
        
        
        
        item = self.simulatorTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PC"))
        item = self.simulatorTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Machine Code"))
        __sortingEnabled = self.simulatorTable.isSortingEnabled()
        self.simulatorTable.setSortingEnabled(False)
        
        #
        #here PC and Machine Code
        #
        pc = 0x0
        for i in range(self.inst_count):
            item = QtWidgets.QTableWidgetItem(str(hex(pc)))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.simulatorTable.setItem(i, 0, item)
            
            item = QtWidgets.QTableWidgetItem(str(pipelining.instructions[pc]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.simulatorTable.setItem(i, 1, item)
            pc += 4

        
        
        self.simulatorTable.setSortingEnabled(__sortingEnabled)
        self.regButton.setText(_translate("MainWindow", "Registers"))
        self.memButton.setText(_translate("MainWindow", "Memory"))
        
        item = self.registerTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.registerTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.registerTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.registerTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        item = self.registerTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "4"))
        item = self.registerTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.registerTable.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.registerTable.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.registerTable.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.registerTable.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.registerTable.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.registerTable.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.registerTable.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.registerTable.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.registerTable.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.registerTable.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16"))
        item = self.registerTable.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "17"))
        item = self.registerTable.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "18"))
        item = self.registerTable.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "19"))
        item = self.registerTable.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "20"))
        item = self.registerTable.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "21"))
        item = self.registerTable.verticalHeaderItem(21)
        item.setText(_translate("MainWindow", "22"))
        item = self.registerTable.verticalHeaderItem(22)
        item.setText(_translate("MainWindow", "23"))
        item = self.registerTable.verticalHeaderItem(23)
        item.setText(_translate("MainWindow", "24"))
        item = self.registerTable.verticalHeaderItem(24)
        item.setText(_translate("MainWindow", "25"))
        item = self.registerTable.verticalHeaderItem(25)
        item.setText(_translate("MainWindow", "26"))
        item = self.registerTable.verticalHeaderItem(26)
        item.setText(_translate("MainWindow", "27"))
        item = self.registerTable.verticalHeaderItem(27)
        item.setText(_translate("MainWindow", "28"))
        item = self.registerTable.verticalHeaderItem(28)
        item.setText(_translate("MainWindow", "29"))
        item = self.registerTable.verticalHeaderItem(29)
        item.setText(_translate("MainWindow", "30"))
        item = self.registerTable.verticalHeaderItem(30)
        item.setText(_translate("MainWindow", "31"))
        item = self.registerTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "zero"))
        item = self.registerTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "0x00000000"))
        __sortingEnabled = self.registerTable.isSortingEnabled()
        self.registerTable.setSortingEnabled(False)
        
        
        item = self.registerTable.item(0, 0)
        item.setText(_translate("MainWindow", "ra (x1)"))
        item = self.registerTable.item(1, 0)
        item.setText(_translate("MainWindow", "sp (x2)"))
        item = self.registerTable.item(2, 0)
        item.setText(_translate("MainWindow", "gp (x3)"))
        item = self.registerTable.item(3, 0)
        item.setText(_translate("MainWindow", "tp (x4)"))
        item = self.registerTable.item(4, 0)
        item.setText(_translate("MainWindow", "t0 (x5)"))
        item = self.registerTable.item(5, 0)
        item.setText(_translate("MainWindow", "t1 (x6)"))
        item = self.registerTable.item(6, 0)
        item.setText(_translate("MainWindow", "t2 (x7)"))
        item = self.registerTable.item(7, 0)
        item.setText(_translate("MainWindow", "s0 (x8)"))
        item = self.registerTable.item(8, 0)
        item.setText(_translate("MainWindow", "s1 (x9)"))
        item = self.registerTable.item(9, 0)
        item.setText(_translate("MainWindow", "a0 (x10)"))
        item = self.registerTable.item(10, 0)
        item.setText(_translate("MainWindow", "a1 (x11)"))
        item = self.registerTable.item(11, 0)
        item.setText(_translate("MainWindow", "a2 (12)"))
        item = self.registerTable.item(12, 0)
        item.setText(_translate("MainWindow", "a3 (13)"))
        item = self.registerTable.item(13, 0)
        item.setText(_translate("MainWindow", "a4 (14)"))
        item = self.registerTable.item(14, 0)
        item.setText(_translate("MainWindow", "a5 (15)"))
        item = self.registerTable.item(15, 0)
        item.setText(_translate("MainWindow", "a6 (a16)"))
        item = self.registerTable.item(16, 0)
        item.setText(_translate("MainWindow", "a7 (a17)"))
        item = self.registerTable.item(17, 0)
        item.setText(_translate("MainWindow", "s2 (x18)"))
        item = self.registerTable.item(18, 0)
        item.setText(_translate("MainWindow", "s3 (x19)"))
        item = self.registerTable.item(19, 0)
        item.setText(_translate("MainWindow", "s4 (x20)"))
        item = self.registerTable.item(20, 0)
        item.setText(_translate("MainWindow", "s5 (x21)"))
        item = self.registerTable.item(21, 0)
        item.setText(_translate("MainWindow", "s6 (x22)"))
        item = self.registerTable.item(22, 0)
        item.setText(_translate("MainWindow", "s7 (x23)"))
        item = self.registerTable.item(23, 0)
        item.setText(_translate("MainWindow", "s8 (x24)"))
        item = self.registerTable.item(24, 0)
        item.setText(_translate("MainWindow", "s9 (x25)"))
        item = self.registerTable.item(25, 0)
        item.setText(_translate("MainWindow", "s10 (x26)"))
        item = self.registerTable.item(26, 0)
        item.setText(_translate("MainWindow", "s11 (x27)"))
        item = self.registerTable.item(27, 0)
        item.setText(_translate("MainWindow", "t3 (x28)"))
        item = self.registerTable.item(28, 0)
        item.setText(_translate("MainWindow", "t4 (x29)"))
        item = self.registerTable.item(29, 0)
        item.setText(_translate("MainWindow", "t5 (x30)"))
        item = self.registerTable.item(30, 0)
        item.setText(_translate("MainWindow", "t6 (x31)"))
        
        self.registerTable.setSortingEnabled(__sortingEnabled)
        
        item = self.dataMem.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.dataMem.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        __sortingEnabled = self.dataMem.isSortingEnabled()
        self.dataMem.setSortingEnabled(False)
        
        # Setting the values of data memory equal to 0
        for i in range(1000):
            item = QtWidgets.QTableWidgetItem(str(hex((0x10000000+(4*i)))))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.dataMem.setItem(i, 0, item)
            
            item = QtWidgets.QTableWidgetItem(str(pipelining.memory[int((0x10000000+(4*i)))]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.dataMem.setItem(i, 1, item)
            
        self.dataMem.setSortingEnabled(__sortingEnabled)
        self.radioButton.setText(_translate("MainWindow", "Data"))
        self.radioButton_2.setText(_translate("MainWindow", "Stack"))
        self.radioButton_3.setText(_translate("MainWindow", "Heap"))
        item = self.stackMem.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.stackMem.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        __sortingEnabled = self.stackMem.isSortingEnabled()
        self.stackMem.setSortingEnabled(False)
        
        # Setting the values of stack memory equal to 0
        for i in range(1000):
            item = QtWidgets.QTableWidgetItem(str(hex((0x7FFFFFFC-(4*i)))))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.stackMem.setItem(i, 0, item)
            
            item = QtWidgets.QTableWidgetItem(str(pipelining.memory[int((0x7FFFFFFC-(4*i)))]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.stackMem.setItem(i, 1, item)
       
        self.stackMem.setSortingEnabled(__sortingEnabled)
        item = self.heapMem.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "0"))
        item = self.heapMem.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "0"))
        __sortingEnabled = self.heapMem.isSortingEnabled()
        self.heapMem.setSortingEnabled(False)
        
        # Setting the values of heap memory equal to 0
        for i in range(1000):
            item = QtWidgets.QTableWidgetItem(str(hex((0x10007FE8+(4*i)))))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.heapMem.setItem(i, 0, item)
            
            item = QtWidgets.QTableWidgetItem(QTableWidgetItem(str(pipelining.memory[int((0x10007FE8+(4*i)))])))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.heapMem.setItem(i, 1, item)
        

        self.heapMem.setSortingEnabled(__sortingEnabled)
        
        # all registers = 0
        for i in range(0, 31):
            self.registerTable.setItem(i, 1, QTableWidgetItem(str(0)))
            
        self.stepBtn.setText(_translate("MainWindow", "Step"))
        self.exitBtn.setText(_translate("MainWindow", "Run"))
        
        
        
        # For list widget
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", ""))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        
        # For listwidget 2
        __sortingEnabled = self.listWidget2.isSortingEnabled()
        self.listWidget2.setSortingEnabled(False)
        item = self.listWidget2.item(0)
        item.setText(_translate("MainWindow", ""))
        self.listWidget2.setSortingEnabled(__sortingEnabled)
        
        # for input listwidget 3
        __sortingEnabled = self.listWidget3.isSortingEnabled()
        self.listWidget3.setSortingEnabled(False)
        item = self.listWidget3.item(0)
        item.setText(_translate("MainWindow", ""))
        self.listWidget3.setSortingEnabled(__sortingEnabled)
        
        # For forwarding checkbox
        self.forwarding_box.setText(_translate("MainWindow", "Forwarding"))
        
        # For register checkbox
        self.register_box.setText(_translate("MainWindow", "Registers"))
        
        # For inputbutton
        self.inputButton.setText(_translate("MainWindow", "Instruction Number"))
        
        
    def step_clicked(self): # Function for self button
        if pipelining.register_counter != -2: #Only do things if there are instructions left
            x = len(pipelining.branch_predicted)
            y = len(pipelining.data_hazard_path)
            pipelining.main1() # Run the main function
            self.listWidget.clear() # clear the list widget
            self.listWidget2.clear() # 
            self.listWidget3.clear()
            #self.simulatorTable.selectRow(self.inst_num) # To highlight the current instruction
            # Update the registers
            if self.register_change == 1:
                for i in range(31):
                    self.registerTable.setItem(i, 1, QTableWidgetItem(str(pipelining.registers[i+1])))
            
            # Update the data memory
            for i in range(1000):
                self.dataMem.setItem(i, 1, QTableWidgetItem(str(pipelining.memory[int((0x10000000+(4*i)))])))
            
            # Updating the stack memory
            for i in range(1000):
                self.stackMem.setItem(i, 1, QTableWidgetItem(str(pipelining.memory[int((0x7FFFFFFC-(4*i)))])))
                
            # Updating the heap memory
            for i in range(1000):
                self.heapMem.setItem(i, 1, QTableWidgetItem(str(pipelining.memory[int((0x10007FE8+(4*i)))])))
            
            # 
            fe = (pipelining.status_to_pc["Fetch"]) // 4
            d = (pipelining.status_to_pc["Decode"]) // 4
            e = (pipelining.status_to_pc["Execute"]) // 4
            m = (pipelining.status_to_pc["Memory_Write"]) // 4
            r = (pipelining.status_to_pc["Register_Update"]) // 4
            
            item = QtWidgets.QTableWidgetItem(str("Fetch"))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.simulatorTable.setItem(fe, 2, item)
            
            item = QtWidgets.QTableWidgetItem(str("Decode"))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.simulatorTable.setItem(d, 2, item)
            
            item = QtWidgets.QTableWidgetItem(str("Execute"))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.simulatorTable.setItem(e, 2, item)
            
            item = QtWidgets.QTableWidgetItem(str("Memory"))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.simulatorTable.setItem(m, 2, item)
            
            item = QtWidgets.QTableWidgetItem(str("Register"))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.simulatorTable.setItem(r, 2, item)
            
            # For buffers or stats in listwidget
            if pipelining.register_counter == -2:
                pipelining.print_stmt()
                for el in pipelining.stats:
                    item = QListWidgetItem(str(el))
                    self.listWidget.addItem(item)
                pipelining.print_stmt()
                for i in range(self.inst_count):
                    item = QtWidgets.QTableWidgetItem(str( ))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.simulatorTable.setItem(i, 2, item)
            elif pipelining.register_counter != -2:
                for el in pipelining.buffers:
                    item = QListWidgetItem(str(el))
                    self.listWidget.addItem(item)
            
            # 3, 4, 5 in listwidget1
            if len(pipelining.branch_predicted) != x:
                item = QListWidgetItem(str(pipelining.branch_predicted[-1]))
                self.listWidget2.addItem(item)
            if len(pipelining.data_hazard_path) != y:
                item = QListWidgetItem(str(pipelining.data_hazard_path[-1]))
                self.listWidget2.addItem(item)
                
            

                
            #self.inst_num = (pipelining.PC) // 4 # update pc
        else:
            return
    
    
    def run_clicked(self):
        while pipelining.register_counter != -2:
            pipelining.main1() # Run the main
            #self.inst_num = (pipelining.PC) // 4 # update pc
            
        self.listWidget.clear() # clear the list widget
        self.listWidget2.clear() # 
        self.listWidget3.clear()
        
        # Update the registers
        for i in range(31):
            self.registerTable.setItem(i, 1, QTableWidgetItem(str(pipelining.registers[i+1])))
        
        # Update the data memory
        for i in range(1000):
            self.dataMem.setItem(i, 1, QTableWidgetItem(str(pipelining.memory[int((0x10000000+(4*i)))])))
        
        # Updating the stack memory
        for i in range(1000):
            self.stackMem.setItem(i, 1, QTableWidgetItem(str(pipelining.memory[int((0x7FFFFFFC-(4*i)))])))
            
        # Updating the heap memory
        for i in range(1000):
            self.heapMem.setItem(i, 1, QTableWidgetItem(str(pipelining.memory[int((0x10007FE8+(4*i)))])))
        
        pipelining.print_stmt()
        # stat in listwidget
        for el in pipelining.stats:
            item = QListWidgetItem(str(el))
            self.listWidget.addItem(item)
        
        # 
        
        
        for i in range(self.inst_count):
            item = QtWidgets.QTableWidgetItem(str( ))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.simulatorTable.setItem(i, 2, item)

        
        

        
    def radioButton(self):
        self.regButton = QtWidgets.QRadioButton(self.Simulator)
        self.regButton.setGeometry(QtCore.QRect(740, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.regButton.setFont(font)
        self.regButton.setObjectName("regButton")
        self.regButton.toggled.connect(self.onRadioButton)
        
        
        self.memButton = QtWidgets.QRadioButton(self.Simulator)
        self.memButton.setGeometry(QtCore.QRect(890, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        self.memButton.setChecked(True)
        font.setPointSize(10)
        self.memButton.setFont(font)
        self.memButton.setObjectName("memButton")
        self.memButton.toggled.connect(self.onRadioButton)
        
    def onRadioButton(self):

        sendBtn = self.sender()
        
        if sendBtn.isChecked():
            if sendBtn.objectName()=="memButton":
                self.dataMem.setVisible(True)
                self.groupBox.setVisible(True)
                
                self.registerTable.setVisible(False)
            #elif sendBtn.text()=="regButton":
            else:
                self.dataMem.setVisible(False)
                self.heapMem.setVisible(False)
                self.stackMem.setVisible(False)
                self.groupBox.setVisible(False)
                self.radioButton.setChecked(True)
                self.registerTable.setVisible(True)
                
    def radioButton2(self):
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(self.onRadioButton2)
        self.radioButton.setChecked(True)
        
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(120, 30, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.onRadioButton2)
        
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(230, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.toggled.connect(self.onRadioButton2)
        
        
        
    def onRadioButton2(self):

        sendBtn = self.sender()
        
        if sendBtn.isChecked():
            
            if sendBtn.objectName()=="radioButton_2":
                self.dataMem.setVisible(False)
                self.registerTable.setVisible(False)
                self.heapMem.setVisible(False)
                self.stackMem.setVisible(True)
                
            elif sendBtn.objectName()=="radioButton_3":
                self.dataMem.setVisible(False)
                self.registerTable.setVisible(False)
                self.heapMem.setVisible(True)
                self.stackMem.setVisible(False)
            
            else:
                self.dataMem.setVisible(True)
                self.registerTable.setVisible(False)
                self.heapMem.setVisible(False)
                self.stackMem.setVisible(False)      

    def forwarding_checked(self, checked):
        if checked:
            pipelining.data_frwd = 1
            pipelining.stall = False
        else:
            pipelining.data_frwd = 0
            pipelining.stall = True
    
    def register_checked(self, checked):
        if checked:
            self.register_change = 1
        else:
            self.register_change = 0
            
    
    def take_input(self):
        inst_number, done = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter the instruction number:')
        if done:
            pc = (inst_number-1) * 4
            x = pipelining.pc_to_status[pc]
            item = QListWidgetItem(str(x))
            self.listWidget3.addItem(item)
            print("input taken")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())