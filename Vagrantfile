$postinstall = <<SCRIPT
#yum makecache
yum install -y net-tools epel-release
#yum groupinstall -y "Compute Node"
#yum groupinstall -y "Compatibility Libraries"
#yum group insttall -y "Development Tools"
sed -i 's/SELINUXTYPE=targeted/SELINUXTYPE=disabled/g' /etc/sysconfig/selinux
SCRIPT

Vagrant.configure("2") do |config|

  config.vm.define "centoss1" do |centoss1|
      centoss1.vm.box = "centos/7"
      centoss1.vm.hostname = "centoss1"
      centoss1.vm.network "private_network", ip: "192.168.56.220"
      #  config.vm.synced_folder "src/", "/var/www/html"
      centoss1.vm.provision "shell", inline: $postinstall

  centoss1.vm.provider "virtualbox" do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.memory = "1024"
      v.cpus = "2"
  end
  end

  config.vm.define "centoss2" do |centoss2|
      centoss2.vm.box = "centos/7"
      centoss2.vm.hostname = "centoss2"
      centoss2.vm.network "private_network", ip: "192.168.56.221"
      #config.vm.synced_folder "src/", "/var/www/html"
      centoss2.vm.provision "shell", inline: $postinstall

  centoss2.vm.provider "virtualbox" do |v|
      #v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.memory = "1024"
      v.cpus = "2"
  end
  end

  config.vm.define "ubuntus1" do |ubuntus1|
      ubuntus1.vm.box = "ubuntu/trusty64"
      ubuntus1.vm.hostname = "ubuntus1"
      ubuntus1.vm.network "private_network", ip: "192.168.56.222"
      #config.vm.synced_folder "src/", "/var/www/html"
      #ubuntus1.vm.provision "shell", inline: $postinstall

  ubuntus1.vm.provider "virtualbox" do |v|
      #v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.memory = "1024"
      v.cpus = "2"
  end
  end

end
