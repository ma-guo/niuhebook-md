# -*- coding: utf-8 -*-  
import os
import sys
from fabric.api import(
    local,
    cd,
    roles,
    env,
    run,
    put,
    sudo,
    settings,
)

from datetime import datetime

env.roledefs = {
    'zuxing':[
        'ubuntu@zuxing.net:22',
    ]
}

env.passwords = {
    'ubuntu@zuxing.net': 'DequanKim'
}


def _deployproduct(app):
    dist = 'book'
    local('cd %(dir)s &&zip %(app)s.zip -r ./*' % dict(dir=dist, app=app))
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    target = '/data/upload/%(app)s/%(now)s' % dict(app=app, now=now)
    current = '/data/upload/%(app)s/current' % dict(app=app)
    run('mkdir -p %(target)s/%(dist)s' % dict(target=target, dist=dist))
    put('%(dir)s/%(app)s.zip' % dict(dir=dist, app=app), '%(target)s/%(dist)s' % dict(target=target, dist=dist))
    run('unzip -d %(dir)s/book -o %(dir)s/%(dist)s/%(app)s.zip' % dict(dir=target, app=app, dist=dist))
    run('rm %(dir)s/%(dist)s/%(app)s.zip' % dict(dir=target, dist=dist, app=app))
    local('rm %(dir)s/%(app)s.zip' % dict(dir=dist, app=app))

    run('rm -f %(current)s && ln -s %(target)s %(current)s' % {
        'current': current,
        'target': target,
    })

@roles('zuxing')
def deployproduct():
    '''
    更新发布机器上的 app
    '''
    _deployproduct('niuhebook')
