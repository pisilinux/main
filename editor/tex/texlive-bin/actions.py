#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import texlivemodules

import os

WorkDir = "."
buildDir = 'texlive-20220321-source/build'

def setup():
    shelltools.makedirs(buildDir)
    shelltools.cd(buildDir)
    shelltools.sym("../configure", "configure")
    autotools.configure("--with-x \
                         --enable-ipc \
                         --prefix=/usr \
                         --disable-xindy \
                         --enable-shared \
                         --disable-luatex \
                         --disable-static \
                         --with-system-gd \
                         --sysconfdir=/etc \
                         --bindir=/usr/bin \
                         --disable-psutils \
                         --disable-t1utils \
                         --disable-dvisvgm \
                         --with-system-zlib \
                         --with-system-t1lib \
                         --datadir=/usr/share \
                         --with-system-libpng \
                         --with-system-ncurses \
                         --without-system-xpdf \
                         --with-system-zziplib \
                         --with-system-harfbuzz \
                         --mandir=/usr/share/man \
                         --disable-multiplatform \
                         --with-system-graphite2 \
                         --with-system-freetype2 \
                         --datarootdir=/usr/share \
                         --with-banner-add=/PisiLinux \
                         --disable-native-texlive-build ")

def build():
    shelltools.cd(buildDir)
    autotools.make()

