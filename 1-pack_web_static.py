#!/usr/bin/python3
""" making archive from a folder files """
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ function to compress and create archive """
    location = None
    repo = "web_static"
    new_directory = "versions"
    static = "web_static_"
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name_archive = static + time + ".tgz"
    location = new_directory + '/' + name_archive
    local(f"mkdir -p {new_directory}")
    creation = local(f"tar -cvzf {location} {repo}")
    return location if creation else None
