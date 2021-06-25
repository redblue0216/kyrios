# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个算法应用的状态模块，主要用于组件监控。
"""
模块介绍
-------

这是一个算法应用的状态模块，主要用于组件监控。

功能
----

    设计模式：              

        （1）监控模式     

    功能：              

        （1）观察者      

        （2）被观察者                                                                                                                   

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from abc import ABCMeta,abstractmethod
from transitions import Machine



####### 模型监控模块基础类 ###################################################
### 设计模式：                                                            ###
### （1）监控模式                                                         ###
### 功能：                                                                ###
### （1）观察者                                                           ###
### （1）被观察者                                                         ###
############################################################################



####### 算法监控模块观察者基础类 ##########################################################################
#########################################################################################################



class Observer(metaclass=ABCMeta):
    """
    类介绍：

        这是一个观察者的基类，主要用于更新模型监控器的状态
    """


    @abstractmethod
    def update(self,observable,object):
        """
        方法功能：

            定义一个更新状态的函数

        参数：
            obserable (object)：被观察者
            object (object)：占位对象
        """

        pass



###### 算法监控模块被观察者基础类 ################################################################
################################################################################################



class Observable(object):
    """
    类介绍：

        这是一个被观察者的基类，主要用于模型监控器的基类。功能：（1）添加观察者（2）删除观察者（3）依次运行观察者更新动作的方法
    """


    def __init__(self):
        """
        属性方法功能：

            定义一个初始化方法，主要用于收集观察者
           
        参数：   
            __observers (list)：观察者列表
        """

        self.__observers = []


    def addObserver(self,observer):
        """
        方法功能：

            定义一个添加观察者对象的方法
               
        参数：	   
            observer (object)：观察者对象
        """

        self.__observers.append(observer)


    def removeObserver(self,observer):
        """
        方法功能：

            定义一个删除观察者对象的方法

        参数：
            observer (object)：观察者对象
        """

        self.__observers.remove(observer)


    def notifyObservers(self,object=0):
        """
        方法功能：

            定义一个依次运行观察者更新动作的方法

        参数：
            object (object)：占位对象
        """

        for o in self.__observers:
            o.update(self,object)



################################################################################
################################################################################


####### 算法监控模块观察者基础类 ##########################################################################
#########################################################################################################



class FiniteStateMachine(Observable):
    """
    类介绍：

        这是一个模型监控器类，主要用于监控模型是否需要重新训练，该监控器采用有限状态机技术，调用transitions包,实现有限状态机的控制器，并将该类修改成执行器。
            
        关键技术：（1）有限状态机.功能：（1）监控器（2）控制器（3）执行器
    """


    states = ['idle','actived','deactived']
    transitions = [
        {'trigger':'start','source':'idle','dest':'actived'},
        {'trigger':'restart','source':'*','dest':'actived'},
        {'trigger':'stop','source':'*','dest':'idle'},
        {'trigger':'done','source':'actived','dest':'deactived'}
    ]


    def __init__(self):
        """
        属性方法功能：

            定义一个初始化方法，主要用来指标数据存储和有限状态机扩展

        参数：
            __index (float)：指标
            machine (object)：有限状态机
        """

        super().__init__()
        self.__index = 0
        self.machine = Machine(model = self,states = FiniteStateMachine.states,transitions = FiniteStateMachine.transitions,initial = 'idle')


    def getIndex(self):
        """
        方法功能：

            定义一个获取当前指标的方法
            
        返回  
            返回 (float)：指标
        """

        return self.__index


    def setIndex(self,index):
        """
        方法功能：

            定义一个设置当前指标的方法，该输入主要从数据库中扫描得到
            
        参数：   
            index (float)：指标

        返回：
            返回：无返回
        """

        self.__index = index
        print("现在的指标是",self.__index)
        self.notifyObservers()


    def update_mode(self,update_rule = '>=0.6'):
        update_mode = UpdateMode(update_rule)
        self.addObserver(update_mode)


####### 模型监控模块观察者基础类 ##########################################################################
#########################################################################################################



class UpdateMode(Observer):
    """
    类介绍：

        这是一个更新模型类，主要用于根据事件转换状态，有限状态机事件状态转换

    参数：
        start (str): idle->actived
        restart (str): *->actived
        stop (str): *->idle
        done (str)：actived->deactived
    """

    def __init__(self,assert_eval):
        self.assert_eval = assert_eval


    def update(self,observable,object):
        """
        方法功能：

            定义一个更新动作实现的方法

        参数：
            observable (object)：被观察者对象
            object (object)：占位对象

        返回：
            返回：无返回
        """


        bool_eval = eval("observable.getIndex() {}".format(str(self.assert_eval)))
        if isinstance(observable,FiniteStateMachine) and bool_eval:
            observable.start()
        


###########################################################################################################
###########################################################################################################



class StateFSM(object):
    """
    类介绍：

        这是一个有限状态机挂载虚类
    """


    def __init__(self):
        """
        属性功能：

            FiniteStateMachine (Object): 有限状态机对象
        """

        self.FiniteStateMachine = FiniteStateMachine()



##############################################################################################################
##############################################################################################################


