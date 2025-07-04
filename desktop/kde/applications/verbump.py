#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import time
from optparse import OptionParser
from pisi.specfile import SpecFile

RELEASE = """\
        <Update release="%(RELEASE)s">
            <Date>%(DATE)s</Date>
            <Version>%(VERSION)s</Version>
            <Comment>%(COMMENT)s</Comment>
            <Name>%(NAME)s</Name>
            <Email>%(EMAIL)s</Email>
        </Update>"""

def get_and_save_user_info():
    info = [("NAME", "Please enter your full name as seen in pspec files"),
            ("EMAIL", "Please enter your e-mail as seen in pspec files")]
    res = {}
    conf_file = os.path.expanduser("~/.packagerinfo")
    if not os.path.exists(conf_file): open(conf_file, "a") 
    for line in open(conf_file, "r"):
        line = line.strip().split("=")
        try:
            res[line[0].strip()] = line[1].strip()
        except IndexError:
            pass
    for i in info:
        if not res.has_key(i[0]) or not res[i[0]]:
            print "%s is not defined in %s. %s" % (i[0], conf_file, i[1])
            res[i[0]] = raw_input("> ")
            open(conf_file, "a").write("%s\t= %s\n" % (i[0], res[i[0]]))
    return res

def bump(options, path):
    if path.endswith("/"): path = path[:-1]
    if not path.endswith("/pspec.xml"): path += "/pspec.xml"
    
    if not os.path.isfile(path):
        print "%s not found!" % path
        sys.exit(1)
    if not os.access(path, os.W_OK):
        print "Cannot write to %s." % path
        sys.exit(1)

    info = get_and_save_user_info()

    pspec = open(path, "r").read().strip()
    specfile = SpecFile(path)

    old_archive = specfile.source.archive 
    if len(old_archive) == 0:
        print("No <Archive> tag found in %s." % path)
        return
    elif len(old_archive) > 1 and not options.many and not options.release and not options.rrelease:
        print("Multiarchive pspec.xml not supported yet.")
        sys.exit(1)
    old_archive = old_archive[0].uri
    old_type = re.sub(ver_ext_pattern, "\\2", old_archive).replace(".", "").replace("src", "")
    new_type = old_type

    last = specfile.history[0]
    old_version = last.version

    if options.many:
        verfrom = options.many.split("-")[0]
        new_version =  options.many.split("-")[1]
        if not old_version == verfrom:
            print "skipping %s, different versions" % specfile.source.name
            return
        new_archive = old_archive.replace(old_version, new_version)
    elif options.uri:
        if not options.uri.split(":")[0] in ["ftp", "file", "http", "https", "mirrors"]:
            print "Wrong uri: %s" % options.uri
            sys.exit(1)
        new_archive = options.uri
        new_version = re.sub(ver_ext_pattern, "\\1", new_archive)
        new_type = re.sub(ver_ext_pattern, "\\2", new_archive).replace(".", "").replace("tgz", "targz").replace("src", "")
    elif options.ver:
        if not re.search("[\d\.]", options.ver):
            print "Wrong version number: %s" % options.ver
            sys.exit(1)
        new_version = options.ver
        new_archive = old_archive.replace(old_version, new_version)
        if "." in old_version:
            mver = ".".join(old_version.split(".")[:-1])
            if "/%s/" % mver in new_archive:
                 new_archive = new_archive.replace("/%s/" % mver, "/%s/" % ".".join(new_version.split(".")[:-1]))
    elif options.release or options.rrelease:
        new_type = old_type
        new_archive = old_archive
        new_version = old_version
    else:
        print old_archive
        sys.exit(0)
    
    info["RELEASE"] = int(last.release) + 1
    info["DATE"] = time.strftime("%Y-%m-%d")
    info["VERSION"] = new_version
    if options.release or options.rrelease:
        info["COMMENT"] = "Release bump."
    else:
        info["COMMENT"] = "Version bump."

    new_release = RELEASE % info
    new_pspec = ''
    if new_type == "tgz": new_type = "targz"
    elif not new_type in types: new_type = "binary"

    for line in pspec.split("\n"):
        if "<Archive" in line and old_archive in line:
            new_line = line.split('>')
            new_line = new_line[0] + '>' + new_archive + '<' + new_line[1].split('<')[1] + '>'
            new_pspec = "\n".join((new_pspec, new_line))
        elif "<History>" in line:
            new_pspec = "\n".join((new_pspec, "    <History>\n%s" % new_release))
        elif options.vfrom and "<Dependency versionFrom" in line:
            new_pspec = "\n".join((new_pspec, line.replace(old_version, new_version)))
        else: 
            if not new_pspec: new_pspec = line
            else: new_pspec = "\n".join((new_pspec, line))

    open(path, "w").write(new_pspec)
    open(path, "a").write("\n")

    if options.release or options.rrelease: return specfile.source.name
    
    if os.getenv("USER") != "root":
        os.system("sudo pisi build %s --fetch" % path)
    else:
        os.system("pisi build %s --fetch" % path)

    pspec = open(path, "r").read().strip()
    new_pspec = ''
    for line in pspec.split("\n"):
        if "<Archive" in line and os.path.basename(new_archive) in line:
            sha1sum = os.popen("sha1sum /var/cache/pisi/archives/%s" % os.path.basename(new_archive)).read().split()[0]
            new_line = re.sub("(.*sha1sum=)[\"\'][^\"^\']+[\"\'](.*)", r'\1"%s"\2' % sha1sum, line)
            new_line = re.sub("(.*type=)[\"\'][^\"^\']+[\"\'](.*)", r'\1"%s"\2' % new_type, new_line)
            new_pspec = "\n".join((new_pspec, new_line))
        else: 
            if not new_pspec: new_pspec = line
            else: new_pspec = "\n".join((new_pspec, line))

    open(path, "w").write(new_pspec)
    open(path, "a").write("\n")
    
    return specfile.source.name

