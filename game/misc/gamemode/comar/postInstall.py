import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("groupadd -f gamemode")
