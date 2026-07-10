"""Answers about STASH."""

# ### Question 1: What does the `git stash` command do?
#
# Answer: `git stash` temporarily saves all uncommitted changes (staged and unstaged) and reverts the working directory to a clean state matching the last commit. This lets me switch context without committing unfinished work.

# ### Question 2: How do you view the list of all saved stashes?
#
# Answer:  `git stash list` displays all saved stashes with indexes like `stash@{0}`, `stash@{1}`, etc.

# ### Question 3. Which command is used to apply the top stash?
#
# Answer: `git stash apply` applies the most recent stash (`stash@{0}`). Alternatively, `git stash pop` applies it and removes it from the list.

# ### Question 4. How do you apply a specific stash by its number?
#
# Answer: I use `git stash apply stash@{n}`, by replacing `n` with the stash number. Example: `git stash apply stash@{2}`.

# ### Question 5. Difference between `git stash apply` and `git stash pop`?
#
# Answer: `git stash apply` applies the changes but keeps the stash in the list. `git stash pop` applies the changes and then removes the stash from the list.

# ### Question 6. What does `git stash drop` do?
#
# Answer: `git stash drop stash@{n}` deletes a specific stash without applying it. Without an argument, it drops the most recent stash.

# ### Question 7. How do you completely clear all saved stashes?
#
# Answer: Command `git stash clear`. This permanently removes all stashes.

# ### Question 8. When is it convenient to use `git stash`?
#
# Answer: For switching branches or pull updates without committing unfinished work. If I want a temporarily clean working directory, or when I started work on the wrong branch.

# ### Question 9. What happens if `git stash pop` hits conflicting changes?
#
# Answer: Git applies the stash and reports a merge conflict that I must resolve manually. Because of the conflict, the stash is **not** dropped from the list, so I will not lose it.

# ### Question 10. Can you restore a stash after `git stash drop`?
#
# Answer: Not directly. It may sometimes be recovered via the reflog using `git fsck --unreachable` to find the dropped stash's commit hash, then `git stash apply <hash>` - but there's no guarantee before garbage collection.

# ### Question 11. What does `git stash save "NAME_STASH"` do?
#
# Answer: Saves current changes to a stash with a custom name for easy identification. Note: `git stash save` is deprecated in favor of `git stash push -m "NAME_STASH"`.

# ### Question 12. What does `git stash apply "NUMBER_STASH"` do?
#
# Answer: Applies the stash at the specified index (e.g. `git stash apply stash@{1}`), keeping it in the list.

# ## Question 13. What does `git stash pop "NUMBER_STASH"` do?
#
# Answer: Applies the stash at the specified index and then removes it from the list.

# ### Question 14. Save current changes to a stash named "SENATOROV ver1"
# git stash push -m "SENATOROV ver1"
#
# <img src="./images/stash_ver1.png" alt="SENATOROV ver1" width="700">

# ### Question 15. Make any changes to your repository and save a second stash under the name "SENATOROV ver2"
# git stash push -m "SENATOROV ver2"
# git stash list
#
# <img src="./images/stash_ver2.png" alt="SENATOROV ver2" width="700">

# ### Question 16. Restore your stash "SENATOROV ver1", insert a screenshot from the terminal
# git stash apply "stash@{1}"
#
# <img src="./images/stash_ver3.png" alt="SENATOROV ver1" width="700">

# ### Question 17. Delete all stashes from history, insert a screenshot from the terminal
# git stash clear
# git stash list
#
# <img src="./images/stash_ver4.png" alt="Clear" width="700">
