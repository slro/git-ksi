# About
This project in a nutshell a simple script that allows to sign and verify Git commits with [Guardtime KSI](https://www.google.com) blockchain technology. Moreover it acts like a git executable wrapper with automatic sign/verify hooks when committing/pulling changes e.g. you can use it instead of a Git executable by creating an alias in your `.bashrc` or `.profile` configuration files:

```shell
alias git='git-ksi'
```

Currently only *Nix systems are supported but it's possible that it also works under Windows. The recommended approach is to place this script in your host's `PATH` but you can also use it directly from your project directory. 

# Usage
First of all, in order to use KSI in a development process the one need a KSI account. It can be obtained via [this link](https://guardtime.com/technology/blockchain-developers).

The script itself pipes all Git commands directly to Git executable but in occasion of committing or pulling it automatically triggers corresponding actions involving [KSI Cantena DB](https://tryout-catena.guardtime.net/) middleware solution. 

```shell
# simply forwarding commands to Git executable
git-ksi status
git-ksi add .
git-ksi fetch origin
```

```shell
# initialize commit signing with KSI
git-ksi commit -m '<your commit message>'

# initialize commit verification with KSI
git-ksi pull origin <branch_to_pull_from>
```

During a signing/verification process you'll be asked your KSI credentials and during verification you also have to provide a Catena DB commit GUID that is provided after successfully signing a commit.

# Contact
This is a rather 'test' project and if the one has any questions they can be forwarded to our development team (contacts can be found derectly on GitHub). Any bugs and requests belong to issues tab of this repository.

### Have a nice time hacking!
