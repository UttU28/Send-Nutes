# Project README

## Author
- **Name:** Utsav Chaudhary
- **Name:** UttU28
- **Email:** [utsavmaan28@gmail.com](mailto:utsavmaan28@gmail.com)

# **ANSIBLE MODULES**

1.   https://faun.pub/ansible-30-most-important-modules-for-devops-professional-part-1-fdd536b0790d
2.   https://faun.pub/ansible-30-most-important-modules-for-devops-professional-part-2-bb3f9739898e
3.   https://faun.pub/ansible-30-most-important-modules-for-devops-professional-part-3-6494507184bb

# **PING**
Ping module is used for checking up on the remote host, specifically for connectivity to remote host and for checking python on the remote host. It can also be used to check user login and privilages


---
- name: ping module
  hosts: all
  become: false
  tasks:
    - name: #test connection
      ping:

# **SETUP**
*   Facts gathering about the target nodes like hostname, ip, os etc.
*   This module is automatically called by playbook to gather useful variable about remote host.
*   All the information is presented in a friendly JSON format, with all values being preceded with “ansible_”.


ansible host-1 -m setup -u ec2-user
ansible all -m setup -u ec2-user -a 'filter=ansible_os_family'

# **YUM**
Yum module is used to install different packages/software on Redhat based linux flavours.


- name: #Uninstall Apache
    yum:
      name: nginx
      state: absent

  - name: #Install a list of packages with a list variable
    yum:
      name: "{{ packages }}"
    vars:
      packages:
      - httpd
      - httpd-tools

# **APT**
Apt package module is used for managing software on debian based linux os.


- name: #Run the equivalent of "apt-get update" as a separate step
    apt:
      update_cache: yes

  - name: #Install latest version of "openjdk-6-jdk"
    apt:
      name: openjdk-6-jdk
      state: latest
      install_recommends: no

# **PACKAGE**
This modules manages packages on a target without specifying a package manager module (lyum, apt, …). It is convenient to use in an heterogeneous environment of machines without having to create a specific task for each package manager. This module acts as a proxy to the underlying package manager module. While all arguments will be passed to the underlying module,


- name: #Install ntpdate
    ansible.builtin.package:
      name: ntpdate
      state: present

  - name: #Install the latest version of Apache and MariaDB
    ansible.builtin.package:
      name:
        - httpd
        - mariadb-server
      state: latest

# **PIP**
Pip module is used for managing python packages on the target system.


- name: #Install multi python packages with version specifiers
    pip:
      name:
        - django>1.11.0,<1.12.0
        - bottle>0.10,<0.20,!=0.11

  - name: #Install specified python requirements
    pip:
      requirements: /my_app/requirements.txt

# **NPM**
Npm module is used for managing of node.js packages. This module is not part of ansible-core modules. To use it in a playbook, specify: community.general.npm.


- name: #Install "coffee-script" node.js package.
    community.general.npm:
      name: coffee-script
      path: /app/location

  - name: #Install packages based on package.json.
    community.general.npm:
      path: /app/location

# **RAW**
The RAW module in Ansible is employed for executing direct and basic SSH commands, typically used for tasks like installing Python on systems lacking it or communicating with devices, such as routers, without Python installed.


