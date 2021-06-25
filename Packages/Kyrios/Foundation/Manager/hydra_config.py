# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个算法应用组件管理模块，主要提供脚本动态配置相关功能，主要技术采用Hydra
"""
模块介绍
-------

这是一个算法应用组件管理模块，主要提供脚本动态配置相关功能，主要技术采用Hydra

设计模式：

    （1）无   

关键点：    

    （1）Hydra 

主要功能：            

    （1）动态配置                                                     

使用示例
-------

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from Kyrios.Extend.Base.basic import *
from Kyrios.Foundation.Function.function_interface import *



####### 管理模块 ###########################################################
### 设计模式：                                                           ###
### （1）无                                                              ###
### 关键点：                                                             ###
### （1）Hydra                                                          ###
### 主要功能：                                                           ###
### （1）动态配置                                                        ###
############################################################################



###### HydraConfig #####################################################################
########################################################################################



class HydraConfig(Baseitem):
    """
    类介绍：

        这是一个Hydra动态配置类，主要用于生成Hydra配置剧本
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

        exec('self.extend.Prolong.prolong_instance.{}(**{})'.format(function_name,kwargs))
        print('Test execute!')


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


