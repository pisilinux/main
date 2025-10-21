#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # Eski link'i her zaman sil
    if os.path.exists("/usr/bin/kdesu"):
        os.remove("/usr/bin/kdesu")
    # Yeni link'i oluştur
    os.symlink("/usr/lib/kf6/kdesu", "/usr/bin/kdesu")
