#!/bin/sh
#export PATH=$HOME/.local/bin:$PATH

# picom 
#picom &

# systray battery icon
#cbatticon -u 5 &
# systray volume

# random background image
# path_bg_arch=~/Pictures/backgroundArchlinux
#max_random=$(ls -l $path_bg_arch|grep -v "total"|wc -l)
#number_random=$(($RANDOM % $max_random + 1))

#bg_fill=$path_bg_arch/bg${number_random}.jpg

# feh --bg-fill ~/Wallpaper/robot-rgb_informatic-leonardo-ai.jpg
feh --bg-fill ~/Wallpaper/120_-_KnFPX73.jpg
# Composer
picom &
# Network
# nm-applet &
# Keyboard Layout
#setxkbmap us &
# Automount Devices
# udiskie -t &


