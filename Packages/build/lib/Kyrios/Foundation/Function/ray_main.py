# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个根据模板生成分布式计算剧本的脚本
"""
模块介绍
-------

这是一个根据模板生成分布式计算剧本的脚本

设计模式：

    （1）无

关键点：    

    （1）Ray  

主要功能：            

    （1）分布式计算                                                   

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import hydra
from omegaconf import DictConfig,OmegaConf
from Kyrios.Foundation.Function.gen_jinja2 import * ### 安装的时候使用这一行引入需要的包
from ServerManager.ServerCommandInterface import *



####### RayAPP #############################################################
### 设计模式：                                                            ###
### （1）无                                                              ###
### 关键点：                                                             ###
### （1）Ray                                                             ###
### 主要功能：                                                           ###
### （1）分布式计算                                                       ###
############################################################################



###### RayAPP ########################################################################
######################################################################################
# tmp_value = ServerManager.InputParameter(host = "10.2.65.46",
#                                         port = 8500,
#                                         key = 'hydra_config_path',
#                                         value = './conf')
# tmp_value = ServerManager.InputParameter(host = "10.2.65.46",
#                                         port = 8500,
#                                         key = 'hydra_jinja2_searchpath',
#                                         value = 'D:\\AEwork\\algorithm_platform\\Kyrios\\TEST')
# tmp_value = ServerManager.InputParameter(host = "10.2.65.46",
#                                         port = 8500,
#                                         key = 'hydra_gen_file',
#                                         value = 'D:\\AEwork\\algorithm_platform\\Kyrios\\TEST\\tmp_hydra.py')                                        
# tmp_value = ServerManager.InputParameter(host = "10.2.65.46",
#                                         port = 8500,
#                                         key = 'hydra_template_name',
#                                         value = 'test_hydra_template')
# value = str({'test':{'a':1,'b':2},'tmp':{}})
# tmp_value = ServerManager.InputParameter(host = "10.2.65.46",
#                                         port = 8500,
#                                         key = 'hydra_parameters',
#                                         value = value)    
ServerManager = ServerManagerCommandInterface()
config_path = ServerManager.GetParameter(host = "10.2.65.46",
                                        port = 8500,
                                        key = 'ray_config_path')
ray_jinja2_searchpath = ServerManager.GetParameter(host = "10.2.65.46",
                                        port = 8500,
                                        key = 'ray_jinja2_searchpath')
ray_gen_file =  ServerManager.GetParameter(host = "10.2.65.46",
                                        port = 8500,
                                        key = 'ray_gen_file')                                       
ray_template_name = ServerManager.GetParameter(host = "10.2.65.46",
                                        port = 8500,
                                        key = 'ray_template_name')
# ray_parameters = ServerManager.GetParameter(host = "10.2.65.46",
#                                         port = 8500,
#                                         key = 'ray_parameters')                                                                               
@hydra.main(config_path=config_path)
def my_app(cfg : DictConfig) -> None:
    tmp_yaml = OmegaConf.to_yaml(cfg)
    print(tmp_yaml)
    # exec('from {} import *'.format(cfg.algorithm.py_name))
    print(cfg.algorithm)
    function_list =  list(cfg.algorithm.function_list)
    result_list = list(cfg.algorithm.result_list)
    import_packages = list(cfg.algorithm.import_packages)
    ray_parameters = dict(cfg.algorithm.parameters)
    ray_list = list(cfg.algorithm.ray_list)
    print("?????????",ray_parameters,type(ray_parameters))
    gen_jinja2(searchpath=ray_jinja2_searchpath,
            template_name=ray_template_name,
            render_paras_dict={'import_packages':import_packages,
                                'function_list':function_list,
                                'parameters_dict':ray_parameters,
                                'result_list':result_list,
                                'ray_list':ray_list},
            gen_file=ray_gen_file)
    print(cfg.db.driver)
    print(cfg.algorithm)


if __name__ == "__main__":
    my_app()



### python D:\AEwork\algorithm_platform\Kyrios\Demo\Kyrios\Foundation\Function\ray_main.py +db=mysql +algorithm=ai_1



########################################################################################################################
########################################################################################################################


