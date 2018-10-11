import json
import os
import shutil
import re


def mkdir(path):
    for roots,dirs,names in os.walk(path):
        root = re.findall(r'\d+.\d+.\d',roots)
        if len(root)!=0:
            dirName = ('winxp','win8','win7','win2003','win2008','centos','ubuntu_16_4','debian')
            for name in dirName:
                isExists = os.path.exists(roots+'\\'+name)
                if not isExists:
                    verPath = roots+'\\'+name
                    os.mkdir(verPath)
                    verPaths = verPath.split()
                    print(verPath)

def getPath(path): ##所有网段目录
    paths = list()
    for roots,dirs,files in os.walk(path):
        root = re.findall(r'\d+.\d+.\d',roots)
        if len(root) != 0:
            paths.append(roots)
        else:
            pass
    return paths        
            # return roots
def getName(path): #所有ip文件
    files = list()
    for roots,dirs,names in os.walk(path):
        for name in names:
            name = re.findall(r'\d+.\d+.\d+.\d+.txt',name)
            if len(name) == 0:
                continue
            else:
                files.append(name[0])
    return files
def getVer(file):
    try:
        data = open(file)
        setting = json.load(data)
        Ver = setting['system']
        print (Ver)
        data.close()
        return Ver
    except Exception as e:
        pass
    

def moveFile(path,Ver,name):
    print(path)
    print(Ver)
    print(name)
    try:
        if Ver == 'winxp':
            shutil.move(path+'\\'+name,path+'\\'+'win2003'+'\\'+name)
        elif Ver == 'win8':
            shutil.move(path+'\\'+name,path+'\\'+'win2008'+'\\'+name)
        elif Ver == 'win7':
            shutil.move(path+'\\'+name,path+'\\'+'win2003'+'\\'+name)
        elif Ver == 'win7-32':
            shutil.move(path+'\\'+name,path+'\\'+'win2008'+'\\'+name)
        elif Ver == 'win2003':
            shutil.move(path+'\\'+name,path+'\\'+'win2003'+'\\'+name)
        elif Ver == 'win2008':
            shutil.move(path+'\\'+name,path+'\\'+'win2008'+'\\'+name)
        elif Ver == 'centos':
            shutil.move(path+'\\'+name,path+'\\'+'centos'+'\\'+name)
        elif Ver == 'ubuntu':
            shutil.move(path+'\\'+name,path+'\\'+'centos'+'\\'+name)
        elif Ver == 'debian':
            shutil.move(path+'\\'+name,path+'\\'+'centos'+'\\'+name)
    except Exception as e:
        pass
if __name__ == '__main__':
    path = "F:\\json_solve\\file"
    paths = getPath(path)
    print (paths)
    for path in paths:
        # print(path)
        os.chdir(path)
        mkdir(path)
        names = getName(path)
        for name in names:
            # print(name)
            file_path = path+'\\'+name
            Ver = getVer(path+'\\'+name)
            # new_path = path+'\\'+Ver+
            moveFile(path,Ver,name)
            print(Ver)
