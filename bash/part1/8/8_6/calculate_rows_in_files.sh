#!/bin/bash

sudo find /etc -maxdepth 1 -type f -exec wc -l "{}" \;

