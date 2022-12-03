#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools

def setup():
	cmaketools.configure("-B_build -L")

def build():
	cmaketools.make("-C _build")

def install():
	cmaketools.install("-C _build install")
