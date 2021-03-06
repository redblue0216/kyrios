
from Kyrios.Extend.Base.basic import *
# from Kyrios.Extend.Tools.state import *
# from Kyrios.Extend.Tools.structure import *
# import networkx as nx
# from Kyrios.Extend.Tools.extend import *
# from Kyrios.Extend.Tools.interface import *
from Kyrios.Foundation.Manager.hydra_config import *
from Kyrios.Controller.Create.factory_mode import *
from Kyrios.Controller.Create.build_mode import *
from Kyrios.Controller.Behaviour.command_mode import *
from Kyrios.Foundation.Function.function_interface import *


Baseitem = Baseitem()
### info测试
print("======================================================================== （1）info测试")
Baseitem.info.info_dict = {'1':'测试信息类'}
print(Baseitem.info.info_dict)
### state测试
print("======================================================================== （2）state测试")
Baseitem.state.FiniteStateMachine.update_mode(' >= 0.6')
Baseitem.state.FiniteStateMachine.setIndex(0.7)
print("接收到指标后的状态：",Baseitem.state.FiniteStateMachine.state)
Baseitem.state.FiniteStateMachine.stop()
print("运行完成后的状态",Baseitem.state.FiniteStateMachine.state)
Baseitem.state.FiniteStateMachine.restart()
print("重新启动：",Baseitem.state.FiniteStateMachine.state)
### structure测试
print("======================================================================== （3）structure测试")
Baseitem.structure.graph.add_edges_from([('n', 'n1'), ('n3', 'n1'), ('n2', 'n3')])
toposort_list = Baseitem.structure.graph_algorithm(algorithm = 'toposort')
print(Baseitem.structure.graph.nodes(),toposort_list)
### extend测试
print("======================================================================== （4）extend测试")
from Kyrios.Extend.Tools.tmp import *
Baseitem.extend.Prolong.add_dynamic_method(set_age,'set_age')
Baseitem.extend.Prolong.add_dynamic_method(set_sex,'set_sex')
print(Baseitem.extend.Prolong.show_function())
Baseitem.extend.Prolong.prolong_instance.set_age(10)
print(Baseitem.extend.Prolong.prolong_instance.data['age'])
Baseitem.extend.Prolong.prolong_instance.set_age(20)
print(Baseitem.extend.Prolong.prolong_instance.data['age'])
### interface测试
print("======================================================================== （5）interface测试")
from Kyrios.Extend.Tools.tmp import *
def test():
    test_source_target.test()
Baseitem.interface.Wedge.add_source_target(test_source_target)
Baseitem.interface.Wedge.function(test,'test')
Baseitem.interface.Wedge.run_interface('test')
print(Baseitem.interface.Wedge.function_dict)
### Foundation测试
print("======================================================================== （6）HydraConfig测试")
Hydraitem = HydraConfig()
Hydraitem.info.info_dict = {'1':'测试信息类'}
print(Hydraitem.info.info_dict)
Hydraitem.customize(set_sex,'set_sex')
Hydraitem.execute(function_name = 'set_sex',sex = 'male')
print(Hydraitem.extend.Prolong.show_function())
print(Hydraitem.extend.Prolong.prolong_instance.data['sex'])
Hydraitem.customize(generate_execute_file,'gen_exec_file')
print(Hydraitem.extend.Prolong.show_function())
cmd_tmp = 'python D:\\AEwork\\algorithm_platform\\Kyrios\\Demo\\Kyrios\\Foundation\\Function\\hydra_main.py +db=mysql +algorithm=ai_1'
Hydraitem.execute(function_name = 'gen_exec_file',cmd = str(cmd_tmp))
### factory_mode测试
print("======================================================================== （7）factory_mode测试")
factory = ProductFactory()
ProductHydra = factory.create_product(ProductType.ProductTypeManager)
print(ProductHydra.extend.Prolong.show_function())
ProductHydra.execute(function_name = 'set_sex',sex = 'female')
print(ProductHydra.extend.Prolong.show_function())
print(ProductHydra.extend.Prolong.prolong_instance.data['sex'])
### build_mode测试
print("======================================================================== （8）build_mode测试")
from Kyrios.Extend.Tools.tmp import *
custom_item = BuildManager()
custom_item.add_customize_component(set_age,'set_age')
custom_item.add_customize_component(set_sex,'set_sex')
custom_item.add_customize_component(set_value,'set_value')
components = custom_item.show_components('all')
print(ProductHydra.extend.Prolong.show_function())
custom_item.mount_component('set_value',ProductHydra)
print(ProductHydra.extend.Prolong.show_function())
### command_mode测试
print("======================================================================== （9）command_mode测试")
command_interfacer = CommandInterface()
command_interfacer.add_foundation(ProductHydra,'Hydra')
return_result = command_interfacer.simple_execute_macrocommand(ProductHydra,function_name = 'set_sex',sex = 'male_male')
print(return_result)
### hydra测试
print("======================================================================== （10）hydra测试")
factory = ProductFactory()
ProductHydra = factory.create_product(ProductType.ProductTypeManager)
print(ProductHydra.extend.Prolong.show_function())
cmd_tmp = 'python D:\\AEwork\\algorithm_platform\\Kyrios\\Demo\\Kyrios\\Foundation\\Function\\hydra_main.py +db=mysql +algorithm=ai_1'
ProductHydra.execute(function_name = 'generate_execute_file',cmd = cmd_tmp)
### ray测试
print("======================================================================== （11）ray测试")
cmd_tmp = 'python D:\\AEwork\\algorithm_platform\\Kyrios\\Demo\\Kyrios\\Foundation\\Function\\ray_main.py +db=mysql +algorithm=ray'
factory = ProductFactory()
ProductRay = factory.create_product(ProductType.ProductTypeCompute)
print(ProductRay.extend.Prolong.show_function())
ProductRay.execute(function_name = 'generate_execute_file',cmd = cmd_tmp)
### 辅助测试
print("======================================================================== （12）辅助测试")
# from ServerManager.ServerCommandInterface import *
# # minio server test
# object_file = 'D:\\AEwork\\algorithm_platform\\Kyrios\\TEST\\ray\\tmp_ray.py'
# tmp_interface = ServerManagerCommandInterface()
# tmp_value = tmp_interface.PutObject(connect_info = '10.2.12.248:9000',
#                                                     access_key = 'minioadmin',
#                                                     secret_key = 'minioadmin',
#                                                     secure = False,
#                                                     object_file = object_file,
#                                                     bucket = 'ray')                                                    
# print("===============>",tmp_value)
# SSH_host_dict = {
# 	'host' : '10.2.12.248',
# 	'port' : 22,
# 	'username' : 'shihua',
# 	'pwd' : 'ATTACK7121553rb1'
# }
# command = "cd /home/shihua/tulip/test/ray/;mv 'D:\\AEwork\\algorithm_platform\\Kyrios\\TEST\\ray\\tmp_ray.py' tmp_ray.py"
# tmp_value = ServerManagerCommandInterface.SSHRunCMD(SSH_host_dict = SSH_host_dict,
#                                                     command = command)
# print("===============>",tmp_value)
### Alluxio测试
factory = ProductFactory()
ProductAlluxio = factory.create_product(ProductType.ProductTypeStore)
print(ProductAlluxio.extend.Prolong.show_function())
alluxio_client = ProductAlluxio.execute(function_name = 'generate_alluxio_client',host = '10.2.12.248',port = 39999)
print(alluxio_client.ls('/'))
print(dir(alluxio_client))





















































































