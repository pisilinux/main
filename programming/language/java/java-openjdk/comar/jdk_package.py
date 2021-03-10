#!/usr/bin/env python

import os

from pisi.util import join_path

executables = (
    'jstatd', 'jshell', 'jarsigner', 'javap', 'jstack', 'javadoc', 'jdeprscan', 'jmap', 'jconsole',
    'jmod', 'jcmd', 'jar', 'javac', 'rmic', 'jps', 'serialver', 'jstat', 'jdb', 'jinfo', 'jhsdb',
    'jlink', 'jimage', 'jdeps'
)
bin_dir = '/usr/bin'
jvm_dir = '/usr/lib/jvm/java-13-openjdk'


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for executable in executables:
        try:
            os.system('update-alternatives --install %s %s %s 2' % (
                join_path(bin_dir, executable), executable, join_path(jvm_dir, 'bin', executable)
            ))
            os.system('update-alternatives --auto %s' % executable)
        except:
            pass


def postRemove():
    for executable in executables:
        try:
            os.system('update-alternatives --remove %s %s' % (executable, join_path(jvm_dir, 'bin', executable)))
            os.system('update-alternatives --auto %s' % executable)
        except:
            pass
