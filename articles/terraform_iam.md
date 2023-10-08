Who doesnt like terraform? Being able to create, recreate and modify (at least some) of your infrastructure at your will with just a few commands or cliks(if you have a terraform cloud for example)

Today I wanna explore 3 ways you can integrate IAM in terraform, some like it some dont, but lets make it suck less when working with IAM policies.

Method 1
File

Method 2
EOF and <<POLICY>>



Method 3

json code!


This is the most common arround, because it is very easy to implement and if you dont have a lot of experience with json it is your main go, but it also has some complications such as the need of changing the file everytime you need to change something, lets say include a arn or a acion in the policy

the more you use tf and start to have similar issues as mentioned above you could go to one of the next 2 solutions, though we accomplish the same thing, the implementation is quite different.

now let's say you have this code , 

bucket changing name everytime.

you would need to change the configs everytime, even though you are not using json files anymore you still need to change the arn and the action in code


interpolation

now you dinamically change your iam policy based on the tfcode.

magical isnt it?

json code
this one is estimated to be the "most professional way"




What's your favorite? Will you jump back into legacy code and change it? Any ideas or toughts? 

Please comment, like and share :)

<a href="https://www.buymeacoffee.com/tbrondani" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>


