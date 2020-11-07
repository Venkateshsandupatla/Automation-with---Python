import os

os.system("tput setaf 3")

print()
print("\t\t\t Welcome to My Automation tool")
print("\t\t\t -----------------------------")


os.system("tput setaf 3")



print('press 6 to install ansible')
cmd=input()

os.system("tput setaf 7")

if cmd=='6':
    os.system("tput setaf 4")
    os.system('sudo yum install python3')  #to install python software
    print()
    os.system("tput setaf 5")
    os.system('sudo pip3 install ansible ') #to install ansible software
    print()
    os.system("tput setaf 6")
    os.system('ansible --version') # to check the version of ansible or to confirm whether or not ansible is istalled or not