if __name__ == "__main__":
    ver_ext_pattern = re.compile("^.+?-?[\D^\-]*?([\d\._]+\d)[\D^\.]*?\.([\w\.]+)$")
    types = ["targz", "tarbz2", "tarlzma", "tarxz", "tarZ", "tar", "zip", "gz", "gzip", "bz2", "bzip2", "lzma", "xz"]

    usage = "Usage: %prog [options] [PATH]"
    parser = OptionParser(usage)
    parser.add_option("-r", "--release-bump", action="store_true", default=False, dest="release", help="release bump")
    parser.add_option("-R", "--release-bump-recursively", action="store_true", default=False, dest="rrelease", help="release bump recursively")
    parser.add_option("-u", "--new-uri", dest="uri", help="version bump using specified uri")
    parser.add_option("-m", "--bump-many", dest="many", help="version/release bump for many packages")
    parser.add_option("-v", "--new-version", dest="ver", help="version bump using specified version")
    parser.add_option("-f", "--from-version", dest="vfrom", help="modify versionFrom too")
    (options, args) = parser.parse_args()
    try:
        path = args[0]
    except IndexError:
        path = "."

    if options.uri and options.ver:
        print "Using options -u and -v together not allowed"
        sys.exit(1)
    elif options.many and (options.uri or options.ver):
        print "Using options -m with -u or -v not allowed"
        sys.exit(1)
    elif (options.release or options.rrelease) and (options.uri or options.ver):
        print "Using options -r or -R with -u or -v not allowed"
        sys.exit(1)
    elif options.many:
        if not len(options.many.split("-")) == 2:
            print "Wrong argument for option -m: %s\nYou have to write 'version from' and 'version to' separated by '-'\ne.g: -m x.y-x.z" % options.many
            sys.exit(1)

    if options.rrelease or options.many:
        bumped = []
        for root, dirs, files in os.walk(path):
            if "pspec.xml" in files:
                name = bump(options, root)
                if name: bumped.append(name)
        
        if not bumped: print "No bumped packages."
        else:
            print "Bumped packages:"
            print "----------------"
            for b in bumped: print b
    else: bump(options, path)
