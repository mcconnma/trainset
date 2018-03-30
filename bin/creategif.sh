
animate() {
	convert -delay 200 -loop 0 $1*.png $1.gif
}

tile() {
	montage $1*.png -geometry +4+4 all$1.png
}

$1 $2

