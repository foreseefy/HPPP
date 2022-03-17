import os
import shutil

def mycopyfile(file_name,srcfile,dstpath):
    #判断文件存在
    if not os.path.isfile(srcfile):
        print("%s not exist"%(srcfile))
    else:
        # fpath,fname = os.path.split(srcfile)
        #判断路径存在
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)
        fname = dstpath + '\\' + file_name + '.txt'
        #复制文件并命名
        shutil.copy(srcfile,fname)
        print("copy %s -> %s"%(srcfile,dstpath))

#其中的一个例子
def rename(file_name,graph_name):
    src_dir = f'..\{graph_name}\{file_name}'
    dst_dir = f'.\{graph_name}'
    src_file= src_dir + f'\{graph_name}.txt'
    # print(src_file)
    mycopyfile(file_name,src_file,dst_dir)
