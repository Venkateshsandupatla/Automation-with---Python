import os

os.system("tput setaf 2")

print()

print("\t\t\t aws Automation ")
print("\t\t\t ---------------")

os.system("tput setaf 3")

print("""press 1 to create your own key pair
press 2 to create a security group
press 3 to create EBS volume
press 4 to create a S3 bucket
press 5 to launch an instance
press 6 to use custom aws CLI command by your own""")

cmd=input('enter your choice: ')

if cmd=='1':
	key_pair = input('Enter the key name you want to create: ')
	os.system('aws ec2 create-key-pair --key-name {}' .format(key_pair))

if cmd=='2':
	security_group_name = input('Enter security group name you want to create: ')
	os.system('aws ec2 create-security-roup --group-name {} --description "Allow SSH' .format(security_group_name))

if cmd=='3':
	ebs_volume_size = input('enter the Volume size you want to create: ')
	availability_zone = input('enter the region where you want to create the volume1: ')
	os.system('aws ec2 create-volume --size {} --volume-type gp2 --availability-zone {}' .format(ebs_volume_size,availability_zone))


if cmd=='4':
	region_name = input('Enter the region where you want to create a S3 bucket')
	bucket_name = input('Enter a unique bucket name to create in your given region')
	os.system('aws s3api create-bucket --bucket {} --region {}' .format(bucket_name,region_name))

if cmd=='5':
	image_id = input('Enter the AMI ID: ' )
	count = input('enter the no. of instance you want to launch: ')
	instance_type = input('Enter the instance type: ')
	key_name = input('enter the key pair: ')
	security = input('enter the security group id: ')
	print()
	os.system('aws ec2 run-instances --image-id {} --count {} --instance-type {} --key-name {} --security-group-ids {}' .format(image_id,count,instance_type,key_name,security))


if cmd=='6':
	os.system('tput setaf 6')
	custom = input("""Enter the aws command below:  
>>>aws """)
	os.system('aws {}' .format(custom))
	






