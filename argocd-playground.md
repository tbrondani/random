Install argocd using kind

```
kind create cluster --name argo

kubectl create ns argocd

k apply -f kubectl apply -n argocd -f \
https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
```
argocd admin initial-password -n argocd
argocd login 
```
```
kubectl edit cm -n argocd argocd-cm
```
add the following and shift zz.
```
data:
  accounts.tales: apiKey,login
  accounts.tales.enabled: "true"
```
```
argocd account generate-token --account tales
```
```
argocd account update-password --account tales
```

disable security in argo
```
k edit cm -n argocd argocd-cmd-params-cm
```
add in the end of the yaml file 
```
data
  server.insecure: "true"
```

curl calls
```
export TOKEN=token_generated_through_argocli
curl -vk $ARGOCD_SERVER/api/v1/applications --cookie "argocd.token=$TOKEN"
```

add the cluster to your kind environment
```
argo cluster add kind-argo
```

known issue with kind and argocd- connection refused solution.
``
https://github.com/argoproj/argo-cd/issues/4204#issuecomment-1040210354
``

add a sample app
```
argo app create grafana \
--repo https://grafana.github.io/helm-charts \
--helm-chart grafana \
--revision 7.0.0 \
--dest-server https://kubernetes.default.svc
```

refs:  
1 - https://kind.sigs.k8s.io/docs/user/quick-start/  
2 - https://argo-cd.readthedocs.io/en/stable/operator-manual/user-management/  
3 - https://argo-cd.readthedocs.io/en/stable/operator-manual/ingress/#disable-internal-tls  
