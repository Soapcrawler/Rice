#/bin/bash

ch=$(echo -e "Power off\nReboot\nLogout" | rofi -dmenu -p "Choice")

case "$ch" in
	"Power off")
		shutdown -h now
		;;
	"Reboot")
		reboot
		;;
	"Logout")
	    pkill -u dell
		;;
	*)
		exit
		;;
esac
