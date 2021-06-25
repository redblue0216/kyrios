# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个算法应用组件的基础模块，主要功能是将Kyrios基本单元的功能抽象出来。
# 主要技术有描述符协议，图论，有限状态机，观察者模式，适配器模式
"""
模块介绍
-------

这是一个算法应用组件的基础模块，主要功能是将Kyrios基本单元的功能抽象出来。

设计模式：

    （1）观察者模式

    （2）适配器模式   

关键点：    

    （1）描述符协议，图论，有限状态机  

主要功能：            

    （1）抽象Kyrios基本单元                                                     

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from Kyrios.Extend.Tools.info import *
from Kyrios.Extend.Tools.state import *
from Kyrios.Extend.Tools.structure import *
from Kyrios.Extend.Tools.extend import *
from Kyrios.Extend.Tools.interface import *



####### 算法应用组件基本单元类 ###############################################
### 设计模式：                                                           ###
### （1）观察者模式                                                      ###
### （2）适配器模式                                                      ###
### 关键点：                                                             ###
### （1）描述符协议，图论，有限状态机                                      ###
### 主要功能：                                                           ###
### （1）抽象Kyrios基本单元                                               ###
############################################################################



###### 基础模块类 #####################################################################
######################################################################################
class Baseitem(object):
    """
    类介绍：

        这是一个基础模块类，主要将Kyrios基本单元的功能抽象出来，包括信息、结构、状态、扩展、接口和执行六大共嗯。

        主要采用技术有描述符协议、图论(Networkx)、有限状态机(transition)、观察者模式和适配器模式
    """


    def __init__(self):
        """
        属性功能：

            info (Object): 信息类，在创建时有tools中的工具生成实例
            structure (Object): 结构类，在创建时有tools中的工具生成实例
            state (Object): 状态类，在创建时有tools中的工具生成实例
            extend (Object): 扩展类，在创建时有tools中的工具生成实例
            interface (Object): 接口类，在创建时有tools 中的工具生成实例
        """

        self.info = self.get_info_object()
        self.state = self.get_state_object()
        self.structure = self.get_structure_object()
        self.extend = self.get_extend_object()
        self.interface = self.get_interface_object()


    def get_info_object(self):
        """
        方法功能：

            定义一个创建信息类实例的方法
        """

        return Infoprint(name = 'info')


    def get_state_object(self):
        """
        方法功能：

            定义一个创建状态类实例的方法
        """        

        FiniteStateMachine = StateFSM()

        return FiniteStateMachine


    def get_structure_object(self):
        """
        方法功能：

            定义一个创建结构类实例的方法
        """  

        DAG = StarAtlas()
        
        return DAG


    def get_extend_object(self):
        """
        方法功能：

            定义一个创建扩展类实例的方法
        """  

        ProlongInstance = ProlongIndirect()

        return ProlongInstance
        

    def get_interface_object(self):
        """
        方法功能：

            定义一个创建接口类实例的方法
        """  

        AdapterInstance =AdapterIndirect()

        return AdapterInstance



#######################################################################################
#######################################################################################


