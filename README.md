Some of my personal dotfiles.

nvim requires vim-plug. Install it and :PlugInstall

[(Neo)Vim Setup Screenshots](https://imgur.com/a/M9jpWJP)


* Picom config requires aur/picom-jonaburg-git.


* Qtile: Check out the config before running. You may wanna change a few things according to what you use.

I use paru, not yay. Change the update command in the package widget (default "sudo pacman -Syu").
Change myTerm to your terminal. For the neofetch config to work you need kitty and the very latest fish-git master or there will be a memory overflow.

Only 6 workspaces are visible, remove "visible_groups or add more names".

Color options for the bar and window borders:
* All the gruvbox colors are defined in the config.
* Change border at "border_focus", "border_normal"
* Change colors by swapping the defined names (bg, bg0-4, fg0-4, colors by the numbers indicated as comments after list items.
* in the widget.GroupBox, change colors[X] to the color you want.
* The >/< images are in the images dir. Change the name of all the widget.Image accordingly. Either all the same or every other as i have done.


Keybindings:
* Swap window focus: mod+j k
* Shuffle window around: mod shift+j k
* Grow/shrink window: mod+h l
* Split stack swap (window behind another in a stack, kind of like tabs.. maybe just use kitty tabs?): mod ctrl+enter
* Launch terminal: mod+enter
* Launch rofi runner: mod shift+enter
* Toggle layout: mod+tab
* Kill window: mod+q
* Restart Qtile: mod control+r
* Quit Qtile: mod control+q
* Fullscreen toggle a window: mod+f
* Launch dmenu: mod shift+d
App launchers:
* Firefox: mod shift+b
* kitty chat tabs-script: mod shift+f
* Thunar: mod shift+t
* Discord mod shift+d
* (not implemented) Keybinding-show-script: mod+F1

* Rofi scripts: @adi1090x on github (submodule included here)
* Apps quicklauncher: mod shift+space
* Power launcher: mod shift+q

Spaceship Prompt: My own .toml. Made to mimic OMF bobthefish gruvbox theme. Displays git info and many coding languages in the dir you are in.
Pretty much hacked together so far, but works fine.


I use the Klaus gtk theme. Great Gruvbox look.


Also running shell-color-scripts (pls remove pipes scripts)

neofetch is set to show a custom arch image at scale. *This will produce mommory overflow if you use fish from the aur, use latest git master and compile* Some code was just removed that corrects a terminal size fetching issue.







Probably dont use my awesome for now!
AwesomeWM: a lot of themes and libraries are unused. Some stuff in rc.lua like autostart is disabled, got some errors i havent gotten around to fixing.
Spotify widget requires streeturtles build of sp.
´´git clone https://gist.github.com/wandernauta/6800547.git
        cd ./6800547
        chmod +x sp
        sudo cp ./sp /usr/local/bin/ 
´´

Use at your own risk.
