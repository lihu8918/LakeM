#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Created on Tue May 23 13:28:05 2017
written by lihu
"""
import sys
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from PyQt5 import QtCore, QtWidgets
from ui_mainwindow import Ui_MainWindow
from ui_helpdialog import Ui_helpDialog
from ui_aboutdialog import Ui_aboutDialog
from ui_tracerdialog import Ui_tracerDialog

#%% 定义示踪物模块的class
class MyTracerDialog(QtWidgets.QDialog, Ui_tracerDialog):    
    def __init__(self):    
        super(MyTracerDialog, self).__init__()
        self.setupUi(self)
        
        # 创建两个列表，一个为参数名，一个为参数值，两者一一对应
        self.paramName = ['outputpath', 'tracerfile', 'nx', 'dx', 'ny', 'dy', 'nt', 'dt', 'dh', 'nout']
        self.paramValue = ['' for i in range(10)]
        
        # 连接信号与槽
        self.pushButton_1.clicked.connect(self.set_hydropath)  # 槽函数不用加括号
        self.pushButton_2.clicked.connect(self.set_tracerfile)
        self.pushButton_3.clicked.connect(self.get_params)
        self.pushButton_3.clicked.connect(self.run_tracer)

    # pushButton_1的槽函数，用于打开水动力文件所在的目录
    def set_hydropath(self):
        self.paramValue[0] = QtWidgets.QFileDialog.getExistingDirectory(caption='设置水动力文件目录')
        self.lineEdit_1.setText(self.paramValue[0])
     
    # pushButton_2的槽函数，用于打开示踪物初始浓度文件
    def set_tracerfile(self):
        self.paramValue[1], filt = QtWidgets.QFileDialog.getOpenFileName(caption='设置示踪物初始场文件', filter='Text Files(*.txt *.dat *.csv)')
        self.lineEdit_2.setText(self.paramValue[1])

    # 获取对话框内所有lineEdit的字符串，并赋值给self.paramValue
    def get_params(self):
        self.paramValue[2] = self.lineEdit_3.text()
        self.paramValue[3] = self.lineEdit_4.text()
        self.paramValue[4] = self.lineEdit_5.text()
        self.paramValue[5] = self.lineEdit_6.text()
        self.paramValue[6] = self.lineEdit_7.text()
        self.paramValue[7] = self.lineEdit_8.text()
        self.paramValue[8] = self.lineEdit_9.text()
        self.paramValue[9] = self.lineEdit_10.text()
    
    def run_tracer(self):
        from numpy.ctypeslib import load_library, ndpointer
        from ctypes import c_int
        
        # 主程序中用到的参数
        pi    = 3.14159265359
        omega = 2*pi/(24*3600)  # 地球自转角速度
        theta = float('35')     # 区域所在纬度
        nt    = int(self.paramValue[6])  # 模拟时间步数
        nout  = int(self.paramValue[9])  # 计算结果输出间隔，即隔多少个时间步将计算结果保存一次
        txMAX = float(self.paramValue[8])  # x方向风应力
        tyMAX = float(self.paramValue[9])  # y方向风应力
        nx    = int(self.paramValue[2])  # x方向网格数
        ny    = int(self.paramValue[4])  # y方向网格数
        
        # 动态连接库proc.dll中用到的参数，将其构建为一个结构体，作为形参传入proc.dll中的子程序
        dx    = float(self.paramValue[3])  # x方向空间步长
        dy    = float(self.paramValue[5])  # y方向空间步长
        dt    = float(self.paramValue[7])  # 时间步长
        hmin  = float('0.05')  # 最小截断水深
        rho   = float('1025')  # 水密度
        g     = 9.81  # 重力加速度
        f     = 2*omega*np.sin(theta*pi/180)  # 科氏力参数
        beta  = (0.5*dt*f)**2  # beta系数
        r     = float('0.001')  # 底摩擦系数
        taux  = 0.0  # 初始化x方向风应力
        tauy  = 0.0  # 初始化y方向风应力
        ah    = float('1.0')  # 水平方向湍流粘性系数
        dh    = float(self.paramValue[8])  # 示踪物在水平方向的湍流扩散系数
        mode  = int('1')  # 对流项差分格式
        slip  = float('0.0')  # 滑移边界类型
        
        # 定义以上参数的结构体
        arg_params = np.dtype([('dx',   'float64', 1),
                               ('dy',   'float64', 1),
                               ('dt',   'float64', 1),
                               ('hmin', 'float64', 1),
                               ('rho',  'float64', 1),
                               ('g',    'float64', 1),
                               ('f',    'float64', 1),
                               ('beta', 'float64', 1),
                               ('r',    'float64', 1),
                               ('taux', 'float64', 1),
                               ('tauy', 'float64', 1),
                               ('ah',   'float64', 1),
                               ('dh',   'float64', 1),
                               ('mode', 'int32',   1),
                               ('slip', 'float64', 1)])
        # 创建该结构体，并赋值
        params = np.array([(dx, dy, dt, hmin, rho, g, f, beta, r, taux, tauy, ah, dh, mode, slip)], dtype=arg_params)
        
        # 初始化u_cur, v_cur, tracer_cur, tracer_nex
        u_cur = np.zeros((nx+2, ny+2), dtype='float64', order='F')
        v_cur = np.zeros((nx+2, ny+2), dtype='float64', order='F')
        tracer_cur = np.zeros((nx+2, ny+2), dtype='float64', order='F')
        tracer_nex = np.zeros((nx+2, ny+2), dtype='float64', order='F')
        
        # 读取流速文件，将最后时间步的稳态流速赋值给u_cur, v_cur
        u_raw = np.loadtxt(self.paramValue[0]+'/u.txt')
        v_raw = np.loadtxt(self.paramValue[0]+'/v.txt')
        
        u_3d = np.reshape(u_raw, (-1, ny+2, nx+2))
        v_3d = np.reshape(v_raw, (-1, ny+2, nx+2))
        
        u_cur[:, :] = np.transpose(u_3d[-1, :, :])  # 注意，这里必须使用u_cur[:, :]，进行原位赋值
        v_cur[:, :] = np.transpose(v_3d[-1, :, :])  # 注意，这里必须使用v_cur[:, :]，进行原位赋值
        
        # 读取示踪物初始场文件，并赋值给tracer_cur
        tracer_raw = np.loadtxt(self.paramValue[1])
        tracer_cur[:, :] = np.transpose(tracer_raw)
        
        # 加载proc.dll
        fdll = load_library('proc', './')  # 注意，只在当前目录寻找dll
        
#        # cal_u args setup
#        fdll.cal_u.argtypes = [ndpointer(dtype='int32', ndim=2, flags='F'),
#                               ndpointer(dtype='float64', ndim=2, flags='F'),
#                               ndpointer(dtype='float64', ndim=2, flags='F'),
#                               ndpointer(dtype='float64', ndim=2, flags='F'),
#                               ndpointer(dtype='float64', ndim=2, flags='F'),
#                               ndpointer(dtype='float64', ndim=2, flags='F'),
#                               c_int,
#                               c_int,
#                               ndpointer(dtype=arg_params)]
#        
#        # cal_v args setup
#        fdll.cal_v.argtypes = [ndpointer(dtype='int32', ndim=2, flags='F'),
#                               ndpointer(dtype='float64', ndim=2, flags='F'),
#                               ndpointer(dtype='float64', ndim=2, flags='F'),
#                               ndpointer(dtype='float64', ndim=2, flags='F'),
#                               ndpointer(dtype='float64', ndim=2, flags='F'),
#                               ndpointer(dtype='float64', ndim=2, flags='F'),
#                               c_int,
#                               c_int,
#                               ndpointer(dtype=arg_params)]
#        
#        # cal_eta args setup
#        fdll.cal_eta.argtypes = [ndpointer(dtype='float64', ndim=2, flags='F'),
#                                 ndpointer(dtype='float64', ndim=2, flags='F'),
#                                 ndpointer(dtype='float64', ndim=2, flags='F'),
#                                 ndpointer(dtype='float64', ndim=2, flags='F'),
#                                 ndpointer(dtype='float64', ndim=2, flags='F'),
#                                 c_int,
#                                 c_int,
#                                 ndpointer(dtype=arg_params)]
        
        # 设置proc.dll中cal_tracer子程序形参的类型
        fdll.cal_tracer.argtypes = [ndpointer(dtype='float64', ndim=2, flags='F'),
                                    ndpointer(dtype='float64', ndim=2, flags='F'),
                                    ndpointer(dtype='float64', ndim=2, flags='F'),
                                    ndpointer(dtype='float64', ndim=2, flags='F'),
                                    c_int,
                                    c_int,
                                    ndpointer(dtype=arg_params)]
        
        # 创建保存计算结果的文本文件
        tracer_fid = open(self.paramValue[0]+'/tracer.txt', 'w+')
        
        # 迭代计算tracer_nex，并将结果保存
        for n in np.arange(1, nt+1):
            model_time = n*dt
        #    params['taux'] = txMAX*np.minimum(model_time/(1.0*24.0*3600.0), 1.0)
        #    params['tauy'] = tyMAX*np.minimum(model_time/(1.0*24.0*3600.0), 1.0)

        #    fdll.cal_u(mask, h, eta_cur, u_cur, v_cur, u_nex, nx, ny, params)
        #    fdll.cal_v(mask, h, eta_cur, u_cur, v_cur, v_nex, nx, ny, params)
        #    fdll.cal_eta(h, eta_cur, u_nex, v_nex, eta_nex, nx, ny, params)
            fdll.cal_tracer(tracer_cur, u_cur, v_cur, tracer_nex, nx, ny, params)
            
            # 更新tracer_cur
            tracer_cur[:, :] = tracer_nex[:, :]
            
            # 保存计算结果
            if n%nout == 0:
                np.savetxt(tracer_fid, np.transpose(tracer_cur[:, :]), fmt='%10.6f', delimiter=' ', newline='\n')  # 结果文件中列数对应nx+2
                print('Output data at time = {}days'.format(model_time/(24.0*3600)))
        
        # 计算结束，关闭结果文件
        tracer_fid.close()

#%% 定义帮助对话框的class
class MyHelpDialog(QtWidgets.QDialog, Ui_helpDialog):    
    def __init__(self):    
        super(MyHelpDialog, self).__init__()    
        self.setupUi(self)

#%% 定义关于对话框的class
class MyAboutDialog(QtWidgets.QDialog, Ui_aboutDialog):    
    def __init__(self):    
        super(MyAboutDialog, self).__init__()    
        self.setupUi(self)

#%% 定义作图对话框的class
class MyPlotDialog(QtWidgets.QDialog):    
    def __init__(self):    
        super(MyPlotDialog, self).__init__()
        # 设置对话框标题
        self.setWindowTitle('Make Plot')
        
        # 实例化一个figure，作图命令都将画在此self.figure上
        self.figure = plt.figure()

        # 实例化一个画布用于显示self.figure，以self.figure为参数用于__init__
        self.canvas = FigureCanvas(self.figure)

        # 实例化一个matplotlib作图窗口的工具栏
        self.toolbar = NavigationToolbar(self.canvas, self)

        # 实例化作图对话框内的一些控件
        self.label1 = QtWidgets.QLabel('Grid Number(x)')  # 用于输入nx
        self.lineEdit1 = QtWidgets.QLineEdit()
        self.label2 = QtWidgets.QLabel('Grid Number(y)')  # 用于输入ny
        self.lineEdit2 = QtWidgets.QLineEdit()
        self.label3 = QtWidgets.QLabel('Timestamp Index')  # 用于输入作图时间步
        self.lineEdit3 = QtWidgets.QLineEdit()
        self.button1 = QtWidgets.QPushButton('Open')  # 打开计算结果所在目录，目录内必须包括eta.txt, u.txt, v.txt
        self.button2 = QtWidgets.QPushButton('Plot')
        
        # 创建两个水平布局，分别添加lineEdit和pushButton
        hlayout1 = QtWidgets.QHBoxLayout()
        hlayout1.addWidget(self.label1)
        hlayout1.addWidget(self.lineEdit1)
        hlayout1.addWidget(self.label2)
        hlayout1.addWidget(self.lineEdit2)
        hlayout1.addWidget(self.label3)
        hlayout1.addWidget(self.lineEdit3)
        
        hlayout2 = QtWidgets.QHBoxLayout()
        hlayout2.addWidget(self.button1)
        hlayout2.addWidget(self.button2)
        
        # 创建垂直布局
        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(self.toolbar)
        vlayout.addWidget(self.canvas)
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)
        self.setLayout(vlayout)
        
        # 连接信号与槽
        self.button1.clicked.connect(self.set_outputpath)
        self.button2.clicked.connect(self.make_plot)
        
        # 初始化 nx, ny, timeindex, outputpath
        self.nx = ''
        self.ny = ''
        self.timeindex = ''
        self.outputpath = ''
    
    def set_outputpath(self):
        self.outputpath = QtWidgets.QFileDialog.getExistingDirectory(caption='Setup Outputs Path')
        
    def make_plot(self):
        # 输入参数若非数字，则弹出警告对话框
        try:
            nx = int(self.lineEdit1.text())
            ny = int(self.lineEdit2.text())
            timeindex = int(self.lineEdit3.text())
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, 'Plot Parameters', 'Illegal parameters，Please Check!', QtWidgets.QMessageBox.Yes)
        
        # 设置计算结果文件的绝对路径
        etafile = self.outputpath + '/eta.txt'
        ufile = self.outputpath + '/u.txt'
        vfile = self.outputpath + '/v.txt'
        
        # 读取计算结果，此时数组的shape为（nt*（ny+2）, nx+2）
        eta_raw = np.loadtxt(etafile)
        u_raw = np.loadtxt(ufile)
        v_raw = np.loadtxt(vfile)
        
        # 将以上数组reshape为（nt，ny+2, nx+2）
        eta = np.reshape(eta_raw, (-1, ny+2, nx+2))
        u = np.reshape(u_raw, (-1, ny+2, nx+2))
        v = np.reshape(v_raw, (-1, ny+2, nx+2))
        
        # 将数组中的干点设置为nan
        eta[np.where(eta>=1.0)] = np.nan
        u[np.where(eta>=1.0)] = np.nan
        v[np.where(eta>=1.0)] = np.nan
        
        # 以数组中的nan为mask，创建掩膜数组，在作图时干点的颜色将被屏蔽
        eta_masked = np.ma.array(eta, mask=np.isnan(eta))
        u_masked = np.ma.array(u, mask=np.isnan(eta))
        v_masked = np.ma.array(v, mask=np.isnan(eta))
        
        # 清空现有figure的内容（注意，ax.hold(False)语法已废止）
        self.figure.clear()

        # 创建一个subplot
        ax = self.figure.add_subplot(111)

        # 作图
        pc = ax.pcolormesh(eta_masked[timeindex, :, :], shading='flat', vmin=-0.02, vmax=0.02)
        self.figure.colorbar(pc)
        qv = ax.quiver(u_masked[timeindex, :, :], v_masked[timeindex, :, :], width=0.0015, scale=5)
        qk = ax.quiverkey(qv, 0.81, 0.08, 0.2, r'0.2 m/s', labelpos='E', coordinates='figure')
        
        # 刷新画布
        self.canvas.draw()

#%% 定义动画对话框的class
class MyAnimationDialog(QtWidgets.QDialog):    
    def __init__(self):    
        super(MyAnimationDialog, self).__init__()
        # 设置对话框标题
        self.setWindowTitle('Make Animation')
        
        # 实例化一个figure，作图命令都将画在此self.figure上
        self.figure = plt.figure()

        # 实例化一个画布用于显示self.figure，以self.figure为参数用于__init__
        self.canvas = FigureCanvas(self.figure)

        # 实例化一个matplotlib作图窗口的工具栏
        self.toolbar = NavigationToolbar(self.canvas, self)

        # 实例化作图对话框内的一些控件，同作图对话框
        self.label1 = QtWidgets.QLabel('Grid Number(x)')
        self.lineEdit1 = QtWidgets.QLineEdit()
        self.label2 = QtWidgets.QLabel('Grid Number(y)')
        self.lineEdit2 = QtWidgets.QLineEdit()
        self.button1 = QtWidgets.QPushButton('Open')
        self.button2 = QtWidgets.QPushButton('Animate')
        
        # 创建两个水平布局，分别添加lineEdit和pushButton
        hlayout1 = QtWidgets.QHBoxLayout()
        hlayout1.addWidget(self.label1)
        hlayout1.addWidget(self.lineEdit1)
        hlayout1.addWidget(self.label2)
        hlayout1.addWidget(self.lineEdit2)
        
        hlayout2 = QtWidgets.QHBoxLayout()
        hlayout2.addWidget(self.button1)
        hlayout2.addWidget(self.button2)
        
        # 创建垂直布局
        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(self.toolbar)
        vlayout.addWidget(self.canvas)
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)
        self.setLayout(vlayout)
        
        # 连接信号与槽
        self.button1.clicked.connect(self.set_outputpath)
        self.button2.clicked.connect(self.make_animation)
        
        # 初始化nx, ny, outputpath
        self.nx = ''
        self.ny = ''
        self.outputpath = ''
    
    def set_outputpath(self):
        self.outputpath = QtWidgets.QFileDialog.getExistingDirectory(caption='Setup Outputs Path')
        
    def make_animation(self):
        # 输入参数若非数字，则弹出警告对话框
        try:
            nx = int(self.lineEdit1.text())
            ny = int(self.lineEdit2.text())
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, 'Animation Parameters', 'Illegal parameters，Please Check!', QtWidgets.QMessageBox.Yes)
        
        # 设置计算结果文件的绝对路径
        etafile = self.outputpath + '/eta.txt'
        ufile = self.outputpath + '/u.txt'
        vfile = self.outputpath + '/v.txt'
        
        # 读取计算结果，此时数组的shape为（nt*（ny+2）, nx+2）
        eta_raw = np.loadtxt(etafile)
        u_raw = np.loadtxt(ufile)
        v_raw = np.loadtxt(vfile)
        
        # 将以上数组reshape为（nt，ny+2, nx+2）
        eta = np.reshape(eta_raw, (-1, ny+2, nx+2))
        u = np.reshape(u_raw, (-1, ny+2, nx+2))
        v = np.reshape(v_raw, (-1, ny+2, nx+2))
        
        # 将数组中的干点设置为nan
        eta[np.where(eta>=1.0)] = np.nan
        u[np.where(eta>=1.0)] = np.nan
        v[np.where(eta>=1.0)] = np.nan
        
        # 以数组中的nan为mask，创建掩膜数组，在作图时干点的颜色将被屏蔽
        eta_masked = np.ma.array(eta, mask=np.isnan(eta))
        u_masked = np.ma.array(u, mask=np.isnan(eta))
        v_masked = np.ma.array(v, mask=np.isnan(eta))
        
        # 清空现有figure的内容（注意，ax.hold(False)语法已废止）
        self.figure.clear()

        # 创建一个subplot
        ax = self.figure.add_subplot(111)
        
        # 初始化figure
        pc = ax.pcolormesh(eta_masked[0, :, :], shading='flat', vmin=-0.02, vmax=0.02)
        self.figure.colorbar(pc)
        qv = ax.quiver(u_masked[0, :, :], v_masked[0, :, :], width=0.0015, scale=5)
        qk = ax.quiverkey(qv, 0.81, 0.08, 0.2, r'0.2 m/s', labelpos='E', coordinates='figure')
        ax_text = ax.text(0.2, 0.9, '', color='w', ha='center', transform=ax.transAxes, fontsize=10)
        # title_text = ax.set_title('', fontsize=10)
        
        # 设置initial frame
        def init():
            pc = ax.pcolormesh(eta_masked[0, :, :], shading='flat', vmin=-0.02, vmax=0.02)
            qv = ax.quiver(u_masked[0, :, :], v_masked[0, :, :], width=0.0015, scale=5)
            qk = ax.quiverkey(qv, 0.81, 0.08, 0.2, r'0.2 m/s', labelpos='E', coordinates='figure')
            ax_text.set_text('time = {0:<6.3f} day'.format(0.0))
            # title_text.set_text('time = {0:<6.3f} day'.format(0.0))
            return pc, qv, qk, ax_text
        
        # 设置update frame
        def update(i):
            pc = ax.pcolormesh(eta_masked[i, :, :], shading='flat', vmin=-0.02, vmax=0.02)
            qv.set_UVC(u_masked[i, :, :], v_masked[i, :, :])
            ax_text.set_text('time = {0:<6.3f} day'.format(2400*3*(i+1)/86400.0))
            # title_text.set_text('time = {0:<6.3f} day'.format(2400*3*(i+1)/86400.0))
            return pc, qv, qk, ax_text
        
        # 更新画布
        anm = animation.FuncAnimation(self.figure, update, init_func=init, frames=eta.shape[0], interval=300, repeat=True, blit=True)
        self.canvas.draw()

#%% 定义软件主窗口的class
class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):    
    def __init__(self):    
        super(MyMainWindow, self).__init__()    
        self.setupUi(self)
        
        # 创建两个列表，一个为参数名，一个为参数值，两者一一对应
        self.paramName = ['depfile', 'savepath', 'nx', 'dx', 'ny', 'dy', 'nt', 'dt', 'txMAX', 'tyMAX',
                          'theta', 'hmin', 'rho', 'r', 'ah', 'nout', 'mode', 'slip']
        self.paramValue = ['' for i in range(18)]
        
        # 连接信号与槽
        self.actionOpen.triggered.connect(self.set_depfile)  # 设置水深文件
        self.actionSave.triggered.connect(self.set_outputpath)  # 设置计算结果保存目录
        self.actionClear.triggered.connect(self.clear_all)  # 清空参数
        self.actionStart.triggered.connect(self.get_params)  # 获取参数
        self.actionStop.triggered.connect(self.stop_hydro)  # 开始水动力模块的计算
        self.actionTracer.triggered.connect(self.open_tracerdialog)  # 弹出示踪物模块对话框
        self.actionPlot.triggered.connect(self.open_plotdialog)  # 弹出作图对话框
        self.actionAnimation.triggered.connect(self.open_anmdialog)  # 弹出动画对话框
        self.actionHelp.triggered.connect(self.open_helpdialog)  # 弹出帮助对话框
        self.actionAbout.triggered.connect(self.open_aboutdialog)  # 弹出关于对话框

        # 创建一个新线程，用于运行后台计算程序
        self.thread = MyCore(self.paramName, self.paramValue)  # 实例化一个线程 
        self.thread.log_signal.connect(self.update_log)  # 线程发过来的信号挂接到update_log，实时更新显示区内容及进度条
        self.actionStart.triggered.connect(self.run_hydro)
    
    # actionOpen的槽函数，设置水深文件
    def set_depfile(self):
        self.paramValue[0], filt = QtWidgets.QFileDialog.getOpenFileName(caption='设置水深文件', filter='Text Files(*.txt *.dat *.csv)')
    
    # actionSave的槽函数，设置文件保存目录
    def set_outputpath(self):
        self.paramValue[1] = QtWidgets.QFileDialog.getExistingDirectory(caption='设置计算结果目录')
    
    # actionClear的槽函数，清空设置参数
    def clear_all(self):
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.lineEdit_13.clear()
        self.lineEdit_14.clear()
        
        self.textBrowser.clear()
        self.progressBar.reset()

    # actionStartd的槽函数
    def get_params(self):
        # 从lineEdit里获取参数
        self.paramValue[2] = self.lineEdit_1.text()
        self.paramValue[3] = self.lineEdit_2.text()
        self.paramValue[4] = self.lineEdit_3.text()
        self.paramValue[5] = self.lineEdit_4.text()
        self.paramValue[6] = self.lineEdit_5.text()
        self.paramValue[7] = self.lineEdit_6.text()
        self.paramValue[8] = self.lineEdit_7.text()
        self.paramValue[9] = self.lineEdit_8.text()
        self.paramValue[10] = self.lineEdit_9.text()
        self.paramValue[11] = self.lineEdit_10.text()
        self.paramValue[12] = self.lineEdit_11.text()
        self.paramValue[13] = self.lineEdit_12.text()
        self.paramValue[14] = self.lineEdit_13.text()
        self.paramValue[15] = self.lineEdit_14.text()
        
        # 从ComboBox里获取参数        
        index_cmb1 = self.comboBox_1.currentIndex()
        dict_cmb1 = {0:'1', 1:'2', 2:'3'}
        self.paramValue[16] = dict_cmb1[index_cmb1]

        index_cmb2 = self.comboBox_2.currentIndex()
        dict_cmb2 = {0:'0.0', 1:'1.0', 2:'2.0'}
        self.paramValue[17] = dict_cmb2[index_cmb2]
        
        # 检查参数，若检查到参数不正确则弹出警告对话框
        if not all(self.paramValue[0:15]):
            QtWidgets.QMessageBox.warning(self, '模型参数设置', '参数设置不得为空，请检查！', QtWidgets.QMessageBox.Yes)
            return
        elif not all([var.lstrip('-').replace('.', '', 1).isdigit() for var in self.paramValue[2:15]]):
            QtWidgets.QMessageBox.warning(self, '模型参数设置', '参数设置错误，请检查！', QtWidgets.QMessageBox.Yes)
            return
        
        # 设置进度条最大值为nt
        self.progressBar.setMaximum(int(self.paramValue[6]))
        
        # 模型开始运行前，显示所有参数
        self.textBrowser.setText('*'*27 + '模型参数设置' + '*'*27)
        for pn, pv in zip(self.paramName, self.paramValue):
            self.textBrowser.append('{0:<16}:{1:<10}'.format(pn, pv))

    # actionStart的槽函数，开启后台计算程序的线程
    def run_hydro(self):
        if all(self.paramValue[0:15]):
            self.textBrowser.append('*'*27 + '模型开始运行' + '*'*27)
            self.thread.start()

    # actionStop的槽函数，停止后台计算程序的线程
    def stop_hydro(self):
        self.thread.terminate()
        self.progressBar.reset()
        
        content = self.textBrowser.toPlainText()
        if content[-2] != '*':
            self.textBrowser.append('*'*26 + '模型非正常结束' + '*'*26)

    # actionTracer的槽函数，弹出示踪物模块对话框
    def open_tracerdialog(self):
        tracerdialog = MyTracerDialog()
        tracerdialog.exec_()

    # actionPlot的槽函数，弹出作图对话框
    def open_plotdialog(self):
        plotdialog = MyPlotDialog()
        plotdialog.exec_()
        
    # actionAnimation的槽函数，弹出动画对话框
    def open_anmdialog(self):
        animation_dialog = MyAnimationDialog()
        animation_dialog.exec_()

    # actionHelp的槽函数，弹出帮助块对话框
    def open_helpdialog(self):
        helpdialog = MyHelpDialog()
        helpdialog.exec_()
    
    # actionAbout的槽函数，弹出关于对话框
    def open_aboutdialog(self):
        aboutdialog = MyAboutDialog()
        aboutdialog.exec_()

    # 新线程内log_signal的槽函数
    def update_log(self, info, step):
        self.textBrowser.append(info)
        self.progressBar.setValue(step)
        if int(self.paramValue[6])-step < int(self.paramValue[15]):
            self.textBrowser.append('*'*27 + '模型正常结束' + '*'*27)

#%%  定义后台计算模块的class
class MyCore(QtCore.QThread):
    log_signal = QtCore.pyqtSignal(str, int)  # 创建信号，发射str和int，对应update_log槽函数的形参
  
    def __init__(self, paramName, paramValue):  
        super(MyCore, self).__init__()
        # 将主窗口设置的参数传递进来
        self.paramName = paramName
        self.paramValue = paramValue
          
    def run(self):
        from numpy.ctypeslib import load_library, ndpointer
        from ctypes import c_int
        
        # 主程序中用到的参数
        pi    = 3.14159265359
        omega = 2*pi/(24*3600)  # 地球自转角速度
        theta = float(self.paramValue[10])  # 区域所在纬度
        nt    = int(self.paramValue[6])  # 模拟时间步数
        nout  = int(self.paramValue[15])  # 计算结果输出间隔，即隔多少个时间步将计算结果保存一次
        txMAX = float(self.paramValue[8])  # x方向风应力
        tyMAX = float(self.paramValue[9])  # y方向风应力
        nx    = int(self.paramValue[2])  # x方向网格数
        ny    = int(self.paramValue[4])  # y方向网格数
    
        # 动态连接库proc.dll中用到的参数，将其构建为一个结构体，作为形参传入proc.dll中的子程序
        dx    = float(self.paramValue[3])  # x方向空间步长
        dy    = float(self.paramValue[5])  # y方向空间步长
        dt    = float(self.paramValue[7])  # 时间步长
        hmin  = float(self.paramValue[11])  # 最小截断水深
        rho   = float(self.paramValue[12])  # 水密度
        g     = 9.81  # 重力加速度
        f     = 2*omega*np.sin(theta*pi/180)  # 科氏力参数
        beta  = (0.5*dt*f)**2  # beta系数
        r     = float(self.paramValue[13])  # 底摩擦系数
        taux  = 0.0  # 初始化x方向风应力
        tauy  = 0.0  # 初始化y方向风应力
        ah    = float(self.paramValue[14])  # 水平方向湍流粘性系数
        dh    = float('0.1')   # 示踪物在水平方向的湍流扩散系数（备用，耦合计算时将用到此参数）
        mode  = int(self.paramValue[16])  # 对流项差分格式
        slip  = float(self.paramValue[17])  # 滑移边界类型
        
        # 定义以上参数的结构体
        arg_params = np.dtype([('dx',   'float64', 1),
                               ('dy',   'float64', 1),
                               ('dt',   'float64', 1),
                               ('hmin', 'float64', 1),
                               ('rho',  'float64', 1),
                               ('g',    'float64', 1),
                               ('f',    'float64', 1),
                               ('beta', 'float64', 1),
                               ('r',    'float64', 1),
                               ('taux', 'float64', 1),
                               ('tauy', 'float64', 1),
                               ('ah',   'float64', 1),
                               ('dh',   'float64', 1),
                               ('mode', 'int32',   1),
                               ('slip', 'float64', 1)])
        # 创建该结构体，并赋值
        params = np.array([(dx, dy, dt, hmin, rho, g, f, beta, r, taux, tauy, ah, dh, mode, slip)], dtype=arg_params)
        
        # 初始化各变量
        hs      = np.zeros((nx+2, ny+2), dtype='float64', order='F')
        eta_cur = np.zeros((nx+2, ny+2), dtype='float64', order='F')
        eta_nex = np.zeros((nx+2, ny+2), dtype='float64', order='F')   
        h       = np.zeros((nx+2, ny+2), dtype='float64', order='F')
        mask    = np.zeros((nx+2, ny+2), dtype='int32', order='F')
        u_cur   = np.zeros((nx+2, ny+2), dtype='float64', order='F')
        u_nex   = np.zeros((nx+2, ny+2), dtype='float64', order='F')
        v_cur   = np.zeros((nx+2, ny+2), dtype='float64', order='F')
        v_nex   = np.zeros((nx+2, ny+2), dtype='float64', order='F')
        
        # 读取净水深文件
        dep_raw = np.loadtxt(self.paramValue[0])
        inner_dep = np.transpose(dep_raw)
        hs[1:-1, 1:-1] = inner_dep[:, :]
        # 设置外围边界的净水深
        hs[0, :]  = -1.0
        hs[-1, :] = -1.0
        hs[:, 0]  = -1.0
        hs[:, -1] = -1.0
        
        eta_cur[:, :] = -np.minimum(hs, 0.0)
        eta_nex[:, :] = eta_cur[:, :]
        
        h[:, :] = hs[:, :]+eta_cur[:, :]
        
        mask[:, :] = 1
        mask[h[:, :]<hmin] = 0
        
        u_cur[:, :] = 0.0
        u_nex[:, :] = 0.0
        v_cur[:, :] = 0.0
        v_nex[:, :] = 0.0
        
        # 加载proc.dll
        fdll = load_library('proc', './')  # 注意，只在当前目录寻找dll
        
        # 设置proc.dll中cal_u子程序形参的类型
        fdll.cal_u.argtypes = [ndpointer(dtype='int32', ndim=2, flags='F'),
                               ndpointer(dtype='float64', ndim=2, flags='F'),
                               ndpointer(dtype='float64', ndim=2, flags='F'),
                               ndpointer(dtype='float64', ndim=2, flags='F'),
                               ndpointer(dtype='float64', ndim=2, flags='F'),
                               ndpointer(dtype='float64', ndim=2, flags='F'),
                               c_int,
                               c_int,
                               ndpointer(dtype=arg_params)]
        
        # 设置proc.dll中cal_v子程序形参的类型
        fdll.cal_v.argtypes = [ndpointer(dtype='int32', ndim=2, flags='F'),
                               ndpointer(dtype='float64', ndim=2, flags='F'),
                               ndpointer(dtype='float64', ndim=2, flags='F'),
                               ndpointer(dtype='float64', ndim=2, flags='F'),
                               ndpointer(dtype='float64', ndim=2, flags='F'),
                               ndpointer(dtype='float64', ndim=2, flags='F'),
                               c_int,
                               c_int,
                               ndpointer(dtype=arg_params)]
        
        # 设置proc.dll中cal_eta子程序形参的类型
        fdll.cal_eta.argtypes = [ndpointer(dtype='float64', ndim=2, flags='F'),
                                 ndpointer(dtype='float64', ndim=2, flags='F'),
                                 ndpointer(dtype='float64', ndim=2, flags='F'),
                                 ndpointer(dtype='float64', ndim=2, flags='F'),
                                 ndpointer(dtype='float64', ndim=2, flags='F'),
                                 c_int,
                                 c_int,
                                 ndpointer(dtype=arg_params)]
        
        # 创建保存计算结果的文本文件
        eta_fid = open(self.paramValue[1]+'/eta.txt', 'w+')
        u_fid = open(self.paramValue[1]+'/u.txt', 'w+')
        v_fid = open(self.paramValue[1]+'/v.txt', 'w+')
        
        # 迭代计算u_nex, v_nex, eta_nex, 并将结果保存
        for n in np.arange(1, nt+1):
            model_time = n*dt
            params['taux'] = txMAX*np.minimum(model_time/(1.0*24.0*3600.0), 1.0)
            params['tauy'] = tyMAX*np.minimum(model_time/(1.0*24.0*3600.0), 1.0)
            
            fdll.cal_u(mask, h, eta_cur, u_cur, v_cur, u_nex, nx, ny, params)
            fdll.cal_v(mask, h, eta_cur, u_cur, v_cur, v_nex, nx, ny, params)
            fdll.cal_eta(h, eta_cur, u_nex, v_nex, eta_nex, nx, ny, params)
            
            # 更新eta_cur, h, mask, u_cur, v_cur
            eta_cur[:, :] = eta_nex[:, :]
            h[:, :]       = hs[:, :]+eta_cur[:, :]
            mask[:, :]    = 1
            mask[h[:, :]<hmin] = 0
            u_cur[:, :]   = u_nex[:, :]
            v_cur[:, :]   = v_nex[:, :]
            
            # 保存计算结果
            if n%nout == 0:
                np.savetxt(eta_fid, np.transpose(eta_cur[:, :]), fmt='%10.6f', delimiter=' ', newline='\n')
                np.savetxt(u_fid, np.transpose(u_cur[:, :]), fmt='%10.6f', delimiter=' ', newline='\n')
                np.savetxt(v_fid, np.transpose(v_cur[:, :]), fmt='%10.6f', delimiter=' ', newline='\n')
                self.log_signal.emit('Writing output data at time: {0:16} days'.format(model_time/(24.0*3600)), n)
        
        # 计算结束，关闭结果文件
        eta_fid.close()
        u_fid.close()
        v_fid.close()

#%% 主窗口循环监听
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)    
    gui = MyMainWindow()    
    gui.show()    
    sys.exit(app.exec_()) 