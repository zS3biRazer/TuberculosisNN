#!/bin/bash

#Just fixing the Images:

#for img in ./*.png ; do
#    magick "$img" -fuzz 4% -trim -resize 512x512! -colorspace Gray "./$(basename "$img")"
#done

#Adding data augmentation: rotation (0-10°), random flips, flop, transverses, transposes
declare -i y=0
for img in ./*.png; do
    y=$((y + 1))
    t=$((y % 5))
    rnd=$(echo "scale=0; $RANDOM / 327.68" | bc)  # Integer between 0 and 10
    case "$t" in
    0)
        magick "$img" -fuzz 4% -trim -resize 512x512! -distort SRT $((rnd * 2 - 10)) -colorspace Gray "./$(basename "$img")"
    ;;

    1)
        magick "$img" -fuzz 4% -trim -resize 512x512! -distort SRT $((rnd * 2 - 10)) -flip -colorspace Gray "./$(basename "$img")"
    ;;

    2)
        magick "$img" -fuzz 4% -trim -resize 512x512! -distort SRT $((rnd * 2 - 10)) -flop -colorspace Gray "./$(basename "$img")"
    ;;

    3)
        magick "$img" -fuzz 4% -trim -resize 512x512! -distort SRT $((rnd * 2 - 10)) -transverse -colorspace Gray "./$(basename "$img")"
    ;;

    4)
        magick "$img" -fuzz 4% -trim -resize 512x512! -distort SRT $((rnd * 2 - 10)) -transpose -colorspace Gray "./$(basename "$img")"
    ;;
    esac
done