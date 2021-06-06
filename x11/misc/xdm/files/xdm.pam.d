# Begin /etc/pam.d/xdm

auth     requisite      pam_nologin.so
auth     required       pam_env.so
auth     include        system-auth

account  include        system-account

password include        system-password

session  required       pam_limits.so
session  include        system-session

# End /etc/pam.d/xdm