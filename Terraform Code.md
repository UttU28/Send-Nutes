# Project README

## Author
- **Name:** Utsav Chaudhary
- **Name:** UttU28
- **Email:** [utsavmaan28@gmail.com](mailto:utsavmaan28@gmail.com)


# **MAIN.TF**


provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "vm" {
  ami           = "DUMMY_VALUE_AMI_ID"
  subnet_id     = "DUMMY_VALUE_SUBNET_ID"
  instance_type = "t3.micro"
  tags = {
    Name = "my-first-tf-node"
  }
}

# **TERRAFORM INIT**
*  Initializing the working directory.
*  Downloads supporting or ancillary code (Providers), modules and plugins.
*  Sets **BACKEND** for ***Terraform State File***

## **TERRAFORM PLAN**
* Reads the code and creates a **PLAN** if EXECUTION / DEPLOYMENT.
* Doesn't deploy anything. Justr a **READ-ONLY** command.
* Allows review of action plan before executing anything.
* Authentication Credentials are used to connect your Infrastructure, ***IF REQUIRED***

## **TERRAFORM APPLY**
* Deploys the code.
* It tracks all the resources and then stores the data inside the **STATE FILE** *(STate Tracking Mechanism File)*

## **TERRAFORM DESTROY**
* **USE WITH *! i !* CAUTION *! i !* , NON REVERSIBLE**
* Looks at the records from the **STATE FILE** and deletes everything.

# **INSTALL TERRAFORM**
1. Download Manually and add the file to **PATH**
2. Setup Terraform Repo on Linux, Use package maanger to install it. For **LINUX ONLY**
```
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo yum -y install terraform
```

# **Terraform PROVIDERS**
*  Will always look at **TERRAFORM PROVIDER REGISTRY** *(Public)*.
*  Always mention the VERSION you wanna use.


provider "aws" {
    version = "L.0.L"
    region = "us-west-2"
}

# **VARIABLES**
*  Ab kya he batau
*  Referencing a variable in Terraform ```var.varName```
*  **terraform.tfvars** is where all the variables are stored for further usage.
*  **Sensetive** data can be hidden using ```sensetive = true```


variable "varName" {
    description = "My Test Variable"
    type = string
    default = "Hello"
    sensetive = true / false                    # If the data is Sensetive then do true, it'll hide those data.
}
# OR    OROR    OROR    OROR    OROR    OR
variable "varName" {}

## **VARIABLE VALUDATION**
*  Can add a condiiton to Validate the varialbe value.
*  Making some set of Rules for variable value to follow.


variable "varName" {
    description = "Why this kolaveri di??"
    type = string
    default = "WHYYY?"
    validation {
        condition = length(var.varName) > 4
        error_message = "The string should be more than 4 characters."
    }
}

*  **BASE TYPE**:
    * String
    * Number
    * Bool
* **COMPLEX TYPE**:
    * List
    * Map
    * Set
    * Object
    * Tuple


variable "example_string" {
  type    = string
  default = "Hello, Terraform!"
}

variable "example_number" {
  type    = number
  default = 42
}

variable "example_bool" {
  type    = bool
  default = true
}


variable "example_list" {
  type    = list(string)
  default = ["item1", "item2", "item3"]
}

variable "example_map" {
  type    = map(string)
  default = {
    key1 = "value1"
    key2 = "value2"
    key3 = "value3"
  }
}

variable "example_set" {
  type    = set(string)
  default = ["item1", "item2", "item3"]
}

variable "example_object" {
  type = map(string)
  default = {
    key1 = "value1"
    key2 = "value2"
    key3 = "value3"
  }
}

variable "example_tuple" {
  type    = tuple(string, number, bool)
  default = ("item1", 42, true)
}


# LIST OF OBJECTS
variable "whoAmI" {
    type = list(object({
        name = string
        age = number
        areYouFemale = bool
    }))

    default = [{
        name = Utsav
        age = 24
        areYouFemale = false
    }]
}

# **OUTPUT Variables**
*  Used for printing the Output of the variable values on the shell after running ***terraform apply***
*  These can be also called **Return Values**
*  Can output the value of other **Resources**


output "instanceIP" {
    description = "Current Private IP of the VM"
    value = aws_instance.vmName.private_ip
}

# **Terraform STATE**
*  Advanced State Mangement
*  Manually remove resources form the state file so its not managed by Terraform anymore.
*  List out tracked resources and their details.


terraform state list                                    # List out all resources tracked by Terraform State file.
terraform state rm sometingFromTheListAbove             # Delete a Resource from Terraform State fiel.
terraform state show sometingFromTheListAbove           # Show details of a resource tracked in the Sttae file.

# **Terraform FORMAT**
*   Formats code for readability.
*   Helps in keeping code, consistant.
*   Safe to run at anytime


terraform fmt

# **Terraform TAINT**
*   Forces a resource to be **DESTROYED** and **RECREATED**
*   Modifies the **State File**, other Resources might be affected by it.
*   Replace **Misbehaving Resources *FORCEFULLY***
*   Once marked Tainted, it'll destroy and recreate in next ```terraform apply``` command.


terraform taint resourceAddress
terraform taint aws_instance.my_instance

# **Terraform IMPORT**
*   Used to import existing infrastructure into Terraform's state.
*   Useful when you have resources that were created outside of Terraform, and you want to start managing them using Terraform.


terraform import [OPTIONS] ADDR ID
terraform import aws_instance.my_instance i-0c1234567890abcdef

# **Terraform WORKSPACES**
*   Workspaces are alternate **STATE FILES** within the same working directory.
*   It starts with a single workspace that is ***DEFAULT*** and cannot be deleted.
*   Terraform workspaces allow you to manage multiple instances of your infrastructure in a single Terraform configuration.
*   Each workspace has its own state file, allowing you to maintain separate sets of resources for development, testing, staging, and production environments.
*   USES:
    *   **Environment Isolation**: Can have seperate workspace for Testing, Staging, Production and Development
    *   **Parallel Deployment**: Enable you to deploy multiple instances of your infrastructure simultaneously without interference.
    *   **Configuration Overrides**: You can override specific variables or resources for different workspaces.


terraform workspace new workspaceName               # Creation
terraform workspace select workspaceName            # Selection



# main.tf
provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}

terraform workspace new dev
terraform workspace new prod

terraform workspace select dev
terraform apply -var 'aws_region=us-west-2'

terraform workspace select prod
terraform apply -var 'aws_region=us-east-1'

# **Terraform DEBUGGING**
*   Valid values for **TF_LOG** are ***TRACE, DEBUG, INFO, WARN, and ERROR***.
*   The **TF_LOG** environment variable controls the verbosity of the Terraform command-line output.
    *   ```TF_LOG=DEBUG terraform apply```
*   The **TF_LOG_PATH** environment variable allows you to specify a file where the logs will be written.
    *   ```TF_LOG=DEBUG TF_LOG_PATH=terraform.log terraform apply```


