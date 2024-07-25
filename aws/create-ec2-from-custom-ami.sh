#create a EC2 via aws cli - quick win
aws ec2 run-instances \
--image-id ami-12312312312312312 \
--instance-type t2.micro \
--count 1 \
--subnet-id subnet-123456789123 \
--key-name yourkey \
--security-group-ids 'sg-xxxxxxxxxxxxxxx' \
--block-device-mappings '[{"DeviceName":"/dev/xvda","Ebs":{"VolumeSize":20,"VolumeType":"gp3"}}]' \
--iam-instance-profile Name=SuperEC2Role \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=EC2MACHINE},{Key=environment,Value=DEV},{Key=billing,Value=cloud},{Key=payer,Value=organization}]' \
--dry-run
