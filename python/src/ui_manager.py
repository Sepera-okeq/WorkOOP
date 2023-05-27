from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QGraphicsScene, QGraphicsView
from PyQt6.QtWidgets import QApplication, QLabel, QMenuBar, QMenu, QStatusBar, QTextEdit, QHBoxLayout
from PyQt6.QtGui import QAction, QIcon
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPen, QColor

from core.point2d import Point2D

from ui import Ui_MainWindow
from qframelesswindow import FramelessMainWindow, FramelessDialog

class MainWidget(FramelessMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.count_dots = 2
		
		self.windowEffect.setAcrylicEffect(self.winId(), "F2F2F299")
		self.ui.stackedWidget.setStyleSheet(
		"""
QWidget {
	background: #f3f3f3;
	color: rgb(0, 0, 0);
	font-size: 17px;
	font-family: &quot;Segoe UI Variable Small&quot;, serif;
	font-weight: 400;
}

/*MENU*/
QMenuBar {
	background-color: transparent;
	color: rgba(0, 0, 0);
	padding: 10px;
	font-size: 17px;
	font-family: &quot;Segoe UI Variable Small&quot;, serif;
	font-weight: 400;
}

QMenuBar::item {
	background-color: transparent;
	padding: 10px 13px;
	margin-left: 5px;
	border-radius: 5px;
}

QMenuBar::item:selected {
	background-color: rgb(0, 0, 0, 10);
}

QMenuBar::item:pressed {
	background-color: rgb(0, 0, 0, 7);
	color: rgb(0, 0, 0, 150);
}

QMenu {
	background-color: #f3f3f3;
	padding-left: 1px;
	padding-top: 1px;
	border-radius: 5px;
	border: 1px solid rgb(0, 0, 0, 13);
}

QMenu::item {
    background-color: transparent;
	padding: 5px 15px;
	border-radius: 5px;
	min-width: 60px;
	margin: 3px;
}

QMenu::item:selected {
	background-color: rgb(0, 0, 0, 10);
}

QMenu::item:pressed {
	background-color: rgb(0, 0, 0, 7);
}

QMenu::right-arrow {
	image: url(:/newPrefix/img light/TreeViewClose.png);
	min-width: 40px;
	min-height: 18px;
}

QMenuBar:disabled {
	color: rgb(0, 0, 0, 150);
}

QMenu::item:disabled {
	color: rgb(0, 0, 0, 150);
	background-color: transparent;
}

/*PUSHBUTTON*/
QPushButton {
	background-color: rgb(0, 0, 0, 3);
	border: 1px solid rgb(0, 0, 0, 13);
	border-radius: 7px;
	min-height: 38px;
	max-height: 38px;
}

QPushButton:hover {
	background-color: rgb(0, 0, 0, 7);
	border: 1px solid rgb(0, 0, 0, 13);
}

QPushButton::pressed {
	color: rgb(0, 0, 0, 150);
}

QPushButton::disabled {
	color: rgb(0, 0, 0, 110);
	background-color: rgb(0, 0, 0, 13);
	border: 1px solid rgb(0, 0, 0, 5);
}

/*RADIOBUTTON*/
QRadioButton {
	min-height: 30px;
	max-height: 30px;
}

QRadioButton::indicator {
	width: 22px;
	height: 22px;
	border-radius: 13px;
	border: 2px solid #999999;
	background-color: rgb(0, 0, 0, 5);
	margin-right: 5px;
}

QRadioButton::indicator:hover {
	background-color: rgb(0, 0, 0, 0);
}

QRadioButton::indicator:pressed {
	background-color: rgb(0, 0, 0, 5);
	border: 2px solid #bbbbbb;
	image: url(:/RadioButton/img light/RadioButton.png);
}

QRadioButton::indicator:checked {
	background-color: &quot;+accent+&quot;;
	border: 2px solid &quot;+accent+&quot;;
	image: url(:/RadioButton/img light/RadioButton.png);
	color: rgb(255, 255, 255);
}

QRadioButton::indicator:checked:hover {
	image: url(:/RadioButton/img light/RadioButtonHover.png);
}

QRadioButton::indicator:checked:pressed {
	image: url(:/RadioButton/img light/RadioButtonPressed.png);
}

QRadioButton:disabled {
	color: rgb(0, 0, 0, 110);
}

QRadioButton::indicator:disabled {
	border: 2px solid #bbbbbb;
	background-color: rgb(0, 0, 0, 0);
}

/*CHECKBOX*/
QCheckBox {
	min-height: 30px;
	max-height: 30px;
}

QCheckBox::indicator {
	width: 22px;
	height: 22px;
	border-radius: 5px;
	border: 2px solid #999999;
	background-color: rgb(0, 0, 0, 0);
	margin-right: 5px;
}

QCheckBox::indicator:hover {
	background-color: rgb(0, 0, 0, 15);
}

QCheckBox::indicator:pressed {
	background-color: rgb(0, 0, 0, 24);
	border: 2px solid #bbbbbb;
}

QCheckBox::indicator:checked {
	background-color: &quot;+accent+&quot;;
	border: 2px solid &quot;+accent+&quot;;
	image: url(:/CheckBox/img light/CheckBox.png);
	color: rgb(255, 255, 255);
}

QCheckBox::indicator:checked:pressed {
	image: url(:/CheckBox/img light/CheckBoxPressed.png);
}

QCheckBox:disabled {
	color: rgb(0, 0, 0, 110);
}

QCheckBox::indicator:disabled {
	border: 2px solid #bbbbbb;
	background-color: rgb(0, 0, 0, 0);
}

/*GROUPBOX*/
QGroupBox {
	border-radius: 5px;
	border: 1px solid rgb(0, 0, 0, 13);
	margin-top: 36px;
}

QGroupBox::title {
	subcontrol-origin: margin;
	subcontrol-position: top left;
    background-color: rgb(0, 0, 0, 10);
	padding: 7px 15px;
	margin-left: 5px;
	border-top-left-radius: 5px;
	border-top-right-radius: 5px;
}

QGroupBox::title::disabled {
	color: rgb(0, 0, 0, 150);
}

/*TABWIDGET*/
QTabWidget {
}

QWidget {
	border-radius: 5px;
}

QTabWidget::pane {
	border: 1px solid rgb(0, 0, 0, 13);
	border-radius: 5px;
}

QTabWidget::tab-bar {
	left: 5px;
}

QTabBar::tab {
    background-color: rgb(0, 0, 0, 0);
	padding: 7px 15px;
	margin-right: 2px;
}

QTabBar::tab:hover {
	background-color: rgb(0, 0, 0, 13);
	border-top-left-radius: 5px;
	border-top-right-radius: 5px;
}

QTabBar::tab:selected {
    background-color: rgb(0, 0, 0, 10);
	border-top-left-radius: 5px;
	border-top-right-radius: 5px;
}

QTabBar::tab:disabled {
	color: rgb(0, 0, 0, 150)
}

/*SPINBOX*/
QSpinBox {
	background-color: rgb(0, 0, 0, 7);
	border: 1px solid rgb(0, 0, 0, 13);
	border-radius: 5px;
	padding-left: 10px;
	min-height: 38px;
	max-height: 38px;
	min-width: 100px;
	border-bottom: 1px solid rgb(0, 0, 0, 100);
}

QSpinBox:hover {
	background-color: rgb(0, 0, 0, 13);
	border: 1px solid rgb(0, 0, 0, 13);
	border-bottom: 1px solid rgb(0, 0, 0, 100);
}

QSpinBox::focus {
	background-color: rgb(0, 0, 0, 5);
	border: 1px solid rgb(0, 0, 0, 10);
	color: rgb(0, 0, 0, 200);
	border-bottom: 2px solid &quot;+accent+&quot;;
}

QSpinBox::up-button {
	image: url(:/SpinBox/img light/SpinBoxUp.png);
	background-color: rgb(0, 0, 0, 0);
	border: 1px solid rgb(0, 0, 0, 0);
	border-radius: 4px;
	margin-top: 1px;
	margin-bottom: 1px;
	margin-right: 2px;
	min-width: 30px;
	max-width: 30px;
	min-height: 20px;
}

QSpinBox::up-button:hover {
	background-color: rgb(0, 0, 0, 10);
}

QSpinBox::up-button:pressed {
	background-color: rgb(0, 0, 0, 5);
}

QSpinBox::down-button {
	image: url(:/SpinBox/img light/SpinBoxDown.png);
	background-color: rgb(0, 0, 0, 0);
	border: 1px solid rgb(0, 0, 0, 0);
	border-radius: 4px;
	margin-top: 1px;
	margin-bottom: 1px;
	margin-right: 2px;
	min-width: 30px;
	max-width: 30px;
	min-height: 20px;
}

QSpinBox::down-button:hover {
	background-color: rgb(0, 0, 0, 10);
}

QSpinBox::down-button:pressed {
	background-color: rgb(0, 0, 0, 5);
}

QSpinBox::drop-down {
	background-color: transparent;
    width: 50px;
}

QSpinBox:disabled {
	color: rgb(0, 0, 0, 110);
	background-color: rgb(0, 0, 0, 13);
	border: 1px solid rgb(0, 0, 0, 5);
}

QSpinBox::up-button:disabled {
	image: url(:/SpinBox/img light/SpinBoxUpDisabled.png);
}

QSpinBox::down-button:disabled {
	image: url(:/SpinBox/img light/SpinBoxDownDisabled.png);
}

/*DOUBLESPINBOX*/
QDoubleSpinBox {
	background-color: rgb(0, 0, 0, 7);
	border: 1px solid rgb(0, 0, 0, 13);
	border-radius: 5px;
	padding-left: 10px;
	min-height: 38px;
	max-height: 38px;
	min-width: 100px;
	border-bottom: 1px solid rgb(0, 0, 0, 100);
}

QDoubleSpinBox:hover {
	background-color: rgb(0, 0, 0, 13);
	border: 1px solid rgb(0, 0, 0, 13);
	border-bottom: 1px solid rgb(0, 0, 0, 100);
}

QDoubleSpinBox::focus {
	background-color: rgb(0, 0, 0, 5);
	border: 1px solid rgb(0, 0, 0, 10);
	color: rgb(0, 0, 0, 200);
	border-bottom: 2px solid &quot;+accent+&quot;;
}

QDoubleSpinBox::up-button {
	image: url(:/SpinBox/img light/SpinBoxUp.png);
	background-color: rgb(0, 0, 0, 0);
	border: 1px solid rgb(0, 0, 0, 0);
	border-radius: 4px;
	margin-top: 1px;
	margin-bottom: 1px;
	margin-right: 2px;
	min-width: 30px;
	max-width: 30px;
	min-height: 20px;
}

QDoubleSpinBox::up-button:hover {
	background-color: rgb(0, 0, 0, 10);
}

QDoubleSpinBox::up-button:pressed {
	background-color: rgb(0, 0, 0, 5);
}

QDoubleSpinBox::down-button {
	image: url(:/SpinBox/img light/SpinBoxDown.png);
	background-color: rgb(0, 0, 0, 0);
	border: 1px solid rgb(0, 0, 0, 0);
	border-radius: 4px;
	margin-top: 1px;
	margin-bottom: 1px;
	margin-right: 2px;
	min-width: 30px;
	max-width: 30px;
	min-height: 20px;
}

QDoubleSpinBox::down-button:hover {
	background-color: rgb(0, 0, 0, 10);
}

QDoubleSpinBox::down-button:pressed {
	background-color: rgb(0, 0, 0, 5);
}

QDoubleSpinBox::drop-down {
	background-color: transparent;
    width: 50px;
}

QDoubleSpinBox:disabled {
	color: rgb(0, 0, 0, 110);
	background-color: rgb(0, 0, 0, 13);
	border: 1px solid rgb(0, 0, 0, 5);
}

QDoubleSpinBox::up-button:disabled {
	image: url(:/SpinBox/img light/SpinBoxUpDisabled.png);
}

QDoubleSpinBox::down-button:disabled {
	image: url(:/SpinBox/img light/SpinBoxDownDisabled.png);
}

/*DATETIMEEDIT*/
QDateTimeEdit {
	background-color: rgb(0, 0, 0, 7);
	border: 1px solid rgb(0, 0, 0, 13);
	border-radius: 5px;
	padding-left: 10px;
	min-height: 38px;
	max-height: 38px;
	min-width: 100px;
	border-bottom: 1px solid rgb(0, 0, 0, 100);
}

QDateTimeEdit:hover {
	background-color: rgb(0, 0, 0, 13);
	border: 1px solid rgb(0, 0, 0, 13);
	border-bottom: 1px solid rgb(0, 0, 0, 100);
}

QDateTimeEdit::focus {
	background-color: rgb(0, 0, 0, 5);
	border: 1px solid rgb(0, 0, 0, 10);
	color: rgb(0, 0, 0, 200);
	border-bottom: 2px solid &quot;+accent+&quot;;
}

QDateTimeEdit::up-button {
	image: url(:/SpinBox/img light/SpinBoxUp.png);
	background-color: rgb(0, 0, 0, 0);
	border: 1px solid rgb(0, 0, 0, 0);
	border-radius: 4px;
	margin-top: 1px;
	margin-bottom: 1px;
	margin-right: 2px;
	min-width: 30px;
	max-width: 30px;
	min-height: 20px;
}

QDateTimeEdit::up-button:hover {
	background-color: rgb(0, 0, 0, 10);
}

QDateTimeEdit::up-button:pressed {
	background-color: rgb(0, 0, 0, 5);
}

QDateTimeEdit::down-button {
	image: url(:/SpinBox/img light/SpinBoxDown.png);
	background-color: rgb(0, 0, 0, 0);
	border: 1px solid rgb(0, 0, 0, 0);
	border-radius: 4px;
	margin-top: 1px;
	margin-bottom: 1px;
	margin-right: 2px;
	min-width: 30px;
	max-width: 30px;
	min-height: 20px;
}

QDateTimeEdit::down-button:hover {
	background-color: rgb(0, 0, 0, 10);
}

QDateTimeEdit::down-button:pressed {
	background-color: rgb(0, 0, 0, 5);
}

QDateTimeEdit::drop-down {
	background-color: transparent;
    width: 50px;
}

QDateTimeEdit:disabled {
	color: rgb(0, 0, 0, 110);
	background-color: rgb(0, 0, 0, 13);
	border: 1px solid rgb(0, 0, 0, 5);
}

QDateTimeEdit::up-button:disabled {
	image: url(:/SpinBox/img light/SpinBoxUpDisabled.png);
}

QDateTimeEdit::down-button:disabled {
	image: url(:/SpinBox/img light/SpinBoxDownDisabled.png);
}

/*SLIDERVERTICAL*/
QSlider:vertical {
	min-width: 30px;
	min-height: 100px;
}

QSlider::groove:vertical {
    width: 5px; 
    background-color: rgb(0, 0, 0, 100);
	border-radius: 2px;
}

QSlider::handle:vertical {
    background-color: &quot;+accent+&quot;;
    border: 6px solid #dbdbdb;
    height: 13px;
	min-width: 15px;
    margin: 0px -10px;
    border-radius: 12px;
}

QSlider::handle:vertical:hover {
    background-color: &quot;+accent+&quot;;
    border: 4px solid #dbdbdb;
    height: 17px;
	min-width: 15px;
    margin: 0px -10px;
    border-radius: 12px
}

QSlider::handle:vertical:pressed {
    background-color: &quot;+accent+&quot;;
    border: 7px solid #dbdbdb;
    height: 11px;
	min-width: 15px;
    margin: 0px -10px;
    border-radius: 12px
}

QSlider::groove:vertical:disabled {
    background-color: rgb(0, 0, 0, 75);
}

QSlider::handle:vertical:disabled {
    background-color: #808080;
    border: 6px solid #cccccc;
}

/*SLIDERHORIZONTAL*/
QSlider:horizontal {
	min-width: 100px;
	min-height: 30px;
}

QSlider::groove:horizontal {
    height: 5px; 
    background-color: rgb(0, 0, 0, 100);
	border-radius: 2px;
}

QSlider::handle:horizontal {
    background-color: &quot;+accent+&quot;;
    border: 6px solid #dbdbdb;
    width: 13px;
	min-height: 15px;
    margin: -10px 0;
    border-radius: 12px
}

QSlider::handle:horizontal:hover {
    background-color: &quot;+accent+&quot;;
    border: 4px solid #dbdbdb;
    width: 17px;
	min-height: 15px;
    margin: -10px 0;
    border-radius: 12px
}

QSlider::handle:horizontal:pressed {
    background-color: &quot;+accent+&quot;;
    border: 7px solid #dbdbdb;
    width: 11px;
	min-height: 15px;
    margin: -10px 0;
    border-radius: 12px
}

QSlider::groove:horizontal:disabled {
    background-color: rgb(0, 0, 0, 75);
}

QSlider::handle:horizontal:disabled {
    background-color: #808080;
    border: 6px solid #cccccc;
}

/*PROGRESSBAR*/
QProgressBar {
	background-color: qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:0.5, y2:1, stop:0.233831 rgba(0, 0, 0, 255), stop:0.343284 rgba(0, 0, 0, 0));
	border-radius: 2px;
	min-height: 4px;
	max-height: 4px;
}

QProgressBar::chunk {
	background-color: &quot;+accent+&quot;;
	border-radius: 2px;
}

/*COMBOBOX*/
QComboBox {
	background-color: rgb(0, 0, 0, 7);
	border: 1px solid rgb(0, 0, 0, 13);
	border-radius: 5px;
	padding-left: 10px;
	min-height: 38px;
	max-height: 38px;
}

QComboBox:hover {
	background-color: rgb(0, 0, 0, 13);
	border: 1px solid rgb(0, 0, 0, 13);
}

QComboBox::pressed {
	border: 1px solid rgb(0, 0, 0, 10);
}

QComboBox::down-arrow {
	image: url(:/newPrefix/img light/ComboBox.png);
}

QComboBox::drop-down {
	background-color: transparent;
    min-width: 50px;
}

QComboBox:disabled {
	color: rgb(0, 0, 0, 110);
	background-color: rgb(0, 0, 0, 13);
	border: 1px solid rgb(0, 0, 0, 5);
}

QComboBox::down-arrow:disabled {
	image: url(:/newPrefix/img light/ComboBoxDisabled.png);
}

/*LINEEDIT*/
QLineEdit {
	background-color: rgb(0, 0, 0, 7);
	border: 1px solid rgb(0, 0, 0, 13);
	font-size: 16px;
	font-family: &quot;Segoe UI&quot;, serif;
	font-weight: 500;
	border-radius: 7px;
	border-bottom: 1px solid rgb(0, 0, 0, 100);
	padding-top: 0px;
	padding-left: 5px;
}

QLineEdit:hover {
	background-color: rgb(0, 0, 0, 13);
	border: 1px solid rgb(0, 0, 0, 13);
	border-bottom: 1px solid rgb(0, 0, 0, 100);
}

QLineEdit:focus {
	border-bottom: 2px solid &quot;+accent+&quot;;
	background-color: rgb(0, 0, 0, 5);
	border-top: 1px solid rgb(0, 0, 0, 13);
	border-left: 1px solid rgb(0, 0, 0, 13);
	border-right: 1px solid rgb(0, 0, 0, 13);
}

QLineEdit:disabled {
	color: rgb(0, 0, 0, 150);
	background-color: rgb(0, 0, 0, 13);
	border: 1px solid rgb(0, 0, 0, 5);
}

/*SCROLLVERTICAL*/
QScrollBar:vertical {
    border: 6px solid rgb(0, 0, 0, 0);
    margin: 14px 0px 14px 0px;
	width: 16px;
}

QScrollBar:vertical:hover {
    border: 5px solid rgb(0, 0, 0, 0);
}

QScrollBar::handle:vertical {
    background-color: rgb(0, 0, 0, 110);
	border-radius: 2px;
	min-height: 25px;
}

QScrollBar::sub-line:vertical {
	image: url(:/ScrollVertical/img light/ScrollTop.png);
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical:hover {
	image: url(:/ScrollVertical/img light/ScrollTopHover.png);
}

QScrollBar::sub-line:vertical:pressed {
	image: url(:/ScrollVertical/img light/ScrollTopPressed.png);
}

QScrollBar::add-line:vertical {
	image: url(:/ScrollVertical/img light/ScrollBottom.png);
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical:hover {
	image: url(:/ScrollVertical/img light/ScrollBottomHover.png);
}

QScrollBar::add-line:vertical:pressed {
	image: url(:/ScrollVertical/img light/ScrollBottomPressed.png);
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
	background: none;
}

/*SCROLLHORIZONTAL*/
QScrollBar:horizontal {
    border: 6px solid rgb(0, 0, 0, 0);
    margin: 0px 14px 0px 14px;
	height: 16px;
}

QScrollBar:horizontal:hover {
    border: 5px solid rgb(0, 0, 0, 0);
}

QScrollBar::handle:horizontal {
    background-color: rgb(0, 0, 0, 110);
	border-radius: 2px;
	min-width: 25px;
}

QScrollBar::sub-line:horizontal {
	image: url(:/ScrollHorizontal/img light/ScrollLeft.png);
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal:hover {
	image: url(:/ScrollHorizontal/img light/ScrollLeftHover.png);
}

QScrollBar::sub-line:horizontal:pressed {
	image: url(:/ScrollHorizontal/img light/ScrollLeftPressed.png);
}

QScrollBar::add-line:horizontal {
	image: url(:/ScrollHorizontal/img light/ScrollRight.png);
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal:hover {
	image: url(:/ScrollHorizontal/img light/ScrollRightHover.png);
}

QScrollBar::add-line:horizontal:pressed {
	image: url(:/ScrollHorizontal/img light/ScrollRightPressed.png);
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
	background: none;
}

/*TEXTEDIT*/
QTextEdit {
	background-color: rgb(0, 0, 0, 7);
	border: 1px solid rgb(0, 0, 0, 13);
	font-size: 16px;
	font-family: &quot;Segoe UI&quot;, serif;
	font-weight: 500;
	border-radius: 7px;
	border-bottom: 1px solid rgb(0, 0, 0, 100);
	padding: 5px;
}

QTextEdit:hover {
	background-color: rgb(0, 0, 0, 13);
	border: 1px solid rgb(0, 0, 0, 13);
	border-bottom: 1px solid rgb(0, 0, 0, 100);
}

QTextEdit:focus {
	background-color: rgb(0, 0, 0, 5);
	border-top: 1px solid rgb(0, 0, 0, 13);
	border-left: 1px solid rgb(0, 0, 0, 13);
	border-right: 1px solid rgb(0, 0, 0, 13);
	border-bottom: 2px solid &quot;+accent+&quot;;
}

QTextEdit:disabled {
	color: rgb(0, 0, 0, 110);
	background-color: rgb(0, 0, 0, 13);
	border: 1px solid rgb(0, 0, 0, 5);
}

/*CALENDAR*/
QCalendarWidget {
}

QCalendarWidget QToolButton {
  	height: 36px;
  	font-size: 18px;
  	background-color: rgb(0, 0, 0, 0);
	margin: 5px;
}

QCalendarWidget QWidget#qt_calendar_navigationbar { 
	background-color: rgb(0, 0, 0, 0); 
	border: 1px solid rgb(0, 0, 0, 13);
	border-top-left-radius: 5px;
	border-top-right-radius: 5px;
	border-bottom-left-radius: 0px;
	border-bottom-right-radius: 0px;
	border-bottom: none;
}

QCalendarWidget QMenu {
	background-color : #f3f3f3;
}

#qt_calendar_prevmonth {
	qproperty-icon: url(:/PrevNext/img light/PrevMonth.png);
	width: 32px;
}

#qt_calendar_nextmonth {
	qproperty-icon: url(:/PrevNext/img light/NextMonth.png);
	width: 32px;
}

#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
	background-color: rgb(0, 0, 0, 10);
	border-radius: 5px;
}

#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
	background-color: rgb(0, 0, 0, 7);
	border-radius: 5px;
}

#qt_calendar_yearbutton, #qt_calendar_monthbutton {
    color: rgb(0, 0, 0);
	margin: 5px 0px;
	padding: 0px 10px;
}

#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
    background-color: rgb(0, 0, 0, 10);
	border-radius: 5px;
}

#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
    background-color: rgb(0, 0, 0, 7);
	border-radius: 5px;
}

QCalendarWidget QToolButton::menu-indicator#qt_calendar_monthbutton {
	background-color: transparent;
}

QCalendarWidget QSpinBox {
	margin: 5px 0px;
}

QCalendarWidget QSpinBox::focus {
	background-color: rgb(0, 0, 0, 5);
	border: 1px solid rgb(0, 0, 0, 10);
	color: rgb(0, 0, 0, 200);
	border-bottom: 2px solid &quot;+accent+&quot;;
}

QCalendarWidget QSpinBox::up-button {
	image: url(:/SpinBox/img light/SpinBoxUp.png);
	background-color: rgb(0, 0, 0, 0);
	border: 1px solid rgb(0, 0, 0, 0);
	border-radius: 4px;
	margin-top: 1px;
	margin-bottom: 1px;
	margin-right: 2px;
	min-width: 30px;
	max-width: 30px;
	min-height: 20px;
}

QCalendarWidget QSpinBox::up-button:hover {
	background-color: rgb(0, 0, 0, 10);
}

QCalendarWidget QSpinBox::up-button:pressed {
	background-color: rgb(0, 0, 0, 5);
}

QCalendarWidget QSpinBox::down-button {
	image: url(:/SpinBox/img light/SpinBoxDown.png);
	background-color: rgb(0, 0, 0, 0);
	border: 1px solid rgb(0, 0, 0, 0);
	border-radius: 4px;
	margin-top: 1px;
	margin-bottom: 1px;
	margin-right: 2px;
	min-width: 30px;
	max-width: 30px;
	min-height: 20px;
}

QCalendarWidget QSpinBox::down-button:hover {
	background-color: rgb(0, 0, 0, 10);
}

QCalendarWidget QSpinBox::down-button:pressed {
	background-color: rgb(0, 0, 0, 5);
}

QCalendarWidget QWidget { 
	alternate-background-color: rgb(0, 0, 0, 0); 
}

QCalendarWidget QAbstractItemView:enabled {
 	color: rgb(0, 0, 0);  
 	selection-background-color: &quot;+accent+&quot;;
 	selection-color: black;
	border: 1px solid rgb(0, 0, 0, 10);
	border-top-left-radius: 0px;
	border-top-right-radius: 0px;
	border-bottom-left-radius: 5px;
	border-bottom-right-radius: 5px;
	outline: 0;
}

QCalendarWidget QAbstractItemView:disabled {
 	color: rgb(30, 30, 30);  
 	selection-background-color: rgb(30, 30, 30);
 	selection-color: black;
	border: 1px solid rgb(0, 0, 0, 13);
	border-top-left-radius: 0px;
	border-top-right-radius: 0px;
	border-bottom-left-radius: 5px;
	border-bottom-right-radius: 5px;
}

#qt_calendar_yearbutton:disabled, #qt_calendar_monthbutton:disabled {
    color: rgb(0, 0, 0, 110);
}

#qt_calendar_prevmonth:disabled {
	qproperty-icon: url(:/PrevNext/img light/PrevMonthDisabled.png);
}

#qt_calendar_nextmonth:disabled {
	qproperty-icon: url(:/PrevNext/img light/NextMonthDisabled.png);
}

/*TREEWIDGET*/
QTreeView {
	background-color: transparent;
   	border: 1px solid rgb(0, 0, 0, 13);
	border-radius: 5px;
	outline: 0;
	padding-right: 5px;
}

QTreeView::item {
	padding: 7px;
	margin-top: 3px;
}

QTreeView::item:selected {
	color: rgb(0, 0, 0);
	background-color: rgb(0, 0, 0, 7);
	border-radius: 5px;
	margin-bottom: 3px;
	padding-left: 0px;
}

QTreeView::item:!selected:hover {
    background-color: rgb(0, 0, 0, 13);
    border-radius: 5px;
	margin-bottom: 3px;
	padding-left: 0px;
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
	image: url(:/newPrefix/img light/TreeViewClose.png);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings {
	image: url(:/newPrefix/img light/TreeViewOpen.png);
}

QTreeView:disabled {
	color: rgb(0, 0, 0, 110);
}

/*TOGGLESWITCH*/
#toggleSwitch {
	color: rgb(0, 0, 0);
	font-size: 17px;
	font-family: &quot;Segoe UI Variable Small&quot;, serif;
	font-weight: 400;
}

#toggleSwitch::indicator {
	width: 22px;
	height: 22px;
	border-radius: 13px;
	border: 2px solid #999999;
	background-color: rgb(0, 0, 0, 0);
	image: url(:/ToggleSwitch/img light/ToggleSwitchOff.png);
	margin-right: 5px;
	padding-right: 25px;
	padding-left: 0px;
}

#toggleSwitch::indicator:hover {
	background-color: rgb(0, 0, 0, 15);
	image: url(:/ToggleSwitch/img light/ToggleSwitchOffHover.png);
}

#toggleSwitch::indicator:pressed {
	background-color: rgb(0, 0, 0, 24);
	width: 26px;
	padding-right: 21px;
	image: url(:/ToggleSwitch/img light/ToggleSwitchOffPressed.png);
}

#toggleSwitch::indicator:checked {
	background-color: &quot;+accent+&quot;;
	border: 2px solid &quot;+accent+&quot;;
	image: url(:/ToggleSwitch/img light/ToggleSwitchOn.png);
	color: rgb(255, 255, 255);
	padding-left: 25px;
	padding-right: 0px;
}

#toggleSwitch::indicator:checked:hover {
	background-color: &quot;+accent+&quot;;
	image: url(:/ToggleSwitch/img light/ToggleSwitchOnHover.png);
}

#toggleSwitch::indicator:checked:pressed {
	background-color: &quot;+accent+&quot;;
	width: 26px;
	padding-left: 21px;
	image: url(:/ToggleSwitch/img light/ToggleSwitchOnPressed.png);
}

#toggleSwitch:disabled {
	color: rgb(0, 0, 0, 110);
}

#toggleSwitch::indicator:disabled {
	border: 2px solid #bbbbbb;
	image: url(:/ToggleSwitch/img light/ToggleSwitchDisabled.png);
}

/*HYPERLINKBUTTON*/
#hyperlinkButton {
	color: &quot;+accent+&quot;;
	font-size: 17px;
	font-family: &quot;Segoe UI Variable Small&quot;, serif;
	border-radius: 5px;
	background-color: rgb(0, 0, 0, 0);
	border: none;
}

#hyperlinkButton:hover {
	background-color: rgb(0, 0, 0, 10);
}

#hyperlinkButton::pressed {
	background-color: rgb(0, 0, 0, 7);
	color: &quot;+accent+&quot;;
}

#hyperlinkButton:disabled {
	color: rgb(0, 0, 0, 110)
}

/*LISTVIEW*/
QListView {
	background-color: transparent;
	font-size: 17px;
	font-family: &quot;Segoe UI Variable Small&quot;, serif;
	font-weight: 400;
	padding: 7px;
	border-radius: 10px;
	outline: 0;
}

QListView::item {
	height: 35px;
}

QListView::item:selected {
	background-color: rgb(0, 0, 0, 13);
	color: black;
	border-radius: 5px;
	padding-left: 0px;
}
		"""
		)
		# add menu bar
		menuBar = QMenuBar(self.titleBar)

		menu = QMenu(' Редактор фигрур', self)

		button_action_open_workspace = QAction(QIcon("bug.png"), "#", self)
		button_action_open_workspace.triggered.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
		button_action_open_workspace.setCheckable(True)
  
		menuBar.addAction(button_action_open_workspace)

		button_action_editor_add = QAction(QIcon("bug.png"), "&Добавить", self)
		button_action_editor_add.triggered.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
		button_action_editor_add.setCheckable(True)
        
		button_action_editor_move = QAction(QIcon("bug.png"), "&Переместить", self)
		button_action_editor_move.triggered.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
		button_action_editor_move.setCheckable(True)

		button_action_editor_remove = QAction(QIcon("bug.png"), "&Удалить", self)
		button_action_editor_remove.triggered.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
		button_action_editor_remove.setCheckable(True)
  
		button_action_editor_con = QAction(QIcon("bug.png"), "&Пересечение", self)
		button_action_editor_con.triggered.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
		button_action_editor_con.setCheckable(True)
		menu.addAction(button_action_editor_add)
		menu.addAction(button_action_editor_move)
		menu.addAction(button_action_editor_remove)
		menu.addAction(button_action_editor_con)
		menuBar.addMenu(menu)
		menuMainWindoW = QMenu(' Рабочая зона', self)
  
		button_action_mainwindowmanager_open = QAction(QIcon("bug.png"), "&Открыть", self)
		button_action_mainwindowmanager_open.triggered.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
		button_action_mainwindowmanager_open.setCheckable(True)
		button_action_mainwindowmanager_clear = QAction(QIcon("bug.png"), "&Очистить", self)
		button_action_mainwindowmanager_clear.triggered.connect(self.on_clearCanvas)
		button_action_mainwindowmanager_clear.setCheckable(True)
		button_action_mainwindowmanager_perimetr = QAction(QIcon("bug.png"), "&Периметр", self)
		button_action_mainwindowmanager_perimetr.triggered.connect(self.on_perimeterFigure)
		button_action_mainwindowmanager_perimetr.setCheckable(True)
		button_action_mainwindowmanager_squard = QAction(QIcon("bug.png"), "&Площадь", self)
		button_action_mainwindowmanager_squard.triggered.connect(self.on_squareFigure)
		button_action_mainwindowmanager_squard.setCheckable(True)
		menuMainWindoW.addAction(button_action_mainwindowmanager_open)
		menuMainWindoW.addAction(button_action_mainwindowmanager_clear)
		menuMainWindoW.addAction(button_action_mainwindowmanager_perimetr)
		menuMainWindoW.addAction(button_action_mainwindowmanager_squard)
		menuBar.addMenu(menuMainWindoW)
		self.titleBar.layout().insertWidget(0, menuBar, 0, Qt.AlignmentFlag.AlignLeft)
		self.titleBar.layout().insertStretch(1, 1)
		self.setMenuWidget(self.titleBar)

		# add status bar
		statusBar = QStatusBar(self)
		statusBar.addWidget(QLabel('  Режим отладки: Включен / Собрано на PyQt 6.5.0  '))
		self.setStatusBar(statusBar)
  
		self.setStyleSheet("""
		    QMenuBar{background: #F0F0F0; padding: 5px 0}
		    QTextEdit{border: none; font-size: 15px}
		    QDialog > QLabel{font-size: 15px}
		""")


		self.figureType = self.findChild(QtWidgets.QComboBox, "figureType")
		self.ui.figureType.currentIndexChanged.connect(self.on_figureType_changed)

		self.windowEffect.setAcrylicEffect(self.winId(), "106EBE99")

		self.intersectionFigure1 = self.findChild(QtWidgets.QComboBox, "intersectionFigure1")
		self.intersectionFigure2 = self.findChild(QtWidgets.QComboBox, "intersectionFigure2")

		self.figureDotsCount = self.findChild(QtWidgets.QLineEdit, "figureDotsCount")
		self.ui.figureDotsCount.textChanged.connect(self.figureDotsCountActions)

		self.xshift = self.findChild(QtWidgets.QLineEdit, "xShift")
		self.yshift = self.findChild(QtWidgets.QLineEdit, "yShift")
		self.phi = self.findChild(QtWidgets.QLineEdit, "phi")
		self.symmetry = self.findChild(QtWidgets.QSpinBox, "symmetry")

		self.x1  = self.findChild(QtWidgets.QLineEdit, "x1" )
		self.x2  = self.findChild(QtWidgets.QLineEdit, "x2" )
		self.x3  = self.findChild(QtWidgets.QLineEdit, "x3" )
		self.x4  = self.findChild(QtWidgets.QLineEdit, "x4" )
		self.x5  = self.findChild(QtWidgets.QLineEdit, "x5" )
		self.x6  = self.findChild(QtWidgets.QLineEdit, "x6" )
		self.x7  = self.findChild(QtWidgets.QLineEdit, "x7" )
		self.x8  = self.findChild(QtWidgets.QLineEdit, "x8" )
		self.x9  = self.findChild(QtWidgets.QLineEdit, "x9" )
		self.x10 = self.findChild(QtWidgets.QLineEdit, "x10")
		self.x11 = self.findChild(QtWidgets.QLineEdit, "x11")
		self.x12 = self.findChild(QtWidgets.QLineEdit, "x12")
		self.x13 = self.findChild(QtWidgets.QLineEdit, "x13")
		self.x14 = self.findChild(QtWidgets.QLineEdit, "x14")
		self.x15 = self.findChild(QtWidgets.QLineEdit, "x15")
		self.masX = [self.x1,  self.x2,  self.x3,  self.x4,  self.x5,
		        self.x6,  self.x7,  self.x8,  self.x9,  self.x10,
		        self.x11, self.x12, self.x13, self.x14, self.x15]

		self.y1  = self.findChild(QtWidgets.QLineEdit, "y1")
		self.y2  = self.findChild(QtWidgets.QLineEdit, "y2")
		self.y3  = self.findChild(QtWidgets.QLineEdit, "y3")
		self.y4  = self.findChild(QtWidgets.QLineEdit, "y4")
		self.y5  = self.findChild(QtWidgets.QLineEdit, "y5")
		self.y6  = self.findChild(QtWidgets.QLineEdit, "y6")
		self.y7  = self.findChild(QtWidgets.QLineEdit, "y7")
		self.y8  = self.findChild(QtWidgets.QLineEdit, "y8")
		self.y9  = self.findChild(QtWidgets.QLineEdit, "y9")
		self.y10 = self.findChild(QtWidgets.QLineEdit, "y10")
		self.y11 = self.findChild(QtWidgets.QLineEdit, "y11")
		self.y12 = self.findChild(QtWidgets.QLineEdit, "y12")
		self.y13 = self.findChild(QtWidgets.QLineEdit, "y13")
		self.y14 = self.findChild(QtWidgets.QLineEdit, "y14")
		self.y15 = self.findChild(QtWidgets.QLineEdit, "y15")
		self.masY = [self.y1,  self.y2,  self.y3,  self.y4,  self.y5,
		        self.y6,  self.y7,  self.y8,  self.y9,  self.y10,
		        self.y11, self.y12, self.y13, self.y14, self.y15]
		
		self.figureRadius = self.findChild(QtWidgets.QTextEdit, "figureRadius")
		self.ui.figureRadius.textChanged.connect(self.figureRadiusActions)

		self.viewPerimeter = self.findChild(QtWidgets.QTextBrowser, "viewPerimeter")
		self.viewSquare = self.findChild(QtWidgets.QTextBrowser, "viewSquare")
		self.isIntersect = self.findChild(QtWidgets.QTextBrowser, "isIntersect")

		self.figuresArray = []

		self.createAddFigure = self.findChild(QtWidgets.QPushButton, "createAddFigure")
		self.ui.createAddFigure.clicked.connect(self.addFigure)

		self.graphicsView = self.findChild(QtWidgets.QGraphicsView, "graphicsView")

		self.scene = QGraphicsScene()
		self.graphicsView.setScene(self.scene)



		self.scene.addLine(-5000, 0, 5000, 0, QPen(QColor("Gray"), 1))
		self.scene.addLine(0, -5000, 0, 5000, QPen(QColor("Gray"), 1))

		self.clearCanvas = self.findChild(QtWidgets.QPushButton, "clearCanvas")
		self.ui.clearCanvas.clicked.connect(self.on_clearCanvas)

		self.moveFigureList = self.findChild(QtWidgets.QComboBox, "moveFigureList")
		self.deleteFigureList = self.findChild(QtWidgets.QComboBox, "deleteFigureList")

		self.deleteFigureButton = self.findChild(QtWidgets.QPushButton, "deleteFigureButton")
		self.ui.deleteFigureButton.clicked.connect(self.deleteFigure)

		self.replaceFigureBox = self.findChild(QtWidgets.QComboBox, "replaceFigureBox")
		self.ui.replaceFigureBox.currentIndexChanged.connect(self.on_replaceFigureBox_changed)

		self.changePlaceFigure = self.findChild(QtWidgets.QPushButton, "changePlaceFigure")
		self.ui.changePlaceFigure.clicked.connect(self.on_moveFigure)
		
		self.perimeterFigure = self.findChild(QtWidgets.QPushButton, "perimeterFigure")
		self.ui.perimeterFigure.clicked.connect(self.on_perimeterFigure)

		self.squareFigure = self.findChild(QtWidgets.QPushButton, "squareFigure")
		self.ui.squareFigure.clicked.connect(self.on_squareFigure)

		self.intersectionFigureButton = self.findChild(QtWidgets.QPushButton, "intersectionFigureButton")
		self.ui.intersectionFigureButton.clicked.connect(self.on_intersectionFigureButton)


	def on_figureType_changed(self, index, pen = None): # Выбор фигуры
		current_text = self.figureType.currentText()
		self.figureRadius.setEnabled(False)
		self.figureRadius.setText('')
		if (current_text == "Отрезок"):
			self.figureDotsCount.setText("2")
			self.figureDotsCount.setEnabled(False)
		elif (current_text == "Ломаная"):
			self.figureDotsCount.setText("3")
			self.figureDotsCount.setEnabled(True)
		elif (current_text == "Окружность"):
			self.figureDotsCount.setText("1")
			self.figureDotsCount.setEnabled(False)
			self.figureRadius.setEnabled(True)
		elif (current_text == "Многоугольник"):
			self.figureDotsCount.setText("5")
			self.figureDotsCount.setEnabled(True)
		elif (current_text == "Треугольник"):
			self.figureDotsCount.setText("3")
			self.figureDotsCount.setEnabled(False)
		elif (current_text == "Четырёхугольник"):
			self.figureDotsCount.setText("4")
			self.figureDotsCount.setEnabled(False)
		elif (current_text == "Прямоугольник"):
			self.figureDotsCount.setText("4")
			self.figureDotsCount.setEnabled(False)
		elif (current_text == "Трапеция"):
			self.figureDotsCount.setText("4")
			self.figureDotsCount.setEnabled(False)
		

	def figureDotsCountActions(self):
		if self.figureDotsCount.text() == '':
			self.count_dots = 0
		else:
			self.count_dots = int(self.figureDotsCount.text())
			if self.count_dots > 15:
				self.count_dots = 15
				self.figureDotsCount.setText("15")

		for i in range(self.count_dots):
			self.masX[i].setEnabled(True)
			self.masY[i].setEnabled(True)
		for j in range(self.count_dots, 15):
			self.masX[j].setEnabled(False)
			self.masY[j].setEnabled(False)

	def figureRadiusActions(self):
		if self.figureRadius.toPlainText() == '':
			self.figureRadius.setText("0")
		else:
			if float(self.figureRadius.toPlainText()) < 0:
				self.figureRadius.setText("0")

	def plotFigure(self, figure, pen = None):
		figure_type = type(figure)
		if str(figure_type) == "<class 'core.segment.Segment'>":
			x1 = figure.getStart().getX()[0]
			y1 = figure.getStart().getX()[1]
			x2 = figure.getFinish().getX()[0]
			y2 = figure.getFinish().getX()[1]
			if pen != None:
				self.scene.addLine(x1, -y1, x2, -y2, pen)
			else:
				self.scene.addLine(x1, -y1, x2, -y2)
		elif str(figure_type) == "<class 'core.polyline.Polyline'>":
			points = figure.getP()
			for i in range(len(points)-1):
				x1 = points[i].getX()[0]
				y1 = points[i].getX()[1]
				x2 = points[i+1].getX()[0]
				y2 = points[i+1].getX()[1]
				if pen != None:
					self.scene.addLine(x1, -y1, x2, -y2, pen)
				else:
					self.scene.addLine(x1, -y1, x2, -y2)
		elif str(figure_type) == "<class 'core.circle.Circle'>":
			r = figure.getR()
			center = figure.getP()
			x = center.getX()[0] - r
			y = center.getX()[1] + r
			if (y == 0):
				if pen != None:
					self.scene.addEllipse(x, y, r*2, r*2, pen)
				else:
					self.scene.addEllipse(x, y, r*2, r*2)
			else:
				if pen != None:
					self.scene.addEllipse(x, -y, r*2, r*2, pen)
				else:
					self.scene.addEllipse(x, -y, r*2, r*2)
		else:
			points = figure.getP()
			for i in range(len(figure.getP())-1):
				x1 = points[i].getX()[0]
				y1 = points[i].getX()[1]
				x2 = points[i+1].getX()[0]
				y2 = points[i+1].getX()[1]
				if pen == None:
					self.scene.addLine(x1, -y1, x2, -y2)
				else:
					self.scene.addLine(x1, -y1, x2, -y2, pen)
			if pen == None:
				self.scene.addLine(points[figure.getN()-1].getX()[0], 
				              -points[figure.getN()-1].getX()[1],
			                   points[0].getX()[0],
			                  -points[0].getX()[1])
			else:
				self.scene.addLine(points[figure.getN()-1].getX()[0], 
				              -points[figure.getN()-1].getX()[1],
			                   points[0].getX()[0],
			                  -points[0].getX()[1], pen)

	def plotFigures(self, figuresArray):
		for figure in figuresArray:
			self.plotFigure(figure)

	def is_trapezoid(self, points):
		x1, y1 = points[0].getX()[0], points[0].getX()[1]
		x2, y2 = points[1].getX()[0], points[1].getX()[1]
		x3, y3 = points[2].getX()[0], points[2].getX()[1]
		x4, y4 = points[3].getX()[0], points[3].getX()[1]

		# Проверка параллельности сторон
		slope_1 = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float('inf')
		slope_2 = (y4 - y3) / (x4 - x3) if (x4 - x3) != 0 else float('inf')
		if slope_1 == slope_2:
			return False

		# Проверка непересекающихся сторон
		if max(x1, x2) < min(x3, x4) or max(x3, x4) < min(x1, x2):
			return True

		# Проверка ненулевой площади
		if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
			return False

		print(x1)
		print(y1)

		return True

	def is_qgon(self, points):
		x1, y1 = points[0].getX()[0], points[0].getX()[1]
		x2, y2 = points[1].getX()[0], points[1].getX()[1]
		x3, y3 = points[2].getX()[0], points[2].getX()[1]
		x4, y4 = points[3].getX()[0], points[3].getX()[1]

		# Проверка прямых углов
		if (x2 - x1) * (x3 - x2) + (y2 - y1) * (y3 - y2) != 0:
			return False

		# Проверка равных длин сторон
		if ((x2 - x1) ** 2 + (y2 - y1) ** 2) != ((x3 - x2) ** 2 + (y3 - y2) ** 2):
			return False

		return True

	def is_tgon(self, points):
		x1, y1 = points[0].getX()[0], points[0].getX()[1]
		x2, y2 = points[1].getX()[0], points[1].getX()[1]
		x3, y3 = points[2].getX()[0], points[2].getX()[1]

		# Проверка ненулевой площади
		area = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
		if area == 0:
			return False

		return True


	def addFigure(self):
		figure_type = self.figureType.currentText()
		self.points = []
		flag = False
		for i in range(self.count_dots):
			if self.masX[i].text() == '' or self.masY[i].text() == '':
				QMessageBox.critical(None, "Ошибка добавления фигуры", "Введены не все необходимые координаты!")
				flag = True
				break
			else:
				self.points.append(Point2D([int(self.masX[i].text()), int(self.masY[i].text())]))
		if flag:
			return

		if (figure_type == "Отрезок"):
			from core.segment import Segment
			self.figuresArray.append(Segment(self.points[0], self.points[1]))
			self.moveFigureList.addItem(str(Segment(self.points[0], self.points[1])))
			self.deleteFigureList.addItem(str(Segment(self.points[0], self.points[1])))
			self.intersectionFigure1.addItem(str(Segment(self.points[0], self.points[1])))
			self.intersectionFigure2.addItem(str(Segment(self.points[0], self.points[1])))
		elif (figure_type == "Ломаная"):
			from core.polyline import Polyline
			self.figuresArray.append(Polyline(len(self.points), self.points))
			self.moveFigureList.addItem(str(Polyline(len(self.points), self.points)))
			self.deleteFigureList.addItem(str(Polyline(len(self.points), self.points)))
			self.intersectionFigure1.addItem(str(Polyline(len(self.points), self.points)))
			self.intersectionFigure2.addItem(str(Polyline(len(self.points), self.points)))
		elif (figure_type == "Окружность"):
			from core.circle import Circle
			r = float(self.figureRadius.toPlainText())
			self.figuresArray.append(Circle(self.points[0], r))
			self.moveFigureList.addItem(str(Circle(self.points[0], r)))
			self.deleteFigureList.addItem(str(Circle(self.points[0], r)))
			self.intersectionFigure1.addItem(str(Circle(self.points[0], r)))
			self.intersectionFigure2.addItem(str(Circle(self.points[0], r)))
		elif (figure_type == "Многоугольник"):
			from core.ngon import NGon
			self.figuresArray.append(NGon(self.points))
			self.moveFigureList.addItem(str(NGon(self.points)))
			self.deleteFigureList.addItem(str(NGon(self.points)))
			self.intersectionFigure1.addItem(str(NGon(self.points)))
			self.intersectionFigure2.addItem(str(NGon(self.points)))
		elif (figure_type == "Треугольник"):
			if not self.is_tgon(self.points):
				QMessageBox.critical(None, "Ошибка создания фигуры", "Неправильно заданы координаты треугольника!")
				return
			from core.tgon import TGon
			self.figuresArray.append(TGon(self.points))
			self.moveFigureList.addItem(str(TGon(self.points)))
			self.deleteFigureList.addItem(str(TGon(self.points)))
			self.intersectionFigure1.addItem(str(TGon(self.points)))
			self.intersectionFigure2.addItem(str(TGon(self.points)))
		elif (figure_type == "Четырёхугольник"):
			from core.qgon import QGon
			self.figuresArray.append(QGon(self.points))
			self.moveFigureList.addItem(str(QGon(self.points)))
			self.deleteFigureList.addItem(str(QGon(self.points)))
			self.intersectionFigure1.addItem(str(QGon(self.points)))
			self.intersectionFigure2.addItem(str(QGon(self.points)))
		elif (figure_type == "Прямоугольник"):
			if not self.is_qgon(self.points):
				QMessageBox.critical(None, "Ошибка создания фигуры", "Неправильно заданы координаты прямоугольника!")
				return
			from core.rectangle import Rectangle
			self.figuresArray.append(Rectangle(self.points))
			self.moveFigureList.addItem(str(Rectangle(self.points)))
			self.deleteFigureList.addItem(str(Rectangle(self.points)))
			self.intersectionFigure1.addItem(str(Rectangle(self.points)))
			self.intersectionFigure2.addItem(str(Rectangle(self.points)))
		elif (figure_type == "Трапеция"):
			if not self.is_trapezoid(self.points):
				QMessageBox.critical(None, "Ошибка создания фигуры", "Неправильно заданы координаты трапеции!")
				return
			from core.trapeze import Trapeze
			self.figuresArray.append(Trapeze(self.points))
			self.moveFigureList.addItem(str(Trapeze(self.points)))
			self.deleteFigureList.addItem(str(Trapeze(self.points)))
			self.intersectionFigure1.addItem(str(Trapeze(self.points)))
			self.intersectionFigure2.addItem(str(Trapeze(self.points)))

		self.plotFigures(self.figuresArray)
		QMessageBox.information(None, "Добавление завершено", "Добавление успешно завершено")
			


	def on_clearCanvas(self):
		self.scene.clear()

		l = len(self.figuresArray)
		for i in range(l, 0, -1):
			self.moveFigureList.removeItem(i-1)
			self.deleteFigureList.removeItem(i-1)
			self.intersectionFigure1.removeItem(i-1)
			self.intersectionFigure2.removeItem(i-1)
			del self.figuresArray[i-1]

		self.scene.addLine(-5000, 0, 5000, 0, QPen(QColor("Gray"), 1))
		self.scene.addLine(0, -5000, 0, 5000, QPen(QColor("Gray"), 1))

		self.isIntersect.setText("")

		QMessageBox.information(None, "Очищение завершено", "Очищение плоскости успешно завершено")

	def deleteFigure(self):
		if not self.figuresArray:
			QMessageBox.critical(None, "Ошибка удаления фигуры", "Не создано ни одной фигуры!")
			return

		figureIndex = self.deleteFigureList.currentIndex()

		self.moveFigureList.removeItem(figureIndex)
		self.deleteFigureList.removeItem(figureIndex)
		self.intersectionFigure1.removeItem(figureIndex)
		self.intersectionFigure2.removeItem(figureIndex)

		self.scene.clear()

		self.scene.addLine(-200, 0, 200, 0, QPen(QColor("black"), 1))
		self.scene.addLine(0, -200, 0, 200, QPen(QColor("black"), 1))

		del self.figuresArray[figureIndex]
		self.plotFigures(self.figuresArray)

		QMessageBox.information(None, "Удаление фигуры завершено", "Удаление фигуры успешно завершено")

		self.isIntersect.setText("")

	def on_replaceFigureBox_changed(self):
		current_text = self.replaceFigureBox.currentText()
		if (current_text == "Сдвиг"):
			self.xshift.setEnabled(True)
			self.yshift.setEnabled(True)
			self.phi.setEnabled(False)
			self.symmetry.setEnabled(False)
		elif (current_text == "Поворот"):
			self.xshift.setEnabled(False)
			self.yshift.setEnabled(False)
			self.phi.setEnabled(True)
			self.symmetry.setEnabled(False)
		elif (current_text == "Симметрия"):
			self.xshift.setEnabled(False)
			self.yshift.setEnabled(False)
			self.phi.setEnabled(False)
			self.symmetry.setEnabled(True)

	def on_moveFigure(self):
		current_text = self.replaceFigureBox.currentText()
		if not self.figuresArray:
			QMessageBox.critical(None, "Ошибка перемещения фигуры", "Не создано ни одной фигуры!")
			return
		else:
			figure = self.figuresArray[self.moveFigureList.currentIndex()]
		if (current_text == "Сдвиг"):
			numberXShift = 0
			numberYShift = 0
			if self.xshift.text() != '':
				numberXShift = float(self.xshift.text())
			if self.yshift.text() != '':
				numberYShift = float(self.yshift.text())

			if not self.figuresArray:
				pass
			else:
				self.figuresArray[self.moveFigureList.currentIndex()] = figure.shift(Point2D([numberXShift, numberYShift]))
				
				self.scene.clear()

				self.scene.addLine(-200, 0, 200, 0, QPen(QColor("Gray"), 1))
				self.scene.addLine(0, -200, 0, 200, QPen(QColor("Gray"), 1))

				self.plotFigures(self.figuresArray)

		elif (current_text == "Поворот"):

			if self.phi.text() == '':
				numberPhi = 0
			else:
				from math import pi
				numberPhi = float(self.phi.text())

			if not self.figuresArray:
				pass
			else:
				self.figuresArray[self.moveFigureList.currentIndex()] = figure.rot(numberPhi)
				
				self.scene.clear()

				self.scene.addLine(-200, 0, 200, 0, QPen(QColor("Gray"), 1))
				self.scene.addLine(0, -200, 0, 200, QPen(QColor("Gray"), 1))

				self.plotFigures(self.figuresArray)
		elif (current_text == "Симметрия"):
			if self.symmetry.text() == '':
				numberSymmetry = 0
			else:
				numberSymmetry = int(self.symmetry.text())

			if not self.figuresArray:
				pass
			else:
				print(numberSymmetry)
				self.figuresArray[self.moveFigureList.currentIndex()] = figure.symAxis(numberSymmetry)
				
				self.scene.clear()

				self.scene.addLine(-200, 0, 200, 0, QPen(QColor("Gray"), 1))
				self.scene.addLine(0, -200, 0, 200, QPen(QColor("Gray"), 1))

				self.plotFigures(self.figuresArray)
		self.isIntersect.setText("")
		self.moveFigureList.setItemText(self.moveFigureList.currentIndex(), str(self.figuresArray[self.moveFigureList.currentIndex()]))
		QMessageBox.information(None, "Перемещение завершено", "Перемещение фигуры успешно завершено")

	def on_perimeterFigure(self):
		if not self.figuresArray:
			QMessageBox.critical(None, "Ошибка нахождения периметра фигуры", "Не создано ни одной фигуры!")
			return
		pSum = 0
		for figure in self.figuresArray:
			if hasattr(figure, 'length'):
				pSum += round(figure.length(), 2)
		self.viewPerimeter.setText(str(pSum))

	def on_squareFigure(self):
		if not self.figuresArray:
			QMessageBox.critical(None, "Ошибка нахождения площади фигуры", "Не создано ни одной фигуры!")
			return
		sSum = 0
		for figure in self.figuresArray:
			sSum += round(figure.square(), 2)
		self.viewSquare.setText(str(sSum))

	def on_intersectionFigureButton(self):
		if len(self.figuresArray) < 2:
			QMessageBox.critical(None, "Ошибка нахождения пересечения фигур", "Задано меньше двух фигур!")
			return
		figure1Index = self.intersectionFigure1.currentIndex()
		figure2Index = self.intersectionFigure2.currentIndex()
		figure1 = self.figuresArray[figure1Index]
		figure2 = self.figuresArray[figure2Index]

		if type(figure1) == "<class 'core.ngon.NGon'>" or type(figure1) == "<class 'core.ngon.TGon'>" or type(figure1) == "<class 'core.ngon.TGon'>" or type(figure1) == "<class 'core.ngon.QGon'>":
			QMessageBox.critical(None, "Ошибка нахождения пересечений фигур", "Неверный тип первой фигуры!")
		if type(figure2) == "<class 'core.ngon.NGon'>" or type(figure1) == "<class 'core.ngon.TGon'>" or type(figure1) == "<class 'core.ngon.TGon'>" or type(figure1) == "<class 'core.ngon.QGon'>":
			QMessageBox.critical(None, "Ошибка нахождения пересечений фигур", "Неверный тип второй фигуры!")

		print(figure1)
		print(figure2)

		if figure1 == figure2:
			QMessageBox.critical(None, "Ошибка нахождения пересечения фигур", "Выбрана одна и та же фигура!")
			return

		if figure1.cross(figure2) or figure2.cross(figure1):
			print("YES")
			pen_color = QColor(255, 0, 0)
			pen = QPen(pen_color)
			self.plotFigure(figure1, pen)
			self.plotFigure(figure2, pen)
			self.isIntersect.setText("Пересекаются")
			QMessageBox.information(None, "Пересечение првоерено", "Фигуры пересекаются")
		else:
			self.isIntersect.setText("Не пересекаются")
			QMessageBox.information(None, "Пересечение првоерено", "Фигуры НЕ пересекаются")