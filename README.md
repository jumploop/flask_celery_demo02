# flask-celery-redis学习

## 1. 安装redis服务
    [root@python-server01 ~]# yum install epel-release
    [root@python-server01 ~]# yum install redis
    [root@python-server01 ~]# vim /etc/redis.conf
    protected-mode no
    [root@python-server01 ~]# systemctl start redis
    [root@python-server01 ~]# systemctl enable redis
    Created symlink from /etc/systemd/system/multi-user.target.wants/redis.service to /usr/lib/systemd/system/redis.service.
    [root@python-server01 ~]# redis-cli 
    127.0.0.1:6379> ping
    PONG
    127.0.0.1:6379> exit
    
## 2. 创建Python虚拟环境

这里的过程不做过多介绍了，主要是下面几步

    (venv3_test) [root@python-server01 ~]# python -V
    Python 3.6.4
    (venv3_test) [root@python-server01 ~]# pip install redis
    (venv3_test) [root@python-server01 ~]# pip install Flask Flask-Script
    (venv3_test) [root@python-server01 ~]# pip install Celery Flask-Celery-Helper

## 3. 拉取源码

    (venv3_test) [root@python-server01 ~]# git clone https://github.com/sinrro/flask_celery_demo01.git

## 4. 讲解与测试
偷个懒

    https://github.com/sinrro/flask_celery_demo01

## 5. 运行

    (venv3_test) [root@python-server01 ~]#  celery -A manage.celery worker --loglevel=info

