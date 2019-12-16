#!/usr/bin/env python


import gitlab,re

client = gitlab.Gitlab('gitlab私服ip端口', private_token='gitlab私服自己上面生成的私钥', timeout=5, api_version='4')
client.auth()

pro = client.projects.get(1)
#打印出id为1的项目的所有信息 键值对json格式
print(pro.attributes)

#打印出id为1的项目的namespace
#print(pro.namespace)

#打印出id为1的项目的http访问的路径
#print(pro.http_url_to_repo)


#branchs = pro.branches.list()

#for bran in branchs:
#    print(bran.name)

"""
counts=1
#找出这个gitlab私服上的所有项目 
project = client.projects.list(all=True)
for pro in project:
    #如果访问http项目路径中包含以下的字符串，则统计这个项目的所有分支
    if re.findall("jryms_group/dev", pro.http_url_to_repo):
           # print(counts)
           # counts = counts + 1
            print(pro.http_url_to_repo)
            branchs = pro.branches.list()
            for bran in branchs:
                print(counts)
                counts = counts + 1
                print(bran.name)
"""
