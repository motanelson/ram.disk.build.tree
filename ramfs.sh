printf "\033c\033[40;39m\ngive the image file name ? "
read a
mkdir /tmp/rams 2>/dev/null
sudo mount -t tmpfs $a /tmp/rams

