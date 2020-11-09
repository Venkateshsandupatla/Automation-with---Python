import os

print('\t\t Automation Assistant ')
print('\t\t--------------------------------')
print()

#----------------------------------------------------functions for local vm---------------------------------------------------#

#-------------------------- Function for docker installation------------------

def docker():
    os.system('sudo cp docker.repo /etc/yum.repos.d/docker.repo')
    repolist= os.system('sudo yum repolist')
    os.system('sudo yum install docker-ce --nobest')
    os.system('sudo systemctl start docker')
    os.system('sudo systemctl enable docker')
    status= os.system('sudo systemctl status docker')


# --------------------------Function for docker services--------------------------


def container():

 while True:  
     print('press 1 to pull the image')
     print('press 2 to list images')
     print('press 3 to run the docker conatiner')
     print('press 4 to check the status/list  of docker conatiners')
     print('press 5 to install and configure apache webserver on docker conatiner')
     print('press 6 to install python interpreter on docker conatiner and run a python code')
     print('press 7 to stop the docker conatiner')
     print('press 8 to delete all docker containers')
     print('press 9 to exit') 
     con = input('Enter what you want to do on docker: ')
   

     if int(con) == 1:
       imagename = input('Enter image name: ')
       
       os.system('docker pull {}'.format(imagename))
     elif int(con) == 2:
       list_images = os.system('sudo docker images')
       print(list_images)
     elif int(con) == 3:
       os_name = input('Enter os name: ')
       imagename = input('Enter image name: ')
      
       os.system('sudo docker run -dit --name {}   {}'.format(os_name,imagename))
     elif int(con) == 4:
       status = os.system('sudo docker ps -a')
       print(status)
     elif int(con) == 5:
       nameoftheos = input('Enter os name where you want to configure apache webserver: ')
       nameoftheimage = input('Enter imagenamewithversion: ')
       portno = input('Enter port number: ')
       os.system('sudo systemctl stop firewalld')
       os.system('sudo systemctl disable firewalld')
       os.system('sudo docker run -dit --name {} -p {}:80 {}'.format(nameoftheos,portno,nameoftheimage))
       os.system('sudo docker exec {} yum install httpd -y'.format(nameoftheos))
       os.system('sudo docker cp index.html {}:/var/www/html'.format(nameoftheos))
       os.system('sudo docker exec {} /usr/sbin/httpd'.format(nameoftheos))
     elif int(con) == 6:
       st = os.system('docker ps')
       print(st)
       osname = input('Enter your container name: ') 
       os.system('sudo docker exec {} yum install python3 -y'.format(osname))           
       os.system('sudo docker cp hi.py {}:/'.format(osname)) 
       pyoutput = os.system('docker exec {} python3 hi.py'.format(osname))
       print(pyoutput)
     elif int(con) == 7:
       conatiners =os.system('sudo docker ps') 
       name = input('Enter which os you have to stop: ')
       os.system('sudo docker stop {}'.format(name))
     elif int(con) == 8:
       os.system('sudo docker rm -f $(docker ps -a -q)')
       ot =  os.system('sudo docker ps -a')
       print(ot)   
     elif int(con) == 9:
       break         
     else: 
       print("sorry")

# ---------------Function for Configuring Webserver--------------------

