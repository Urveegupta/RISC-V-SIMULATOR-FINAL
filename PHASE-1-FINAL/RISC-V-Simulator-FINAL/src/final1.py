from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
import temp3




class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.inst_count = len(temp3.instructions)
        self.inst_num = 1
        self.clock_count = 0
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 1500)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Simulator = QtWidgets.QGroupBox(self.centralwidget)
        self.Simulator.setGeometry(QtCore.QRect(10, 0, 1500, 1500))
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
        self.simulatorTable.setColumnCount(2)
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
            
        """item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.simulatorTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.simulatorTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.simulatorTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.simulatorTable.setHorizontalHeaderItem(1, item)"""
        
        
        #for the cells inside the table with address (i,j)
        
        for i in range(2):
            for j in range(2):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.simulatorTable.setItem(i, j, item)
                
                
        """item = QtWidgets.QTableWidgetItem()
        self.simulatorTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.simulatorTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.simulatorTable.setItem(1, 1, item)"""
        
        
        
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
        
        """item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(30, item)"""
        
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setHorizontalHeaderItem(1, item)
        
        for j in range(2):
            for i in range(31):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.registerTable.setItem(i, j, item)
            
        
        """item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(14, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(15, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(16, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(17, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(18, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(19, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(20, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(21, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(22, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(23, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(24, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(25, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(26, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(27, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(28, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(29, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setItem(30, 0, item)"""
        
        
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
        
        # List Widget to display the messages
        self.listWidget = QtWidgets.QListWidget(self.Simulator)
        self.listWidget.setGeometry(QtCore.QRect(1050, 110, 400, 500))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.listWidget.setWordWrap(True)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        
        # Label for clock count
        self.clockLabel = QtWidgets.QLabel(self.Simulator)
        self.clockLabel.setGeometry(QtCore.QRect(1060, 710, 390, 50))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        self.clockLabel.setFont(font)
        self.clockLabel.setObjectName("clockLabel")
        self.clockLabel.setStyleSheet('QLabel {background-color: #000000; color: #00aa00; border:3px solid green;}')
        
        
        self.simulatorTable.selectRow(0) # Highlighting the very first instruction
        
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.stepBtn.clicked.connect(self.step_clicked) #call step clicked
        self.exitBtn.clicked.connect(self.run_clicked) # Run clicked
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
            
            
        """item = self.simulatorTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))"""
        
        
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
            
            item = QtWidgets.QTableWidgetItem(str(temp3.instructions[pc]))
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
        
        
        
        ######
        
        ##### change value of t6 (x31) in below for loop
        ##### for displaying the value at the (i)th register
        #####
        #for i in range(31):
            #item = self.registerTable.item(i, 1)
            #item.setText(_translate("MainWindow", "t6 (x31)"))
        
        
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
            
            item = QtWidgets.QTableWidgetItem(str(temp3.memory[int((0x10000000+(4*i)))]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.dataMem.setItem(i, 1, item)
            
        #item = self.dataMem.item(0, 0)
        #item.setText(_translate("MainWindow", "xxx"))
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
            
            item = QtWidgets.QTableWidgetItem(str(temp3.memory[int((0x7FFFFFFC-(4*i)))]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.stackMem.setItem(i, 1, item)
       
        #item = self.stackMem.item(0, 0)
        #item.setText(_translate("MainWindow", "xxxxx"))
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
            
            item = QtWidgets.QTableWidgetItem(QTableWidgetItem(str(temp3.memory[int((0x10007FE8+(4*i)))])))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.heapMem.setItem(i, 1, item)
        
        #item = self.heapMem.item(0, 0)
        #item.setText(_translate("MainWindow", "xxxxxxxxx"))
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
        
        # For clock count
        self.clockLabel.setText(_translate("MainWindow", "Clock Cycle Count = 0"))
        
        
    def step_clicked(self): # Function for self button
        if self.inst_num < self.inst_count: #Only do things if there are instructions left
            temp3.main() # Run the main function
            self.clock_count += 1 #increment clock cycle
            self.listWidget.clear() # clear the list widget
            self.simulatorTable.selectRow(self.inst_num) # To highlight the current instruction
            # Update the registers
            for i in range(31):
                self.registerTable.setItem(i, 1, QTableWidgetItem(str(temp3.registers[i+1])))
            
            # Update the data memory
            for i in range(1000):
                self.dataMem.setItem(i, 1, QTableWidgetItem(str(temp3.memory[int((0x10000000+(4*i)))])))
            
            # Updating the stack memory
            for i in range(1000):
                self.stackMem.setItem(i, 1, QTableWidgetItem(str(temp3.memory[int((0x7FFFFFFC-(4*i)))])))
                
            # Updating the heap memory
            for i in range(1000):
                self.heapMem.setItem(i, 1, QTableWidgetItem(str(temp3.memory[int((0x10007FE8+(4*i)))])))
            
            # To display the messages
            for el in temp3.message:
                item = QListWidgetItem(str(el))
                self.listWidget.addItem(item)
            
            # Display clock count
            self.clockLabel.setText("Clock Cycle Count = " + str(self.clock_count))
                
            self.inst_num = (temp3.PC) // 4 # update pc
        else:
            return
    
    def run_clicked(self):
        while self.inst_num < self.inst_count - 1:
            temp3.main() # Run the main
            self.clock_count += 1 #increment clock cycle
            self.inst_num = (temp3.PC) // 4 # update pc
            
        self.listWidget.clear() # clear the list widget
        
        # Update the registers
        for i in range(31):
            self.registerTable.setItem(i, 1, QTableWidgetItem(str(temp3.registers[i+1])))
        
        # Update the data memory
        for i in range(1000):
            self.dataMem.setItem(i, 1, QTableWidgetItem(str(temp3.memory[int((0x10000000+(4*i)))])))
        
        # Updating the stack memory
        for i in range(1000):
            self.stackMem.setItem(i, 1, QTableWidgetItem(str(temp3.memory[int((0x7FFFFFFC-(4*i)))])))
            
        # Updating the heap memory
        for i in range(1000):
            self.heapMem.setItem(i, 1, QTableWidgetItem(str(temp3.memory[int((0x10007FE8+(4*i)))])))
        
        # To display the messages
        for el in temp3.message:
            item = QListWidgetItem(str(el))
            self.listWidget.addItem(item)
        
        # Display clock count
        self.clockLabel.setText("Clock Cycle Count = " + str(self.clock_count))
        
        # Highlight the last one
        self.simulatorTable.selectRow(self.inst_num)
        
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())