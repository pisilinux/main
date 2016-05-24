#!/usr/bin/python

import os


def postInstall(a, b, c, d):
    os.system("/usr/bin/mkinitcpio -p linux")


def preRemove():
    pass
