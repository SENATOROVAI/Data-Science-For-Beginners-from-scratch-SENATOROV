"""Answers to questions about working with GitHub Issues."""

# # GitHub Issues
#
# ## General questions
#
# ### Question 1. What are Issues on GitHub and what are they used for?
#
# Answer: Issues are GitHub's built-in tracking system for tasks, bugs, and feature
# requests. They let a team organize, discuss, assign, and prioritize work
# directly next to the code.
#
# ### Question 2. How do Issues differ from other task management tools?
#
# Answer: Issues are tightly integrated with the repository: they can be linked to
# commits, branches, and pull requests, closed automatically by keywords in
# commit messages, and referenced from code reviews. External tools (Jira,
# Trello) are more feature-rich but live outside the codebase.
#
# ### Question 3. What are the main components (fields) of each Issue?
#
# Answer: Title, description, comments, assignees, labels, milestone, projects,
# linked pull requests, and status (open/closed).

# ## Creating Issues
#
# ### Question 4. How to create a new Issue in a repository?
#
# Answer: Open the **Issues** tab -> click **New issue** -> fill in the title and
# description -> **Submit new issue**.
#
# ### Question 5. What data is recommended in the Issue description?
#
# Answer: A clear description of the problem or task, steps to reproduce (for bugs),
# expected vs. actual behavior, screenshots or logs, and environment details.
#
# ### Question 6. What labels can be added? Which are standard?
#
# Answer: Any custom labels can be created. Default ones: `bug`, `documentation`,
# `duplicate`, `enhancement`, `good first issue`, `help wanted`, `invalid`,
# `question`, `wontfix`.
#
# ### Question 7. How to assign Assignees to an Issue?
#
# Answer: In the right sidebar of the issue, click **Assignees** and pick one or
# more users (up to 10).

# ## Working with Issues
#
# ### Question 8. How to use Labels to classify tasks?
#
# Answer: Apply labels for type (`bug`, `enhancement`), priority, or status. Labels
# make filtering and searching issues fast and consistent.
#
# ### Question 9. What is a Milestone and how to link it to an Issue?
#
# Answer: A milestone groups issues toward a goal (release, sprint). Select it in
# the **Milestone** field of the issue sidebar.
#
# ### Question 10. How to link an Issue to a Pull Request?
#
# Answer: Reference the issue in the PR description (`Closes #5` or the full URL for
# cross-repo links), or use the **Development** section in the sidebar.
#
# ### Question 11. How to add a comment to an existing Issue?
#
# Answer: Scroll to the comment box at the bottom of the issue page, write the
# comment, and click **Comment**.

# ## Closing and completing Issues
#
# ### Question 12. How to close an Issue manually?
#
# Answer: Click **Close issue** at the bottom of the issue page.
#
# ### Question 13. Can an Issue be closed automatically from a commit or PR?
#
# Answer: Yes. Add a keyword with the issue number to the commit message or PR
# description: `Closes #2`, `Fixes #2`, `Resolves #2`. The issue closes
# when the commit/PR is merged into the default branch. For issues in
# another repository, the full URL is required:
# `Closes https://github.com/OWNER/REPO/issues/2`.
#
# ### Question 14. How to reopen a closed Issue?
#
# Answer: Open the closed issue and click **Reopen issue**.

# ## Filtering and search
#
# ### Question 15. How to find all open or closed Issues?
#
# Answer: Use the filter bar on the Issues tab: `is:issue is:open` or
# `is:issue is:closed`.
#
# ### Question 16. How to filter Issues by labels, assignees, or other criteria?
#
# Answer: Use search qualifiers: `label:bug`, `assignee:username`,
# `author:username`, `milestone:"v1.0"` - or the dropdown filters above
# the issue list.
#
# ### Question 17. How to sort Issues?
#
# Answer: Use the **Sort** dropdown: newest, oldest, most commented, least
# commented, recently updated, reactions.

# ## Integrations and automation
#
# ### Question 18. How to set up notifications for Issues?
#
# Answer: **Watch** the repository (all activity or custom -> issues), or subscribe
# to a single issue via the **Subscribe** button. Notification delivery is
# configured in personal settings.
#
# ### Question 19. What are Projects and how to link them with Issues?
#
# Answer: Projects are kanban-style boards/tables for planning. An issue is added
# to a project from the **Projects** field in its sidebar, then moves
# through columns (Todo -> In Progress -> Done).
#
# ### Question 20. What third-party tools can automate work with Issues?
#
# Answer: GitHub Actions, bots (Dependabot, Stale bot), webhooks that trigger
# external services, and integrations like Zapier or Slack.

# ## Collaboration
#
# ### Question 21. How to mention another user in a comment?
#
# Answer: Type `@username` - the user gets a notification.
#
# ### Question 22. How to request additional information from the Issue author?
#
# Answer: Comment with a question mentioning the author (`@author`), and optionally
# add a label like `question` or `needs more info`.
#
# ### Question 23. What to do if an Issue is irrelevant or duplicates another one?
#
# Answer: Close it with a comment explaining why; for duplicates, write
# `Duplicate of #N` so GitHub marks the relationship.

# ## Practical aspects
#
# ### Question 24. How to use templates for creating Issues?
#
# Answer: Add template files to `.github/ISSUE_TEMPLATE/` in the repository. When
# users create a new issue, GitHub offers the templates as forms.
#
# ### Question 25. What are Linked Issues and how to create links between tasks?
#
# Answer: Linked issues/PRs show relationships. Reference another issue by `#number`
# (same repo) or full URL (cross-repo), or use the **Development** section
# to link a PR that closes the issue.
#
# ### Question 26. What metrics can be tracked using Issues?
#
# Answer: Number of open/closed issues over time, time to close, time to first
# response, and per-assignee throughput (via Insights or external tools).
#
# ### Question 27. What best practices are recommended when working with Issues in a team?
#
# Answer: Write descriptive titles, use labels consistently, assign responsibility
# early, keep one topic per issue, link issues to PRs, and close resolved
# issues promptly.
