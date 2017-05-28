Create a Linux tun device in Python
===================================

* Install `libcap` with a `capsh` that supports `--addamb`.
  As of May 28, 2017 this means you must compile `libcap` from source.

* Install `python-pytun` (say, with `pip install --user python-pytun`).

* Run `./run.sh` to run `pytuntest.py` with `CAP_NET_ADMIN` capabilities.
