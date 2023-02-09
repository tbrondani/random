#!/bin/bash

# Files to work with
yesterday_file="ips_yesterday.txt"
today_file="ips_today.txt"

# Function to read files
function read_ips {
  local filename="$1"
  cat "$filename"
}

# Actual reading of the files
yesterday_ips=$(read_ips "$yesterday_file")
today_ips=$(read_ips "$today_file")

echo "##########"
echo "Baseline IPs from yesterday:"
echo "$yesterday_ips"
echo "##########"

# Creating arrays for yesterday and today
added_ips=($(echo "$today_ips" | grep -Fxv "$yesterday_ips"))
removed_ips=($(echo "$yesterday_ips" | grep -Fxv "$today_ips"))

# Checking changes
if [ ${#added_ips[@]} -gt 0 ] || [ ${#removed_ips[@]} -gt 0 ]; then
  # echoing stuff
  if [ ${#added_ips[@]} -gt 0 ]; then
    echo "Added IPs from yesterday:"
    for ip in "${added_ips[@]}"; do
      echo "$ip"
    done
  fi

  if [ ${#removed_ips[@]} -gt 0 ]; then
    echo "Removed IPs from yesterday:"
    for ip in "${removed_ips[@]}"; do
      echo "$ip"
    done
  fi
else
  # Nothing changed in the land of ips
  echo "Nothing changed"
fi
