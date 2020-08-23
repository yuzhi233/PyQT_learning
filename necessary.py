# 由于找不到好的解决方法 每次运行代码前需要添加
# 具体https://blog.csdn.net/ouening/article/details/81093697
import PySide2
import os
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path