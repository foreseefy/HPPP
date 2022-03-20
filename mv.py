import os
import shutil

def mycopyfile(srcfile,dstfile):
    #判断文件存在
    if not os.path.isfile(srcfile):
        print("%s not exist"%(srcfile))
    else:
        fpath,fname = os.path.split(dstfile)
        #判断路径存在
        if not os.path.exists(fpath):
            os.makedirs(fpath)

        #复制文件并命名
        shutil.copy(srcfile,dstfile)
        print("copy %s -> %s"%(srcfile,dstfile))


srcfile = '..\dispersion\BN\dispersion.txt'
dstfile = '.\dispersion\y\dispersion.txt'
mycopyfile(srcfile,dstfile)