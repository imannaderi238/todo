import os
import time
import colorama as clr
# Get the variables sent by the user during the execution of the program
import sys

#***************************************
#this function create a user and password forthe user , i think it is nice .but i have a problem!!!
#line 232 and 233 when active this function , i want to execute just one time.afther the user input command like -l ,-a ,... one part of this fuction and function load username execute
def save_username_to_file( personal_information_file):
    """
    function dutty : create a file and save username and password
    arguments :
    personal_information_file :name of the file that it  has username and password
    """
    try:
        
        if os.path.isfile(personal_information_file) == False:
            print_command_line(2, 'Welcome to Command Line To Do Application ! ',
                       'First, lets create username and password ')
            with open(personal_information_file, 'w') as write_file:
                username = input('enter the username please :')
                #password = input('input the password please :')
                format_user_pass = f'username is :{username} and password is ******* '
                write_file.write(format_user_pass)
                write_file.close()
                clean_screen()
                
        if os.path.isfile(personal_information_file) == True:
            print_command_line(2, 'Welcome to Command Line To Do Application ! ',
                       'First, lets load username and enter your password. Please wait ... ')
            time.sleep(1.2)
            # print(load_username(personal_information_file))
            with open(personal_information_file, 'r') as read_file:
                user_password = input('Please input your password :')
                file_contnet =read_file.read()
                for i in range(len(file_contnet)-1  ,-1 ,-1):
                    if file_contnet[i] == ' ':
                        load_pass_file =file_contnet[i+1 :len(file_contnet)]
                        break
                        #print_command_line(1 ,load_pass_file)
                if user_password == load_pass_file:
                    print_command_line(1 ,'Your password is correct.please wait to load command line application')
                    time.sleep(1)
                    read_file.close()
                    clean_screen()
                    time.sleep(1)
                    return True
                else:
                    print_command_line(1 ,'Your password is not correct')
                    time.sleep(1)
                    clean_screen()
                    print_command_line(1 ,'see you next time')
                    time.sleep(1)
                    read_file.close()
                    return False
                    sys.exit()
                    
                
    except Exception as exep:
        print(exep)


def load_username(personal_information_file):
    """
    function dutty :give the username 
    argument :
    personal_information_file : the name of the file that it has the username and passsword
    return: a string that it is username
    """
    strat_position = 0
    with open(personal_information_file, 'r') as read_file:
        file_contnet =read_file.read()
        for i in range(0 ,len(file_contnet)):
            if file_contnet[i] == ':':
                strat_position = i
                for j in range(i , len(file_contnet)):
                    if file_contnet[j] == ' ':
                        # print(i)
                        # print(strat_position)
                        # print(file_contnet[strat_position : j])
                        return file_contnet[strat_position + 1 : j]
   
                                

def clean_screen():
    """
    function dutty : clean the screen
    """
    os.system('cls')


def print_command_line(numbers_msg=1 ,*messages):
    """
    function dutty : print the several messages in the terminal
    arguments :
    numbers_msg : the number of messages that you want to print
    *messages : all messages that you want to print and show the user
    """
    try :
        print()
        for i in range(0, numbers_msg):
            msg_tuple = messages[i]
            for j in range(0, len(msg_tuple)):
                str_temp = msg_tuple[j]
                print(f'{clr.Fore.CYAN}{str_temp}', end='', flush=True)
                time.sleep(0.04)
            print(clr.Fore.WHITE)
    except TypeError as ty_error:
        numbers_msg = 1 


def print_usage():
    """
    function dutty : the print all commands that you can work with on
    """
    print('****************************************')
    print_command_line(1, 'Welcome to Command Line To Do Application !')
    time.sleep(1)
    #print(f'{clr.Fore.GREEN} you are ***  {load_username(my_password_file)}  ***')
    print(f'{clr.Fore.CYAN}')
    print('Command Line To Do Application')
    print(f'{clr.Fore.YELLOW}')
    print(f'{' *' * 15}')
    print(f'{clr.Fore.WHITE} Command-line arguments:\n-l Lists all the tasks\n-a Adds a new task\n-r Removes a task\n-c Completes a task')


