# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个算法组件自定义模块，主要技术采用构建模式
"""
模块介绍
-------

这是一个算法组件自定义模块，主要技术采用构建模式

设计模式：

    （1）构建者模式   

关键点：    

    （1）自定义

主要功能：            

    （1）算法应用组件自定义                                                     

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from abc import ABCMeta,abstractmethod



####### 算法应用组件自定义 ###################################################
### 设计模式：                                                            ###
### （1）构建者模式                                                        ###
### 关键点：                                                              ###
### （1）自定义                                                           ###
### 主要功能：                                                            ###
### （1）算法应用组件自定义                                                ###
############################################################################



###### 基础模块类 #####################################################################
######################################################################################



class Component(metaclass = ABCMeta):
    """
    类介绍：

        这是一个构建模式中的组件抽象类，构建模式主要用于提供自定义的开发人员选项。
    """


    def __init__(self,name):
        """
        属性功能：

            name (str): 组件名称
            __components (Dict): 函数功能字典，主要用于手机各个自定义函数对象
        """

        self.name = name
        self.__components = {}


    def get_name(self):
        """
        方法功能：

            定义一个获取组件名称的方法
        """

        return self.name


    def add_component(self,component,component_name):
        """
        方法功能：

            定义一个向函数字典添加函数并挂载到Foundation上，具体向实例添加和挂载。

        参数：
            component (Object): 组件对象
            component_name (str): 组件名称
        
        返回：
            无
        """

        self.__components[component_name] = component


    def get_components(self,component_name):
        """
        方法功能：

            定义一个获取组件对象的功能

        参数：
            component_name (str): 组件名称

        返回：
            component (Object): 组件对象
        """

        if component_name == 'all':
            return self.__components
        else:
            return self.__components[component_name]


    @abstractmethod
    def feature(self):
        """
        方法功能：

            定义一个展示组合特征的抽象魔法方法
        """

        pass



class ComponentCustom(Component):
    """
    类介绍：

        这是一个构建模式中的组件具体实现类
    """


    def feature(self):
        """
        方法功能：

            定义一个展示组合特征的具体方法
        """

        print("Compose!")



####### 算法应用构建者组织类 ###############################################################################
##########################################################################################################



class ComponentBuilder(metaclass = ABCMeta):
    """
    类介绍：

        这是一个构建模式中的构建者抽象类
    """


    @abstractmethod
    def mount_component(self):
        """
        方法功能：

            定义一个构建组件的抽象方法
        """

        pass



class CustomizeComponentBuilder(ComponentBuilder):
    """
    类介绍：

        这是一个自定义构建者类，主要用于动态添加功能，主要技术采用MethodType对象绑定。
    """


    def mount_component(self,component_name,component_custom,foundation_item):
        """
        方法功能：

            定义一个构建组件的具体方法，利用Foundation中的extend功能

        参数：
            component_name (str): 组件名称
            component_custom (Object): 自定义组件对象
            foundation_item (Object): 基础组件对象

        返回：
            无
        """

        tmp_component = component_custom.get_components(component_name)
        foundation_item.extend.Prolong.add_dynamic_method(tmp_component,component_name)

        return 'Mount component successful!'



class BuildManager(object):
    """
    类介绍：

        这是一个构建者管理类
    """


    def __init__(self):
        """
        属性功能：

            component_custom_builder (Object): 自定义组件管理者实例
            component_custom_compose (Object): 自定义组件组合实例
        """

        self.component_custom_builder = CustomizeComponentBuilder()
        self.component_custom_compose = ComponentCustom('CustomComponent')


    def add_customize_component(self,component,component_name):
        """
        方法功能：

            定义一个添加自定义组件的方法

        参数：
            component (Object): 组件对象
            component_name (str): 组件名称

        返回：
            无
        """

        self.component_custom_compose.add_component(component,component_name)
        

    def show_components(self,component_name):
        """
        方法功能：

            定义一个展示指定组件的方法

        参数：
            component_name (str): 组件名称

        返回：
            component (Object): 组件对象
        """

        components = self.component_custom_compose.get_components(component_name)

        return components


    def mount_component(self,component_name,foundation_item):
        """
        方法功能：

            定义一个挂载具体组件的方法

        参数：
            component_name (str): 组件名称
            foundation_item (Object): 基础组件对象

        返回：
            无
        """

        self.component_custom_builder.mount_component(component_name,self.component_custom_compose,foundation_item)



###############################################################################################################################
###############################################################################################################################


