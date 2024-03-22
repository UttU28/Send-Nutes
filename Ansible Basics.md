# Project README

## Author
- **Name:** Utsav Chaudhary
- **Name:** UttU28
- **Email:** [utsavmaan28@gmail.com](mailto:utsavmaan28@gmail.com)


# **ANSIBLE**
-   Mutable Infrastructure.
-   Hostless / Agentless
-   Idompotency

# **PRO TIP**
![](https://drive.google.com/uc?export=view&id=sdv)
*  **RETRY**: If error, then hosts are saved and retry will run on those hosts.
    ```
    - name: Try to connect to a service, retry up to 3 times with a delay of 10 seconds
    some_module:
        # module parameters...
    retries: 3
    delay: 10
    until: result is succeeded
    ```
*  **LIMIT**: The limit parameter is used to restrict the execution of a playbook or specific tasks to a subset of hosts defined in the inventory.
    ```
    ansible-playbook -i inventory.ini playbook.yml --limit web_servers
    ```
*  **WATCH 4 SPACES**: *INDENTATION IS THE KEY< DONT MESSS BOIIIIIIII*
*  **Handlers** and **Variables** are shared accross Roles on the same system.


---

# **INVENTORIES**

*  Inventories are used by Ansible to locate and run against multiple systems.
*  It has list of Hosts, can be in groups too.
*  Default location for inventories are **/etc/ansible/hosts**
*  Can be **YAML** or **INI** file
*  It contains

## Types of Inventories:
* ### Dynamic Inventories:
    *  Executable file in place of Inventory file is called "Dynamic Inv"
    *  Output from the Inv file should be JSON
    *  Can code in Python, Java, C, Bash, etc.
    *  Make it **EXECUTABLE** using
        ```chmod +x fileName.py```
    *  Any file you make should give:
        ```
        --list
        ```
        ```
        --host[hostName]
        ```

    *  You can pull Inventory Information from
        *  A Cloud provider     (AWS EC2, Rackspace, OpenStack)
        *  LDAP
        *  Cobbler
        *  Other Configuration Management Database (CMDB) S/W
* ### Static & Dynamic
![](https://drive.google.com/uc?export=view&id=1V8byFDP10fovOhmb-yJlof3UmvhIZIlA)

## Group-vars & Host-vars:
*  In short, its providing private access to the variables based on the group and hosts.
*  web_server_variable will be available to all hosts in the web_servers group, while host_specific_variable will only be available to web_server1.

## Types of Hosts:
* ### Single
```
host1.example.com
host2.example.com
```
* ### Grouped / Collection
```
[groupName]
host1.example.com
host2.example.com
```
* ### Range
```
host[0:5].example.com
```


## Ping to Hosts:
```
ansible host1.example.com -m ping
ansible all -m ping
ansible -i inventory.yml groupName -m ping
```

# **MODULES**

*  Tools for particular Tasks
*  Returns JSON Data
*  Run from CMD or using Ansible Playbook
*  Custom Modules can be made using **Python**

## **More on Modules**
https://colab.research.google.com/drive/1KAqf7ayJb7rrs3NhK9xYszah-olk6S6V?usp=drive_link

# **VARIABLES**

*  Variable can be scoped by a Group, Host or even by a Playbook
*  Can be defined in Inventories, Ansible Roles and Block Groups.
*  Should be Letters, Numbers and Underscore, nothing else
*  Can also store return value.
*  It can be also used as input in command line  ```ansible-playbook play.yml -e'{"myVar":"myValue", ...}'```
*  You can also use a .yml file for the variables ```ansible-playbook -e @path/to/your/variable_file.yml playbook.yml```
*  There are already some of the **predefined** variables in Ansible

### **Dictionary Variables**
*  Allows Python style Dictinoaries to be used as Variable
*  Format to access Dict values:
    *  ```dictName['key']```
    *  ```dictName.key```

### **Magic Variables & Filters**
*  Special Vars are Magic Vars .... (WOW, so informational)
*  **hostvars**: ```{{hostvars['node1']['ansible_distribution']}}```
*  **groups**: ```{{groups['webservers']}}```
*  **Jinja2 / Template**: ```{{groups['webservers'] | join(' ')}}```
*  And many more...


### **Predefined Variables**
*  ***ansible_version***: Provides information about the version of Ansible.
*  ***ansible_os_family***: Specifies the operating system family (e.g., Debian, RedHat, Windows).
*  ***ansible_distribution***: Specifies the name of the distribution (e.g., Ubuntu, CentOS).
*  ***ansible_distribution_version***: Specifies the version of the distribution.
*  ***ansible_hostname***: Provides the hostname of the target machine.
*  ***ansible_facts***: A dictionary containing various facts about the system, such as network interfaces, IP addresses, and more.
*  ***ansible_nodename***: Provides the nodename of the target machine.
*  ***inventory_hostname***: The name of the current target host.
*  ***inventory_hostname_short***: The short name of the current target host.
*  ***group_names***: A list of groups to which the current host belongs.
*  ***hostvars***: A dictionary of all variables for a host.
*  ***play_hosts***: A list of all hosts in the current play.
*  ***playbook_dir***: The directory of the playbook being run.
*  ***ansible_managed***: String indicating that a file is managed by Ansible.

```
- name: Debug predefined variables
  hosts: localhost
  tasks:
    - name: Display predefined variables
      debug:
        var: hostvars[inventory_hostname]

```

# **FACTS**

*  Facts provide information about a given Target Host.
*  Facts are automatically collected by Ansible
*  To manually collect facts befroehand, use ***ad-hoc commands***: ```ansible all -m setup```
*  With ad-hoc commands you can use ***Filters*** and ***RegEx*** to get te specific chunk of Information
*  ```ansible all -m setup -a "filter=*ipv4*"```
*  It can be disabled :)

### **USE FACTS**
*  All collected Facts can be accessed through Variables, like ```{{ ansible_default_ipv4['address']}}```

### **Facts.d (Custom Facts)**
*  All ***Custom Facts*** are stored under ***ansible_local***.
*  Can create custom facts and store it in ```/etc/ansible/facts.d``` directory with extension ```fileName.fact```
*  Facts are only created on the ***Host-Nodes***, not on the ***Control-Node***
*  Ansible will accept JSON output from an executable file. And YAML / INI.

# **PLAYS & PLAYBOOK**

*  Its a series of Plays.
*  

## **Conditional**
*  **Register** for **Returning results** of a Command
*  **When** for **Conditional Execution** of Command
*  **Changed_When** for setting the ***TASK*** to **CHANGED** only if condition satisfies
*  **Failed_When** for setting the ***TASK*** to **FAIL** only if condition satisfies
*  **Notify** is like calling a **Function** which is saved in the **Handler**


## **ERROR HANDLING**
*  Ignoring acceptable Errors
*  Defining Failure Condition
*  Defining "Changes"
*  Blocks

# **CONFIGURATION FILES**

## Possilbe Locations (In Order)
*  ANSIBLE_CONFIG (env var)
*  ansible.cfg (curent dir)
*  .ansible.cfg (hidden in home dir)
*  /etc/ansible/ansible.cfg

Using the config folder you can set some basic default values

# **AD_HOC COMMANDS**

*  Ad-hocs are usually oneliners
*  Operational Commands:
    1.   Checking Logs
    2.   Daemon Control
    3.   Process Management
*  Informational Commands:
    1.   Check installed SW
    2.   Check System properties
*  Research
    1. Do ***wht ya want***, test new things

```
ansible host/groupName -i inventoryFile.yml -b -m yum -a "name=httpd state=latest"
ansible host/groupName -i inventoryFile.yml -b -m file -a "path=fileLocation  state=touch"
```

![](https://drive.google.com/uc?export=view&id=1UAHIhFXpVckFbAf6ykl7qOB8XDQci4MV)

# **TEMPLATE** (JINJA)

*   Set values dynamically.
*   The template module will only have access to Host Variables for Hosts Targeted by the current play.
*   The template will have access to Ansible facts.

#### **CODE AVAILABE IN MODULE FILES**

#  **TAGS**

*  Tags let you Play specific tasks in the Playbook.
*  Allowing you to execute specific tasks in the **Playbook**

# **ROLES**

## **BIG PICTURE...         literally**
![](https://drive.google.com/uc?export=view&id=10_TXUqyN3sWD-AZYqTNnj_iPQlZAfXL3)

#### **ROLES, how it looks**
![](https://drive.google.com/uc?export=view&id=1GnVunrF5qCYzHGOxFAso8uOIFnzrzErR)
*  Roles are same as assigning roles / access to someone
*  Roles can be found in ```/etc/ansible/roles/```
*  In Ansible each role has a different Directory
*  It requires this particular Directory Structure, **atleast one** dir containing ```main.yml``` should exist.

### **TASKS**
*  Main list of **Tasks** to be executed by the **Host**
*  Should contain ```main.yml``` if the **Task** directory is in use.

### **VARS**
*  Contains Variables used within the roles.
*  **Highest** Level of precedence.
*  Can be overwritten by passing values through CLI

### **DEFAULTS**
*  Contains Default value of the variables.
*  If nothing is given then I'll use the default value brother.
*  **Lowest** leve of precedence

### **HANDLERS**
*  Containg **Handlers**, that can be used by this **Role** as well as anyone **outside** accessing this DIR.
*  Handlers are functions just like in python, but it executes at very end of all tasks.
*  Even if called multiple times, it'll just execute once at end :) Happy Boi

### **FILES & TEMPLATES**
*  Can be accessed directly, no in depth path needed.
*  ***Files***: are **Static**
*  ***Templates***: are for **Dynamic** ...... thats it

### **META**
*  Store files related to the metadata of a role.
*  Useful for organizing metadata-related files and tasks.
*  Dependencies and other things can be defined in the Meta for a Role.
*  
```
dependencies:
  - { role: username.rolename, some_parameter: 3 }
```

![](https://drive.google.com/uc?export=view&id=sdv)
![](https://drive.google.com/uc?export=view&id=sdv)
![](https://drive.google.com/uc?export=view&id=sdv)
![](https://drive.google.com/uc?export=view&id=sdv)

# **ANSIBLE-GALAXY**

*  Ansible Galaxy is a **Large Public Repos for Ansible**.
*  Contains large number of roles that are constantly evolving and increasing.
*  Galaxy can use **GIT** allowing for other role sources such as **GitHub**.
*  ```ansible-galaxy init roleName```
*  ```ansible-galaxy install userName.Role```
*  ```ansible-galaxy list``` --for all the roles installed in the role path.

# **PARALLELISM IN ANISBLE***

*  Can control / execute multiple hosts at the same time.
*  Use ```-f``` with either ```ansible``` or ```ansible-playbook``` commands to set the number of **FORKS**
*  Default can be changed in ```ansible.cfg```

# **ANSIBLE VAULT**

*  Allows **File Encryption** and **Decryption** with Password
*  ```ansible-vault encrypt fileName```
*  The ```ansible-vault rekey``` allows user to reencrypt the file, but will require old password to do so.
* Supply **Password** during **Play Execution**, must use either ```--ask-vault-password``` or ```--ask-vault-file``` flags.
*  New feature ```--vault-id``` supersees the password, and lets us have multiple passwords, unlike the above.
*  Can set ```no_log``` in a module for sensetive information.

# **ANSIBLE TOWER**

*  Web Server - Interface for Ansible
*  System Requirements are **HEAVY**, Office Laptop ke gaand fat jayegi
*  Tower is free for Minimal Use
*  Benifits:
    * Provisioning
    * Audit Trail (Only by License)


## **KEY FEATURES**
* **Graphical Interface**: Ansible Tower offers a user-friendly web-based interface that allows users to define, manage, and monitor automation tasks and workflows.
* **Role-Based Access Control (RBAC)**: It provides role-based access control to ensure that only authorized users have the appropriate permissions to view or execute certain tasks. This helps in maintaining security and restricting access to sensitive information.
* **Job Scheduling**: Ansible Tower enables users to schedule automation jobs at specific times or intervals. This is useful for automating routine tasks, backups, and maintenance activities.
* **Job Templates**: Job templates in Ansible Tower allow users to define and reuse automation jobs easily. These templates encapsulate the required playbook, inventory, and other parameters, making it simpler to execute tasks consistently.
* **Inventory Management**: Ansible Tower helps manage dynamic inventories, allowing users to define and update inventory sources dynamically. This is particularly useful in dynamic cloud environments.
* **Logging and Auditing**: Ansible Tower maintains detailed logs of automation job runs, providing visibility into job status, output, and errors. This audit trail is valuable for troubleshooting and compliance purposes.
* **Notifications**: It supports notifications and alerts, allowing users to receive notifications about job outcomes, failures, or other specified events via various channels like email, Slack, or other integrations.
* **REST API**: Ansible Tower provides a RESTful API that allows integration with external systems and tools, facilitating automation and orchestration within larger IT ecosystems.
