#!/usr/bin/python3
# 4. Keep it clean!
from fabric.api import *
env.hosts = ['54.175.223.8', '35.175.104.36']


def do_clean(number=0):
    """ deletes out-of-date archives """
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1
    local("cd versions ; ls -t | tail -n +{} | xargs rm -rf".format(number))
    folder = "/data/web_static/releases"
    run("cd {} ; ls -t | tail -n +{} | xargs rm -rf".format(folder, number))
