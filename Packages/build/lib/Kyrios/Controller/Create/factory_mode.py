# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个算法应用组件创建模块，主要技术采用工厂模式
"""
模块介绍
-------

这是一个算法应用组件创建模块，主要技术采用工厂模式

设计模式：

    （1）工厂模式   

关键点：    

    （1）通过工厂模式划分功能模块 

主要功能：            

    （1）创建算法应用组件                                                  

使用示例
-------

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from abc import ABCMeta,abstractmethod
from enum import Enum
from Kyrios.Foundation.Manager.hydra_config import *
from Kyrios.Foundation.Compute.ray_config import *
from Kyrios.Foundation.Store.alluxio_client import *
from Kyrios.Extend.Tools.tmp import *



####### 算法应用组件工厂类 ##################################################
### 设计模式：                                                           ###
### （1）工厂模式                                                        ###
### 关键点：                                                             ###
### （1）通过工厂模式划分功能模块                                          ###
### 主要功能：                                                           ###
### （1）创建算法应用组件                                                 ###
############################################################################



###### 基础模块类 #####################################################################
######################################################################################



class ProductType(Enum):
    """
    类介绍：

        这是一个功能操作枚举类，主要包括设计、计算、存储、通信、管理和接口六大功能
    """


    ### 设计
    ProductTypeDesign = 1
    ### 计算
    ProductTypeCompute = 2
    ### 存储
    ProductTypeStore = 3
    ### 通信
    ProductTypeCommunication = 4
    ### 管理
    ProductTypeManager = 5
    ### 接口
    ProductTypeInterface = 6



class Product(metaclass=ABCMeta):
    """
    类介绍：

        这是一个工厂模式中的抽象产品类
    """


    def __init__(self,name):
        """
        属性功能：

            name (str): 工厂产品名称
        """

        self.__name = name


    @abstractmethod
    def set_product(self):
        """
        方法功能：

            定义一个配置产品的方法
        """

        pass


    def get_name(self):
        """
        方法功能：

            定义一个获取产品名称的方法
        """

        return self.__name



####### 算法应用组件具体实现类 ##########################################################################
#######################################################################################################



class ProductManager(Product):
    """
    类介绍：

        这是一个算法应用管理组件的具体实现类，主要技术有Hydra，支持动态配置功能
    """


    def __init__(self,name):
        """
        属性功能：

            集成父类
        """

        super().__init__(name)


    def set_product(self):
        """
        方法功能：

            定义一个配置产品的具体方法
        """

        Hydraitem = HydraConfig()
        Hydraitem.info.info_dict = {'HydraConfig':'Hydra动态配置'}
        Hydraitem.customize(generate_execute_file,'generate_execute_file')

        return Hydraitem# 'Set product successfully!'



class ProductComputer(Product):
    """
    类介绍：

        这是一个算法应用计算组件的具体实现类，主要技术有Ray，支持生成分布式计算代码的功能
    """    


    def __init__(self,name):
        """
        属性功能：

            集成父类
        """

        super().__init__(name)


    def set_product(self):
        """
        方法功能：

            定义一个配置产品的具体方法
        """

        Rayitem = RayConfig()
        Rayitem.info.info_dict = {'RayConfig':'Ray动态配置'}
        Rayitem.customize(generate_execute_file,'generate_execute_file')

        return Rayitem# 'Set product successfully!'



class ProductStore(Product):
    """
    类介绍：

        这是一个算法应用存储组件的具体实现类，主要技术有Alluxio，支持与数据抽象层交互的功能
    """    


    def __init__(self,name):
        """
        属性功能：

            集成父类
        """

        super().__init__(name)


    def set_product(self):
        """
        方法功能：

            定义一个配置产品的具体方法
        """        

        Alluxioitem = AlluxioClient()
        Alluxioitem.info.info_dict = {'AlluxioClient':'Alluxio客户端'}
        Alluxioitem.customize(generate_alluxio_client,'generate_alluxio_client')

        return Alluxioitem# 'Set product successfully!'



####### 算法组件工厂类 ####################################################################################
##########################################################################################################



class ProductFactory(object):
    """
    类介绍：

        这是一个产品工厂类，主要用于根据具体的模板生产制作Foundation对象，主要技术采用抽象工厂
    """


    def __init__(self):
        """
        属性功能：

            __products (Dict): 产品字典
        """

        self.__products = {}


    def get_single_object(self,product_name):
        """
        方法功能：

            定义一个获取单个对象的方法

        参数：
            product_name (str): 产品名称

        返回：
            product (Object): 产品对象 
        """

        return self.__products[product_name]


    def create_product(self,product_type):
        """
        方法功能：

            定义一个调用制作Foundation对象的方法，主要利用Foundation中的Extend功能添加具体功能，在set_product中实现。

        参数：
            product_type (Enum): 枚举类中的类型

        返回：
            无 ：直接返回在属性中
        """
        if (self.__products.get(product_type) is None):
            if product_type == ProductType.ProductTypeDesign:
                print("ProductTypeDesign!")
            elif product_type == ProductType.ProductTypeStore:
                ProductAlluxioClient = ProductStore('AlluxioClient')
                product = ProductAlluxioClient.set_product()
            elif product_type == ProductType.ProductTypeCompute:
                ProductRayConfig = ProductComputer('RayConfig')
                product = ProductRayConfig.set_product()
            elif product_type == ProductType.ProductTypeManager:
                ProductHydraConfig = ProductManager('HydraConfig')
                product = ProductHydraConfig.set_product()
            elif product_type == ProductType.ProductTypeCommunication:
                print("ProductTypeCommunication")
            elif product_type == ProductType.ProductTypeInterface:
                print("ProductTypeInterface")
            else:
                product = Product("")
            self.__products[product_type] = product 

        return self.__products[product_type]
            


####################################################################################################################
####################################################################################################################


