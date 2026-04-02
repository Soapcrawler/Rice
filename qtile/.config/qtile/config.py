import libqtile.resources
from libqtile import bar, layout, qtile, widget,hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import subprocess,os
mod = "mod4"
terminal = "alacritty"

col = {
        'bar':'#3c3836',
        'bg':'#282828',
        'bg1':'#665c54',
        'fg':'#ebdbb2',
        'red':'#cc241d',
        'green':'#98971a',
        'yellow':'#d79921',
        'blue':'#458588',
        'purple':'#b16286',
        'aqua':'#689d6a',
        'lred':'#fb4934',
        'lgreen':'#b8bb26',
        'lyellow':'#fabd2f',
        'lblue':'#83a598',
        'lpurple':'#d3869b',
        'laqua':'#8ec07c',
        }

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"],"Return",lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod],"f",lazy.window.toggle_fullscreen(),desc="Toggle fullscreen on the focused window",),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn('rofi -show drun'), desc="Spawn a command using a prompt widget"),
    #Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-"), desc="Lower Volume by 5%"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+"), desc="Raise Volume by 5%"),
    Key([], "XF86AudioMute", lazy.spawn("amixer sset Master 1+ toggle"), desc="Mute/Unmute Volume"),
    #brightness
    Key([], "XF86MonBrightnessUp",lazy.spawn("brightnessctl s 5%+")),
    Key([], "XF86MonBrightnessDown",lazy.spawn("brightnessctl s 5%-")),
]

for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

groups = [Group(i) for i in "12345"]
#Groups
for i in groups:
    keys.extend(
        [
            Key([mod],i.name,lazy.group[i.name].toscreen(),desc=f"Switch to group {i.name}",),
            # mod + shift + group number = switch to & move focused window to group
            Key([mod, "shift"],i.name,lazy.window.togroup(i.name, switch_group=True),desc=f"Switch to & move focused window to group {i.name}",
            ),
        ]
    )
#Layouts
layouts = [
        layout.Spiral(border_width = 4 ,ratio = 0.5,border_focus =col['yellow'],border_normal = col['bg1'],margin = 20)
]
#Widgets
widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=25,
    padding=6,
    background=col['bg'],
    foreground=col['lyellow'],
)
separator = widget.Sep(size_percent=65, foreground=col['bg1'])

extension_defaults = widget_defaults.copy()

widgets=[
        widget.GroupBox(
            borderwidth = 8,
            use_mouse_wheel = False,
            highlight_method = "text",
            this_current_screen_border = col['lyellow'],
            active = col['yellow'],
        inactive = col['bg1']),
       separator,
       widget.Prompt(),
       widget.Spacer(),
       #Clock
       separator,
       widget.Clock(format="   %d %a %I:%M %p ",),
       separator,
       widget.Spacer(),
       #CPUusage
       separator,
       widget.CPU(format='  {freq_current}GHz ', update_interval = 3,fontsize=23,),
       separator,
       #Memory
       widget.Memory(format=' {MemUsed: .0f}{mm} ', update_interval = 3,fontsize=23,),
       libqtile.widget.Systray(),
       #Volume
       separator,
       widget.Volume(
           emoji = True,
           emoji_list = ['󰖁' , '󰕿' , '󰖀' , '󰕾'],
           fontsize=20,),
       widget.Volume(fontsize=23,),
       separator,
       widget.Wlan(interface="wlan0",format='{essid} {percent:2.0%} '+'󰸋 ',disconnected_message='󰤮 '),
       separator,
       widget.TextBox(text=' ⏻  ',mouse_callbacks={"Button1":lazy.spawn("/home/abhijitp/.config/qtile/power.sh",shell=True)})
]

screens = [
    Screen(
        top=bar.Bar(
        widgets,
        size=50,
        margin=[10,10,0,10]),
        background="#000000",
        wallpaper='~/Downloads/wallpapers/planetw.png',
        wallpaper_mode="fill",
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=col['yellow'],
    border_width = 4,
    border_nomral=col['bg'],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "LG3D"
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call(home)
