#!/bin/sh
exec sudo capsh \
	--caps='cap_net_admin+eip cap_setpcap,cap_setuid,cap_setgid+ep' \
	--keep=1 \
	--user="$USER" \
	--addamb=cap_net_admin \
	-- -c 'env -i -- /usr/bin/python3 pytuntest.py "$@"' -- "$@"
