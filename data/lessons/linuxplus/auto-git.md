# Version Control with Git

Scripts, configuration files and Infrastructure as Code all belong under version
control, and **Git** is the universal choice. Git records the history of a project
so you can see what changed, roll back mistakes, and collaborate without
overwriting each other. This lesson covers the day-to-day Git an administrator
needs.

## What Git is

Git is a **distributed** version control system: every clone is a *complete* copy
of the project and its entire history, not just a checkout of the latest version.
You can commit, branch and view history fully offline, then sync with others when
convenient. This is the key contrast with older *centralized* systems, where the
history lives only on a central server.

## The three areas

Git's mental model has three places a file can be, and the commands move files
between them:

| Area | What it holds |
|------|---------------|
| **Working directory** | Your actual files, where you edit |
| **Staging area (index)** | Changes marked to go into the next commit |
| **Repository** (`.git`) | The committed, permanent history |

The flow is: edit a file (it becomes *modified*) → `git add` it (now *staged*) →
`git commit` it (now saved in history). A commit is a labeled snapshot with an
author, timestamp and message.

## First-time setup and starting a repo

Git needs to know who you are before your first commit:

```
$ git config --global user.name  "Jordan Lee"
$ git config --global user.email "jordan@example.com"
```

Start tracking a project in one of two ways:

```
$ git init                    # turn the current directory into a new repo
$ git clone https://example.com/infra.git   # copy an existing remote repo
```

## The everyday cycle

```
$ git status                  # what's modified, staged, untracked
$ git add deploy.sh           # stage one file (git add . stages everything)
$ git commit -m "Add deploy script"
$ git log --oneline           # browse history, newest first
$ git diff                    # unstaged changes vs. the last commit
```

> `git add` and `git commit` are **two deliberate steps**. Staging lets you craft
> a commit from exactly the changes that belong together, even if you've edited
> several files. Nothing enters history until you commit.

**`HEAD`** is a pointer to the commit you're currently on — usually the tip of
your current branch.

## Branching and merging

A **branch** is an independent line of development, so you can build a feature
without disturbing the stable `main` branch:

```
$ git branch feature-logs         # create a branch
$ git switch feature-logs         # move onto it (older syntax: git checkout)
$ # ...edit, add, commit on the branch...
$ git switch main
$ git merge feature-logs          # fold the branch's commits into main
```

If both branches changed the same lines, Git reports a **merge conflict** and
marks the clashing regions in the file with `<<<<<<<`, `=======` and `>>>>>>>`.
You edit the file to the desired result, remove the markers, `git add` it, and
commit to finish the merge.

## Working with remotes

A **remote** is another copy of the repo, typically on a shared server (GitHub,
GitLab, an internal host). The default remote is named **`origin`**.

```
$ git remote -v               # list configured remotes
$ git push origin main        # upload your commits to the remote
$ git pull origin main        # fetch remote commits AND merge them in
$ git fetch origin            # fetch remote commits WITHOUT merging
```

> `git fetch` only *downloads* new history; `git pull` is `fetch` **plus** a
> merge. When you want to inspect what changed on the server before integrating,
> fetch first.

## Ignoring files and undoing changes

A **`.gitignore`** file lists patterns Git should never track — build artifacts,
logs, secrets, `*.key`. Keeping these out of history avoids clutter and leaks.

To undo, in increasing severity:

- `git restore file` discards *uncommitted* changes in the working directory.
- `git reset` moves the branch pointer / unstages changes.
- `git revert <commit>` creates a *new* commit that undoes an old one — the safe
  choice for history that has already been pushed and shared.

## Exam focus

- Git is **distributed**: every clone has the full history and works offline. The
  default remote is **`origin`**.
- Know the **three areas**: working directory → staging area (**`git add`**) →
  repository (**`git commit`**). Adding and committing are separate steps; `git
  status` and `git diff` show where things stand.
- Start a repo with **`git init`** (new) or **`git clone`** (existing). Set
  identity first with `git config --global user.name/user.email`.
- Branch with `git branch`/`git switch` (or `git checkout`); combine lines of work
  with `git merge`; resolve a **merge conflict** by editing the marked regions,
  then `git add` and commit.
- **`git fetch`** downloads only; **`git pull`** = fetch **+ merge**; **`git
  push`** uploads your commits.
- `.gitignore` keeps files out of version control. To undo: `git restore`
  (working dir), `git reset` (unstage/move), `git revert` (new undo commit, safe
  for shared history).
