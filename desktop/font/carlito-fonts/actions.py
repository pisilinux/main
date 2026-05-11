#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools, pisitools

def install():
    pisitools.insinto("/usr/share/fonts/carlito", "fonts/ttf/*.ttf")
    conf_content = """<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <match target="pattern">
    <test qual="any" name="family"><string>Calibri</string></test>
    <edit name="family" mode="assign" binding="same">
      <string>Carlito</string>
    </edit>
  </match>
</fontconfig>
"""
    shelltools.echo("30-calibri-to-carlito.conf", conf_content)
    pisitools.insinto("/etc/fonts/conf.avail", "30-calibri-to-carlito.conf")
    pisitools.dosym("/etc/fonts/conf.avail/30-calibri-to-carlito.conf", "/etc/fonts/conf.d/30-calibri-to-carlito.conf")
    pisitools.dodoc("OFL.txt", "README.md")