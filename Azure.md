# Project README

## Author
- **Name:** Utsav Chaudhary
- **Name:** UttU28
- **Email:** [utsavmaan28@gmail.com](mailto:utsavmaan28@gmail.com)


https://learn.microsoft.com/en-us/azure/well-architected/service-guides/?product=popular

https://readme.so/editor

# **AZURE CORE ARCHITECTURE COMPONENTS**
-   ## **Physical Infrastructure** :
    
    ```
    Data Center ---> Availability Zone ---> Region ---> Geography
    ```
    
    -   Use Availability Zones to protect from **FAILURE**
    -   Increase availability by **CO-LOCATING** ```Compute, Network, Storage, Data ``` within the *Availability Zones* and **REPLICATING** it in other *Availability Zones*
    -   A **Data Center** is a ***Physical Facility*** housing computing infrastructure, located within an **Availability Zone (AZ)** within a **Region**, which in turn belongs to a specific **Geographic Location**.

    ### Services that **Supports** Availability Zones are:
    -   **Zonal Services**: Pin resources to **Specific Zone**
        ```VM, Managed Disk, IP Addr```

    -   **Zone Redundant Services**:    The platform **Replicates Automatically** according to the Zones.
        ```Zone Redundant Storage, SQL Database```

    -   **Non Regional Services**:  Set in other **Geographies**, you'll face **HIGH Latency** but ***USEFUL***
    -   **WHAT IF?**: ```Large event impacts multiple AZone in a Region??``` **--->** ***REGION PAIRS***

-   ## **Management Infrastructure**
    -   **Resources and Resource Groups**:
        -   Anything you **Create, Provision, Deploy** is a Resource.
    -   **Subscriptions**:
        -   Allows you to organize your **Resource Groups**.
        -   **Single Subscription**:
            -   Single Billing Mode, Single Access Managememnt Policy
        -   **Multiple Subscription**:
            -   Multiple Billing Mode, Multiple Access Managememnt Policy
    -   **Managememnt Groups**:
        -   Manages Everything.
        -   **Rules applied to MGroup** is applied to all the **Resources / Resource Groups**.
    -   Use **RBAC** - ***Rule Based Access Control*** for assigining **PERMISSIONS**

# **Computing Options**

## **Virtual Machines (VMs)**
-   Provides **Infrasructure as a Code (IaaC)**
-   Needs **Configuration, Updation and Management** if VM.
-   Group of VMs can be Managed using:
    -   **VM Scale Set (VMSS)**:
        -   Automate, Manage, Configure & Update multiple VM.
        -   Automatically applies Load Balancer.
        -   Scaling Scheduler for Horizontal Scaling and Dynamic Workload.
        -   Suited for **STATELESS**

    -   **VM Availability Set**:
        -   Ensures **High Availability** and **Fault Tolerance** by distributing VM instances across fault and update domains within an Azure data center.
        -   Uses Fault Domain (Same Data Center but different RIGS) and Update Domain (Group of Domains that needs to be updated together)
        -   Suited for **STATEFUL**

-   ### **Azure VM Image Builder**
    -   Automate the ***Creation, Customization and Distribution of VM***.
    -   Can use the image in ***Azure*** and other ***Cloud Platforms***
    -   Can use the image for ***VM, VMSS, Other Cloud Services***
    -   Allows ***Customization and Control*** over ***OS, VM, Environments***.
    -   Integrate with ***Azure DevOps*** and other ***CI / CD pipeline***

-   ### **Azure Dedicated Hosts**
    -   Provides Dedicated Host for your Organization.
    -   Hardware of **Your CHOICE**
    -   Doesnt share **Hardware resources**.
    -   ***Isolation*** at **Physical Level**
    -   Service Supported by: ***Virtual Machines, Azure Virtual Machine Scale Set, Azure Kuberneted Service, Azure App Service***

-   ### **Azure Spot Virtual Machines**
    -   Access to unused ***Azure Compute Capacity***.
    -   Good for **Batch Processing, Dev/Test Environments**.
    -   **Interruption** with **30s Timer**.
    -   Service Supported by: ***Virtual Machines, Batch, Kubernetes, Functions, VMSS***

-   ### **SQL Server on Azure Virtual Machines (VMs)**
    -   It's a SQL server hosted on a Virtual Machine
    -   Provides more **flexibility and control** but requires users to **manage infrastructure**.

