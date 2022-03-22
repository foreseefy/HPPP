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



#
list = ['BN','BP','AlN','AlP','GaP']
# list2 = ['x','y','z']
# for i in list:
#     for j in list2:
#         path = f'..\dispersion\{i}\{j}'
#         create(path)
# for i in list:
#     srcfile = f'..\dispersion\{i}\z\OUTCAR.txt'
#     dstfile = f'..\dispersion\{i}\y\OUTCAR.txt'
#     mycopyfile(srcfile,dstfile)
i = 'AlP'
srcfile1 = r'C:\Users\ADMIN\Desktop\phonopy.yaml'
srcfile2 = r'C:\Users\ADMIN\Desktop\qpoints.yaml'
dstfile1 = f'..\dispersion\{i}\y\phonopy.yaml'
dstfile2 = f'..\dispersion\{i}\y\qpoints.yaml'
jianqie(srcfile1,dstfile1)
jianqie(srcfile2,dstfile2)