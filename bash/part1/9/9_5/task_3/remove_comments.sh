#!/bin/bash
# Comment 1
out_script=/tmp/"$1".without_comments
cat "$1" | sed '/^#[^!]/d' > "$out_script"
echo "The new scipt without comments is: "$out_script""