def install():
    shelltools.cd(buildDir)
    autotools.rawInstall("prefix=/usr DESTDIR=%s" % get.installDIR())
    shelltools.system("pwd")
    #install biber
    pisitools.dobin("../../biber-2.16/bin/biber")

    #pisitools.dodir("/usr/share/tlpkg/TeXLive")
    #shelltools.move("%s/source/utils/biber/TeXLive/*.pm" % get.workDIR(), "%s/usr/share/tlpkg/TeXLive" % get.installDIR())

    # remove aleph from fmtutil.cnf
    pisitools.dosed("%s/usr/share/texmf-dist/web2c/fmtutil.cnf" % get.installDIR(), "^.*aleph.*$")

    pisitools.insinto("/etc/texmf/texconfig", "%s/usr/share/texmf-dist/texconfig/tcfmgr.map" % get.installDIR(), sym=True)

    # fix symlinks, some are incorrect
    # makefile patching is another way, but there ar/dvipdfmx.cfge lot of scripts
    # pathing each makefile makes it much harder, for now this is a "simpler" solution
    for binary in shelltools.ls(get.installDIR() + "/usr/bin"):
        real_path = shelltools.realPath(get.installDIR() + "/usr/bin/" + binary)
        if "texmf" in real_path and not os.path.exists(real_path): # modify only if it is broken
            base_path = real_path.replace(get.installDIR() + "/usr", "")
            new_path = "/usr/share" + base_path
            shelltools.unlink(get.installDIR() + "/usr/bin/" + binary)
            pisitools.dosym(new_path, "/usr/bin/" + binary)


    bibtexextra_scripts=["bbl2bib", "bib2gls", "bibdoiadd", "bibexport", "bibmradd", "biburl2doi", "bibzbladd", "convertgls2bib", "listbib", "ltx2crossrefxml", "multibibliography", "urlbst"]

    core_scripts=["a2ping", "a5toa4", "adhocfilelist", "afm2afm", "allcm", "allec", "allneeded", "arara", "arlatex", "autoinst", "bundledoc", "checkcites", "checklistings", "chklref", "chkweb", "cjk-gs-integrate", "cluttex", "cllualatex", "clxelatex", "context", "contextjit", "ctanbib", "ctanify", "ctanupload", "ctan-o-mat", "de-macro", "depythontex", "deweb", "dosepsbin", "dtxgen", "dvi2fax", "dviasm", "dviinfox", "dvired", "e2pall", "epstopdf", "findhyph", "fmtutil", "fmtutil-sys", "fmtutil-user", "fontinst", "fragmaster", "ht", "htcontext", "htlatex", "htmex", "httex", "httexi", "htxelatex", "htxetex", "installfont-tl", "jfmutil", "ketcindy", "kpsepath", "kpsetool", "kpsewhere", "kpsexpand", "latex-git-log", "latex-papersize", "latex2man", "latex2nemeth", "latexdef", "latexdiff", "latexdiff-vc", "latexfileversion", "latexindent", "latexmk", "latexpand", "latexrevise", "listings-ext.sh", "ltxfileinfo", "ltximg", "luaotfload-tool", "luatools", "lwarpmk", "make4ht", "match_parens", "mf2pt1", "mk4ht", "mkjobtexmf", "mkt1font", "mktexfmt", "mktexlsr", "mktexmf", "mktexpk", "mktextfm", "mptopdf", "mtxrun", "mtxrunjit", "ot2kpx", "pamphletangler", "pdfatfi", "pdfbook2", "pdfcrop", "pdfjam", "pdflatexpicscale", "pdftex-quiet", "pdfxup", "pfarrei", "pkfix", "pkfix-helper", "ps2eps", "ps2frag", "pslatex", "purifyeps", "pythontex", "repstopdf", "rpdfcrop", "rungs", "simpdftex", "srcredact", "sty2dtx", "tex4ebook", "texconfig", "texconfig-dialog", "texconfig-sys", "texcount", "texdef", "texdiff", "texdirflatten", "texdoc", "texdoctk", "texexec", "texfot", "texhash", "texindy", "texlinks", "texliveonfly", "texloganalyser", "texmfstart", "texosquery", "texosquery-jre5", "texosquery-jre8", "texplate", "thumbpdf", "tlcockpit", "tlshell", "typeoutfileinfo", "updmap", "updmap-sys", "updmap-user", "vpl2ovp", "vpl2vpl", "xhlatex", "xindex", "xindy"]

    games_scripts=["rubikrotation"]
    
    humanities_scripts=["diadia"]

    langcyrillic_scripts=["rubibtex", "rumakeindex"]
    langkorean_scripts=["jamo-normalize komkindex ttf2kotexfont"]
    langcjk_scripts=["convbkmk", "ptex2pdf", "kanji-fontmap-creator", "kanji-config-updmap", "kanji-config-updmap-sys", "kanji-config-updmap-user"]

    langextra_scripts=["ebong"]

    langgreek_scripts=["mkgrkindex"]

    latexextra_scripts=["authorindex", "exceltex", "l3build", "makedtx", "makeglossaries", "makeglossaries-lite", "pdfannotextractor", "perltex", "ps4pdf", "splitindex", "svn-multi", "vpe", "webquiz", "wordcount", "yplan"]

    music_scripts=["lily-glyph-commands", "lily-image-commands", "lily-rebuild-pdfs", "m-tx", "musixtex", "musixflx", "pmxchords"]

    pictures_scripts=["cachepic", "epspdf", "epspdftk", "fig4latex", "getmapdl", "mathspic", "mathspic", "mkpic", "pn2pdf"]

    pstricks_scripts=["pedigree", "pst2pdf"]

    science_scripts=["pygmentex", "ulqda"]

    # remove unneeded files and symlinks
    dirs = []
    for g in [bibtexextra_scripts, core_scripts, games_scripts, humanities_scripts, \
              langcjk_scripts, langcyrillic_scripts, langextra_scripts, \
              langgreek_scripts, latexextra_scripts, music_scripts, \
              pictures_scripts, pstricks_scripts, science_scripts, \
              ["tlmgr"]]:
        for s in g:
            if shelltools.isLink("%s/usr/bin/%s" % (get.installDIR(), s)):
                realpath = shelltools.realPath("%s/usr/bin/%s" % (get.installDIR(), s))
                dirname = shelltools.dirName(realpath)
                if not dirname in dirs: dirs.append(dirname)
                if not dirname == "%s/usr/bin" % get.installDIR():
                    if shelltools.isFile(realpath): shelltools.unlink(realpath)
                pisitools.remove("/usr/bin/%s" % s)

    # remove empty dirs
    while dirs:
        tmpdirs = dirs[:]
        for d in tmpdirs:
            if not shelltools.ls(d):
                shelltools.unlinkDir(d)
                dirname = shelltools.dirName(d)
                if not dirname in dirs: dirs.append(dirname)
            dirs.remove(d)

    pdftexsymlinks=["amstex", "cslatex", "csplain", "eplain", "etex", "jadetex", "latex", "mex", "mllatex", "mltex"
          ,"pdfetex", "pdfcslatex", "pdfcsplain", "pdfjadetex", "pdflatex", "pdfmex", "pdfxmltex", "texsis", "utf8mex", "xmltex"]

    for symlink in pdftexsymlinks:
        pisitools.dosym("pdftex", "/usr/bin/%s" % symlink)

    luatexsymlinks=["dvilualatex", "dviluatex", "lualatex"]

    for symlink in luatexsymlinks:
        pisitools.dosym("pdftex", "/usr/bin/%s" % symlink)


    pisitools.dosym("eptex", "/usr/bin/platex")
    pisitools.dosym("euptex", "/usr/bin/uplatex")
    pisitools.dosym("xetex", "/usr/bin/xelatex")

    pisitools.removeDir("/usr/share/texmf-dist")
