#!/bin/bash
for ping_host in mail.ru vk.com; do ping -c2 $ping_host &>null && echo "Ping $ping_host OK" || echo "Ping $ping_host not ok"; done
