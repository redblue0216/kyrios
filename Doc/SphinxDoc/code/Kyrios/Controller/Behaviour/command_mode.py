# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个算法应用组件组合类，主要采用命令模式，支持自定义宏命令
"""
模块介绍
-------

这是一个算法应用组件组合类，主要采用命令模式，支持自定义宏命令

设计模式：

    （1）命令模式   

关键点：    

    （1）支持自定义宏命令  

主要功能：            

    （1）算法应用组件自由组合                                                 

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from abc import ABCMeta,abstractmethod
from collections import OrderedDict



####### 算法应用组件组合类 ######################################################
### 设计模式：                                                               ###
### （1）命令模式                                                            ###
### 关键点：                                                                 ###
### （1）支持自定义宏命令                                                     ###
### 主要功能：                                                               ###
### （1）算法应用组件自由组合                                                  ###
################################################################################



###### 基础模块类 #####################################################################
######################################################################################



class CommandBase(metaclass = ABCMeta):
    """
    类介绍：

        这是一个命令模式的基类，主要用于命令对象化的抽象。
    """


    def __init__(self,role,role_name):
        """
        属性功能：

            role (Object): 命令角色对象
            role_name (str): 命令角色名称
        """

        self._role = role
        self.role_name = role_name


    def setRole(self,role):
        """
        方法功能：

            定义一个设置命令角色实体的方法

        参数：
            role (Object): 命令角色对象

        返回：
            无
        """

        self._role = role


    @abstractmethod
    def execute(self):
        """
        方法功能：

            定义一个执行命令的抽象方法
        """

        pass



class CommandInvoker(object):
    """
    类介绍：

        这是一个命令调度者抽象类，主要用于调度各种命令，组合各种逻辑命令实现一项具体功能
    """


    def __init__(self):
        """
        属性功能：

            __command (Object)：命令实体
        """

        self.__command = None


    def setCommand(self,command):
        """
        方法功能：

            定义一个设置命令实体的方法

        参数：
            command (Object): 命令实体

        返回：
            self (Object): 命令调度者实例
        """

        self.__command = command

        return self


    def action(self,**kwargs):
        """
        方法功能：

            定义一个具体执行命令实体的接口
        """

        result = None
        if self.__command is not None:
            result = self.__command.execute(**kwargs)
        return result


    def show_result(self,foundation_instance):
        """
        方法功能：

            定义一个获取命令结果的接口

        参数：
            foundation_instance (Object): 命令实例

        返回：
            result (Object): 结果实例
        """
        
        result = foundation_instance.extend.Prolong.prolong_instance.data

        return result



####### 算法组件组合命令模式具体实现类 #####################################################################
##########################################################################################################



class MacroCommand(CommandBase):
    """
    类介绍：

        这是一个宏命令类，主要用来组合各种具体命令
    """


    def __init__(self,role = None,role_name = None):
        """
        属性功能：

            role (Object): 命令角色实体
            role_name (str): 命令角色名称
            __commands (OrderDict): 命令存储池
            data (Dict): 数据缓存池
        """

        super().__init__(role,role_name)
        self.__commands = OrderedDict()
        self.data = {}


    def addCommand(self,command):
        """
        方法功能：

            定义一个添加命令实体的方法

        参数：
            command (Object): 命令对象

        返回：
            无
        """

        command_name = command.role_name
        self.__commands[command_name] = command


    def removeCommand(self,command):
        """
        方法功能：

            定义一个删除命令对象的方法

        参数：
            command (Object): 命令对象

        返回：
            无
        """

        command_name = command.role_name
        self.__commands.pop(str(command_name))


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个执行命令操作的方法，主要调用命令角色的execute，即Foundation中的execute方法
        """

        result = None
        for command in self.__commands.values():
            result = command.execute(**kwargs)
        return result



class CommandInstance(CommandBase):
    """
    类介绍：

        这是一个对象化的具体命令类，主要作用是抽象具体命令，隔离解耦
    """
    

    def __init__(self,role,role_name):
        """
        属性功能：

            继承父类
            data (Dict): 数据缓存池
        """

        super().__init__(role,role_name)
        self.data ={}


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个执行具体的命令动作的方法
        """

        reuslt = None
        reuslt = self._role.execute(**kwargs)

        return reuslt


    
class CommandInterface(object):
    """
    类介绍：

        这是一个具体命令的接口类，主要用于利用命令模式将Foundation组合成一个新的命令对象并提供接口，主要采用静态方法技术。
    """


    def __init__(self):
        """
        属性功能：

            invoker (Object): 命令调度者实例
            cmd (Object): 宏命令实例
        """

        self.invoker = CommandInvoker()
        self.cmd = MacroCommand()


    def add_foundation(self,foundation_instance,foundation_name):
        """
        方法功能：

            定义一个添加命令对象的方法

        参数：
            foundation_instance (Object): 基础命令示例
            foundation_name (str): 基础命令名称

        返回：
            无
        """

        self.cmd.addCommand(CommandInstance(foundation_instance,foundation_name))
        return 'Add foundation successful!'


    def simple_execute_macrocommand(self,foundation_instance,**kwargs):
        """
        方法功能：

            定义一个依次线性执行宏命令的逻辑方法

        参数：
            foundation_instance (Object): 基础命令示例

        返回：
            return_result (Object): 执行结果            
        """

        result = self.invoker.setCommand(self.cmd).action(**kwargs)
        return_result = self.invoker.show_result(foundation_instance)
        return return_result



#####################################################################################################################
#####################################################################################################################


