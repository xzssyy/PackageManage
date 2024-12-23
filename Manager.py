from pathlib import Path
from Packege import Package
import numpy as np

class Manager:
    """
        读取目录下各个客制化节点的依赖包目录

    """

    def __init__(self, custom_node_path):
        """
        保存数据结构
        节点名称序号映射表， 包名称序号映射表， 节点序号与包序号的关系图
        Args:
            custom_node_path: 
        """
        self.root = Path(custom_node_path)

        self.nodes = []
        self.nodes_idx = None
        self.packages = []
        self.nodes_num = 0
        self.packages_num = 0
        # 初始化为100*1000的数组
        self.np_map = np.zeros((100, 1000))
        self.read_data()




    def read_data(self):
        self.
        self.nodes_idx = {folder.name : idx for idx, folder in enumerate(self.root.iterdir()) if folder.is_dir()}
        for node_name, _ in self.nodes.items():
            self.read_node_packages(node_name)




    def read_node_packages(self, node_name):

        req_path = Path(self.root, node_name, "requirements.txt")
        if not req_path.exists():
            return

        with open(req_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                package = Package(line)



    def judge_conflict(self, base_package, package):
        pass







    def modify_req_file(self, node_name):
        """
        修改对应node的requirements文件
        Args:
            node_name: 

        Returns:

        """
        with open(Path(self.root, node_name, "requirements.txt"), "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                temp_package = Package(line)
                if self.judge_conflict()
