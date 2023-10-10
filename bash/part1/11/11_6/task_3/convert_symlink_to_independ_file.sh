#!/bin/bash
test -L "$1" && cp -p $(ls -l "$1" | cut -d " " -f 11) "$1".real_file && unlink "$1"


