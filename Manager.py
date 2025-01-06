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
        节点名称序号映射表， 包名称序号映射表， 节点序号与包序号的关系
        Args:
            custom_node_path: 
        """
        self.root = Path(custom_node_path)

        self.nodes = []
        self.nodes_idx = None
        # {"package_name": [Package...]}
        self.packages_dict = {}
        # {"package_name": version}
        self.standard_version_package = {}

        self.read_data()
        self.sort_version()
        self.max_overlap_version_intervals()
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
                        self.packages_dict.setdefault(package.name, []).append(package)


    def sort_version(self):
        for package_name, version_list in self.packages_dict.items():
            l = sorted(version_list, key=cmp_to_key(Package.version_cmp))
            self.packages_dict[package_name] = l

            # 考虑修改后受影响的节点数，不进行去重
            # for idx, package in enumerate(l):
            #     if idx == 0 or l[idx-1] != package:
            #         version_list.append(package)


    def updater(self):
        """
        通过比较version和symbol来更新requirements文件
        Args:

        Returns:

        """
        with open(Path(self.root, "requirements.txt"), "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                temp_package = Package(line)


    def judge(self, package):
        """
        判断是否有冲突
        Args:
            package:

        Returns:

        """
        pass

    def max_overlap_version_intervals(self):
        """
        找出最大重叠区间
        Returns:
                Package
        """
        for package_name, package_list in self.packages_dict.items():
            length = len(package_list)
            counter = [0]*length
            for idx, package in enumerate(package_list[1:]):
                symbol = package.symbol
                if symbol == "<" or symbol == "<=":
                    counter[idx+1] = counter[idx]+1
                elif symbol == ">" or symbol == ">=":
                    counter[idx+1] = counter[idx]-1

            max_overlap = max(counter)
            max_index = counter.index(max_overlap)

            # 新建标准对象
            if max_index <= length / 2:
                standard_symbol = ">="
            else:
                standard_symbol = "<="

            version_string = package_list[max_index].name + standard_symbol + package_list[max_index].version
            self.standard_version_package[package_name] = Package(version_string)




