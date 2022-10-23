# Commands for GitHub

#### Normal and miscellaneous commands.

| Commands                              | What it does                                                                                                      |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| git clone + "url of repository"       | Copies the repository that it is on Git Hub and puts it on where you are placed inside Git Bash.                  |
| git status                            | Its for knowing in wich branch are you placed, and wich files did you modify, comparing with the previous commit. |
| git pull                              | Updates your local repository with the changes that where made on the online repository.                          |
| git checkout -b "a name of your will" | Creates a Branch and moves you to that new branch.                                                                |
| git branch -d "branch"                | This will delete the branch you choose.                                                                           |
| git branch -a                         | Shows you all the branchs.                                                                                        |
| git reset --soft HEAD~1               | This rolls back your last commit but saves your changes.                                                          |
| git reset --hard HEAD~1               | This rolls back every change you made since the last commit.                                                      |
#
#### Pushing something to GitHub


|     | Commands                             | What it does                                                                                                                                         |
|-----|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1º  | git add "name of the file"           | 1º First step: Uploads from your computer to the online repository of git hub. (You can also use "git add ." to add all the modifications you made). | 
| 2º  | git commit -m + "a message you want" | 2º Second step: Settles the changes, and they become real. (if you want to go back you have to commit again).                                        |
| 3º  | git push origin "branch"             | 3º Third step: Pushes all the commits you made to the page online. ("origin" refers to the place you clone the commit Branch).                       |

