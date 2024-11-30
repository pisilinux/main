#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."
revnr = get.srcVERSION().split(".")[1]

def setup():
    # Unpack and prepare files
    for tar_file in shelltools.ls(get.workDIR()):
        if tar_file.endswith("xz"):
            shelltools.system("tar Jxfv %s" % tar_file)

def build():
    for folder in ["doc", "source"]:
        shelltools.unlinkDir(folder)

def install():
    # prepare and install installed packs list
    pisitools.dodir("/var/lib/texmf/pisilinux/installedpacks")
    pisitools.dosed("CONTENTS", "^#", deleteLine=True)
    pisitools.insinto("/var/lib/texmf/pisilinux/installedpacks", "CONTENTS", "%s_%s.list" % (get.srcNAME(), revnr))

    for i in shelltools.ls("texmf-dist"):
        shelltools.copytree("texmf-dist/%s/" % i, "%s/usr/share/texmf-dist/" % get.installDIR())
    shelltools.system("find texmf-dist -type f -executable -exec chmod 755 %s/usr/share/{} \;" % get.installDIR())

#    for i in shelltools.ls("."):
#        if shelltools.isDirectory(i) and not i.startswith("texmf"):
#            shelltools.copytree(i, "%s/usr/share/texmf-dist/" % get.installDIR())

    for i in ["tlpkg"]:
        shelltools.copytree("%s/" % i, "%s/usr/share/" % get.installDIR())

    for i in ["bibtex", "dvips", "fonts", "makeindex", "metafont", "metapost", "mft", "scripts", "tex"]:
        shelltools.system("find %s -type d -exec install -d -m755 %s/usr/share/texmf-dist/'{}' \;" % (i, get.installDIR()))
        shelltools.system("find %s -type f -exec install -m644 '{}' %s/usr/share/texmf-dist/'{}' \;" % (i, get.installDIR()))

    # clean config files
    pisitools.dosed("tex/generic/config", "DO NOT EDIT", deleteLine=True, filePattern="language\.d..$")
    pisitools.dosed("texmf-dist/web2c/updmap.cfg", "^(#!\s*)?(Map|MixedMap)", deleteLine=True)
#    pisitools.dosed("%s/usr/share/texmf-dist/fmtutil.cnf" % get.installDIR(), "aleph", deleteLine=True)

    # install config files
    cfs = ["chktex/chktexrc",
           "web2c/mktex.cnf",
           "web2c/updmap.cfg",
           "web2c/fmtutil.cnf",
           "dvips/config/config.ps",
           "dvipdfmx/dvipdfmx.cfg",
           "tex/generic/config/language.dat",
           "tex/generic/config/language.def",
           "tex/generic/tex-ini-files/pdftexconfig.tex",
           "ttf2pk/ttf2pk.cfg",
           "xdvi/XDvi"]
    for cf in cfs:
        d = "/".join(cf.split("/")[:-1])
        p = cf if shelltools.isFile(cf) else "texmf-dist/%s" % cf
        pisitools.insinto("/etc/texmf/%s" % d, p)
    #pisitools.dosym("/etc/texmf/web2c/texmf.cnf", "/usr/share/texmf-dist/web2c/texmf.cnf")

    # fix sandbox violations
    #pisitools.dosed("texmf-dist/scripts/texlive/texlinks.sh", '"\$symlinkdir', r'"%s/$symlinkdir' % get.installDIR())

    # create symlinks
    pisitools.dodir("/usr/bin")
    #shelltools.system("texmf-dist/scripts/texlive/texlinks.sh -f %s/usr/share/texmf-dist/web2c/fmtutil.cnf %s/usr/bin" % ((get.installDIR(), ) * 2))

    # remove upstream updmap.cfg: it contains too many maps
