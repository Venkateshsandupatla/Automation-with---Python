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
    output=os.system('curl 192.168.1.11/index.html')
    print(output)
    
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
    output=os.system('ssh {} curl 192.168.1.10/index.html'.format(remote_ip))
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
        print('press 8 to go back')
        print('Enter your choice : ', end='')
        cmd1 = input()

        if '1' in cmd1:
           docker()
        
        elif '2' in cmd1:
           webserver()
    
        elif '3' in cmd1:
           container()
    
        elif '8' in cmd1:
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
        print('Press 4 to configure ansible[contoller node] in your remote vm')
        print('press 5 to setup hadoop namenode in your remote vm')
        print('press 6 to setup hadoop datanode in your remote vm')
        print('press 8 to go back')
        print('Enter your choice : ', end='')
        cmd2 = input()
        if '1' in cmd2:
          remotedocker()
        elif '2' in cmd2:
          remotewebserver()
        elif '3' in cmd2:
          remotecontainer()
        elif '8' in cmd2:
          break
        else:
          print('Enter valid option')  
    

    elif 'exit' in cmd:
      break
    else:
        print('enter valid option')
