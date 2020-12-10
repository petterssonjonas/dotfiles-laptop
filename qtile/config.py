# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget
from typing import List  # noqa: F401

mod = "mod4"
myTerm = "kitty"

from typing import List  # noqa: F401

from libqtile import hook

# some other imports
import os
import subprocess

# import socket


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),
    # Move windows up or down in current stack
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up()),
    # Switch window focus to other pane(s) of stack
    Key([mod], "l", lazy.layout.grow()),
    Key([mod], "h", lazy.layout.shrink()),
    # Swap panes of split stack
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "control"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    # Key([mod], "r", lazy.spawncmd()),
    Key([mod], 'f', lazy.window.toggle_fullscreen()),
    # DMENU
    Key(
        [mod, "shift"],
        "d",
        lazy.spawn("dmenu_run -p 'Run: '"),
        desc="Dmenu Run Launcher",
    ),
    Key([mod, "shift"], "space", lazy.spawn("~/.config/rofi/applets/menu/apps.sh")),
    Key([mod, "shift"], "q", lazy.spawn("~/.config/rofi/applets/menu/powermenu.sh")),
    Key([mod, "shift"], "Return", lazy.spawn("rofi -show run"), desc="Rofi -show run"),
    Key([mod, "shift"], "b", lazy.spawn("firefox")),
    Key([mod, "shift"], "f", lazy.spawn("kitty --session ~/.config/kitty/kitty-sessions/chat_session")),
    Key([mod, "shift"], "t", lazy.spawn("thunar")),
    Key([mod, "shift"], "d", lazy.spawn("discord")),
    #    Key([mod], "F1", lazy.spawn("qtile-keybinds-show.py")), #not done yet
]


group_names = [
    ("TERM", {"layout": "monadtall"}),
    ("WWW", {"layout": "monadtall"}),
    ("MAIL", {"layout": "monadtall"}),
    ("DEV", {"layout": "monadtall"}),
    ("DOC", {"layout": "monadtall"}),
    ("AUX", {"layout": "monadtall"}),
    ("CHAT", {"layout": "monadtall"}),
    ("VID", {"layout": "monadtall"}),
    ("GFX", {"layout": "floating"}),
]


groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(
        Key([mod], str(i), lazy.group[name].toscreen())
    )  # Switch to another group
    keys.append(
        Key([mod, "shift"], str(i), lazy.window.togroup(name))
    )  # Send current window to another group


layout_theme = {
    "border_width": 2,
    "margin": 6,
    "border_focus": "#d65d0e",  # colors list cannot come before this. layouts break.
    "border_normal": "#32302f",
}

layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    layout.Columns(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(shift_windows=True, **layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=3),
    # layout.TreeTab(
    # font="Ubuntu",
    # fontsize=12,
    # sections=["Windows"], #, "SECOND"],
    # section_fontsize=12,
    # bg_color="#3C3836",
    # active_bg="#B8BB26",
    # active_fg="#1D2021",
    # inactive_bg="#32302F",
    # inactive_fg="#A89984",
    # padding_y=5,
    # section_top=50,
    # panel_width=200,
    # ),
    layout.Floating(**layout_theme),
]

