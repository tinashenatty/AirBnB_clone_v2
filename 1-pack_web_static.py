#!/usr/bin/python3
# A script that generates archive the contents of web_static folder

from datetime import datetime
from time import strftime
from fabric.api import local


def do_pack():
    """ Function that generates the archive """

    filename = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(
              filename))

        return "versions/web_static_{}.tgz".format(filename)
    except Exception as e:
        return None
