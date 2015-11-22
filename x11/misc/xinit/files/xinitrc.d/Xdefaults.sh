SYSRESOURCES=/etc/X11/Xdefaults
USERRESOURCES=$HOME/.Xdefaults

if [ -f $SYSRESOURCES ]; then
    xrdb -load  $SYSRESOURCES
fi

if [ -f "$USERRESOURCES" ]; then
    xrdb -load "$USERRESOURCES"
else
	cp $SYSRESOURCES $USERRESOURCES && xrdb -load  "$USERRESOURCES"
fi