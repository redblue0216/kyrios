# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个算法应用组件存储模块，主要提供数据抽象层功能，主要技术采用Alluxio
"""
模块介绍
-------

这是一个算法应用组件存储模块，主要提供数据抽象层功能，主要技术采用Alluxio

设计模式：

    （1）无  

关键点：    

    （1）Alluxio 

主要功能：            

    （1）数据抽象层                                                    

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from Kyrios.Extend.Base.basic import *
from Kyrios.Foundation.Function.function_interface import *



####### 存储模块 ###########################################################
### 设计模式：                                                           ###
### （1）无                                                              ###
### 关键点：                                                             ###
### （1）Alluxio                                                         ###
### 主要功能：                                                           ###
### （1）数据抽象层                                                       ###
############################################################################



###### AlluxioClient #####################################################################
##########################################################################################



class AlluxioClient(Baseitem):
    """
    类介绍：

        这是一个Alluxio接口类，主要提供与Alluxio服务器交互功能
    """    


    def __init__(self):
        """
        属性功能：

            继承父类
        """

        super().__init__()


    def execute(self,function_name,**kwargs):
        """
        方法功能：

            定义一个执行接口

        参数：
            function_name (str): 函数名称

        返回：
            无
        """

        execute_result = eval('self.extend.Prolong.prolong_instance.{}(**{})'.format(function_name,kwargs))
        print('Test execute!')
        return execute_result


    def customize(self,function,function_name):
        """
        方法功能：

            定义一个自定义挂载具体功能函数的功能

        参数：
            function (Object)：函数对象
            function_name (str): 函数名称

        返回：
            无
        """

        self.extend.Prolong.add_dynamic_method(function,function_name)

        return 'Customize function successfully!'


    def show_function(self):
        """
        方法功能：
            
            定义一个展示所有函数的方法

        参数：
            无

        返回：
            无
        """

        self.extend.Prolong.show_function()



#######################################################################################
#######################################################################################


