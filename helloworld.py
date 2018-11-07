#!/usr/bin/env python
#start write python
print("hello world!")
'''
#gitlab默认的存储位置
/var/opt/gitlab/git-data
课间休息：
a.安装windows软件Git-2.10.0-64-bit.exe  下一步下一步。。。
b. 

[root@gitlab ~]# mkdir -p /application/tools
[root@gitlab ~]# cd /application/tools
[root@gitlab tools]# rz -E   #上传gitlab-ce-9.1.4-ce.0.el7.x86_64.rpm

yum localinstall gitlab-ce-9.1.4-ce.0.el7.x86_64.rpm
gitlab-ctl reconfigure   
gitlab-ctl start/stop/restart
#默认开机自启动
systemctl is-enabled gitlab-runsvdir.service
帐号：root
密码rootroot
git clone git@10.0.0.63:root/40team.git
老男孩教育-张导(744237154)  10:55:12
sshkey
cat  /root/.ssh/id_rsa.pub
老男孩教育-张导(744237154)  10:57:18
ssh git@10.0.0.63


Git global setup

git config --global user.name "Administrator"
git config --global user.email "admin@example.com"

Create a new repository

git clone git@gitlab:root/40team.git
cd 40team
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master

Existing folder

cd existing_folder
git init
git remote add origin git@gitlab:root/40team.git
git add .
git commit
git push -u origin master

Existing Git repository

cd existing_repo
git remote add origin git@gitlab:root/40team.git
git push -u origin --all
git push -u origin --tags
git pull
5. NB的名词 


行话：CI/CD  持续集成/持续交付/持续部署



6. 代码上线

第一步： git clone 代码仓库  （只需要克隆一次）
第二步： git pull (每次代码更新上线，都需要执行一遍)
第三步： 测试，批量分发代码上线

'''
