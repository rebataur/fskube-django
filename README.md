### fsKube Kubernetes Django Kickstart Template

This is Django Kickstart Template, it has all the essential components and integration with your fsKube, AWS and Github built in, so your team can be productive.

Please read the below to understand the structure and worlflow of this project.

### Folder Structure

* .github/workflows
    * This folder houses all files related to github workflow, it is pre-integrated with your AWS and fsKube

* djangoproject
    * The core of this project this is where all your django related project artifact are stored.
* manifests
    * This folder houses all the YAML files for Kubernetes deployment.

### Branching Structure

* Feature Branch
    * This is where all developers pull and push their changes to. Once ready for release, this branch is merged into Master branch.
    * Whenever developer does a push into this branch a workflow is triggered automatically to create a container for your application and register in ECR with unique hash tag of the commit.
    

* Master Branch - This is the main deployable branch to QA and production.
    * Developers are not supposed to work on this branch
    * Releases cut from this branch is deployed into QA and upon approval, the same release is deployed into production.
    
### Local Kubernetes Testing

You can locally test this application by running it as standard Django application or using skaffold tool.
Just cd into the directory and run the following command

```
skaffold dev
```