def webserver():
    os.system('sudo yum install httpd -y')
    os.system('sudo cp index.html  /var/www/html/')
    os.system('sudo systemctl start httpd')
    os.system('sudo systemctl stop firewalld')
    vm_ip = input('Enter your vm ip: ')
    output=os.system('curl {}/index.html'.format(vm_ip) #Ip of the vm for seeing the result
    print(output)

#--------------Function for LVM-------------------
#--------------for this we have to add a hardisk in the vm you can do it from vm settings--------------
def LVM():
    fdisk = os.system('sudo fdisk -l')
    print(fdisk)
    hdname = input('Enter the hardisk name: ')
    pv = os.system('sudo pvcreate {}'.format(hdname))
    print(pv)
    vgname = input('Enter Vgname: ')
    vg = os.system('sudo vgcreate {}  {}'.format(vgname,hdname)) 
    lvname = input('Enter Lvname: ')
    lvsize = input('Enter the size of Lv in G/M: ')
    os.system('sudo lvcreate --size {} --name {} {}'.format(lvsize,lvname,vgname))
    os.system('sudo mkfs.ext4 /dev/{}/{}'.format(vgname,lvname))
    dir = input('Enter a name to create a directory  for mounting to lv: ')
    directory = os.system('sudo mkdir /{}'.format(dir))
    print(directory)
    os.system('sudo mount /dev/{}/{}  /{}'.format(vgname,lvname,dir))
    df = os.system('df -hT')
    print(df)
#-------------Function for Incresing the size of lvm oonfly-----------
def LVMONFLY():
    size = input('Enter the size to increase(+) with G/M: ')
    lvdisplay =  os.system('lvdisplay')
    print(lvdisplay)
    lvm = input('Enter the lv name: ')
    os.system('lvextend --size {} /dev/{}'.format(size,lvm))
    os.system('sudo resize2fs {}'.format(lvm))
    dfht = os.system('df -hT')
    print(dfht)       
#-----------------------------Function for Ansible insatllation-----------
def ansible():

    os.system("tput setaf 4")
    os.system('sudo yum install python3 -y')  #to install python software
    
    os.system("tput setaf 5")
    os.system('sudo pip3 install ansible ') #to install ansible software
    
    os.system("tput setaf 6")
    os.system('ansible --version')
#----------Function-Hadoop -----------

#-------core_site file----------

def core_site():
    print('Enter NameNode IP Address :   ', end='')
    NN_ip=input()
   
    os.system('echo \<configuration\> >> core-site.xml')
    os.system('echo \<property\> >> core-site.xml')
    os.system('echo \<name\>fs.default.name\<\/name\> >> core-site.xml')
   
    if cmd=='1':
        os.system('echo \<value\>hdfs://{}:9001\<\/value\> >> core-site.xml'.format(NN_ip))
    else:
        os.system('echo \<value\>hdfs://{}:9001\<\/value\> >> core-site.xml'.format(NN_ip))
   
    os.system('echo \</property\> >> core-site.xml')
    os.system('echo \<\/configuration\> >> core-site.xml')
   
    if cmd=='2':
        os.system('scp core-site.xml {}:/etc/hadoop/core-site.xml'.format(remote_ip))
    else:
        os.system('cp core-site.xml /etc/hadoop/core-site.xml')

#----Hdfs file-----------------------------    

def hdfs_site():
    
    if cmd1=='6':
        print('Enter DataNode Directory name you want to create :   ' ,end='')
    
    elif cmd1=='5':
        print('Enter NameNode Directory name you want to create :   ' ,end='')
    
    dir_name=input()
    
    if cmd=='2':
        os.system('ssh {} mkdir {}'.format(remote_ip , dir_name))
    else:
        os.system('mkdir {}'.format(dir_name))
    os.system('echo \<configuration\> >> hdfs-site.xml')
    os.system('echo \<property\> >> hdfs-site.xml')
    
    if cmd1=='6':
        os.system('echo \<name\>dfs.data.dir\<\/name\> >> hdfs-site.xml')
    elif cmd1=='5':
        os.system('echo \<name\>dfs.name.dir\<\/name\> >> hdfs-site.xml')
    os.system('echo \<value\>{}\<\/value\> >> hdfs-site.xml'.format(dir_name))
    os.system('echo \</property\> >> hdfs-site.xml')
    os.system('echo \<\/configuration\> >> hdfs-site.xml')
    if cmd=='2':
        os.system('scp hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml'.format(remote_ip))
    else:
        os.system('cp hdfs-site.xml /etc/hadoop/hdfs-site.xml')
#-----------------------------------------------------------Functions for remote vms------------------------------------------#

#------------function for configuring docker--------------

def remotedocker():
   
    os.system('sudo scp docker.repo root@{}:/etc/yum.repos.d/'.format(remote_ip))

    repolist= os.system('sudo ssh {}  yum repolist'.format(remote_ip))
    os.system('sudo ssh {}  yum install docker-ce --nobest'.format(remote_ip))
    os.system('sudo ssh {}  systemctl start docker'.format(remote_ip))
    os.system('sudo ssh {}  systemctl enable docker'.format(remote_ip))

#----Function for configuring webserver -----------    

def remotewebserver():
    os.system('ssh {} sudo yum install httpd -y'.format(remote_ip))
    os.system('sudo scp index.html root@{}:/var/www/html/'.format(remote_ip))
    os.system('ssh {}  systemctl start httpd'.format(remote_ip))
    os.system('ssh {}  systemctl stop firewalld'.format(remote_ip))
    output=os.system('ssh {} curl {}/index.html'.format(remote_ip,remote_ip))
    print(output)
#------Function for docker services----------------

def remotecontainer():

 while True:
     print('press 1 to pull the image')
     print('press 2 to list images')
     print('press 3 to run the docker conatiner')
     print('press 4 to check the status/list  of docker conatiners')
     print('press 5 to install and configure apache webserver on docker conatiner')
     print('press 6 to install python interpreter on docker conatiner and run a python code')
     print('press 7 to stop the docker conatiner')
     print('press 8 to delete all docker containers')
     print('press 9 to exit')
     con = input('Enter what you want to do on docker: ')


     if int(con) == 1:
       imagename = input('Enter image name: ')

       os.system('ssh {} docker pull {}'.format(remote_ip,imagename))
     elif int(con) == 2:
       list_images = os.system('sudo ssh {} docker images'.format(remote_ip))
       print(list_images)
     elif int(con) == 3:
       os_name = input('Enter os name: ')
       imagename = input('Enter image name: ')

       os.system('sudo ssh {}  docker run -dit --name {}   {}'.format(remote_ip,os_name,imagename))
     elif int(con) == 4:
       status = os.system('sudo ssh {} docker ps -a'.format(remote_ip))
       print(status)
     elif int(con) == 5:
       nameoftheos = input('Enter os name where you want to configure apache webserver: ')
       nameoftheimage = input('Enter imagenamewithversion: ')
       portno = input('Enter port number: ')
       os.system('sudo ssh {} systemctl stop firewalld'.format(remote_ip))
       os.system('sudo ssh {} systemctl disable firewalld'.format(remote_ip))
       os.system('sudo ssh {} docker run -dit --name {} -p {}:80 {}'.format(remote_ip,nameoftheos,portno,nameoftheimage))
       os.system('sudo ssh {} docker exec {} yum install httpd -y'.format(remote_ip,nameoftheos))
       os.system('sudo ssh {} docker cp /var/www/html/index.html {}:/var/www/html'.format(remote_ip,nameoftheos))
       os.system('sudo ssh {} docker exec {} /usr/sbin/httpd'.format(remote_ip,nameoftheos))
       weboutput = os.system('sudo ssh {} curl {}:{}'.format(remote_ip,remote_ip,portno)) 
       print(weboutput)
     elif int(con) == 6:
       st = os.system('ssh {} docker ps'.format(remote_ip))
       print(st)
       osname = input('Enter your container name: ')
       os.system('sudo ssh {}  docker exec {} yum install python3 -y'.format(remote_ip,osname))
       os.system('sudo scp hi.py root@{}:'.format(remote_ip)) 
       os.system('sudo ssh {} docker cp hi.py {}:/'.format(remote_ip,osname))
       pyoutput =  os.system('sudo ssh {} docker exec {} python3 hi.py'.format(remote_ip,osname))
      # pypage = input('Enter code for python page: ')
      # os.system('sudo  echo {} > python.py'.format(pypage))
      # os.system('sudo scp python.py root@{}:/home/venky'.format(remote_ip))
      # os.system('sudo ssh {} docker cp /home/venky/python.py {}:/'.format(remote_ip,osname))
      # pyoutput = os.system('ssh {} docker exec {} python3 python.py'.format(remote_ip,osname))
       print(pyoutput)
     elif int(con) == 7:
       conatiners =os.system('ssh {} sudo docker ps'.format(remote_ip))
       name = input('Enter which os you have to stop: ')
       os.system('sudo ssh {} docker stop {}'.format(remote_ip,name))
     elif int(con) == 8:
       os.system('sudo ssh {} docker rm -f $(docker ps -a -q)'.format(remote_ip))
       ot =  os.system('sudo ssh {} docker ps -a'.format(remote_ip))
       print(ot)
     elif int(con) == 9:
       break
     else:
       print("sorry")

# -----------------------------------------------------------Main code -------------------------------------------------------# 

while True:
    print('press 1 to use local systmem \n press 2 to use remote systems ')
    print('Type exit for shutting down services')
    print('Enter your choice : ', end='')
    cmd=input()
    
    if '1' in cmd:
     while True:
        print('Press 1 to setup\install docker and start the docker serivces')
        print('Press 2 to setup apache webserver')
        print('Press 3 to see all serivces of docker')
        print('Press 4 to configure ansible[contoller node]')
        print('press 5 to setup hadoop namenode')
        print('press 6 to setup hadoop datanode')
        print('press 7 to set a lvm partion')
        print('press 8 to increase the size of lvm on fly')
		     # For using aws we have to install aws cli prior in your vm
        print('press 9 to create your own key pair in aws')
        print('press 10 to create a security group in aws')
        print('press 11 to create EBS volume')
        print('press 12 to create a S3 bucket')
        print('press 13 to launch an instance')
        print('press 14 to use custom aws CLI command by your own')
        print('press 15 to go back')
        print('Enter your choice : ', end='')
        cmd1 = input()

        if '1' in cmd1:
           docker()
        
        elif '2' in cmd1:
           webserver()
    
        elif '3' in cmd1:
           container()
        elif '4' in cmd1:
           ansible()
        elif '5' in cmd1:
           os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force')
           os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
           hdfs_site()
           core_site()
           os.system('hadoop namenode -format')
           os.system('hadoop-daemon.sh start namenode')
           jps = os.system('jps')
           print(jps)
        elif '6' in cmd1:
           os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force')
           os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
           hdfs_site()
           core_site()
           os.system('hadoop-daemon.sh start datanode')
           jp = os.system('jps')
           print(jp)
        elif '7' in cmd1:
           LVM()
        elif '8' in cmd1:
           LVMONFLY()
        elif  '9' in cmd1:
	       key_pair = input('Enter the key name you want to create: ')
	       os.system('aws ec2 create-key-pair --key-name {}' .format(key_pair))
        elif '10' in cmd1:
           security_group_name = input('Enter security group name you want to create: ')
	       os.system('aws ec2 create-security-roup --group-name {} --description "Allow SSH' .format(security_group_name))
        elif '11' in cmd1:
           ebs_volume_size = input('enter the Volume size you want to create: ')
	       availability_zone = input('enter the region where you want to create the volume1: ')
   	       os.system('aws ec2 create-volume --size {} --volume-type gp2 --availability-zone {}' .format(ebs_volume_size,availability_zone))
        elif '12' in cmd1:
           region_name = input('Enter the region where you want to create a S3 bucket')
           bucket_name = input('Enter a unique bucket name to create in your given region')
	       os.system('aws s3api create-bucket --bucket {} --region {}' .format(bucket_name,region_name))
        elif '13' in cmd1:
           image_id = input('Enter the AMI ID: ' )
	       count = input('enter the no. of instance you want to launch: ')
	       instance_type = input('Enter the instance type: ')
	       key_name = input('enter the key pair: ')
	       security = input('enter the security group id: ')
	       print()
	       os.system('aws ec2 run-instances --image-id {} --count {} --instance-type {} --key-name {} --security-group-ids {}' .format(image_id,count,instance_type,key_name,security))
        elif '14' in cmd1:
           custom = input("""Enter the aws command below:  >>>aws """)
	       os.system('aws {}' .format(custom))
           
        elif '9' in cmd1:
           break
        
        else:
           print('sorry')
         

    elif '2' in cmd:
      remote_ip = input('Enter your remote vm ip: ')
      while True:
        print('welcome to ssh mode')
        print('press 1 to install and start docker services in your remote vm')
        print('Press 2 to setup apache webserver in your remote vm')
        print('Press 3 to see all serivces of docker in your remote vm')
        print('press 4 to go back')    
        print('Enter your choice : ', end='')
        cmd2 = input()
        if '1' in cmd2:
          remotedocker()
        elif '2' in cmd2:
          remotewebserver()
        elif '3' in cmd2:
          remotecontainer()
        elif '4' in cmd2:
          break
        else:
          print('Enter valid option')  
    

    elif 'exit' in cmd:
      break
    else:
        print('enter valid option')
