#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os

DIR = "/var/lib/tox-bootstrapd"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
	try:
		os.system("useradd -r -m -d %s -s /sbin/nologin -U tox-bootstrapd" % DIR)
	except:
		pass
	os.chmod(DIR, 0700)

def postRemove():
	try:
		os.system("userdel -r tox-bootstrapd")
		os.system("groupdel tox-bootstrapd")
	except:
		pass
