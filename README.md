# UNMANNED ROBOT VACUUM SYSTEM FOR LOW DENSITY POLYETHYLENE PLASTIC WASTE  <a id="top"></a>
This is a repository dedicated for the project codes and diagrams the researchers will make throughout the formulation and realization of their research project

## Project/Task Lists
* 
# Git Cheatsheet

## Git Setup

### Configure Default Git User
```shell
git config --global user.email email@example.com
git config --global user.name username
```

### Access Git Global Config
```shell
git config --global --edit
```

### Access Git Local Repository Config
On the root of your project:
```shell
git config --edit
```

### Adding Git Aliases
Git aliases are great to shorten long git commands. This is a standard format on how to make a git alias:
```shell
git config --global alias.<command_alias_here> <git_command_expression>
```
Examples:
```shell
git config --global alias.unstage 'reset HEAD --'
git config --global alias.logp 'log --graph --decorate --pretty'
git config --global alias.lastc 'log --graph --decorate --pretty -1 HEAD'
```
You may edit them by Editing the Git Global Config if you choose to do so.

Running Git aliases are the same as running them as standard git commands. From the previous examples, they can be executed as follows:
```shell
git unstage		# Equivalent to `git reset HEAD --`
git logp		# Equivalent to `git log --graph --decorate --pretty`
git lastc		# Equivalent to `git log --graph --decorate --pretty -1 HEAD`
```

## Making a Local Git Repository

### Initialise/Create a new Git Repository
On the root of your empty project:
```shell
git init
```

### Clone from Existing Repository
```shell
git clone <uri>.git
```

## Git Phases

### Phases
1. *Untracked/Unstaged Phase* -- All new files and newly modified files are located here, ready for staging.
2. *Staging Phase* -- All files that are staged are ready to commit.
3. *Snapshot Phase* -- Finalised commits that are located in a branch or in multiple branches.

### Passing Files through Git Phases

### *Untracked/Unstaged* -> *Staging*
For all untracked/modified files:
```shell
git add .
```
For specific files:
```shell
git add ./relative/path/to/file.ext
```

### *Staging* -> *Untracked/Unstaged*
For all tracked files:
```shell
git reset .
git restore --staged .
```
For specific files:
```shell
git reset ./relative/path/to/file.txt
git restore --staged ./relative/path/to/file.txt
```

### *Staging* -> *Snapshot (Commit)*
For Multiline commit:
> NOTE: Must set default text editor, either CLI or VSCode
```shell
git commit
```
Shorthand/Single Line Commit:
```shell
git commit -m "<commit message here>"
```

### *Latest Snapshot (Commit)* -> *Staging*
```shell
git reset --soft HEAD~1
```

## Managing Snapshots (Commits)
```shell
git log
```
> NOTE: additional flags may be used to enhance the output of `git log`. Typical flags may be `--pretty`, `--graph`, or `--decorate`.

## Git Remotes
### Remote Repo Management
#### Adding a new Remote Repo
```shell
git remote add <remote_alias> <remote_uri>
```

#### List all Available Remote Repos set
```shell
git remote
```
or
```shell
git remote ls
```
or
```shell
git remote -v
```
for verbose mode (it will show the git remote URI)

#### Remove Remote Repo
```shell
git remote rm <remote_alias>
```

#### Rename Remote Repo Alias
```shell
git remote rename <old_alias> <new_alias>
```

### Push/Pull to/from Remote Repos

#### Push to Remote Repository
Push from default upstream branch (default is master/main, depending on the current branch name set. If you don't know what current branch you're on, refer to Show All Current Branches.)
```shell
git push
```
Push and set default upstream branch
```shell
git push -u <remote_name> <new_upstream_branch_name>
```
Push specific branch
```shell
git push <remote_name> <branch_name>
```

#### Pull from Remote Repository
Pull from default upstream branch, or current branch. (it may prompt you to set a default upstream branch if you do this command.)
```shell
git pull
```
Pull from specific branch from remote repo
```shell
git pull <remote_name> <branch_name>
```
Pull and set default upstream branch
```shell
git pull -u <remote_name> <branch_name>
```

## Git Branches

### Creating a new Branch
#### Method 1: 2 commands
```shell
git branch <new_branch_name>
git checkout <new_branch_name>
```
#### Method 2: 1 command
```shell
git checkout -b <new_branch_name>
```

### Show All Current Branches
```shell
git branch
```
or
```shell
git branch ls
```

