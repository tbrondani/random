#!/bin/bash

while true; do
  aws ec2 describe-volumes-modifications --filters Name=modification-state,Values="optimizing,completed" --query "VolumesModifications[?StartTime>='2021-04-22'].{ID:VolumeId,STATE:ModificationState,PROGRESS:Progress}"
  date
  sleep 30
done