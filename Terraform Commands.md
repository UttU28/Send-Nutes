* **Terraform INIT**
    -   -backend=false
* **Terraform PLAN**
    -   -out=path
    -   -json
    -   -destroy
* **Terraform APPLY**
    -   -var=
    -   -var_dir=
    -   -parallelism=10 (Default 10, can increase based on the **HARDWARE**)
    -   -input=false
    -   -target=
    -   -backup
    -   -out=path
    -   -state=path
    -   -state-out=path
* **Terraform DESTROY**
* **Terraform OUTPUT**
* **Terraform REFRESH**
* **Terraform VALIDATE**
* **Terraform FMT**
* **Terraform GET**
    -   -git
    -   -get-package-dir
* **Terraform IMPORT**
    -   terraform import azurerm_resource_manager.nameInCode resourceID
* **Terraform GRAPH**
    -   terraform graph >> graph.dot
    -   terraform graph | dot -Tpng >> graph.png
* **Terraform STATE**
    -   mv
    -   rm
    -   show stateFileName
* **Terraform SHOW**
* **Terraform WORKSPACE**
    -   new newName
    -   select newName
    -   list