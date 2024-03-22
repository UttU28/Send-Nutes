# Project README

## Author
- **Name:** Utsav Chaudhary
- **Name:** UttU28
- **Email:** [utsavmaan28@gmail.com](mailto:utsavmaan28@gmail.com)

Recipe for deploying **Infrastructure as Code**
1. Create a **RESOURCE GROUP**
2. Create a **VIRTUAL NETWORK**
3. Create a **PUBLIC IP ADDR**
4. Create a **NETWORK INTERFACE** with *PUBLIC IP*
5. Create a **VIRTUAL MACHINE** with *NETWORK INTERFACE*

# **Infrastructure as Code (IaC)**
* Write down what you wanna deploy instead of clicking it. ***AUTOMATION BAYYYY***
* Codification makes tracking everything easy. Version Control, Collaboration is possible.
* Less human intervention means less errors.
* Declarative Coding Language.

# **Why TERRAFORM?**
* Automate Software Defined Networking.
* Interacts and takes care of communication with control layer APIs with ease.
* Supports a vast array of **Public** and **Private** cloud vendors.
* Tracks **State** of each resource deployed.

# **TERRAFORM WORKFLOW**

```
WRITE ---> PLAN ---> APPLY
```
---
# **TERRAFORM KEY CONCEPTS**
## ***PLAN*** **|** ***APPLY*** **|** ***DESTROY***
---

## **Terraform PLAN**
* Reads the code and creates a **PLAN** if EXECUTION / DEPLOYMENT.
* Doesn't deploy anything. Justr a **READ-ONLY** command.
* Allows review of action plan before executing anything.
* Authentication Credentials are used to connect your Infrastructure, ***IF REQUIRED***

## **Terraform APPLY**
* Deploys the code.
* It tracks all the resources and then stores the data inside the **STATE FILE** *(STate Tracking Mechanism File)*

## **Terraform DESTROY**
* **USE WITH *! i !* CAUTION *! i !* , NON REVERSIBLE**
* Looks at the records from the **STATE FILE** and deletes everything.

# **Terraform PROVIDERS**
*  Providers are plugins that enable the management of resources in a specific cloud or infrastructure platform.
*  Providers are usually found in **TERRAFORM PROVIDER REGISTERY** ***(PUBLIC)***
*  Providers serve as the bridge between Terraform and the API of the underlying platform, allowing Terraform to create, update, and delete resources in a consistent and reproducible manner.
*  Aukaat hai to khud ka likh le... (**AUKAAT** is important)

# **Terraform STATE**
*  It is a **JSON** file containing all the metadata of all the resources deployed. The file name is **TERRAFORM.TFSTATE**
*  It is a map file of **Terraform Configuration** and **Managed Infrastructure**
*  Prior to any **Modification** operation, Terraform refreshes the state file.
*  Resource dependency metadata is also tracked via the State File.
*  Kuch bhe Khona, par ye file mat khona mere dost.

# **Terraform PROVISIONERS**
*  Provisioners are used to perform additional tasks on a resource after it's created or destroyed.
*  Typically used to configure or set up software on instances, perform post-deployment tasks, or execute custom scripts.
* Types of **Provisioner**:
 * Local-exec Provisioner
 * Remote-exec Provisioner
 * File Provisioner
 * Ansible Provisioner
 * Chef Provisioner

# **Terraform STATE Storage**

*  LOCALLY
    *  Saves State Locally by Default.
    *  Only for you :)
*  REMOTE
    *  Saves in Remote (AWS S3, Google Storage, et...c)
    *  Sab ko help karega tera bhai, its shared between teams so anyone can see and write depending on the permissions.

*  ***STate Locking***: Once you do ```terraform apply``` then the state is automatically locked, so no **parallel/multiple/redundant** executuion. (Default in Local)
*  Enables Sharing of **OUTPUT** values with other Terraform Configurtion or Code. (After Successful creation of the Resources, my team can access the IP and other details of the Resource, for furhter use)

# **Terraform MODULES**
*  Module is a **Container** for multiple resources that are used together.
*  Every configuration has one module called **ROOT**, which consists of code files in main Directory.
*  Can be downloaded or referenced from
    * **Terraform Public Registry**
    * **A Private Registery**
    * **Local System**
*  Modules can take **INPUT** and provide **OUTPUTS** to plug back into the main code.


module "myModuleName" {
    source = "./modules/vpc"
    version = "0.0.5"
    region = var.region             # Input Parametters for the Modules.
}

# Other Allowed Parameters: count, for_each, providers, depends_on

# **Built-In Functions**
*  Terraform has **Built-In**, **Pre Defined** functions.
*  No **USER-DEFINED** functinos are allowed.
*

# **Variable TYPE CONSTRAINTS**
*  **COLLECTIONS**: Just one primitive type of value throughout.
    *  list(type)
    *  map(type)
    *  set(type)

*  **STRUCTURAL**: Different primitive types of data can be stored.
    *  object(type)
    *  tuple(type)
    *  set(type)

*  ***ANY***: Just write it and I'll figure the **data type** on the runtime of the application.

# **Terraform CLOUD**
*   You can save all your **STATE** files in the **Cloud**, it'll be encrypted and will be safe as all the **Credentials** might be stored in it.