#    pisitools.remove("/usr/share/texmf-dist/updmap.cfg")

    # remove unneeded dir
    # pisitools.removeDir("/usr/share/texmf-dist/scripts/context/stubs/mswin")
    # pisitools.removeDir("/usr/share/texmf-dist/scripts/context/stubs/win64")

    # link programs from /usr/share/texmf-dist/scripts
    linked_scripts ="""
                    a2ping/a2ping.pl
                    accfonts/mkt1font
                    accfonts/vpl2ovp
                    accfonts/vpl2vpl
                    adhocfilelist/adhocfilelist.sh
                    arara/arara.sh
                    attachfile2/pdfatfi.pl
                    bundledoc/arlatex
                    bundledoc/bundledoc
                    checkcites/checkcites.lua
                    checklistings/checklistings.sh
                    chklref/chklref.pl
                    chktex/chkweb.sh
                    chktex/deweb.pl
                    cjk-gs-integrate/cjk-gs-integrate.pl
                    clojure-pamphlet/pamphletangler
                    cluttex/cluttex.lua
                    context/perl/mptopdf.pl
                    context/stubs/unix/context
                    context/stubs/unix/contextjit
                    context/stubs/unix/luatools
                    context/stubs/unix/mtxrun
                    context/stubs/unix/mtxrunjit
                    context/stubs/unix/texexec
                    context/stubs/unix/texmfstart
                    ctan-o-mat/ctan-o-mat.pl
                    ctanbib/ctanbib
                    ctanify/ctanify
                    ctanupload/ctanupload.pl
                    de-macro/de-macro
                    dosepsbin/dosepsbin.pl
                    dtxgen/dtxgen
                    dviasm/dviasm.py
                    dviinfox/dviinfox.pl
                    epstopdf/epstopdf.pl
                    findhyph/findhyph
                    fontools/afm2afm
                    fontools/autoinst
                    fontools/ot2kpx
                    fragmaster/fragmaster.pl
                    installfont/installfont-tl
                    jfmutil/jfmutil.pl
                    ketcindy/ketcindy.sh
                    latex-git-log/latex-git-log
                    latex-papersize/latex-papersize.py
                    latex2man/latex2man
                    latex2nemeth/latex2nemeth
                    latexdiff/latexdiff-vc.pl
                    latexdiff/latexdiff.pl
                    latexdiff/latexrevise.pl
                    latexfileversion/latexfileversion
                    latexindent/latexindent.pl
                    latexmk/latexmk.pl
                    latexpand/latexpand
                    ltxfileinfo/ltxfileinfo
                    ltximg/ltximg.pl
                    luaotfload/luaotfload-tool.lua
                    lwarp/lwarpmk.lua
                    make4ht/make4ht
                    match_parens/match_parens
                    mf2pt1/mf2pt1.pl
                    mkjobtexmf/mkjobtexmf.pl
                    pdfbook2/pdfbook2
                    pdfcrop/pdfcrop.pl
                    pdfjam/pdfjam
                    pdflatexpicscale/pdflatexpicscale.pl
                    pdftex-quiet/pdftex-quiet
                    pdfxup/pdfxup
                    pfarrei/a5toa4.tlu
                    pfarrei/pfarrei.tlu
                    pkfix-helper/pkfix-helper
                    pkfix/pkfix.pl
                    ps2eps/ps2eps.pl
                    purifyeps/purifyeps
                    pythontex/depythontex.py
                    pythontex/pythontex.py
                    simpdftex/simpdftex
                    srcredact/srcredact.pl
                    sty2dtx/sty2dtx.pl
                    tex4ebook/tex4ebook
                    tex4ht/ht.sh
                    tex4ht/htcontext.sh
                    tex4ht/htlatex.sh
                    tex4ht/htmex.sh
                    tex4ht/httex.sh
                    tex4ht/httexi.sh
                    tex4ht/htxelatex.sh
                    tex4ht/htxetex.sh
                    tex4ht/mk4ht.pl
                    tex4ht/xhlatex.sh
                    texcount/texcount.pl
                    texdef/texdef.pl
                    texdiff/texdiff
                    texdirflatten/texdirflatten
                    texdoc/texdoc.tlu
                    texdoctk/texdoctk.pl
                    texfot/texfot.pl
                    texlive-extra/allcm.sh
                    texlive-extra/allneeded.sh
                    texlive-extra/dvi2fax.sh
                    texlive-extra/dvired.sh
                    texlive-extra/e2pall.pl
                    texlive-extra/fontinst.sh
                    texlive-extra/kpsetool.sh
                    texlive-extra/kpsewhere.sh
                    texlive-extra/ps2frag.sh
                    texlive-extra/pslatex.sh
                    texlive-extra/texconfig-dialog.sh
                    texlive-extra/texconfig-sys.sh
                    texlive-extra/texconfig.sh
                    texlive-extra/texlinks.sh
                    texlive/fmtutil-sys.sh
                    texlive/fmtutil-user.sh
                    texlive/fmtutil.pl
                    texlive/mktexlsr
                    texlive/mktexmf
                    texlive/mktexpk
                    texlive/mktextfm
                    texlive/rungs.tlu
                    texlive/updmap-sys.sh
                    texlive/updmap-user.sh
                    texlive/updmap.pl
                    texliveonfly/texliveonfly.py
                    texloganalyser/texloganalyser
                    texplate/texplate.sh
                    thumbpdf/thumbpdf.pl
                    typeoutfileinfo/typeoutfileinfo.sh
                    xindex/xindex.lua
                    xindy/texindy.pl
                    xindy/xindy.pl
                    """
    for p in linked_scripts.split():
        bn = shelltools.baseName(p).split(".")[0]
        if shelltools.isFile("%s/usr/share/texmf-dist/scripts/%s" % (get.installDIR(), p)):
            pisitools.dosym("/usr/share/texmf-dist/scripts/%s" % p, "/usr/bin/%s" % bn)
    pisitools.dosym("/usr/share/texmf-dist/scripts/listings-ext/listings-ext.sh", "/usr/bin/listings-ext.sh")
    
    # additional symlinks
    pisitools.dosym("allcm", "/usr/bin/allec")
    pisitools.dosym("cluttex", "/usr/bin/cllualatex")
    pisitools.dosym("cluttex", "/usr/bin/clxelatex")
    pisitools.dosym("epstopdf", "/usr/bin/repstopdf")
    pisitools.dosym("fmtutil", "/usr/bin/mktexfmt")
    pisitools.dosym("kpsetool", "/usr/bin/kpsepath")
    pisitools.dosym("kpsetool", "/usr/bin/kpsexpand")
    pisitools.dosym("luaotfload-tool", "/usr/bin/mkluatexfontdb")
    pisitools.dosym("mktexlsr", "/usr/bin/texhash")
    pisitools.dosym("pdfcrop", "/usr/bin/rpdfcrop")
    pisitools.dosym("texdef", "/usr/bin/latexdef")
