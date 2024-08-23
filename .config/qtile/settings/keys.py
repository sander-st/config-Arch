# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "q", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ mis configuraciones (s4nder)

    # ventana siguiente del mismo grupo
    ([mod, "control"], "n", lazy.layout.next()),

    # modo de pantalla completa 100%
    ([mod, "control"], "f", lazy.window.toggle_fullscreen()),

    # languaje set
    ([mod, "shift"], "e", lazy.spawn("setxkbmap es")),
    ([mod, "shift"], "u", lazy.spawn("setxkbmap us")),

    # langaje set key space
    #([mod, "space"], lazy.spawn("setxkbmap -layout us,es -option 'grp:alt_shift_toggle'")),


    # ------------ App Configs ------------

    # Menu
    ([mod], "m", lazy.spawn("rofi -show drun -theme ~/.config/rofi/config.rasi")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show window -theme ~/.config/rofi/config.rasi")),

    # Browser
    ([mod], "f", lazy.spawn("firefox")),

    # File Explorer
    ([mod], "e", lazy.spawn("dolphin")),

    # Terminal
    ([mod], "Return", lazy.spawn("kitty")),
    
    #Terminal Warp 
    ([mod, "shift"], "Return", lazy.spawn("warp-terminal")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "Print", lazy.spawn("scrot /home/s4nder/Screenshots/%Y-%m-%d-%T.png")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s /home/s4nder/Screenshots/%Y-%m-%d-%T.png")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
