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

> **Note**:
Cyberbotics license servers are located in Switzerland on a highly reliable
network featuring a 99.9% up-time. However, if for some reason our servers would
fail, a security system will allow you to run Webots, by connecting automatically to an alternate server located in the Cloud
(hosted on Google App Engine).

### Firewall configuration (optional)

If you plan to use Webots behind an Internet firewall, you should create two new
rules in your firewall configuration to allow connections to the following
servers:

- `https://www.cyberbotics.com (port 443)`
- `https://webots-license.appspot.com (port 443)`

> **Note**:
If you are using a proxy to access the Internet, Webots will retrieve your
system proxy configuration automatically.

### License agreement

Please read your license agreement carefully before using Webots. This license
is provided within the software package. By using the software and
documentation, you agree to abide by all the provisions of this license.

### License setup

A Webots license is originally associated with an e-mail address which
corresponds to a user account on Cyberbotics' website.

When Webots is started for the first time, a login dialog invites you to
register a user account on Cyberbotics' website (if not already done) and to
enter the corresponding license information to log in to your Webots session.

> **Note**:
The `Synchronization` field of the Webots login dialog defines how frequently
Webots checks the license server. Setting this field to a small value will cause
more networking activity, but will allow you to release the license quickly
after a crash. This will allow you in turn to restart Webots quicker on another
machine. For example, if you select 5 minutes, you may have to wait for up to 5
minutes if you crashed Webots on a machine and want to restart it on another.

### License administration

If you are the administrator of the license, you can log into your Webots
account on Cyberbotics' website and go to the `Administration` page under the
`My Account` tab. From there, you will be able to monitor your licenses, to
purchase more licenses, to create groups of users and to grant customized user
access to your licenses.

### Using Webots without Internet connection

It is possible to use Webots without any Internet connection for a limited
amount of time. Users who anticipate they will be away from the Internet can
download a license locally on their machine for a specified lease duration.
During this period of time, the license is considered to be in use and is not
available to other users. The maximum lease duration can be defined by the
administrator of the licenses in the "Edit module pack" administration web page.
It can be set to "None" to prevent any off-line use of Webots. Otherwise, the
maximum lease value can be chosen between 1 hour and 7 days.

In order to download a license locally for off-line use, a user should go to the
`Tools` menu of Webots and open the `License Manager...` item. A new window
should pop-up to display the available licenses. The user can then choose which
licenses to download on his local computer as well as the duration of the lease
for these licenses. Warning: this operation cannot be undone. Once transferred
locally, the licenses are not available to other computers for the duration of
the lease period.

Once downloaded, each license is stored into a file located in the following folder:

- Linux: `~/.local/share/Cyberbotics/Webots/licenses/`
- macOS: `~/Library/Application Support/Cyberbotics/Webots/licenses`
- Windows: `%HOMEPATH%\AppData\Roaming\Cyberbotics\Webots\licenses\`

### Getting help about the Webots license system

If you need further information about the Webots license system, please send an e-mail to:

[license@cyberbotics.com](mailto:license@cyberbotics.com)
