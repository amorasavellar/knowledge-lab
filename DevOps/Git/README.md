## What is Git?

Is a distributed version control system, primarily used in software development, but can be used to record the edit history of any type of file.

## Inicial Git Config

Check your git credentials
```bash
$ git config --global list
```

Set your user.email
```bash
$ git config --global user.email "youremail@exemple.com"
```
Set your user.name
```bash
$ git config --global user.name "YOUR USER NAME"
```

Start git on my directory
```bash
$ git init
```

## Simple Git Commands Glue

Get git status
```bash
$ git status
```

Add all changes to staged area
```bash
$ git add .
```

Add specific changes to staged area
```bash
$ git add <file_name.file_extension>
```

Remove specific changes from staged area
```bash
$ git rm --cached <file_name.file_extension>
```

Add commit (saving changes on git)
```bash
$ git commit -m "Commit Text"
```

Rewrite last message commit
```bash
$ git commit --amend "Commit Text Edited"
```

Get changes log
```bash
$ git log
```

Resturn the last version commited from specific file
```bash
$ git restore <file_name.file_extension>
```

View a specific hash from branch
```bash
$ git checkout <hash_id>
```

List branchs
```bash
$ git branch
```

Select a specific branch
```bash
$ git checkout <branch_name>
```

Create a new branch
```bash
$ git checkout -b <new_branch_name>
```

View gitgraph
```bash
$ git log --oneline --graph --all
```