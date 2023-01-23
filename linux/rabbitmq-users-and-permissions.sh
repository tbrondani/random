#!/bin/bash


#create several vhosts based on a list, create a  user based on each existent vhost , add full permissions to the user and generate a random password and in the end, prints out in the stdout.
# List of vhosts to create
vhosts=("vhost1" "vhost2" "vhost3")

# Loop through vhosts array and create each vhost
for vhost in "${vhosts[@]}"
do
    curl -X PUT -k -u user:pass https://localhost:15671/api/vhosts/user-$vhost
done

# Loop through vhosts array and create user with random password
for vhost in "${vhosts[@]}"
do
    # Generate random password
    password=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
    
    # Create user and set permissions
    curl -X PUT -k -u user:pass -H "Content-Type: application/json" \
    -d "{\"password\":\"$password\",\"tags\":\"management\"}" \
    https://localhost:15671/api/users/svc-$vhost
    curl -X PUT -k -u user:pass -H "Content-Type: application/json" \
    -d "{\"configure\":\".*\",\"write\":\".*\",\"read\":\".*\"}" \
    https://localhost:15671/api/permissions/$vhost/user-$vhost
    
    # Print created vhost, user and password to stdout
    echo "Vhost: $vhost, User: user-$vhost, Password: $password"
done


