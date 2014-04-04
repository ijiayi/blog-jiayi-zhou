Title: Git and GitHub flow quickstart
Category:
Tags: git, github, guide, quickstart
Status: draft

[TOC]

This article describes the GitHub flow using shared repository.

The pull request is used for review processing.

# Tools

## Atlassian SourceTree

<http://www.sourcetreeapp.com/>


# Clone repository

```sh
git clone http://192.168.73.211/ivanji/hello-git.git
```

![]({filename}/images/2014-04-01-git-quickstart-repository-path.png)

# Configure username and email address

### Use global config

```sh
git config --global user.name "Jiayi Zhou"
git config --global user.email "jiayizhou@domain.com"
```

### Use repository config

```sh
git config user.name "Jiayi Zhou"
git config user.email "jiayizhou@domain.com"
```


# Create new branch for developing new feature

```sh
git checkout master
git checkout -b feature1
```

# Edit and commit the changes

```sh
git add <edited files>
git commit
```

# GitHub flow

![]({filename}/images/2014-04-01-git-quickstart-github-flow.png)

1. Create a branch from `master` for developing new feature.

    ```sh
    git checkout master
    git checkout -b awesome-feature
    ```

1. Create, edit, rename, move, or delete files.

    ![Git file lifecycle]({filename}/images/2014-04-01-git-quickstart-git-file-lifecycle.jpeg)

    ```sh
    git add <edited files>
    git commit
    ```

1. Push the feature branch to the remote repository.

    ```sh
    git push origin awesome-feature
    ```

1. Send a pull request from your branch with your changes to kick off a discussion.


1. Make changes on your branch as needed. Your pull request will update automatically.

    ```sh
    git push origin awesome-feature
    ```

1. Ask partners to merge the pull request, once the branch is ready to go, using the big green button.


1. Tidy up your branches using the delete button in the pull request or on the branches page.


# Reference

1. [GitHub Flow in the Browser · GitHub Help](https://help.github.com/articles/github-flow-in-the-browser)
1. [Understanding the GitHub Flow · GitHub Guides](https://guides.github.com/overviews/flow/)
1. [GitHub Flow – Scott Chacon](http://scottchacon.com/2011/08/31/github-flow.html)


