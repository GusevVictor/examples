#!/bin/bash

echo "free space in root is: $(echo "100 - $(df -h | grep -w / | awk '{print $5}' | sed 's/%//')" | bc) procent"

