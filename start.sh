#!/bin/bash

if [ ! -x "/usr/bin/python3" ] || [ ! -x "/usr/share/python3" ] || [ ! -x "/usr/bin/python3.6" ];then
    echo "[STATUS] Installing python3"
    sudo apt update && sudo apt install python3
    echo "[STATUS] Done!"
fi
if [ ! -x "/usr/bin/ffmpeg" ] || [ ! -x "/usr/share/ffmpeg" ];then
    echo "[STATUS] Installing ffmpeg"
    sudo apt update && sudo apt install ffmpeg
    echo "[STATUS] Done!"
fi
if [ ! -f "./act" ];then
    echo "[STATUS] Setting virtualenv for python"
    python3 -m venv virtualenv
    ln -s virtualenv/bin/activate act
    echo "[STATUS] Done!"
fi

echo "[STATUS] Starting Program... Please Wait...";
source act; python3 main.py