## **Containers**
-   Lightweight alternative of VM if you dont want anything to do with OS.
-   Run **Multiple Containers** on a single instance of **Physical / Virtual Host**
-   **No Management of OS** is required
-   Quick **Restart** on **FAILURE**
-   **Container Services**:
    -   ### **Container Group**:
        -   **Collection of containers** that get scheduled on the **same host machine**.
        -   The **Containers** in a **Container Group** share a **lifecycle, resources, local network, and storage volume**s.
    -   ### **Azure Container Instances**:
        -   Simplest and Fastest way to run a **Container**.
        -   Ideal for **Batch Processing, Dev/Test environments, or running Microservices** that don't require orchestration.
        -   **PaaS** Service
    -   ### **Azure Container Apps**:
        -   Similar to **Azure Container Instances** but offers more **Control, Scalability and Management**
        -   **BUILT IN**:
            -   Managing Lifeycle of Containerised Apps
            -   Deployment
            -   Scaling
            -   Monitoring
            -   CI / CD Pipeline
    -   ### **Azure Kubernetes Services**:
        -   It is used for **Orchestrating Containerised Application** including:
            -   Automatic Scaling
            -   Rolling Updates
            -   Load Balancing
        -   Offers more **Control and Flexibility** compared to above, but requires more **MANAGEMENT**
        -   Suitable for complex applications with high availability, scalability, and production-grade requirements.

## **Azure Functions Service**:
-   Infrastructure is just **MUAHHHHH**, ready for Everything.
-   **Hard timeout** keep that in mind.
-   Just focus on the code and everything rest is taken care by the Functions
-   **Event Driven** can be triggered by various events like **HTTP requests, Database changes, Service Bus Messages**, many more.
-   **Integrated Security** with ***Azure Active Directory*** for **Authentication** and **Authorization**

## **Azure Batch Service**
-   It's a Cloud-Scale **Job Scheduling and Compute Management** service in Azure that enables you to run **large-scale parallel and high-performance computing (HPC)** workloads efficiently.
-   **Key Features**:
    -   **Automatic Scaling**
    -   **Task Prioritization & Resource Allocation**
    -   **Job Scheduling**
    -   **Task Parallelism** is breaking down a large batch jobs into smaller jobs and run them parallelly.

## **Azure App Service**
-   Allows Management, Deploying and Developing of Web Apps and APIs.
-   Supports framework such as Python, Java, NodeJS, ASP.NET
-   Provides **BUILT-IN** support for **Scaling, Load Balancing and High Availability**

## **Azure Logic Apps**
-   Automate Workflows and Integrate Applications, Data and Services ***WITHOUT CODE***.
-   Many **CONNECTORS** are available for Azure Services and APIs.
-   **TRIGGERS** are events that start logic apps, can be ***HTTP, Email, Message, File Change***
-   Provides **Montoring and Analytics** service.

# **Azure Storage Redundancy**
-   **LRS (Locally Redundant Storage)**:
    -   **Data Replication** 3 times within **same Data Center**
-   **ZRS(Zone-redundant Storage)** :
    -   Data is **replicated synchronously** across multiple **Availability Zones** within the **same region**.
-   **GRS(Geo-redundant Storage)** :
    -   Data is **replicated asynchronously** to a **secondary region** located hundreds of miles away from the **primary region**.
    -   During a **regional outage or failover**, data access is **not available** in the secondary region until **failover completes**.
-   **GZRS(Geo-zone-redundant Storage)** :
    -   Data is **replicated** accross multiple **AZones** and **asynchronously** to **Secondary Storage**
-   **RA-GRS(Read-access Geo-redundant Storage)** :
    -   Similar to GRS but provides **read access** to data in the **secondary region** even in the case of a **primary region outage**.
-   **RA-GZRS(Read-access Geo-zone-redundant Storage)** :  
    -   Provides read access to data in both the **secondary region** and across **multiple Availability Zones** within the **Primary region**.

# Definitions

### **Availability Zones**
-   Physically seperated **1 or More Data Centers**.
-   If 1 goes down, another one continues.
-   Connected by **Fiber Optics**.

### **Regions**
-   Atleast **1 or Many** Data Centers in an **AZone**
-   Nearby or Same area
-   **Low Latency** Connection b/w them

### **Region Pairs**
-   **What If**: ```Large event impacts multiple AZone in a Region?? ``` ---> **REGION PAIRS**
-   300 Miles Away
-   Allows **Replication of Resources** across Geographies.
-   Serves automatically to **Fail Overs** to other region in the **Piar**
-   Eg.:
    ``` West US <---> East US ```
    ``` South East Asia <---> East Asia ```
-   **ADVANTAGES**:
    -   During Extensive Outage, it's **Priority** to make sure if **1 is restored quickly**.
    -   Planned Updates **1 at a Time**.
    -   Data is **LAWFULLY** safe in 1 **Geography**


### **Resource**:
-   Anything you **Create, Provision, Deploy** is a Resource.
-   Grouping of multiple **Resources** is called **Resource Groups**
-   ```1 Group --> Many Resources```
-   ```1 Resource --> 1 Group```
-   **NO** nesting of Groups.

### **Resource Groups**
-   Group of Resources.
-   No need to thank me!
