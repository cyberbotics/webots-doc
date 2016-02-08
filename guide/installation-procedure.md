## Installation procedure

Usually, you will need to be "administrator" to install Webots. Once installed,
Webots can be used by a regular, unprivileged user. To install Webots, please
follow this procedure:

### Linux

Webots will run on most recent Linux distributions running glibc2.11.1 or
earlier. This includes fairly recent Ubuntu, Debian, Fedora, SuSE, RedHat, etc.
Webots comes in two different package types: `.deb` and `.tar.bz2` (tarball).
The `.deb` package is aimed at the latest Ubuntu Linux distribution whereas the
tarball package includes many dependency libraries and there is therefore best
suited for installation on other Linux distributions. These packages can be
downloaded from our [web site](http://www.cyberbotics.com/linux).

#### Using Advanced Packaging Tool (APT)

The advantage of this solution is that Webots will be updated with the system
updates. This installation requires the `root` privileges.

First of all, you may want to configure your apt package manager by adding this
line:


```
deb http://www.cyberbotics.com/debian/ binary-i386/
```

or


```
deb http://www.cyberbotics.com/debian/ binary-amd64/
```

in the "/etc/apt/sources.list" configuration file. Then update the APT packages
by using


```
apt-get update
```

Optionally, Webots can be autentified thanks to the `Cyberbotics.asc` signature
file which can be downloaded [here](http://www.cyberbotics.com/linux), using
this command:


```
apt-key add /path/to/Cyberbotics.asc
```

Then proceed to the installation of Webots using:


```
apt-get install webots
```

#### From the tarball package

This section explains how to install Webots from the tarball package (having the
`.tar.bz2` extension). This package can be installed without the `root`
privileges. It can be uncompressed anywhere using the `tar` `xjf` command line.
Once uncompressed, it is recommended to set the WEBOTS\_HOME environment
variable to point to the webots directory obtained from the uncompression of the
tarball:


```
tar xjf webots-webots_major_version.webots_minor_version.webots_bugfix_version-i386.tar.bz2
```

or


```
tar xjf webots-webots_major_version.webots_minor_version.webots_bugfix_version-x86-64.tar.bz2
```

and


```
export WEBOTS_HOME=/home/username/webots
```

The export line should however be included in a configuration script like
"/etc/profile", so that it is set properly for every session.

Some additional libraries are needed in order to properly run Webots. In
particular *libjpeg62*, *libav-tools*, *libpci* and *libavcodec-extra-54* have
to be installed on the system.

#### From the DEB package

This procedure explains how to install Webots from the DEB package (having the
`.deb` extension).

On Ubuntu, double-click on the DEB package file to open it with the Ubuntu
Software Center and click on the `Install` button. If a previous version of
Webots is already installed, then the text on the button could be different,
like `Upgrade` or `Reinstall`.

Alternatively, the DEB package can also be installed using `dpkg` or `gdebi`
with the `root` privileges. For 32-bit systems:


```
dpkg -i webots_webots_major_version.webots_minor_version.webots_bugfix_version_i386.deb
apt-get -f install
```

or


```
gdebi webots_webots_major_version.webots_minor_version.webots_bugfix_version_i386.deb
```

For 64-bit systems:


```
dpkg -i webots_webots_major_version.webots_minor_version.webots_bugfix_version_amd64.deb
apt-get -f install
```

or


```
gdebi webots_webots_major_version.webots_minor_version.webots_bugfix_version_amd64.deb
```

### Windows

It is possible to install Webots silently from an administrator DOS console, by
typing "webots-
webots\_major\_version.webots\_minor\_version.webots\_bugfix\_version\_setup.exe
/SILENT" or "webots-
webots\_major\_version.webots\_minor\_version.webots\_bugfix\_version\_setup.exe
/VERYSILENT"

If you observe 3D rendering anomalies or Webots crashes, it is strongly
recommend to upgrade your graphics driver.

### Mac OS X

