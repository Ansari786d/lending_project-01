# Scenario 1
# We are starting a project from github repository 

# Step 1
# 1. git clone https://github.com/Ansari786d/Glassdore-Scrapper-Using-Selenium.git

# any folder which is get tracked by git will have a .git folder
# orgin/main (github code)

#1. make changes to existing files / added new files(unstaged)
#2. we have to stage the changes (staged)
#3. we can commit all the staged changes 


# git add . (to stage all the files in currrent diretory) or give a specific file name 
# git commit -m "my messages" (to commit it) (here our code is tracked locally)
# git push origin main  (to push the new changed code into my github repo on main branch)

# scenario 2 we are starting a poject from local 

# 1.git init means we want git to track all the changes on this repository or folder going forward 

# When we clone a remote project the origin is referring to that.

# but when we start developing project on local we need to set the origin 

# to do this we have a command 
# git remote add origin my_repo_url meaning my origin to this remote(github repo)

# to know where our origin point we can check by

# git remote -v 

# git branch  -- it will tell o which branch we are working 

# if you are getting your branch as master you need to changed it to main in order to push the code to github otherise it 
# will throw error (in github it has named "mian")

# to rename 
# git branch -M main (whatever branch we are in will named as main)

