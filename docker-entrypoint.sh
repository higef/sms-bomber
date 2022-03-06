#!/bin/bash

tor --RunAsDaemon 1 --CookieAuthentication 0 --HashedControlPassword "" --SocksPort 0.0.0.0:9050

pip3 install -r requirements.txt
python3 runner.py
