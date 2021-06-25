# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个算法应用组件接口类，主要提供适配器功能。
"""
模块介绍
-------

这是一个算法应用组件接口类，主要提供适配器功能。

设计模式：

    （1）适配器模式   

关键点：    

    （1）灵活接入其他程序  

主要功能：            

    （1）适配各种程序                                                  

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from abc import ABCMeta,abstractmethod



####### 算法应用接口模块 ####################################################
### 设计模式：                                                           ###
### （1）适配器模式                                                      ###
### 关键点：                                                             ###
### （1）灵活接入其他程序                                                 ###
### 主要功能：                                                           ###
### （1）适配各种程序                                                     ###
############################################################################



###### 适配器模块类 #####################################################################
########################################################################################



class Target(metaclass=ABCMeta):
    """
    类介绍：

        这是一个适配模式中的目标类
    """


    @abstractmethod
    def function(self):
        """
        方法功能：

            定义一个目标类的抽象函数
        """

        pass



class Adaptee(object):
    """
    类介绍：

        这是一个源类，主要用于接受需要转接的源类
    """

    
    def __init__(self,source_target = None):
        """
        属性功能：

            source_target (Object): 源类
        """

        self.source_target = source_target


    @abstractmethod
    def specialic_function(self):
        """
        方法功能：

            定义一个根据传入的源类对象实现的具体方法
        """

        pass



class Adapter(Adaptee,Target):
    """
    类介绍：

        这是一个适配器类
    """


    function_dict = dict()


    def add_source_target(self,source_target):
        """
        方法功能：

            定义一个添加源类的方法

        参数：
            source_target (Object): 源类
        
        返回：
            无
        """

        self.source_target = source_target


    def function(self,function,function_name):
        """
        方法功能：

            定义一个执行具体函数的方法

        参数：
            function (Object): 具体函数
            function_name (str): 函数名称

        返回：
            无
        """

        Adapter.function_dict[function_name] = function


    def run_interface(self,function_name):
        """
        方法功能：

            定义一个运行接口

        参数：
            function_name (str): 函数名称

        返回：
            result (Object): 运行结果
        """

        result = Adapter.function_dict[function_name]()

        return result



class AdapterIndirect(object):
    """
    类介绍：

        这是一个适配器挂载的虚类
    """


    Wedge = Adapter() 



###################################################################################################
###################################################################################################


