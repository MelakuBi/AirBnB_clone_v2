#!/usr/bin/python3
""" a module to push a package to servers and deploy """
import os
from fabric.api import put, env, run


env.hosts = ["54.175.223.8", "35.175.104.36"]

env.user = "ubuntu"


def do_deploy(archive_path):
    """ distributes an archive """
    if not os.path.exists(archive_path):
        return False
    try:
        arg = archive_path.split("/")
        folder = arg[0]
        archive = arg[1]
        arch = os.path.splitext(arg[1])
        filename = arch[0]
        extension = arch[1]
        releases = "/data/web_static/releases/"
        current = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}{}/".format(releases, filename))
        run("sudo tar -xzf /tmp/{} -C {}{}/".
            format(archive, releases, filename))
        run("sudo rm /tmp/{}".format(archive))
        run("sudo mv {}{}/web_static/* {}{}/".
            format(releases, filename, releases, filename))
        run("sudo rm -rf {}{}/web_static".format(releases, filename))
        run("sudo rm -rf {}".format(current))
        run("sudo ln -s {}{}/ {}".format(releases, filename, current))
        return True
    except:
        return False
