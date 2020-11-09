#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

	try:
		os.system ("sed -i 's:XFCE\;::' /etc/xdg/autostart/polkit-gnome-authentication-agent-1.desktop")
	except:
		pass

