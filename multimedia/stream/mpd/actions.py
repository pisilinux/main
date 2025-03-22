#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, pisitools

j = ''.join([
    ' -Ddocumentation=enabled',
    '',
    ' -Dfifo=true',
    ' -Dtcp=true',
    ' -Ddsd=true',
    ' -Dcue=true',
    ' -Dpipe=true',
    ' -Dhttpd=true',
    ' -Depoll=true',
    ' -Ddaemon=true',
    ' -Dinotify=true',
    ' -Deventfd=true',
    ' -Dsignalfd=true',
    ' -Drecorder=true',
    ' -Ddatabase=true',
    ' -Dneighbor=true',
    ' -Dwave_encoder=true',
    ' -Dlocal_socket=true',
    '',
    ' -Dao=enabled',
    ' -Dgme=enabled',
    ' -Dmad=enabled',
    ' -Dmms=enabled',
    ' -Dnfs=enabled',
    ' -Dicu=enabled',
    ' -Doss=enabled',
    ' -Dfaad=enabled',
    ' -Dflac=enabled',
    ' -Dipv6=enabled',
    ' -Dcurl=enabled',
    ' -Dalsa=enabled',
    ' -Dopus=enabled',
    ' -Dlame=enabled',
    ' -Djack=enabled',
    ' -Dsoxr=enabled',
    ' -Ddbus=enabled',
    ' -Dpcre=enabled',
    ' -Dyajl=enabled',
    ' -Dzlib=enabled',
    ' -Dzzip=enabled',
    ' -Diconv=enabled',
    ' -Dshout=enabled',
    ' -Dbzip2=enabled',
    ' -Dshine=enabled',
    ' -Dpulse=enabled',
    ' -Dexpat=enabled',
    ' -Dopenal=enabled',
    ' -Dmpg123=enabled',
    ' -Dvorbis=enabled',
    ' -Dudisks=enabled',
    ' -Dwebdav=enabled',
    ' -Dmpcdec=enabled',
    ' -Dffmpeg=enabled',
    ' -Dmikmod=enabled',
    ' -Did3tag=enabled',
    ' -Dsqlite=enabled',
    ' -Dmodplug=enabled',
    ' -Dwavpack=enabled',
    ' -Dtwolame=enabled',
    ' -Diso9660=enabled',
    ' -Dsndfile=enabled',
    ' -Dio_uring=enabled',
    ' -Dsmbclient=enabled',
    ' -Daudiofile=enabled',
    ' -Dvorbisenc=enabled',
    ' -Dfluidsynth=enabled',
    ' -Dchromaprint=enabled',
    ' -Dlibmpdclient=enabled',
    ' -Dlibsamplerate=enabled',
    ' -Dcdio_paranoia=enabled',
    ' -Dsolaris_output=enabled',
    '',
    ' -Dupnp=pupnp',
    ' -Dzeroconf=auto',
    '',
    ' -Dqobuz=disabled',
    ' -Dsndio=disabled',
    ' -Dadplug=disabled',
    ' -Dtremor=disabled',
    ' -Dsidplay=disabled',
    ' -Dsystemd=disabled',
    ' -Dwildmidi=disabled',
    ' -Dsoundcloud=disabled '
    ])

def setup():
    mesontools.configure(j, build_dir="_mpd_build_")

def build():
    mesontools.build("-C _mpd_build_")

def install():
    mesontools.install("-C _mpd_build_")

    pisitools.insinto("/etc", "doc/mpdconf.example", "mpd.conf")
    pisitools.dodoc("AUTHORS", "COPYING")
