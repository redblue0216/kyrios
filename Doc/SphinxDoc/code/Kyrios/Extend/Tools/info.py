# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个算法应用组件的信息类，主要功能是聚合组件信息。
"""
模块介绍
-------

这是一个算法应用组件的信息类，主要功能是聚合组件信息。

    功能：            

        （1）聚合组件信息                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from Kyrios.Extend.Utils.descriptor import *



####### 算法应用序渐信息模块 ###################################################
### 功能：                                                                 ###
### （1）聚合组件信息                                                       ###
##############################################################################



####### 对象实例类 ####################################################################################
######################################################################################################



@entity
class Infoprint(object):
    """
    类介绍：

        这是一个信息类，主要功能是信息聚合，主要采用技术有描述符协议。
    """


    __instance = None
    __isFirstInit = False
    info_dict = DescriptorDict()


    def __new__(cls,name):
        """
        属性功能：

            实现单例模式功能
        """

        if not cls.__instance:
            Infoprint.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self,name):
        """
        属性功能:

            name (str): 信息类名称
        """

        if not self.__isFirstInit:
            self.__name = name
            Infoprint.__isFirstInit = True


    def getName(self):
        """
        方法功能:

            定义一个获取信息类名称的方法
        """

        return self.__name



###################################################################################################
###################################################################################################

