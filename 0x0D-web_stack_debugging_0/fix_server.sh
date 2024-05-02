#!/bin/bash

# Copy /etc/passwd to /tmp
cp /etc/passwd /tmp

# Create a file named isworking in /tmp containing "OK"
echo "OK" > /tmp/isworking

# Verify that both files exist
ls /tmp/passwd /tmp/isworking

