# Vagrant Lab for Ansible learning

Quickly create ansible learning or practice lab using vagrant. 
Follwing instructions will quickly create two centos and one ubuntu hosts


### Prerequisites
A Linux desktop, preferably Ubuntu with 6G RAM

You need to install virtualbox and vagrant on your desktop


### Installing

```
wget https://download.virtualbox.org/virtualbox/6.1.2/virtualbox-6.1_6.1.2-135662~Ubuntu~bionic_amd64.deb
wget https://releases.hashicorp.com/vagrant/2.2.7/vagrant_2.2.7_x86_64.deb
sudo dpkg -i virtualbox-6.1_6.1.2-135662~Ubuntu~bionic_amd64.deb
sudo dpkg -i vagrant_2.2.7_x86_64.deb

```
Install Ansible

* [InstallAnsible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) - Ansible Documentation


```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py --user
pip install --user ansible

```

Steps

```
cd vagrant-ansible
vagrant box add centos/7
vagrant box add ubuntu/trusty64
vagrant up

```

To stop VMs
```
vagrant stop
```
To Delete VMs
```
vagrant destroy
```
Login to VMs

```
vagrant ssh centoss1
```
update ansible_port and ansible_private_key_file path static inventory file. Static inventory file name is "inventory"
To see path ansible_private_key_file run below command, most likely no need to update ansible_port variable

```
./dynamicinventory.py --host centoss1
```
## Running the tests

```
ansible -i inventory vagrant --list-hosts
ansible -i inventory centos --list-hosts

ansible -i dynamicinventory.py all --list-hosts

ansible -i dynamicinventory.py all -m ping

ansible-playbook -i dynamicinventory.py playbooks/uptime.yml
```
For more learning playbooks see here 

* [MoreLearnigPlaybooks](https://github.com/thakurmhn/content-ansible-playbooks/tree/master/Playbooks)

## Congratulations
