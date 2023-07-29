### What is Git?
#### Git is a version control system that allows you to track changes to files over time. It is used by programmers to keep track of all the changes they make to their code. Git is a distributed version control system, which means that the entire codebase and history is available on every developer's computer, which allows for easy branching and merging.

![1](./images/1.png)

> __NOTE:__  befor to install git we need to configure our git account.

----

### Git vs GitHub: What's the Difference?
#### Git is a version control system that lets you manage and keep track of your source code history. GitHub is a cloud-based hosting service that lets you manage Git repositories. If you have open-source projects that use Git, then GitHub is designed to help you better manage them.


---- 

### To install git on linux:
```bash
sudo apt-get install git
```

> __NOTE:__
- sudo: run as root (adminstrator)
- apt-get: package manager
- install: install a package
- git: the package to install

---- 

### To configure git:
```bash
git config --global user.name "your name"
git config --global user.email "your email"
```

---- 

### To check the configuration:
```bash
git config --list
```
----

### What is Repository?
#### A repository is a storage space where your project lives. It can be local to a folder on your computer, or it can be a storage space on GitHub or another online host. You can keep code files, text files, image files, you name it, inside a repository.

> __NOTES:__ 
> - #### Any changes in one repository then the other repository will not be affected.
> - #### we can not create a repository inside another repository, because it will be a sub-repository. that is mean any changes in the parent repository will affect the sub-repository.
> - #### each repo has a Log file that contains all the changes that have been made to the repo.

![2](./images/2.png)


---- 

### To create a repository:
```bash
git init
```
#### then i get hidden folder called .git 

![3](./images/3.png)

--- 

### To check the status of the repository:
```bash
git status
```
---

### To add files to the staging area:
```bash
git add <file name>
```
### To add all files by using:
```bash
git add .
```

### To add multiple files:
```bash
git add <file name> <file name> <file name>
```

![4](./images/4.png)
---

### what is the meaning of commit?
#### A commit is an operation which sends the latest changes of the source code to the repository, making these changes part of the head revision of the repository. A commit is done on a single local repository, and it is not visible to other users unless the commit is pushed to the central repository.

### To commit the changes:
```bash
git commit -m "your message"
```

--- 

### To create file: 
```bash
touch <file name>
```

--- 

### To check the log:
```bash
git log
```
#### you got the log file that contains all the changes that have been made to the repo.

### To get the log in one line. 
 ```bash 
 git log --oneline 
 ``` 

> __NOTE:__ we can not to delete the commit because it is a history of the repo.

---

### Ameding commit for  the last commit:
```bash
git commit --amend 
```
#### Ameding the last commit is useful if you forgot to add some files, or you messaged up the commit message. then the last commit will be replaced by the new commit. and the last commit will be the new commit. 

---

### .gitignore file:
![5](./images/5.png)

#### .gitignore file is a file that contains all the files that we do not want to add to the repo.

![6](./images/6.png)


### To add .gitignore file:
```bash
touch .gitignore
``` 
#### Then we add the files  inside the .gitignore file that we do not want to add to the repo. Then we add the .gitignore file to the staging area and commit the changes.

---