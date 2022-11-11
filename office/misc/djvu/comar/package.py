#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/update-mime-database /usr/share/mime")
