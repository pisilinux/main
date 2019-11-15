#!/usr/bin/python

import os

driver_dir_name = "nvidia-current"
libdir = "/usr/lib/%s" % driver_dir_name
lib32dir = "/usr/lib32/%s" % driver_dir_name
mesa = "/usr/lib/mesa"
mesa32 = "/usr/lib32/mesa"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/sbin/alternatives --set libGL %s/libGL.so.1.2.0" % libdir)
    os.system("/usr/sbin/alternatives --set libGL-32bit %s/libGL.so.1.2.0" % lib32dir)
    os.system("/usr/sbin/alternatives --set libEGL %s/libEGL.so.1.1.0" % libdir)
    os.system("/usr/sbin/alternatives --set libEGL-32bit %s/libEGL.so.1.1.0" % lib32dir)

def preRemove():
    # FIXME This is not needed when upgrading package; but pisi does not
    #       provide a way to learn operation type.
    #os.system("/usr/sbin/alternatives --remove libGL %s/libGL.so.1.2.0" % libdir)
    os.system("/usr/sbin/alternatives --set libGL %s/libGL.so.1.2.0" % mesa)
    os.system("/usr/sbin/alternatives --set libGL-32bit %s/libGL.so.1.2.0" % mesa32)
    os.system("/usr/sbin/alternatives --set libEGL %s/libEGL.so.1.1.0" % mesa)
    os.system("/usr/sbin/alternatives --set libEGL-32bit %s/libEGL.so.1.1.0" % mesa32)
    pass
