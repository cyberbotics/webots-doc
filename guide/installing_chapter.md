# Installing Webots

This chapter explains how to install Webots and configure your license rights.

## Webots licenses

The Webots licenses comes in three different flavors, including Webots PRO,
Webots EDU and Webots MOD. They differ by the features and price. These
different versions are described in this section. The features available in the
different versions are summarized in .

### Webots PRO

Webots PRO is the most powerful version of Webots. It is designed for research
and development projects. Webots PRO includes the possibility to create
supervisor processes for controlling robotics experiments, an extended physics
programming capability and a fast simulation mode (faster than real time). A 30
day trial version of Webots PRO is available from Cyberbotics web site.

### Webots EDU

Webots EDU is tailored for classrooms. Students learn how to model robots,
create their own environments and program the behavior of the robots, using any
of the supported programming languages. To validate their models, they can
optionally transfer their control programs to real robots. A 30 day trial
version of Webots EDU is available upon request.

### Webots MOD

Webots MOD is a special license mode in which the simulation software comes free
of charge and the users pay only for the modules they need. Various modules are
available for purchase at different price tags. They include special robot
models (e.g., NAO, DARwIn-OP, e-puck, Thymio 2, etc.), object models (e.g.,
cardboard box, wooden box, etc.), environment models (e.g., robot soccer field),
programming libraries, programming languages (e.g., C/C++, Matlab, Python),
interfaces to third parties software or hardware, etc. They are all described on
Cyberbotics web site.

### Webots licences overview

The following table summarizes the main differences between Webots PRO, Webots
EDU and Webots MOD.

(1): refer to specific module description.

## System requirements

The following hardware is required to run Webots:

The following operating systems are supported:

Other versions of Webots for other UNIX systems (Solaris, Linux PPC, Irix) may
be available upon request.

## Verifying your graphics driver installation

### Supported graphics cards

Webots officially supports only recent nVidia and ATI graphics adapters. So it
is recommended to run Webots on computers equipped with such graphics adapters
and up-to-date drivers provided by the card manufacturer (i.e., nVidia or ATI).
Such drivers are often bundled with the operating system (Windows, Linux and Mac
OS X), but in some case, it may be necessary to fetch it from the web site of
the card manufacturer.

### Unsupported graphics cards

Webots may nevertheless work with other graphics adapters, in particular the
Intel graphics adapters. However this is unsupported and may work or not,
without any guarantee. Some users reported success with some Intel graphics
cards after installing the latest version of the driver. Graphics drivers from
Intel may be obtained from the `Intel download center web site`. Linux graphics
drivers from Intel may be obtained from the `Intel Linux Graphics web site`. If
some graphical bugs subsist, changing the "RTT prefered mode" from the Webots
OpenGL Preferences from "Framebuffer Object" to "Pixelbuffer Object" or "Direct
Copy" may fix the problems. However, this may also impact the 3D performance.

### Upgrading your graphics driver

On Linux and Windows, you should make sure that the latest graphics driver is
installed. On the Mac the latest graphics driver are automatically installed by
the *Software Update*, so Mac users are not concerned by this section. Note that
Webots can run up to 10x slower without appropriate driver. Updating your driver
may also solve various problems, i.e., odd graphics rendering or Webots crashes.

#### Linux

On Linux, use this command to check if a hardware accelerated driver is
installed: `$ glxinfo | grep OpenGL` If the output contains the string "NVIDIA",
"ATI", or "Intel", this indicates that a hardware driver is currently installed:
`$ glxinfo | grep OpenGL OpenGL vendor string: NVIDIA Corporation OpenGL
renderer string: GeForce 8500 GT/PCI/SSE2 OpenGL version string: 3.0.0 NVIDIA
180.44 ...` If you read "Mesa", "Software Rasterizer" or "GDI Generic", this
indicates that the hardware driver is currently not installed and that your
computer is currently using a slow software emulation of OpenGL: `$ glxinfo |
grep OpenGL OpenGL vendor string: Mesa project: www.mesa3d.org OpenGL renderer
string: Mesa GLX Indirect OpenGL version string: 1.4 (1.5 Mesa 6.5.2) ...` In
this case you should definitely install the hardware driver.

On Ubuntu the driver can usually be installed automatically from the `Additional
Drivers` tab of the `Software amp Update` window. Otherwise you can find out
what graphics hardware is installed on your computer by using this command: `$
lspci | grep VGA 01:00.0 VGA compatible controller: nVidia Corporation GeForce
8500 GT (rev a1)`

Then you can normally download the appropriate driver from the graphics hardware
manufacturer's website: `http://www.nvidia.com` for an nVidia card or
`http://www.amd.com` for a ATI graphics card. Please follow the manufacturer's
instructions for the installation.

#### Windows

### Hardware acceleration tips

#### Linux

Depending on the graphics hardware, there may be a huge performance drop of the
rendering system (up to 10x) when *compiz* desktop effects are on. Also these
visual effects may cause some display bug where the main window of Webots is not
properly refreshed. Hence, on Ubuntu (or other Linux) we recommend to deactivate
the desktop effects. You can easily disable them using some tools like *Compiz
Config Settings Manager* or *Unity Twerk Tool*.

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
downloaded from our `web site`.

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
file which can be downloaded `here`, using this command:


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
Once uncompressed, it is recommended to set the WEBOTS_HOME environment variable
to point to the webots directory obtained from the uncompression of the tarball:


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
webots_major_version.webots_minor_version.webots_bugfix_version_setup.exe
/SILENT" or "webots-
webots_major_version.webots_minor_version.webots_bugfix_version_setup.exe
/VERYSILENT"

