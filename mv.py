import os
import shutil

def mycopyfile(file_name,srcfile,dstpath):
    if not os.path.isfile(srcfile):
        print("%s not exist"%(srcfile))
    else:
        # fpath,fname = os.path.split(srcfile)
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)
        fname = dstpath + '\\' + file_name + '2.txt'
        print(dstpath)
        shutil.copy(srcfile,fname)
        # new_name = '2'+ file_name
        # os.rename()
        print("copy %s -> %s"%(srcfile,dstpath))

def rename(file_name):
    src_dir = f'..\Dispersion\{file_name}'
    dst_dir = '.\dispersion'
    src_file= src_dir + '\dispersion.txt'
    # print(src_file)
    mycopyfile(file_name,src_file,dst_dir)
