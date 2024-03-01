#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("ln -s /usr/lib/kf5/kdesu-kf6 /usr/bin/kdesu-kf6")
