#!/usr/bin/python3
""" a module to packag web_static files and deploy """
import datetime
import os
from fabric.api import put, env, run, local


env.hosts = ["54.175.223.8", "35.175.104.36"]

env.user = "ubuntu"


def do_deploy(archive_path):
    """ deploy package """
    if archive_path is None or not os.path.isfile(archive_path):
        print("NOT PATH")
        return False

    aname = os.path.basename(archive_path)
    rname = aname.split(".")[0]

    put(local_path=archive_path, remote_path="/tmp/")
    run("mkdir -p /data/web_static/releases/{}".format(rname))
    run("tar -xzf /tmp/{} \
        -C /data/web_static/releases/{}".format(aname, rname))
    run("rm /tmp/{}".format(aname))
    run("rm -rf /data/web_static/current")
    run("ln -fs /data/web_static/releases/{}/ \
        /data/web_static/current".format(rname))
    run("mv /data/web_static/current/web_static/* /data/web_static/current/")
    run("rm -rf /data/web_static/curren/web_static")

    return True


def do_pack():
    """ package function """
    if not os.path.isdir("./versions"):
        os.makedirs("./versions")
    ntime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -czzf versions/web_static_{}.tgz web_static/*".format(ntime))
    return ("{}/versions/web_static_{}.tgz".format(os.path.dirname(
        os.path.abspath(__file__)), ntime))


def deploy():
    """ package && deploy to servers """
    path = do_pack()
    if path is None:
        return False
    return(do_deploy(path))

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
