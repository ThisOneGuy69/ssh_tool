import os
import json

CLIENTS_FILE = "clients.json"
# format: {"names": [], "ips": []}


#function to connect to devices
def connect_action(kind, ip, name): #kind is something like ssh ftp sftp etc.
    os.system(f"{kind} {name}@{ip}")

#function to clear the screen
def clear_action():
    os.system("cls" if os.name == "nt" else "clear")

#function to show the clients
def show_clients():
    for index, name_client in enumerate(list_name_clients):
            index_str = str(index)
            ip_client = list_ip_clients[index]
            print(f"{index_str}.  {name_client}   {ip_client}")
            print("-------------------------------")

#function to get user input on selection
def usr_number_input(promt, max_nbr):
    while True:
        try:
            usr_input = int(input(promt))
            if usr_input <= max_nbr and usr_input > -1: #only allows upto max ammount of nubers and no negative
                break  # Exit loop if successfull
            else:
                print("Please choose a valid option!")
        except ValueError:
            print("Please choose a valid option!")
    return usr_input

#function to get ip an username
def get_ip_and_usrname(index):
    return list_ip_clients[index], list_name_clients[index]

#json shit 
def load_clients():
    if os.path.exists(CLIENTS_FILE):
        with open(CLIENTS_FILE, "r") as f:
            data = json.load(f)
            return data.get("names", []), data.get("ips", [])
        return ["test_a", "test_b", "test_c"], ["192.168.178.200", "192.168.178.201", "192.168.178.202"]
def save_clients():
    with open(CLIENTS_FILE, "w") as f:
        json.dump({"names": list_name_clients, "ips": list_ip_clients}, f)

list_name_clients, list_ip_clients = load_clients() or ([], [])


#clear screen
clear_action()

# #Welcoming section
# print("Welcome to my SSH thingy :D")
print("-------------------------------")
print("0. SSH into client")
print("1. Add/Remove a client") 
print("2. FTP into client")
print("3. SFTP into client")
print("4. Ping a client")
print("5. Exit")
print("-------------------------------")

#calling the input function for numbers
usr_input = usr_number_input("Choose one of the options: ", 5)

#clear screen
clear_action()

if usr_input == 0:
    print("Client selection:")
    print("-------------------------------")
    #as the name implies it shows the clients with their stats (ip, name and position in the array  
    show_clients()
    selected_client_pos_array = usr_number_input("Select a client: ", len(list_ip_clients)-1)

    ip_client_selected, name_client_selected = get_ip_and_usrname(selected_client_pos_array)
    clear_action()
    print("-------------------------------")
    print(f"SSH'ing into client {ip_client_selected} with name {name_client_selected}!")
    print("-------------------------------")
    connect_action("ssh", ip_client_selected, name_client_selected)
elif usr_input == 1:
    print("0. Add client")
    print("1. Remove client")
    usr_input = usr_number_input("Choose: ", 1)
    if usr_input == 0:
        ip_new_client = input("IP of the client you want to add: ")
        name_new_client = input("Name of the user you want to use: ")
        list_ip_clients.append(ip_new_client)
        list_name_clients.append(name_new_client)
        save_clients()
        print("Client added and saved!")
    elif usr_input == 1:
        if not list_ip_clients:
            print("No clients to remove!")
        else:
            show_clients(list_name_clients, list_ip_clients)
            to_remove = usr_number_input("Select client to remove: ", len(list_ip_clients) - 1)
            del list_ip_clients[to_remove]
            del list_name_clients[to_remove]
            save_clients()
            print("Client removed and saved!")
elif usr_input == 2:
    print("Client selection:")
    print("-------------------------------")
    #as the name implies it shows the clients with their stats (ip, name and position in the array  
    show_clients()
    selected_client_pos_array = usr_number_input("Select a client: ",max_nbr = len(list_ip_clients)-1)
    ip_client_selected, name_client_selected = get_ip_and_usrname(selected_client_pos_array)
    clear_action()
    print("-------------------------------")
    print(f"FTPing into client {ip_client_selected} with name {name_client_selected}!")
    print("-------------------------------")
    connect_action("ftp", ip_client_selected, name_client_selected)
elif usr_input == 3:
    print("Client selection:")
    print("-------------------------------")
    #as the name implies it shows the clients with their stats (ip, name and position in the array  
    show_clients()
    selected_client_pos_array = usr_number_input("Select a client: ",max_nbr = len(list_ip_clients)-1)
    ip_client_selected, name_client_selected = get_ip_and_usrname(selected_client_pos_array)
    clear_action()
    print("-------------------------------")
    print(f"SFTPing into client {ip_client_selected} with name {name_client_selected}!")
    print("-------------------------------")
    connect_action("sftp", ip_client_selected, name_client_selected)
elif usr_input == 4:
    print("Client selection:")
    print("-------------------------------")
    #as the name implies it shows the clients with their stats (ip, name and position in the array  
    show_clients()
    selected_client_pos_array = usr_number_input("Select a client: ",max_nbr = len(list_ip_clients)-1)
    ip_client_selected, name_client_selected = get_ip_and_usrname(selected_client_pos_array)
    clear_action()
    print("-------------------------------")
    print(f"Pinging client {ip_client_selected} with name {name_client_selected}!")
    print("-------------------------------")
    os.system(f"ping {ip_client_selected}")
elif usr_input == 5:
    print("Exiting ...")
