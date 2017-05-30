# Overview
An internal reporting tool that generates informative summaries from a news database.

This project satisfies a project requirement for Udacity's Full Stack Web Developer Degree.

***

# Enviroment Setup

### Installing the virtual machine

1. Download & install  [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

2. Download & install [Vagrant](https://www.vagrantup.com/downloads.html)

Check if Vagrant is successfully installed by running on terminal.

```vagrant --version```

If you see the version number, then you're good.

### Download VM configuration

1. Download & unzip
[FSND-Virtual-Machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2017/May/59125904_fsnd-virtual-machine/fsnd-virtual-machine.zip)

2. Or you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

3. ```cd``` into directory **FSND-Virtual-Machine**. Inside, you will find another directory called **vagrant**. Change directory into the vagrant directory

### Running the VM
1. Inside the vagrant subdirectory, run the command
```vagrant up```. Doing so will download & install the Linux OS.

2. Once ```vagrant up``` is completed and your shell prompt returns, run ```vagrant ssh``` to log into newly installed Linux OS.

3. Lastly, run ```cd /vagrant```

### Download the data
1. Download & unzip [news db](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

2. Place the file ```newsdata.sql``` inside of the ```vagrant``` directory