If you observe 3D rendering anomalies or Webots crashes, it is strongly
recommend to upgrade your graphics driver.

### Mac OS X

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

### Firewall configuration (optional)

If you plan to use Webots behind an Internet firewall, you should create two new
rules in your firewall configuration to allow connections to the following
servers:

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

### License administration

If you are the administrator of the license, you can log into your Webots
account on Cyberbotics' web site and go to the `Administration` page under the
`My Account` tab. From there, you will be able to monitor your licenses, to
purchase more licenses, to create groups of users and to grant customized user
access to your licenses.

### Module download folder

By default, Webots will download the different modules you purchased and store
them in the local user application folder:

You may want to change this behavior and have Webots storing its module files in
a different folder. This is possible by setting the `WEBOTS_MODULES_PATH`
environment variable to point to a folder where the modules files will be
downloaded and stored. It can be useful to do so if you want to avoid that each
user has its own copy of the module files. In such a case, it is recommended for
the users to start Webots with the `--disable-modules-download` option to avoid
overwritting files in this folder.

If you need further information about license issues, please send an e-mail to:

`license@cyberbotics.com`

## Classroom license setup

This section explains how to setup your Webots licenses to grant access to
students in a classroom. It also explains how to manage student access to Webots
licenses for homework Webots exercices or projects. Let's assume you purchased
20 licenses of Webots EDU and want to let some of your students use them. You
should ensure that your classroom machines can access the Internet and in
particular the `license server of Cyberbotics`. If it doesn't work, you may need
to configure your local firewall to allow Webots to access this URL.

### User account

There are two methods to handle student access to Webots licenses: a single user
account, or multiple user accounts.

#### Single user account

The single user account method is simpler to setup as you don't need to know the
e-mail addresses of the students. Nevertheless, you need to setup an e-mail
address for a generic user for which you can read the e-mails received. It could
be your own personal e-mail address. Let's call this e-mail address
`webots@my.university.edu`. A drawback to this method is that it allows a single
student to use simultaneously several instances of your 20 licenses, possibly
all of them, thus preventing other students to use them.

#### Multiple user accounts

The multiple user accounts license requires that you have the list of e-mail
addresses of the students to whom you want to grant access to your Webots
licenses. You will be able to limit the number of simultaneous instances of
Webots used per student to 1, so that a single student cannot use multiple
licenses simultaneously. Hence a single student cannot prevent the others from
using Webots.

### Classrom

#### Setup

You can install Webots on all the computers in a classroom, even if you have
more computers than licenses. In our example, if you have 20 licenses and 30
computers, then 20 students could use the software simultaneously on any of the
30 computers. If a 21rst student comes in, he won't be able to start Webots
until one of the 20 students stops using Webots.

#### Restrict the license to specific machines

It is possible to restrict the use of your licenses to a specific classroom, or
more generally, to a number of specific computers. This can be achieved from the
"Module pack" section of the administration web page: click on the license you
want to restrict and a new page entitled "Edit module pack" should be displayed.
On this page, set an IP range value to limit the use of this pack to machines
with a specific IP address. For example: "128.179.67.143, 128.179.67.146,
123.179.67.145" will limit the use of Webots to these 3 IP addresses. It is also
possible to use an IP mask (CIDR notation) to specify a range of IP addresses.
For example, "128.179.67.143/24, 128.178.12.122" will limit the use of Webots to
any machine whose IP address starts with 128.179.67 and also to the machine
whose IP address is 128.178.12.122. Machines that do not match the values
provided in the IP range field won't be able to access the licenses.

#### Making things even simpler for students

To save the students from having to type an e-mail address and password on the
first run of Webots, you may want to do it for them before the class starts. If
you do it from the user account they are supposed to use, this information will
be saved and the students won't need to enter it again. You may also automate
this process by copying an already configured Webots preferences to all the user
accounts used by the students. On Windows, the Webots preferences are stored in
the registry under the "HKEY_CURRENT_USER/SOFTWARE/Cyberbotics" key (so you need
to use a tool that copies registry keys across user accounts). On Mac OS X, the
Webots preferences are stored in a file under the user home directory at
"~/Library/Preferences/com.cyberbotics.Webots
webots_major_version.webots_minor_version.webots_bugfix_version.plist". On
Linux, the Webots preferences are stored in a file under the user home directory
at "~/.config/Cyberbotics/Webots
webots_major_version.webots_minor_version.webots_bugfix_version.conf".

### Homework

If no IP restriction is set (see above), then the students will be able to use
Webots anytime, from any computer, including their own personal computers. In
such a case, it's better to use multiple user accounts rather than a single one,
to avoid that a few students use all the licenses permanently.

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

## Translating Webots to your own language

Webots is translated into French, German, Spanish, Chinese and Japanese (and
partially into Italian). However, since Webots is always evolving, including new
text or changing existing wording, these translations may not always be complete
or accurate. As a user of Webots, you are very welcome to help us fix these
incomplete or inaccurate translations. This is actually a very easy process
which merely consists of editing a UTF-8 XML file, and processing it with a
small utility. Your contribution is likely to be integrated into the upcoming
releases of Webots, and your name acknowledged in this user guide.

Even if your language doesn't appear in the current Webots Preferences panel,
under the `General` tab, you can very easily add it. To proceed with the
creation of a new translation or the improvement of an existing one, please
follow the instructions located in the "readme.txt" file in the
"Webots/resources/translations" folder. Don't forget to send us your translation
files!