# Gruvbox color scheme.      # list number (color[#])
colors = [
    ["#282828", "#282828"],  # 0  # bg
    ["#282828", "#282828"],  # 1  # bg0
    ["#1d2021", "#1d2021"],  # 2  # bg0_h
    ["#32302f", "#32302f"],  # 3  # bg0_s
    ["#3c3836", "#3c3836"],  # 4  # bg1
    ["#504945", "#504945"],  # 5  # bg2
    ["#665c54", "#665c54"],  # 6  # bg3
    ["#7c6f64", "#7c6f64"],  # 7  # bg4
    ["#ebdbb2", "#ebdbb2"],  # 8  # fg
    ["#fbf1c7", "#fbf1c7"],  # 9  # fg0
    ["#ebdbb2", "#ebdbb2"],  # 10 # fg1
    ["#d5c4a1", "#d5c4a1"],  # 11 # fg2
    ["#bdae93", "#bdae93"],  # 12 # fg3
    ["#a89984", "#a89984"],  # 13 # fg4
    ["#cc241d", "#cc241d"],  # 14 # red hard
    ["#fb4934", "#fb4934"],  # 15 # red soft
    ["#98971a", "#98971a"],  # 16 # green hard
    ["#b8bb26", "#b8bb26"],  # 17 # green soft
    ["#d79921", "#d79921"],  # 18 # yellow hard
    ["#fabd2f", "#fabd2f"],  # 19 # yellow soft
    ["#458588", "#458588"],  # 20 # blue hard
    ["#83a598", "#83a598"],  # 21 # blue soft
    ["#b16286", "#b16286"],  # 22 # purple hard
    ["#d3869b", "#d3869b"],  # 23 # purple soft
    ["#689d6a", "#689d6a"],  # 24 # aqua hard
    ["#8ec07c", "#8ec07c"],  # 25 # aqua soft
    ["#d65d0e", "#d65d0e"],  # 26 # orange hard
    ["#FE8019", "#FE8019"],  # 27 # orange soft
    ["#a89984", "#a89984"],  # 28 # gray
    ["#928374", "#928374"],  # 29 # gray bg
]  # window name#

# prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
widget_defaults = dict(font="Ubuntu", fontsize=15, padding=2, background=colors[0])
extension_defaults = widget_defaults.copy()

