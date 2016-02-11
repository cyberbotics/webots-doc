## Webots license system

Starting with Webots 8, a new license system was introduced to facilitate the
use of Webots, which replaces the previous system. Webots licenses can now be
set-up on an unlimited number of computers, allowing you to use Webots
seamlessly on any computer (office, home, travel, etc.). This new system relies
on a license server located on Cyberbotics servers and accessible through an
Internet connection. If you would like to use Webots while not connected to the
Internet, you can transfer your Internet license from the server to your local
computer for a limited duration. After the expiration of this duration, your
license will be automatically transferred back to the license server.

> **note**: Cyberbotics license servers are located in Switzerland on a highly reliable
network featuring a 99.9% up-time. However, if for some reason our servers would
fail, a security system will allow you to run Webots even in case of server
failure, by connecting automatically to an alternate server located in the Cloud
(hosted on Google App Engine).

### Firewall configuration (optional)

If you plan to use Webots behind an Internet firewall, you should create two new
rules in your firewall configuration to allow connections to the following
servers:

- `https://www.cyberbotics.com (port 443)`
- `https://webots-license.appspot.com (port 443)`

> **note**: If you are using a proxy to access the Internet, Webots will retrieve your
system proxy configuration automatically.

### License agreement

Please read your license agreement carefully before using Webots. This license
is provided within the software package. By using the software and
documentation, you agree to abide by all the provisions of this license.

### License setup

A Webots license is originally associated with an e-mail address which
corresponds to a user account on Cyberbotics's web site.

When Webots is started for the first time, a login dialog invites you to
register a user account on Cyberbotics's web site (if not already done) and to
enter the corresponding license information to log in your Webots session.

> **note**: The `Synchronization` field of the Webots login dialog defines how frequently
Webots checks the license server. Setting this field to a small value will cause
more networking activity, but will allow you to release the license quickly
after a crash. This will allow you in turn to restart Webots quicker on another
machine. For example, if you select 5 minutes, you may have to wait for up to 5
minutes if you crashed Webots on a machine and want to restart it on another.

### License administration

If you are the administrator of the license, you can log into your Webots
account on Cyberbotics' web site and go to the `Administration` page under the
`My Account` tab. From there, you will be able to monitor your licenses, to
purchase more licenses, to create groups of users and to grant customized user
access to your licenses.

### Module download folder

By default, Webots will download the different modules you purchased and store
them in the local user application folder:

- Windows: "C:\Users\MyName\AppData\Local\Cyberbotics\Webots\8.0"
- Mac OS X: "/Users/MyName/Library/Application Support/Cyberbotics/Webots/8.0"
- Linux: "/home/MyName/.local/share/Cyberbotics/Webots/8.0"

You may want to change this behavior and have Webots storing its module files in
a different folder. This is possible by setting the `WEBOTS_MODULES_PATH`
environment variable to point to a folder where the modules files will be
downloaded and stored. It can be useful to do so if you want to avoid that each
user has its own copy of the module files. In such a case, it is recommended for
the users to start Webots with the `--disable-modules-download` option to avoid
overwritting files in this folder.

If you need further information about license issues, please send an e-mail to:

[license@cyberbotics.com](mailto:license@cyberbotics.com)

