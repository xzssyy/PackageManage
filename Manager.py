from pathlib import Path
from Packege import Package
from functools import cmp_to_key

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
        self.packages_version_dict = {}
        self.packages_updated_version = {}

        self.read_data()
        self.sort_version()
        pass




    def read_data(self):
        """
            读取客制化节点根目录下的描述数据：客制化节点名称，依赖包
        Returns:

        """
        self.nodes = [folder.name for idx, folder in enumerate(self.root.iterdir()) if folder.is_dir()]

        for node_name in self.nodes:
            req_path = Path(self.root, node_name, "requirements.txt")
            if not req_path.exists():
                return

            with open(req_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    package = Package(line.strip('\n'))
                    # 添加version进待排序列表
                    if package.name is not None:
                        self.packages_version_dict.setdefault(package.name, []).append(package)


    def sort_version(self):
        for package_name, version_list in self.packages_version_dict.items():

            l = sorted(version_list, key=cmp_to_key(Package.version_cmp))
            version_list.clear()
            for idx, package in enumerate(l):
                if idx == 0 or l[idx-1] != package:
                    version_list.append(package)

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
                #if self.judge_conflict()
