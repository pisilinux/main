#!/usr/bin/python

import os


def postInstall(a, b, c, d):
    #os.system("/usr/bin/mkinitcpio -p linux")
    os.system("/usr/bin/mkinitramfs -p linux")

def preRemove():
    pass
