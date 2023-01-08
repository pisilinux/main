#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import perlmodules, shelltools

shelltools.export("PERL_USE_UNSAFE_INC", "1")

def setup():
	perlmodules.configure()

def build():
	perlmodules.make()

def check():
	pass
	#perlmodules.make("test")

def install():
	perlmodules.install()
