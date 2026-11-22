# Rice
>My own repository for storing rice dots :)
# 🖥️ dotfiles

> My personal X11 Linux desktop configuration, managed with GNU Stow.

![Desktop Showcase](assets/screenshot.png)

## 🛠️ The Stack

| Category | Tool | Config Path |
| :--- | :--- | :--- |
| **Window Manager** | [Qtile](http://www.qtile.org/) | `qtile/.config/qtile` |
| **Compositor** | [Picom](https://github.com/yshui/picom) | `picom/.config/picom`[cite: 1] |
| **Terminal** | [Alacritty](https://alacritty.org/) | `alacritty/.config/alacritty`[cite: 1] |
| **App Launcher** | [Rofi](https://github.com/davatorium/rofi) | `rofi/.config/rofi`[cite: 1] |
| **System Info** | [Fastfetch](https://github.com/fastfetch-cli/fastfetch) | `fastfetch/.config/fastfetch`[cite: 1] |
| **Dotfile Manager** | [GNU Stow](https://www.gnu.org/software/stow/) | - |

## 🚀 Installation

> **⚠️ Warning:** Back up your existing `~/.config` directories before running `stow` to avoid symlink conflicts.

### 1. Prerequisites
Ensure you have `git`, `stow`, and the core packages installed on your system (e.g., on Arch Linux):

```bash
sudo pacman -S git stow qtile picom alacritty rofi fastfetch