### Delete Branch
```shell
git branch -d <branch_name>
```
if there are unmerged changes in current branch, above command won't work, use this instead:
```shell
git branch -D <branch_name>
```

### Rename Branch
> NOTE: you must be on the current branch you want to rename.
```shell
git branch -m <new_branch_name>
```

### Merge from one Branch to another
> NOTE: you must be on the current branch you want to merge to.
```shell
git merge <branch_name>
```

## Additional Tips/Tricks
1. Always add a `.gitignore` file if you want git to skip file/s or folder/s. 
	Here's an example `.gitignore` file template for a Node.js project:
	```
	# Logs
	logs
	*.log
	npm-debug.log*
	yarn-debug.log*
	yarn-error.log*
	lerna-debug.log*
	.pnpm-debug.log*
	
	# Diagnostic reports (https://nodejs.org/api/report.html)
	report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json

	# Runtime data
	pids
	*.pid
	*.seed
	*.pid.lock

	# Directory for instrumented libs generated by jscoverage/JSCover
	lib-cov

	# Coverage directory used by tools like istanbul
	coverage
	*.lcov
	
	# nyc test coverage
	.nyc_output
	
	# Grunt intermediate storage (https://gruntjs.com/creating-plugins#storing-task-files)
	.grunt

	# Bower dependency directory (https://bower.io/)
	bower_components
	
	# node-waf configuration
	.lock-wscript

	# Compiled binary addons (https://nodejs.org/api/addons.html)
	build/Release
	
	# Dependency directories
	node_modules/
	jspm_packages/

	# Snowpack dependency directory (https://snowpack.dev/)
	web_modules/

	# TypeScript cache
	*.tsbuildinfo

	# Optional npm cache directory
	.npm

	# Optional eslint cache
	.eslintcache

	# Optional stylelint cache
	.stylelintcache

	# Microbundle cache
	.rpt2_cache/
	.rts2_cache_cjs/
	.rts2_cache_es/
	.rts2_cache_umd/

	# Optional REPL history
	.node_repl_history

	# Output of 'npm pack'
	*.tgz

	# Yarn Integrity file
	.yarn-integrity

	# dotenv environment variable files
	.env
	.env.development.local
	.env.test.local
	.env.production.local
	.env.local

	# parcel-bundler cache (https://parceljs.org/)
	.cache
	.parcel-cache
	
	# Next.js build output
	.next
	out

	# Nuxt.js build / generate output
	.nuxt
	dist

	# Gatsby files
	.cache/
	# Comment in the public line in if your project uses Gatsby and not Next.js
	# https://nextjs.org/blog/next-9-1#public-directory-support
	# public

	# vuepress build output
	.vuepress/dist

	# vuepress v2.x temp and cache directory
	.temp
	.cache

	# Docusaurus cache and generated files
	.docusaurus

	# Serverless directories
	.serverless/

	# FuseBox cache
	.fusebox/

	# DynamoDB Local files
	.dynamodb/

	# TernJS port file
	.tern-port

	# Stores VSCode versions used for testing VSCode extensions
	.vscode-test

	# yarn v2
	.yarn/cache
	.yarn/unplugged
	.yarn/build-state.yml
	.yarn/install-state.gz
	.pnp.*
	```
2. If you want to keep empty folders, add a `.gitkeep` file inside the folder so that git can see and track changes from that folder even though it is empty. 

## Commit Messages

Format: `<type>(<scope>): <subject>`

`<scope>` is optional

### Example

```
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
```

More Examples:
- `add`: (create or add a new project or individual submission)
- `feat`: (new feature for the user, not a new feature for build script)
- `fix`: (bug fix for the user, not a fix to a build script)
- `docs`: (changes to the documentation)
- `style`: (formatting, missing semi colons, etc; no production code change)
- `refactor`: (refactoring production code, eg. renaming a variable)
- `test`: (adding missing tests, refactoring tests; no production code change)
- `chore`: (updating grunt tasks etc; no production code change)

References:

- https://www.conventionalcommits.org/
- https://seesparkbox.com/foundry/semantic_commit_messages
- http://karma-runner.github.io/1.0/dev/git-commit-msg.html
- https://gist.github.com/cindrmon/ea9d3c172b8baa2d65ad97811d856066

# The Team ✨
<table>
  <tbody>
    <tr>
  </tbody>
</table>

<p align="right">(<a href="#top">back to top</a>)</p>