- name: #Bootstrap a host without python2 installed
    raw: dnf install -y python2 python2-dnf libselinux-python

  - name: #Run a command that uses non-posix shell-isms (in this example /bin/sh doesn't handle redirection and wildcards together but bash does)
    raw: cat < /tmp/*txt
    args:
      executable: /bin/bash

# **COMMAND**
Command module is used to execute commands on a remote node. It is used mostly to run simple Linux commands . The command(s) will not be processed through the shell, so variables like **$HOSTNAME** and operations like “<”, “>”, “|”, “;” and “&” will not work. For **Windows** targets, use the **win_command** module instead. For windows based target win_command can be used in place of command module.


- name: #Run command if /path/to/database does not exist (without 'args')
    command: /usr/bin/make_database.sh db_user db_name creates=/path/to/database

  - name: #Run command if /path/to/database does not exist (with 'args' keyword)
    ansible.builtin.command: /usr/bin/make_database.sh db_user db_name
    args:
      creates: /path/to/database

# **SHELL**
Shell module is designed to execute shell commands against the target unix based hosts. Unlike the Ansible command module, **Ansible Shell would accept highly complexed commands** with pipes, redirection etc, you can also execute shell scripts using this module. This module is designed to work **only with Linux based** Machines and not Windows, For** windows you should use win_powershell** module


- name: #This command will change the working directory to somedir/ and will only run when somedir/somelog.txt doesn't exist
    shell: somescript.sh >> somelog.txt
    args:
      chdir: somedir/
      creates: somelog.txt

  - name: #This command will change the working directory to somedir/
    shell:
      cmd: ls -l | grep log
      chdir: somedir/

  - name: #Run a command that uses non-posix shell-isms (in this example /bin/sh doesn't handle redirection and wildcards together but bash does)
    shell: cat < /tmp/*txt
    args:
      executable: /bin/bash
# Will execute using Bash

# **SCRIPT**
Script module can be used to run a local script on a remote node.
Transfers the script to the remote node and then executes it.
**No Python** is required, executes through **SHELL**


-  name: #Run a script with arguments (free form)
     ansible.builtin.script: /some/local/script.sh --some-argument 1234

  -  name: #Run a script with arguments (using 'cmd' parameter)
     ansible.builtin.script:
       cmd: /some/local/script.sh --some-argument 1234

# **COPY**
Copy module can be used to copy a file from local/remote machine to remote machine. For windows machine you can use **win_copy** module.


- name: #copy a file from local machine to local machine
    copy:
      src: files/src.txt
      dest: files/dest.txt

  - name: #copy a file from remote machine to remote machine
    copy:
      src: /etc/src.txt
      dest: /etc/dest.txt

  - name: #copy a file from local machine to remote machine with owner and permissions
    copy:
      src: files/src.txt
      dest: /etc/dest.txt
      owner: foo
      group: foo
      mode: '0644'

# **FETCH**


1.   Fetch is inverse of COPY.
2.   File transfer from Remote to Local Machine.
3.   Files are stored in local machine in a directory with the name of thehostname.






- name: #copy a file from remote machine to local machine
    fetch:
      src: /var/log/access.log
      dest: /var/log/fetched

  - name: #copy a file from local machine to remote machine with owner and permissions
    copy:
      src: files/src.txt
      dest: /etc/dest.txt
      owner: foo
      group: foo
      mode: '0644'

# **GET_URL**


*   get_url module can be used to download files form **HTTPS/HTTP/FTP servers**.
*   By default this module uses the proxy configured for the node.
*   **Custom proxy** can be used by setting environment variable or by using **use_proxy** option.




---
- name: get_url module
  hosts: all
  tasks:
  - name: #download tomcat from apache
    get_url:
      url: https://downloads.apache.org/tomcat/tomcat-8/v8.5.81/bin/apache-tomcat-8.5.81-deployer.tar.gz
      dest: /tmp/download/tomcat
      mode: 0755
      owner: tomcat
      group: tomcat

# **ARCHIVE**
*   Archive module is used to create a compressed file package of the format of zip, tar, gz, bz2 and xz.
*   By default it assumes that the source file you are trying to compress does exists and It does not copy source file to target node before compressing.
*   One thing to keep in mind is that It requires the package type that we are using as compressed file output should already be installed on the target node.


- name: #Compress directory /path/to/foo/ into /path/to/foo.tgz
    archive:
      path: /path/to/foo
      dest: /path/to/foo.tgz
  - name: #Compress regular file /path/to/foo into /path/to/foo.gz and remove it
    archive:
      path: /path/to/foo
      remove: yes
  - name: #Create a bz2 archive of multiple files, rooted at /path
    archive:
      path:
      - /path/to/foo
      - /path/wong/foo
      dest: /path/file.tar.bz2
      format: bz2
  - name: #Create a gz archive of a globbed path, while excluding specific dirnames
    archive:
      path:
      - /path/to/foo/*
      dest: /path/file.tar.bz2
      exclude_path:
      - /path/to/foo/bar
      - /path/to/foo/baz
      format: gz

# **UNARCHIVE**
*   Unarchive module is used to unpacks an archive file such as tar, gz, zip.
*   Copy the file to the remote server before uncompressing them.
*   The module use unzip and tar -xzf command to unpack the compressed file so these commands should be installed on target nodes.
*   For windows node **win_unzip** can be used.


- name: #Extract foo.tgz into /var/lib/foo
    unarchive:
      src: foo.tgz
      dest: /var/lib/foo

  - name: #Unarchive a file that is already on the remote machine
    unarchive:
      src: /tmp/foo.zip
      dest: /usr/local/bin
      remote_src: yes               # This is necessary for Remote Servers

  - name: #Unarchive a file that needs to be downloaded
    unarchive:
      src: https://example.com/example.zip
      dest: /usr/local/bin
      remote_src: yes

# **FILE**
*   Creating files and directories, deleting files and directories, creating soft and hard symbolic links, adding and modifying file and directory permissions, and more.
*   For windows machine you could use win_file module.


- name: #Create a file
    file:
      path: /etc/foo.conf
      state: touch
      mode: u=rw,g=r,o=r
  - name: #Create a directory if it does not exist
    file:
      path: /etc/some_directory
      state: directory
      mode: '0755'
  - name:# Remove file (delete file)
    file:
      path: /etc/foo.txt
      state: absent
  - name: #Remove directory and its contents
    file:
      path: /path/to/directory
      state: absent
      recurse: true
  - name: #Change file ownership, group and permissions
    file:
      path: /etc/foo.conf
      owner: foo
      group: foo
      mode: '0644'
  - name: #Create a symbolic link         Ansible allows you to manage symbolic links on remote machines using playbooks. (A Note that says "This thing is there! Andhi Gaand" )
    file:
      src: /file/to/link/to
      dest: /path/to/symlink
      owner: foo
      group: foo
      state: link

# **ACL** (Access Control List)
*   acl module is used to create and modify access control list entries, similar to the **getfacl** (Get Permissions of File/Dir) and **setfacl** (Set Permissions of File/Dir) commands.
*   Requires that **ACLS** are **ENABLED**
*   For windows machine you can use **win_acl** module


- name: #Grant user Joe read access to a file
    acl:
      path: /etc/foo.conf
      entity: joe
      etype: user
      permissions: r
      state: present

  - name: #Removes the acl for Joe on a specific file
    acl:
      path: /etc/foo.conf
      entity: joe
      etype: user
      state: absent

  - name: #Sets default acl for joe on foo.d
    acl:
      path: /etc/foo.d
      entity: joe
      etype: user
      permissions: rw
      default: yes                  # New objects created within that directory inherit these default permissions.
      state: present

# **TEMPLATE** (JINJA)
*   Set values dynamically.
*   The template files will usually have the .j2 extension
*   Copy (scp) the file to the remote server. (After dynamic creation of varialbes in a file, that file is sent to server and saved in the dest)




- name: #Template a file to /etc/file.conf
    template:
      src: /mytemplates/foo.j2
      dest: /etc/file.conf
      owner: bin
      group: wheel
      mode: '0644'

# **FIND**
*   Find files and directories
*   For windows, you should use a **win_find** module instead.

A regular expression or pattern which should be matched against the file content.

If **read_whole_file == false** it matches against the beginning of the line (uses **re.match()**).

If **read_whole_file == true**, it searches anywhere for that pattern (uses **re.search()**).
Works only when file_type is file.



- name: #Recursively find /tmp files older than 2 days
    find:
      paths: /tmp
      age: 2d
      recurse: yes

  - name: #Recursively find /tmp files older than 4 weeks and equal or greater than 1 megabyte
    find:
      paths: /tmp
      age: 4w
      size: 1m
      recurse: yes

  - name: #Recursively find /var/tmp files with last access time greater than 3600 seconds
    find:
      paths: /var/tmp
      age: 3600
      age_stamp: atime
      recurse: yes

# **REPLACE**
*   Replace all the instances of a matching string in a file.
*   Supports regular expression
*   Can also create backup of a file before replacing.


- name: #Ansible replace Unix with Linux
    replace:
      path: /etc/ansible/sample.txt
      regexp: 'Unix'
      replace: 'Linux'

  - name: #Replace before the expression till the begin of the file
    replace:
      path: /etc/apache2/sites-available/default.conf
      before: '# live site config'
      regexp: 'Unix'
      replace: 'Linux'

  - name: #Replace between the expressions and create a backup
    replace:
      path: /etc/hosts
      after: '<VirtualHost [*]>'
      before: '</VirtualHost>'
      regexp: 'Unix'
      replace: 'Linux'
      backup: yes

# **LINEINFILE**
*   Add, remove, modify a single line in a file.
*   Can use **Conditions** with **RegEx**
*   Reuse and modify the matched line using the back reference parameter.
*   **insertafter** and **insertbefore** attributes


- name: #adding a line
    lineinfile:
      path: /etc/selinux/config
      regexp: '^SELINUX='
      line: SELINUX=enforcing

  - name: #deleting a line
    lineinfile:
      path: /etc/sudoers
      state: absent
      regexp: '^%wheel'

  - name: #Replacing a line
    lineinfile:
      path: /etc/hosts
      regexp: '^127\.0\.0\.1'
      line: 127.0.0.1 localhost

  - name: #replace a line only after a specified string
    lineinfile:
      path: /etc/httpd/conf/httpd.conf
      regexp: '^Listen '
      insertafter: '^#Listen '
      line: Listen 8080

# **BLOCKINFILE**
*   Insert/update/remove a block of multi-line text.
*   Block will be surrounded by a markers, **BEGIN** and **END**, to make the task **Idempotent**.
*   By default, the block will be inserted at the end of the file.


- name: #insert a block into a file
    blockinfile:
      path: /etc/ssh/sshd_config
      block: |
        Match User ansible-agent
        PasswordAuthentication no

  - name: #Insert/Update HTML surrounded by custom markers after <body> line
    blockinfile:
      path: /var/www/html/index.html
      marker: "<!-- {mark} ANSIBLE MANAGED BLOCK -->"
      insertafter: "<body>"
      block: |
        <h1>Welcome to {{ ansible_hostname }}</h1>
        <p>Last updated on {{ ansible_date_time.iso8601 }}</p>

# **SERVICE**
*   Control Service on target nodes.
*   **Start** / **Stop** / **Restart** / **Reload** a service.
*   For windows based target machine you can use **win_service** module.


- name: #Start service httpd, if not started
    service:
      name: httpd
      state: started

  - name: #Stop service httpd, if started
    service:
      name: httpd
      state: stopped

  - name: #Restart service httpd, in all cases
    service:
      name: httpd
      state: restarted

  - name: #Reload service httpd, in all cases
    service:
      name: httpd
      state: reloaded

# **USER**
*   Manage USERS on target node.
*   It uses **useradd, usermod** and **userdel** to create, modify and delete users.
*   Can define uid, group, shell, password etc.
*   For windows based target machine you can use win_user module.


- name: #Add the user 'johnd' with a specific uid and group of 'admin'
    user:
      name: johnd
      comment: John Doe
      uid: 1040
      group: admin

  - name: #Add the user 'james' with a bash shell, appending the group 'admins' and 'developers' to the user's groups
    user:
      name: james
      shell: /bin/bash
      groups: admins,developers
      append: yes       #If append: no then the previous groups will be deleted/written over

  - name: #Remove the user 'johnd'
    user:
      name: johnd
      state: absent
      remove: yes       #If remove: no then the user == removed but Home dir and Mail Spool != removed.

  - name: #Create a 2048-bit SSH key for user jsmith in ~jsmith/.ssh/id_rsa
    user:
      name: jsmith
      generate_ssh_key: yes
      ssh_key_bits: 2048
      ssh_key_file: .ssh/id_rsa

  - name: #Added a consultant whose account you want to expire
    user:
     name: james18
     shell: /bin/zsh
     groups: developers
     expires: 1422403387

# **GROUP**
*   Manage GROUPS on target node.
*   It uses **groupadd, groupmod** and **groupdel** to create, modify and delete groups.
*   For windows based target machine you can use win_group module.


- name: #Ensure group "somegroup" exists
    group:
      name: somegroup
      state: present

  - name: #Ensure group "docker" exists with correct gid
    group:
      name: docker
      state: present
      gid: 1750

  - name: #deleting a group
    group:
      name: groupA
      state: absent

# **CRON**
*   Manage crontab entries and define environment variables.


- name: #Ensure a job that runs at 2 and 5 exists. Creates an entry like "0 5,2 * * sh script.sh"
    cron:
      name: "check dirs"
      minute: "0"
      hour: "5,2"
      job: "sh script.sh"

  - name: #'Delete a job from the crontab'
    cron:
      name: "an old job"
      state: absent

  - name: #Creates an entry like "APP_HOME=/srv/app" and insert it after PATH declaration
    cron:
      name: APP_HOME
      env: yes
      job: /srv/app
      insertafter: nthCronJob     #This cron job will be in queue after the nthCronJob

# **DEBUG**
*   Used as print() in python.
*   Can display custom Message and Variables


- name: #Print a simple statement
      debug:
      msg: "Hello World! A custom message"

  - name: #Get uptime information
    shell: /usr/bin/uptime
    register: result

  - name: #Print return information from the previous task
    debug:
      var: result
      verbosity: 2

#   **REGISTER**
*  It's used to capture the output of a task and store it in a variable.
*  This variable can then be used later in the playbook.
*  Can make decisions based on that result.

  * directory_listing.***stdout***: Captures the standard output of the command.
  * directory_listing.***stderr***: Captures the standard error output of the command.
  * directory_listing.***rc***: Captures the return code of the command.


- name: #Run a command and register the output
    command: ls /path/to/some/directory
    register: directory_listing

  - name: #Display the captured output
    debug:
      var: directory_listing.stdout_lines
# OR  OR  OR  OR  OR  OR  OR  OR  OR  OR  OR  OR  OR  OR  OR
  - name: #Display the captured output
    debug:
      msg: "All the files in dir are: \n {{ directory_listing.stdout }}"

# **INCLUDE_VARS**
*   Can be used to dynamically load the variables from the file/directory during a task run.
*   Any variable set using **set_fact** will not be overwritten by it.
*   Can also be used to Read a file and print the data


- name: #include a variable file
    include_vars:
      file: name_vars.yml

  - name: #include a variable file conditionally
    include_vars:
      file: vars-Debian.yml
    when: ansible_os_family == 'Debian'

  - name: #Include all .yaml files in vars directory except bastion.yaml
    include_vars:
      dir: vars
      ignore_files:
        - 'bastion.yaml'
      extensions:
        - 'yaml'

# **INCLUDE_ROLE**
*   Dynamically loads and execute a specified role as a task.


- name: #include role myrole
    include_role:
      name: myrole

  - name: #Run tasks/other.yaml instead of main.yaml
    include_role:
      name: myrole
      tasks_from: other

  - name: #Pass variables to role
    include_role:
      name: myrole
    vars:
      rolevar1: value from task

  - name: #Conditional role
    include_role:
      name: myrole
    when: not idontwanttorun

#  **WHEN**
*  When is used to conditionally execute tasks based on certain conditions.
*  It is a basic **If condition**.
*  Can be combined with **with_items** and **with_files** to iterate through the file or list of items.


- name: #Check if the OS is Ubuntu
      ansible.builtin.command: uname
      register: os_info
    - name: #Install Nginx on Ubuntu
      ansible.builtin.package:
        name: nginx
        state: present
      when: "'Ubuntu' in os_info.stdout"      # Will install NGINX only if the OS is Ubuntu.

# **WITH_ITEMS    &    WITH_FILES**
*  


- name: #Create users using WITH_ITEMS
      user:
        name: "{{ item }}"
      with_items:
        - akhil
        - rakesh
        - abhiram
        - nikhil


    - name: #Check if each file exists
      stat:
        path: "{{ item.path }}"
      with_files:
        - /path/to/file1.txt
        - /path/to/file2.txt
      register: file_info
    - name: #Display file info for existing files
      debug:
        msg: "{{ item.path }} exists - Size: {{ item.stat.size }} bytes"
      with_items: "{{ file_info.results }}"
      when: item.stat.exists

#  **TAGS**
*  Tags let you Play specific tasks in the Playbook.


---
- name: Example Playbook with Tags
  hosts: all
  become: yes
  tasks:
    - name: Install Apache
      ansible.builtin.package:
        name: apache2
        state: present
      tags:
        - install
        - webserver

    - name: Start Apache Service
      ansible.builtin.service:
        name: apache2
        state: started
      tags:
        - start
        - webserver

    - name: Configure Apache
      ansible.builtin.template:
        src: templates/httpd.conf.j2
        dest: /etc/apache2/httpd.conf
      notify: Restart Apache
      tags:
        - configure
        - webserver

  handlers:
    - name: Restart Apache
      ansible.builtin.service:
        name: apache2
        state: restarted
      tags:
        - restart
        - webserver

# How to use tags while executing the Playbook
ansible-playbook playbook.yml --tags "install,start"

# **ANSIBLE-GALAXY**
*  Ansible Galaxy is a **Large Public Repos for Ansible**.
*  Contains large number of roles that are constantly evolving and increasing.
*  Galaxy can use **GIT** allowing for other role sources such as **GitHub**.


- name: #Install Role
      command: ansible-galaxy install elastic.elasticsearch



# **ANSIBLE-VAULT**
*  Allows Encryption and Decryption of Files.


#Encrypt file using this
ansible-vault encrypt --vault-id prod@passwordFile secure

#Run the file and send password using this
ansible-playbook vault.yml --vault-id prod@vault

---
---
# ***ADDITIONAL THINGS TO KEEP IN MIND***
---
---

# **SLURP**

*  Read the contents of a file on a remote host and return the data as a base64-encoded string.


- name: Read File Content
      ansible.builtin.slurp:
        src: "/path/to/your/file.txt"
      register: file_content

    - name: Display File Content
      debug:
        msg: "Content of the file is \n{{ file_content.content | b64decode }}"

#  **ERROR HANDLING**
*  For Handing Errors (hehe)


- name: Install HTTPD if NOT already.
      yum:
        name: httpd
        state: latest
      ignore_errors: yes

    - name: #Setting custom ERROR Conditions
      command: /home/ansible/doSomething.sh
      register: commandOutput
      changed_when: "'CHANGED' in commandOutput.stdout"
      failed_when: "'FAIL' in commandOutput.stdout"

    - name: #TRY / CATCH / ALWAYS
      block:
        - git:
            repo: https://github.com/UttU28/Transparent-Login-Registration-Form-in-HTML-and-CSS.git
            dest: /home/vagrant/webPage
          register: repoStatus
      rescue:
        - debug:
            msg: "Already Existing file with some modifications. Remove it!"
            var: repoStatus
      always:
        - debug:
          msg: "This block will be executed always no matter what."

# **ASYNC TASKS**
*  Can execute tasks Asynchronusly using **ASYNC**.
*  The value provided is the amount of time the task will run in background, after that Ansible will kill the task
*  Can check on the task at certain intervals using **POLL**
*  If **POLL** == 0 then, it will let the task run in background until finished or timeout.


- name:
      command: /home/vagrant/thisScript.sh
      async: 60                 # Total execution time provided to this script in seconds
      poll: 10                  # Check if the task is completed or not at specific intervals in seconds.

# **DELEGATING TASKS**
*  Delegating a particular task to run only on **SPECIFIED HOST**


---
- hosts: midhtech
  tasks:
    - name: #Run Something on Delegated host
      command: /home/vagrant/someScript.sh
      async: 60
      poll: 0
      delegate_to: deployment   # This wont execute on the "MIDHTECH" host rather it'll execute in the **DEPLOYMENT** host.

# **SERIAL**
*  Used for Parallelism in Ansible. It lets us execute multiple **HOSTS** simultaneously.
*  It should be less than **MAX FORKS**, or else will only execute **MAX FORKS** number of **HOSTS** Simultaneously.


---
- hosts: all
  serial: 1             # This will execute 1 host at a time for each task
  become: yes

---
- hosts: all
  serial:
  - 1             # This will execute 1 host in a batch
  - 3             # This will execute 3 host in a batch
  - 5             # This will execute 5 host in a batch
  become: yes

---
- hosts: all
  serial:
  - 10             # This will execute 10 hosts in a batch
  - '30%'             # This will execute 30% of host in a batch
  - '50%'             # This will execute 50% of host in a batch
  become: yes

# **MAX_FAIL_PERCENTAGE**
*  If **max_fail_percentage** number of Hosts fail **--->** **Stop Execution**


---
- hosts: all
  max_fail_percentage: 10                       # If 10 percent of Hosts fail then Stop Execution
  serial: 1
  become: yes

# **RUN ONCE**
*  Just like it says Dumb ass
*  Use it with Delegate to make it work for one host at a time just once.



---
- hosts: all
  become: yes
  run_once: yes