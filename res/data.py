import os
import shutil

def find_class(path):

    fs = os.listdir(path)
    for f in fs:
        p = path +"/"+str(f)
        with open(p, 'r') as fp:
            num = fp.readline().split(" ")[0]
            print("num = "+num)
            if num == '' or len(num) == 0:
                continue
            rf = './dataset/validation/'+str(num)
            f_n = f.split('.txt')[0]+".JPG"
            mkdir_dataset(rf,'./datasets/pest/images/val2017/'+f_n,'./dataset/validation/'+str(num)+"/"+f_n)

def mkdir_dataset(path, src_file, d_file):

    if not os.path.exists(path):
        os.makedirs(path)

        shutil.copyfile(src_file, d_file)
    else:
        shutil.copyfile(src_file, d_file)




find_class('./datasets/pest/labels/val2017')