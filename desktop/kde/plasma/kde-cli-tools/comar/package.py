#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("ln -s /usr/lib/kf6/kdesu /usr/bin/kdesu")
