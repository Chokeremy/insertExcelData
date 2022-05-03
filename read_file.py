class ReadFile:
    """读写文件"""

    def __init__(self, file_path):

        self.file_path = file_path

    def open_file(self):

        with open(self.file_path, 'r+', encoding='utf-8') as f:
            fi = f.read()

            fv = []

            # 把txt文件内容按照换行符分割，然后按照逗号分割追加到fc列表，然后把整个fc列表追加到fv列表，再把fc列表置空，重新生成fc列表
            for i in fi.split('\n'):
                fc = []

                for j in i.split(','):
                    fc.append(j)
                fv.append(fc)
        # 因为换行符导致分割的最后一个是''，所以用pop()删除最后一个''元素
        fv.pop()
        return fv
