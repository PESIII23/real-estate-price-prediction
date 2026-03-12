# Git Reference Guide

A quick reference for managing commits, branches, and code versioning.

---

## 1. Initial Setup

```bash
# Initialize a new repository
git init

# Set user identity (per-project)
git config user.name "Your Name"
git config user.email "you@example.com"

# Set default branch name
git config init.defaultBranch main
```

## 2. Staging & Committing

```bash
# Check status of working directory
git status

# Stage specific files
git add <file>

# Stage all changes
git add .

# Unstage a file (keep changes in working directory)
git restore --staged <file>

# Commit staged changes
git commit -m "short descriptive message"

# Amend the last commit (before pushing)
git commit --amend -m "updated message"
```

## 3. Commit Message Conventions

Use a consistent prefix for each commit:

| Prefix       | Use Case                                |
|--------------|-----------------------------------------|
| `feat:`      | New feature                             |
| `fix:`       | Bug fix                                 |
| `refactor:`  | Code restructuring (no behavior change) |
| `docs:`      | Documentation only                      |
| `style:`     | Formatting, whitespace, linting         |
| `test:`      | Adding or updating tests                |
| `chore:`     | Build scripts, dependencies, config     |
| `data:`      | Data pipeline or dataset changes        |
| `notebook:`  | Notebook additions or updates           |

**Examples:**

```
feat: add feature engineering for square footage
fix: handle missing values in price column
docs: update README with setup instructions
chore: add pandas to requirements.txt
```

## 4. Branching

```bash
# List all branches
git branch

# Create a new branch
git branch <branch-name>

# Switch to a branch
git switch <branch-name>

# Create and switch in one step
git switch -c <branch-name>

# Delete a branch (after merging)
git branch -d <branch-name>

# Force delete an unmerged branch
git branch -D <branch-name>
```

### Branch Naming Conventions

```
main              # Production-ready code
dev               # Active development
feat/<name>       # Feature branches      (e.g., feat/add-model-training)
fix/<name>        # Bug fix branches       (e.g., fix/null-price-handling)
data/<name>       # Data pipeline work     (e.g., data/add-raw-housing-csv)
notebook/<name>   # Notebook experiments   (e.g., notebook/eda-price-dist)
```

## 5. Merging

```bash
# Merge a branch into current branch
git merge <branch-name>

# Merge with no fast-forward (preserves branch history)
git merge --no-ff <branch-name>

# Abort a merge in progress
git merge --abort
```

## 6. Viewing History

```bash
# Compact log (one line per commit)
git log --oneline

# Log with branch graph
git log --oneline --graph --all

# Show changes in the last commit
git show

# Show diff of unstaged changes
git diff

# Show diff of staged changes
git diff --staged
```

## 7. Undoing Changes

```bash
# Discard changes in a file (revert to last commit)
git restore <file>

# Unstage a file
git restore --staged <file>

# Undo last commit but keep changes staged
git reset --soft HEAD~1

# Undo last commit and unstage changes
git reset HEAD~1

# Undo last commit and discard changes (destructive)
git reset --hard HEAD~1
```

## 8. Remote Repositories

```bash
# Add a remote
git remote add origin <url>

# View remotes
git remote -v

# Push a branch (first time, set upstream)
git push -u origin <branch-name>

# Push subsequent commits
git push

# Pull latest changes
git pull

# Fetch without merging
git fetch
```

## 9. Tags (Versioning Releases)

```bash
# Create a lightweight tag
git tag v1.0.0

# Create an annotated tag
git tag -a v1.0.0 -m "First stable release"

# List tags
git tag

# Push a tag to remote
git push origin v1.0.0

# Push all tags
git push --tags
```

### Versioning Scheme

Use [Semantic Versioning](https://semver.org/): `vMAJOR.MINOR.PATCH`

| Bump    | When                                      | Example         |
|---------|-------------------------------------------|-----------------|
| MAJOR   | Breaking / incompatible changes           | `v1.0.0 → v2.0.0` |
| MINOR   | New features, backwards-compatible        | `v1.0.0 → v1.1.0` |
| PATCH   | Bug fixes, small improvements             | `v1.0.0 → v1.0.1` |

## 10. Stashing (Temporary Shelving)

```bash
# Stash current changes
git stash

# Stash with a message
git stash push -m "wip: feature engineering"

# List stashes
git stash list

# Apply most recent stash (keep in stash list)
git stash apply

# Apply and remove from stash list
git stash pop

# Drop a specific stash
git stash drop stash@{0}
```

## 11. .gitignore Tips

```bash
# Stop tracking a file already committed
git rm --cached <file>

# Stop tracking a directory already committed
git rm -r --cached <directory>

# Then commit the removal
git commit -m "chore: remove tracked cache files"
```

## 12. Typical Workflow

```bash
# 1. Create a feature branch
git switch -c feat/add-model-training

# 2. Make changes, stage, and commit
git add .
git commit -m "feat: add baseline linear regression model"

# 3. Push branch to remote
git push -u origin feat/add-model-training

# 4. Open a pull request / merge request (on GitHub/GitLab)

# 5. After review, merge into main
git switch main
git merge --no-ff feat/add-model-training

# 6. Delete the feature branch
git branch -d feat/add-model-training

# 7. Tag a release if needed
git tag -a v0.1.0 -m "Initial model pipeline"
git push --tags
```
