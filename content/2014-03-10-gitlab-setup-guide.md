Title: GitLab setup guide
Category: guide
Tags: gitlab, git, bitnami, guide

[TOC]

In this guide, we use [Bitnami GitLab virtual machine](http://bitnami.com/stack/gitlab)
to deploy the GitLab server.

# Setup guide

## Enable SSH server

```sh
sudo mv /etc/init/ssh.conf.back /etc/init/ssh.conf
sudo start ssh
```

## Set static IP and update

`/etc/network/interfaces`

```
iface eth0 inet static
address 192.168.73.211
netmask 255.255.254.0
gateway 192.168.72.254
dns-servers 8.8.8.8 8.8.4.4
```

`/etc/resolv.conf`

```
nameserver 8.8.8.8
nameserver 8.8.4.4
```

```sh
sudo /opt/bitnami/apps/gitlab/updateip
```

## Configure email

`/opt/bitnami/apps/gitlab/htdocs/config/gitlab.yml`

```yml
email_from: user@example.com
#support_email: user@example.com  # comment out this line
```

`/opt/bitnami/apps/gitlab/htdocs/config/environments/production.rb`

```ruby
config.action_mailer.raise_delivery_errors = true
config.action_mailer.perform_deliveries = true
config.action_mailer.delivery_method = :smtp
config.action_mailer.smtp_settings = {
 :address => "smtp.gmail.com",
 :port => 465,
 :domain => "gmail.com",
 :authentication => :plain,  # if not workable, change :plain to :login
 :tls => true,
 :user_name => "your_account@gmail.com",
 :password => "your_password",
 :enable_starttls_auto => true
}
```

```sh
sudo /etc/init.d/networking restart
```

Then restart Apache server

```sh
sudo /opt/bitnami/ctlscript.sh restart apache
```

## Configure LDAP

`/opt/bitnami/apps/gitlab/htdocs/config/gitlab.yml`

```yml
ldap:
 enabled: false
 host: 192.168.1.2
 base: 'ou=people,dc=domain,dc=com'
 port: 389
 uid: 'uid'
 method: 'plain' # "tls" or "ssl" or "plain"
 bind_dn: 'dc=domain,dc=com'
 password: '_the_password_of_the_bind_user'
```

# Reference

- [BitNami GitLab - Bitnami documentation](http://wiki.bitnami.com/Applications/BitNami_GitLab)