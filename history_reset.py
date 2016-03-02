'''
Created on 24-12-2012

@author: marcin
'''
import os
import re

rootpath = "."
specfile = "pspec.xml"
newcomment = "First release"
newrelease = "1"
relative_backup_path = "../backup"

def read_file(path):
    with open(path) as f:
        return f.read().strip()

def reset_history(spec):
    release = re.compile("(.*?release\s*=\s*)[\"\']\d+[\"\'](.*?)")
    newspec = ''
    history = False
    update1 = False
    skipline = False
    for line in spec.split("\n"):
        if "</History>" in line: history = False
        if "<History>" in line: history = True
        if history:
            if "</Update>" in line:
                if not update1: newspec = "\n".join((newspec, line))
                update1 = True
            if update1: continue
            else:
                if "<Update" in line: line = re.sub(release, r'\1"%s"\2' % newrelease, line)
                elif "<Comment" in line:
                    if not "</Comment" in line:
                        skipline = True
                if "</Comment" in line:
                    skipline = False
                    line = " " * 12 + "<Comment>%s</Comment>" % newcomment
                if not skipline: newspec = "\n".join((newspec, line))
        else: newspec = "\n".join((newspec, line))
    return newspec

if __name__ == '__main__':
    backup_path = os.path.normpath(os.path.join(rootpath, relative_backup_path))
    if not os.path.isdir(backup_path):
        os.makedirs(backup_path)
    else:
        suffix = 0
        parent_backup = os.path.dirname(backup_path)
        base_name = os.path.basename(relative_backup_path)
        for d in os.listdir(parent_backup):
            if d.startswith(base_name):
                ext = d.replace(base_name, '')
                if os.path.isdir("%s/%s" % (parent_backup, d)) and ext.isdigit():
                    if int(ext) > suffix:
                        suffix = int(ext)
        suffix +=1
        suffix = "0%d" % suffix if suffix < 10 else str(suffix)
        os.rename(backup_path, backup_path + suffix)
        os.makedirs(backup_path)
 
    for root, dirs, files in os.walk(rootpath):
        if specfile in files:
            f = "%s/%s" % (root, specfile)
            print(f)
            spec = read_file(f)
            bf = "%s/%s" % (os.path.normpath(root.replace(rootpath, relative_backup_path)), specfile)
            os.makedirs(os.path.dirname(bf))
            open(bf, "w").write(spec)
            open(bf, "a").write("\n")
            open(f, "w").write(reset_history(spec))
            open(f, "a").write("\n")
