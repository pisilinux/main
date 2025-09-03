#!/bin/sh
/usr/bin/dnscrypt-proxy --config /etc/dnscrypt-proxy/dnscrypt-proxy.toml > /dev/null 2>&1 &
echo $! > /run/dnscrypt-proxy.pid

