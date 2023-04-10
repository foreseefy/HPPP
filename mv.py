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

def create(path):
    is_Exists = os.path.exists(path)
    if not is_Exists:
        os.makedirs(path)

def jianqie(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist"%(srcfile))
    else:
        fpath,fname = os.path.split(dstfile)
        #判断路径存在
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        #复制文件并命名
        shutil.move(srcfile,dstfile)
        print("move %s -> %s"%(srcfile,dstfile))



#把matlab运行完后的色散图放进HPPP_plt中画图
# list = ['BN','BP','AlN','AlP']
#
# dire = 'z'
# for item in list:
#     srcfile = f'../dispersion/{item}/{dire}/dispersion.txt'
#     dstfile = f'./dispersion/{dire}/{item}.txt'
#     mycopyfile(srcfile,dstfile)

# i = 'AlP'
# srcfile1 = r'C:\Users\ADMIN\Desktop\phonopy.yaml'
# srcfile2 = r'C:\Users\ADMIN\Desktop\qpoints.yaml'
# dstfile1 = f'..\dispersion\{i}\y\phonopy.yaml'
# dstfile2 = f'..\dispersion\{i}\y\qpoints.yaml'
# jianqie(srcfile1,dstfile1)
# jianqie(srcfile2,dstfile2)