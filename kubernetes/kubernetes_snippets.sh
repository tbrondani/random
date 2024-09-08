## Format the output of a get hpa, filtering the ones you want
# k get hpa ultra-hpa1 -n ultra | awk 'NR == 1 {printf "%-20s%-8s %-8s %9s\n", "NAME", "MINPODS", "MAXPODS", "NOW"} NR != 1 {print$1,$5,$6,$7}' | column -t



# kubectl-pods-older-than-1-day.sh
# https://gist.github.com/rms1000watt/529cf68e57cf5c35db84f377db817292
# https://stackoverflow.com/a/53989428
# kubectl get pod | awk 'match($5,/[0-9]+d/) {print $0}'


# https://gist.github.com/rubberduck203/2869a0a38cbd0ed506db9bec880fb84d#file-cordonallnodes-sh
# kubectl get nodes | awk '{if (NR!=1) {print $1}}' | xargs -I {} kubectl cordon {}