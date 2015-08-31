XDG_CONFIG=$HOME/.config5/user-dirs.dirs
EXAMPLE_CREATION_FILE=$HOME/.local5/example-content-created

mksym()
{
    eval target=\$XDG_$(basename $1)_DIR

    for source in $1/*; do
        test -f "$source" && ln -sf "$source" "$target/"
    done
}

if [[ -f $XDG_CONFIG && ! -f $EXAMPLE_CREATION_FILE ]]; then

    . $XDG_CONFIG

    for d in /usr/share/example-content/*; do
        mksym $d
    done

    touch $EXAMPLE_CREATION_FILE
fi
