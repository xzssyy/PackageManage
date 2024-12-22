from pathlib import Path
from Packege import Package
import numpy as np

class Manager:
    """
        读取目录下各个客制化节点的依赖包目录

    """

    def __init__(self, custom_node_path):
        self.root = Path(custom_node_path)

        # {"pack_name":[(node_name, )]}
        self.data = {}
        # {"pack_bane":"base_version"}
        self.packages_need = {}
        nodes_name = [folder.name for folder in self.root.iterdir() if folder.is_dir()]




    def judge_conflict(self, base_package, package):





    def read_data(self, node_name):
        self.data[node_name] = []
        req_path = Path(self.root, node_name, "requirements.txt")
        package_list = []
        with open(req_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                package = Package(line)



    def modify_req_file(self, node_name):
        with open(Path(self.root, node_name, "requirements.txt"), "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                temp_package = Package(line)
                if self.judge_conflict()
