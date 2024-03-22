# Project README

## Author
- **Name:** Utsav Chaudhary
- **Name:** UttU28
- **Email:** [utsavmaan28@gmail.com](mailto:utsavmaan28@gmail.com)


#   **INSTALLING JENKINS**
---

## Installing **JENKINS** with **DEPENDENCIES (JAVA JDK)**

*   **FEDORA (yum)**
```
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
sudo dnf -y upgrade
# Add required dependencies for the jenkins package
sudo dnf -y install fontconfig java-17-openjdk
sudo dnf -y install jenkins
sudo systemctl daemon-reload
```
*   **DEBIAN / UBUNTU (apt)**
```
    sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
    echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
    sudo apt-get -y update
    sudo apt-get -y install jenkins
```

#   **Additional Things**

### **ON START**
*   Add a **SHELL**.
*   Enable **SSH** by ```Manage Jenkins --> Configure Global Security ```.
*   Ports have 2 Options:
    *   Fixed Port: If you have **FIREWALL** and needs to have **1 PORT** open.
    *   Random Port: Gets chosen **RANDOMLY** on every Jenkins **RESTART**.

#   **CI/CD**
*   **Continuous Integration**:
    *   Automation process designed for Developers (**Automated Code Integration**)
    *   **Early Detection of Issues**: Code changes and running automated tests, any issues are identified and fixed quickly, reducing the likelihood of bugs making it to production.
*   **Continuous Deployment**
    *   **Automated Deployment Pipeline**: Deploying Changes to Production or Staging the environments after **PASSING** all the **TESTS**.
    *   **Faster Time-to-Market**: Reduces the manual effort for **releasing UPDATES**, resulting in faster **time-to-market** and improved customer satisfaction.

#   **JENKINS**
*   Open Source, **JAVA** based **CI/CD TOOL**.
*   Great for Testing, Development, Deployment.
*   Usee plugins for More Control and Access.

#   **PLUGINS**
*   ADDS / CHANGES Apperarence and Functionality.
*   Helps in Testing and Report Generation.
*   If not available already? **BUILD ONE**.
*   Plugins available for **BACKUP** of the server / code.
*   Plugins makes Dev ***HAPPY :)***
*   Do something with PLUGINS:
    *   **GUI**:
        ```
        Manage GUI ---> Manage PLUGINS
        ```
    *   **CLI**:
        ```
        enable-plugin
        install-plugin
        list-plugin
        disable-plugin
        ```

#   **JOBS**
*   Any Automation Process in Jenkins are called **JOBS**.
*   Types of Jobs in Jenkins (DEFAULT 1s):
    *   **Freestyle Project**: Just Freestyle it Baby, do as you please.
    *   **Pipeline Project**: For Workflow Projects
    *   **Multi-Configuration**: If you have Multi-Config setup, (Windows, Linux and $ MONEY $)
    *   **Folder**: Container to Store items in same Location
    *   **MultiBranch Pipeline**: For Multiple Repository Branches (Git, GitHub, BitBucket)
    *   **Organization Folder**: For Porject Subfolders in MultiBranch Repos

#   **PIPELINE**
*   Pipelines are **JOBS** that make use of the **Pipeline Plugin**.
*

#   **Main GUI**
*   Used for **CREATING** and **CONFIGURING** Jobs
*   Create a Job: Self Explainitory (spellcheck)
*   Set Distributed Build: Set up other Jnekins Server.