# layoutimagename = widget.CurrentLayout()
# layoutimg="~/.config/qtile/images/" + layoutimagename


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0, padding=2, foreground=colors[2], background=colors[0]
                ),
                widget.Image(  # make a If .face/.face.icon exists use it, else python or penguin.png.
                    scale=True,
                    filename="~/.config/qtile/images/penguin.png",
                    background=colors[0],
                ),
                widget.Sep(  # Separator between image and group box.
                    linewidth=0, padding=0, foreground=colors[2], background=colors[0]
                ),
                widget.GroupBox(
                    font="Ubuntu Bold",
                    fontsize=11,
                    visible_groups=["TERM", "WWW", "MAIL", "DEV", "DOC", "AUX"],
                    # margin=3,
                    margin_y=3,
                    margin_x=3,
                    # padding=3,
                    padding_y=5,
                    padding_x=3,
                    spacing=0,
                    center_aligned=True,
                    # borderwidth=2,
                    active=colors[8],
                    inactive=colors[8],
                    rounded=True,
                    highlight_color=colors[5],
                    highlight_method="block",
                    this_current_screen_border=colors[5],
                    this_screen_border=colors[5],
                    other_current_screen_border=colors[5],
                    other_screen_border=colors[5],
                    foreground=colors[8],
                    background=colors[0],
                ),
                # widget.Prompt( # Nah, rather use rofi or dmenu.
                # prompt=prompt,
                # font="Ubuntu",
                # padding=10,
                # foreground=colors[8],
                # background=colors[0],
                # ),
                widget.Sep(  # Separator between Groupbox and Window name.
                    linewidth=0, padding=20, foreground=colors[2], background=colors[0]
                ),
                widget.TaskList(
                    font="Ubuntu Bold",
                    fontsize=12,
                    foreground=colors[8],
                    background=colors[0],
                    border=colors[5],
                    center_aligned=True,
                    # borderwidth=2,
                    spacing=6,
                    # margin=3,
                    margin_y=5,
                    margin_x=3,
                    # padding=3,
                    padding_y=0,
                    padding_x=3,
                    max_title_width=300,
                    highlight_color=colors[5],
                    highlight_method="block",
                    rounded=True,
                ),
                widget.Sep(  # Separator between Window name and widgets.
                    linewidth=0, padding=20, foreground=colors[2], background=colors[0]
                ),
                widget.Image(
                    scale=True,
                    background=colors[0],
                    filename="~/.config/qtile/images/arrowleft-trans-bg1.png",
                ),
                widget.TextBox(
                    text=" ",
                    padding=2,
                    foreground=colors[8],
                    background=colors[4],
                   fontsize=12,
                ),
                widget.ThermalSensor(
                    foreground=colors[8], background=colors[4], threshold=90, padding=5
                ),
                widget.Image(
                    scale=True,
                    background=colors[4],
                    filename="~/.config/qtile/images/arrowleft-trans-bg.png",
                ),
                widget.TextBox(
                    text=" ",
                    padding=2,
                    foreground=colors[8],
                    background=colors[0],
                    fontsize=14,
                ),
                widget.CPU(
                    foreground=colors[8],
                    background=colors[0],
                    padding=5,
                    format="{load_percent}%",
                    mouse_callbacks={
                        "Button1": lambda qtile: qtile.cmd_spawn(myTerm + " -e bpytop")
                    },
                ),
                widget.Image(
                    scale=True,
                    background=colors[0],
                    filename="~/.config/qtile/images/arrowleft-trans-bg1.png",
                ),
                widget.TextBox(
                    text=" ",
                    foreground=colors[8],
                    background=colors[4],
                    padding=0,
                    fontsize=14,
                ),
                widget.Memory(
                    foreground=colors[8],
                    background=colors[4],
                    mouse_callbacks={
                        "Button1": lambda qtile: qtile.cmd_spawn(myTerm + " -e bpytop")
                    },
                    padding=4,
                ),
                widget.Image(
                    scale=True,
                    background=colors[4],
                    filename="~/.config/qtile/images/arrowleft-trans-bg.png",
                ),
                widget.TextBox(
                    text="",
                    padding=2,
                    foreground=colors[8],
                    background=colors[0],
                    fontsize=14,
                ),
                widget.Pacman(
                    update_interval=1800,
                    foreground=colors[8],
                    background=colors[0],
                    mouse_callbacks={
                        "Button1": lambda qtile: qtile.cmd_spawn(
                            myTerm + " -e paru -Syu"
                        )
                    },
                ),
                widget.TextBox(
                    text="Updates",
                    foreground=colors[8],
                    background=colors[0],
                    padding=5,
                    mouse_callbacks={
                        "Button1": lambda qtile: qtile.cmd_spawn(
                            myTerm + " -e paru -Syu"
                        )
                    },
                ),
                widget.Image(
                    scale=True,
                    background=colors[0],
                    filename="~/.config/qtile/images/arrowleft-trans-bg1.png",
                ),
                widget.TextBox(
                    text=" ",
                    foreground=colors[8],
                    background=colors[4],
                    padding=0
                ),
                widget.Volume(
                        foreground=colors[8],
                        background=colors[4],
                        padding=5),
                # widget.Net(
                # interface = "enp6s0",
                # format="{down} ↓↑ {up}",
                # foreground=colors[8],
                # background=colors[27],
                # padding=5,
                # ),
                widget.Image(
                    scale=True,
                    background=colors[4],
                    filename="~/.config/qtile/images/arrowleft-trans-bg.png",
                ),
                widget.Clock(
                    foreground=colors[8],
                    background=colors[0],
                    format=" %a, %b %d %H:%M ",
                ),
                widget.Image(
                    scale=True,
                    background=colors[0],
                    filename="~/.config/qtile/images/arrowleft-trans-bg1.png",
                ),
                # widget.BatteryIcon(
                    # update_interval=60, foreground=colors[8], background=colors[4]
                # ),
                widget.Systray(background=colors[4], padding=5),
                widget.Sep(
                    linewidth=0, padding=10, foreground=colors[8], background=colors[4]
                ),
                widget.Image(
                    scale=True,
                    background=colors[4],
                    filename="~/.config/qtile/images/arrowleft-trans-bg.png",
                ),
                # widget.CurrentLayout(
                    # foreground=colors[8], background=colors[0], padding=5
                # ),
                widget.CurrentLayoutIcon(
                    scale=True, foreground=colors[8], background=colors[0]
                ),
            ],
            24,
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        {"wmclass": "confirm"},
        {"wmclass": "dialog"},
        {"wmclass": "download"},
        {"wmclass": "error"},
        {"wmclass": "file_progress"},
        {"wmclass": "notification"},
        {"wmclass": "splash"},
        {"wmclass": "toolbar"},
        {"wmclass": "confirmreset"},  # gitk
        {"wmclass": "makebranch"},  # gitk
        {"wmclass": "maketag"},  # gitk
        {"wname": "branchdialog"},  # gitk
        {"wname": "pinentry"},  # GPG key password entry
        {"wmclass": "ssh-askpass"},  # ssh-askpass
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"  # ho de fuck uses java? Didn't it die like 15 years ago?