def add_list(description):
    """
    function dutty : add a new task to the tasks file
    argument:
    description : the detail about task that you want to do
    """
    if os.path.isfile(my_task_file) == True:
            with open(my_task_file, 'a') as write_file:
                write_file.write(f'[ ] {description}\n')
                print_command_line(1 ,'The new task added successfully!')
                print()
                write_file.close()
    else:
        print_command_line('File is not exist')
        with open(my_task_file, 'a') as write_read_file:
            write_read_file.write(f'{description}\n')
            print_command_line(1 ,'task file created and the new task added successfully!')
            print()
            write_read_file.close()


def list_task():
    """
    function dutty : show the list of the tasks in the file
    """
    if os.path.isfile(my_task_file) == True:
        with open(my_task_file, 'r') as read_file:
            lines = read_file.readlines()
            print()
            print(f'You have {clr.Fore.RED}{len(lines)}{clr.Fore.WHITE} tasks')
            print(f'{clr.Fore.GREEN}{'*' * 16}{clr.Fore.WHITE}')
            if len(lines) == 0:
                print_command_line('No todos for today! :)')
            for i in range(len(lines)) :
                result_str =f' {i} : {lines[i]}'
                print_command_line(1 ,result_str)
            read_file.close()
    elif os.path.isfile(my_task_file) == False:
        with open(my_task_file, 'w') as read_file:
            print_command_line('file created in directory')
            read_file.close()
        print_command_line('No todos for today! :)')


def remove_task(count_task):
    """
    function dutty : remove the task from the task file
    """
    try:
        if os.path.isfile(my_task_file):
            with open(my_task_file, 'r') as read_file:
                lines = read_file.readlines()
            if 0 <= int(count_task) < len(lines):
                # number_of_index = int(count_task) - 1
                # print(number_of_index)
                del lines[int(count_task)]
                print_command_line(1 ,'The new task removed successfully!')
                with open(my_task_file, 'w') as write_file:
                    write_file.writelines(lines)
            else:
                print_command_line(1 ,"Unable to remove:index is out of bound")
        else:
            print_command_line(1 ,'File * {my_task_file}  * not found.')
    except ValueError as val_error:
        print_command_line(1 , 'Unable to remove:index is not a number')    
    

def complete_task(which_task):
    """
    function dutty : complete the task from the task file
    """
    try:
        if os.path.isfile(my_task_file):
            with open(my_task_file, 'r') as read_file:
                lines = read_file.readlines()
            if 0 <= int(which_task) < len(lines):
                complete_task = lines[int(which_task)] 
                del lines[int(which_task)]
                for i in range(0 ,len(complete_task)):
                    if complete_task[i] == '[':
                        complete_task = f'{complete_task[0:i+1]}x]{complete_task[i+3:len(complete_task)]}'
                        #print(complete_task)
                        with open(my_task_file, 'w') as write_file:
                            write_file.writelines(lines) #write the file without the line is changed
                            write_file.write(complete_task)
                        break
                print_command_line(1 ,'The task completed successfully!')
            else:
                print_command_line(1 ,"Unable to complete:index is out of bound")
        else:
            print_command_line(1 ,'File * {my_task_file}  * not found.')

    except ValueError as val_error:
        print_command_line(1 , 'Unable to complete:index is not a number')    

# def all_command():
my_task_file ='tasks.txt'
my_password_file = 'user_pass.txt'

#********************** This fuction set and afther that ask touser for password but i have a problem with it.after login when the user input
# -c 2 ,-a ,-l ,,,, one part of this function and load_username function execute and after execute any command , from user give the password!!!!
#if you have any comment please tel me or tonight i ask my mentor
#give_password =save_username_to_file(my_password_file) 
#if give_password :   



if len(sys.argv) == 1:
    print_usage()
elif sys.argv[1] == '-a':
    try:
        add_list(sys.argv[2])
    except IndexError as index_er:
        print_command_line(1 ,'Unable to add: no task provided')
elif sys.argv[1] == '-l':
    list_task()
elif sys.argv[1] == '-r':
    try:
        remove_task(sys.argv[2])
    except IndexError as index_er:
        print_command_line(1 ,'Unable to remove: noindex provided')
elif sys.argv[1] == '-c':
    try :
        complete_task(sys.argv[2])
    except IndexError as index_err:
        print_command_line(1 ,'Unable to check: no index provided')
else:
    print_command_line(2 ,'Unsupported argument.' ,'Please use the correct command-line arguments.')
    time.sleep(2)
    clean_screen()
    print_usage()