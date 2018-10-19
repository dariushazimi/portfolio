# Git command refences

## See list of ignored files
git ls-files . --ignored --exclude-standard --others

git log
git show
git ls-files  # list tracked files

to unstage changes, 
git reset HEAD filename
to revert back to last known good state, 
git checkout -- file

git log --oneline --graph --decorate --all

git config --global alias.hist "log --oneline --graph --decorate --all"


## check to see the config alias made it into the config

git config --global --list

git rm filename # to remove a file from git
git add -A # adds all files, covers all types of modification and make those
updates.

git add -u, # if 
## comparing changes git diff difftools

git diff hashNumber HEAD
git difftool hashNumber HEAD

git help diff


## Merge

## Fasforward 
Git applies all commits from other branches to Master as if there were no other
branches were there to begin with. Or as we never branched off to begin with.

we can disable fastforward branch

## Automatic
When git deletcts non conlifcting changes in the parent branch.
git is able to automatiallly resolve any conflicts.
In doing so the old branches timeline is preserved and a new merge commit is
created to show the merging of the two branches.

## Manual merge
Automatic merge is not possible
Conflicting merge state
chagnes saved in merge commmit


## 004 Special markers and head
Head is the last commit of the current branch
can be moved
You can also manually move the head. 

Use git difftool branchName HEAD to compare the changes

git checkout master
git merge updates
git branch -d branchName, the timeline is preserved.

## Ignore local changes and pull from master on github.
To update local system with changes from github
pull from github

```
git reset --hard && git clean -df
```
Added this line when in master branch
