Install argocd using kind

```
kind create cluster --name argo

kubectl create ns argocd

k apply -f kubectl apply -n argocd -f \
https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
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
refs:  
https://kind.sigs.k8s.io/docs/user/quick-start/  
https://argo-cd.readthedocs.io/en/stable/operator-manual/user-management/
