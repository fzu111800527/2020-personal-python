import json
import getopt
import sys
import os


def readjson(addr):
    filelist = os.listdir(addr)#读取文件列表
    f2=open('data.json','w',encoding= 'utf-8')
    for file in filelist:#读json文件
        if file[-5:] == '.json':
            pathname = addr + '\\' + file
            with open(pathname,encoding='utf-8') as f:
                for line in f:
                    f2.write(line)#写入data.json
    return

def calculate_result(data,username,reponame,eventname):
    count = 0
    for line in data:
        if not len(username) == 0:
            if username == da['actor']['login']:
                if not reponame == 0:
                    if reponame == da['repo']['name']:
                        if da['type'] == eventname:
                            count += 1
    return count


def main():
    data = []
    username = ''
    reponame = ''
    eventname = ''
    options, args = getopt.getopt(sys.argv[1:], 'i:u:r:e:', ['init=','user=','repo=','event='])
    if options in ('-i', '--init'):
        readjson(options[0][1])
        print(0)
        exit()
    else:
        with open("data.json",encoding='utf-8') as f:
            for line in f:
                data.append(json.loads((line)))
    for name, value in options:
        if name in ('-u'):
            username = value
        if name in ('-r'):
            reponame = value
        if name in ('-e'):
            eventname = value
    print(calculate_result(data,username,reponame,eventname))


if __name__ == "__main__":
    main()
