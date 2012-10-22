#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Deployment script.

This script is coded so it can make the deployments automagically in the 
designed servers.

USE: fab <hosts>:<username> <action>
EX: fab staging:admin release
"""

import os
import sys
import tempfile
import datetime
from string import Template
from fabric.api import env, run, local, require, put, sudo, prompt, cd

BASE_DIR = os.path.dirname(__file__)
env.project_name = 'web-o'
env.use_ssh_config = True
env.key_filename = os.path.join(os.path.expanduser('~/.ssh'), 'fudepan.pem')
def development():
    env.hosts = ["localhost"]
    env.deploy_dir = '/opt/web-o/'

def staging():
    pass
    
def production(username="ec2-user", hosts=["fudepan.org.ar"]):
    env.user = username
    env.hosts = hosts
    env.deploy_dir = '/opt/web-o'
    
def release(rev='HEAD'):
    """Creates a tarball, uploads it and decompresses it in the rigth path."""
    require("hosts", provided_by=[development, staging, production])    
    tar = "%s-%s.tar.gz" % (
        env.project_name ,
        datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
    )
    tmp_file = tempfile.NamedTemporaryFile()
    local("hg archive -p . %s" %tar)
    put(tar, tar)
    run("tar xfz %s -C %s" % (tar, env.deploy_dir))
    run("rm %s" %tar)
    local("rm %s" %tar)

def apache_restart():
    """Restarts the program in the servers."""
    require("hosts", provided_by=[development, staging, production])
    run(env.apache_command)
