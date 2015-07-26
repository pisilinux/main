#!/usr/bin/python
# -*- coding: utf-8 -*-

import shutil
import sys
import re
import os

from optparse import OptionParser

def read_file(path):
    with open(path) as f:
        return f.read().strip()

def write_file(path, content):
    open(path, "w").write(content)
    open(path, "a").write("\n")

class Components():
    COMPONENT_XML = """<PISI>
    <Name>%s</Name>
</PISI>
"""
    EMPTY_COMPONENT = """        <Component>
            <Name>%s</Name>
            <LocalName xml:lang="en">FIXME</LocalName>
            <Summary xml:lang="en">FIXME</Summary>
            <Description xml:lang="en">FIXME</Description>
            <Group>FIXME</Group>
            <Maintainer>
                <Name>PisiLinux Community</Name>
                <Email>admins@pisilinux.org</Email>
            </Maintainer>
        </Component>"""
    CBGN = """<PISI>
    <Components>"""
    CEND = """
    </Components>
</PISI>"""
    LOCALNAME = '            <LocalName xml:lang="%s">%s</LocalName>\n'
    SUMMARY = '            <Summary xml:lang="%s">%s</Summary>\n'
    DESCRIPTION = '            <Description xml:lang="%s">%s</Description>\n'
    COMPONENT = """
        <Component>
            <Name>%s</Name>
%s%s%s            <Group>%s</Group>
            <Maintainer>
                <Name>%s</Name>
                <Email>%s</Email>
            </Maintainer>
        </Component>"""

    def __init__(self, path):
        self.path = path
        self.components = []
        self.components_xml = "%s/components.xml" % self.path
        self.name_ptrn = re.compile("\s*<Name>(.+?)<\/Name>\s*")
        self.lnamech_ptrn = re.compile("\s*<LocalName.*?>(.+?)<\/LocalName>\s*")
        self.lname_ptrn = re.compile("\s*<LocalName\s+xml:lang\s?=\s?[\'\"](\w\w.*?)[\'\"]\s?>(.+?)<\/LocalName>\s*")
        self.summarych_ptrn = re.compile("\s*<Summary.*?>(.+?)<\/Summary>\s*")
        self.summary_ptrn = re.compile("\s*<Summary\s+xml:lang\s?=\s?[\'\"](\w\w.*?)[\'\"]\s?>(.+?)<\/Summary>\s*")
        self.descch_ptrn = re.compile("\s*<Description.*?>(.+?)<\/Description>\s*")
        self.desc_ptrn = re.compile("\s*<Description\s+xml:lang\s?=\s?[\'\"](\w\w.*?)[\'\"]\s?>(.+?)<\/Description>\s*")
        self.group_ptrn = re.compile("\s*<Group>(.+?)<\/Group>\s*")
        self.email_ptrn = re.compile("\s*<Email>(.+?)<\/Email>\s*")
        self.cbgn_ptrn = re.compile("\s*<Component>\s*")
        self.cend_ptrn = re.compile("\s*<\/Component>\s*")
        self.mbgn_ptrn = re.compile("\s*<Maintainer>\s*")
        self.mend_ptrn = re.compile("\s*<\/Maintainer>\s*")
        self.csend_ptrn = re.compile("\s*<\/Components>\s*")

    def read_components(self):
        csfile = read_file(self.components_xml)
        cread = False
        mread = False
        component = {}
        for line in csfile.split("\n"):
            if re.search(self.cbgn_ptrn, line):
                cread = True
                component["err"] = []
                component["unknown"] = []
                component["clname"] = []
                component["csummary"] = []
                component["cdesc"] = []
                continue
            elif re.search(self.cend_ptrn, line):
                cread = False
                self.components.append(component)
                component = {}
                continue
            if cread:
                if re.search(self.mbgn_ptrn, line):
                    mread = True
                    continue
                elif re.search(self.mend_ptrn, line):
                    mread = False
                    continue
                elif re.search(self.name_ptrn, line):
                    if mread: component["mname"] = re.sub(self.name_ptrn, r"\1", line)
                    else: component["cname"] = re.sub(self.name_ptrn, r"\1", line)
                elif re.search(self.lnamech_ptrn, line):
                    if re.search(self.lname_ptrn, line):
                        component["clname"].append(re.sub(self.lname_ptrn, r"\1:\2", line))
                    else:
                        component["err"].append("LocalName") 
                elif re.search(self.summarych_ptrn, line):
                    if re.search(self.summary_ptrn, line):
                        component["csummary"].append(re.sub(self.summary_ptrn, r"\1:\2", line))
                    else:
                        component["err"].append("Summary") 
                elif re.search(self.descch_ptrn, line):
                    if re.search(self.desc_ptrn, line):
                        component["cdesc"].append(re.sub(self.desc_ptrn, r"\1:\2", line))
                    else:
                        component["err"].append("Description") 
                elif re.search(self.group_ptrn, line):        
                    component["cgroup"] = re.sub(self.group_ptrn, r"\1", line)
                elif re.search(self.email_ptrn, line):        
                    component["memail"] = re.sub(self.email_ptrn, r"\1", line)
                else: component["unknown"].append(line)

    def sort_components(self):
        self.components = sorted(self.components, key=lambda k: k['cname'])

    def backup_components(self):
        files = os.walk(self.path).next()[2]
        last = 0
        for f in files:
            if f.startswith("components.xml.") and int(f[-3:]) > last: last = int(f[-3:])
        last = str(last + 1)
        while len(last) < 3: last = "0" + last
        shutil.copyfile(self.components_xml, ".".join((self.components_xml, last))) 

    def write_components(self):
        self.sort_components()
        cs = ''
        for c in self.components:
            ln = ""
            for i in c["clname"]:
                ln += self.LOCALNAME % tuple(i.split(":"))
            s = ""
            for i in c["csummary"]:
                s += self.SUMMARY % tuple(i.split(":"))
            d = ""
            for i in c["cdesc"]:
                d += self.DESCRIPTION % tuple(i.split(":"))
            cs += self.COMPONENT % (c["cname"], ln, s, d, c["cgroup"], c["mname"], c["memail"])
        self.backup_components()
        open(self.components_xml, "w").write(self.CBGN)
        open(self.components_xml, "a").write(cs)
        open(self.components_xml, "a").write(self.CEND)
        open(self.components_xml, "a").write("\n")        

    def edit(self):
        l = []
        mcommands = {"q": "quit",
                    "l": "list components",
                    "c": "choose component",
                    "h": "help"}
        ecommands = {"mn": "set maintainer name",
                     "me": "set maintainer email",
                     "ln": "set local name (lang:name)",
                     "s": "set summary (lang:summary)",
                     "d": "set description (lang:description)",
                     "m": "main menu",
                     "w": "write",
                     "h": "help"}
        
        def read_command(m):
            opts = mcommands.keys() if m == "m" else ecommands.keys()
            return (opts, raw_input(":".join(sorted(opts)) + " > ").split())
        
        def list_components(param, regexp = True):
            res = []
            num = 0
            if not param: param = ".*"
            for c in self.components:
                if regexp and re.search(param, c["cname"]):
                    res.append(c["cname"])
                    print num, c["cname"]
                    num += 1
                elif not regexp and param == c["cname"]:
                    res.append(c["cname"])
                    break
            return res
        
        def get_component_data(name):
            #print self.components
            for c in self.components:
                if name == c["cname"]: return c
            print "Component %s not found!" % name
            return False
        
        def print_help(hdict):
            for i in iter(sorted(hdict.iteritems())):
                print i[0] + "\t" + i[1]
        
        def edit_loop(component):
            def update(key, val, data):
                d = val.split(":")
                if not len(d) == 2: print "Wrong param format! (ln lang:text)"
                else:
                    lexists = -1
                    for i in data[key]:
                        if i.split(":")[0] == d[0]:
                            lexists = data[key].index(i)
                            break  
                    if lexists > -1: data[key][lexists] = val
                    else: data[key].append(val)
                return data
                
            data = get_component_data(component)
            while True:
                print "-" * (len(component) + 8)
                print "Editing " + component
                print "-" * (len(component) + 8)
                print "LocalName:"
                for i in data["clname"]: print "  %s" %i
                print "Summary:"
                for i in data["csummary"]: print "  %s" %i
                print "Description:"
                for i in data["cdesc"]: print "  %s" %i
                print "Group:\n  %s" % data["cgroup"] 
                print "Maintainer name:\n  %s" % data["mname"]
                print "Email:\n  %s" % data["memail"]
                o, c = read_command("c")
                if not c[0] in o: continue
                if len(c) == 1: c.append("")
                if c[0] == "m": break
                elif c[0] == "h": print_help(ecommands)
                elif c[0] == "ln": data = update("clname", c[1], data)
                elif c[0] == "s": data = update("csummary", c[1], data)
                elif c[0] == "d": data = update("cdesc", c[1], data)
                elif c[0] == "mn": data["mname"] = c[1]
                elif c[0] == "me": data["memail"] = c[1]
                elif c[0] == "w":  self.write_components()
                else: print"%s is not implemented yet" % c[0]
        
        def edit_component(param, l):
            try:
                int(param)
                edit_loop(l[int(param)])
            except ValueError:
                l = list_components(param, regexp = False)
            if not len(l) == 1: print "Component %s not found" % param
            else: edit_loop(l[0])
        
        while True:
            o, c = read_command("m")
            if len(c) == 1: c.append("")
            if not c[0] in o: continue
            elif c[0] == "q": break
            elif c[0] == "l": l = list_components(c[1])
            elif c[0] == "c": edit_component(c[1], l)
            elif c[0] == "h": print_help(mcommands) 
            else: print"%s is not implemented yet" % c[0]

    def check(self):      
        cs = []
        for root, dirs, files in os.walk(self.path):
            c = root.split(self.path)[1][1:].split("/")
            if "files" in c or "comar" in c: continue
            c = ".".join(c)
            component_xml = "%s/component.xml" % root
            pspec_xml = "%s/pspec.xml" % root
            actions_py = "%s/actions.py" % root
            if not os.path.isfile(component_xml) and not os.path.isfile(pspec_xml):
                if os.path.isfile(actions_py): print "WARNING: %s not exists" % pspec_xml
                else:
                    is_src_repo = False
                    for r, d, f in os.walk(root):
                        if "pspec.xml" in f:
                            is_src_repo = True
                            break
                    if is_src_repo and c:
                        print "%s not exists. creating..." % component_xml
                        write_file(component_xml, self.COMPONENT_XML % c)
            if os.path.isfile(component_xml) and c: cs.append(c) 
        
        mcs = cs[:]
        csfile = read_file(self.components_xml)
        maintainer = False
        new_file = []
        for line in csfile.split("\n"):
            new_file.append(line)
            if re.search(self.mbgn_ptrn, line): maintainer = True
            elif re.search(self.mend_ptrn, line): maintainer = False
            elif re.search(self.csend_ptrn, line):
                for m in mcs:
                    new_file.insert(-1, self.EMPTY_COMPONENT % m)
            if not re.search(self.name_ptrn, line) or maintainer: continue
            cn = re.sub(self.name_ptrn, r"\1", line)
            if cn in mcs: mcs.pop(mcs.index(cn))
        
        new_file = "\n".join(new_file)
        write_file(self.components_xml, new_file)


if __name__ == "__main__":
    usage = "Usage: %prog [PATH]"
    parser = OptionParser(usage)
    parser.add_option("-c", "--check", action="store_true", dest="check", help="fix missing component.xml files and entries in components.xml")
    parser.add_option("-e", "--edit", action="store_true", dest="edit", help="edit components.xml")
    (options,args) = parser.parse_args()
    try:
        root = args[0]
    except IndexError:
        print "Using ./ as PATH"
        root = "./"

    if root.endswith("/"): root = root[:-1]

    cs = Components(root)        
    if not os.path.isfile(cs.components_xml):
        print "%s not exists!" % cs.components_xml
        sys.exit(1)
    if not os.access(cs.components_xml, os.W_OK): 
        print "Cannot write to %s" % cs.components_xml
        sys.exit(1)
    cs.read_components()

    if options.check: cs.check()
    if options.edit: 
        cs.edit()
