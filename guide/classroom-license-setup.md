## Classroom license setup

This section explains how to setup your Webots licenses to grant access to students in a classroom.
It also explains how to manage student access to Webots licenses for homework Webots exercices or projects.
Let's assume you purchased 20 licenses of Webots EDU and want to let some of your students use them.
You should ensure that your classroom machines can access the Internet and in particular the [license server of Cyberbotics](https://www.cyberbotics.com/license).
If it doesn't work, you may need to configure your local firewall to allow Webots to access this URL.

### User account

There are two methods to handle student access to Webots licenses: a single user account, or multiple user accounts.

#### Single user account

The single user account method is simpler to setup as you don't need to know the e-mail addresses of the students.
Nevertheless, you need to setup an e-mail address for a generic user for which you can read the e-mails received.
It could be your own personal e-mail address.
Let's call this e-mail address `webots@my.university.edu`.
A drawback to this method is that it allows a single student to use simultaneously several instances of your 20 licenses, possibly all of them, thus preventing other students to use them.

1. Log in to your Webots user account using your license administration credentials, e.g., the user account which was used to activate your Webots licenses.
2. Create a new user pack from the administration page and call it "Students".
3. Grant access to all your 20 Webots EDU license (tick boxes).
4. Set the concurrency value to 20 to allow the single user account to use all the licenses simultaneously.
5. Type `webots@my.university.edu` in the "users:" text area.
6. If the account doesn't already exists, `webots@my.university.edu` will receive an e-mail asking to create a user account at [Cyberbotics' website](https://www.cyberbotics.com).
7. Create this account (if needed), log in and visit the Profile page of this account.
Copy the "Alternate password for Webots 8".
This password allows students to use Webots, but not to log in this user account.
It looks like `J6ebgAGRgFtkf8QHiWoHXIUnI98=`.
8. Give this e-mail address and alternate password to your students to allow them to log in Webots using your licenses (but they won't be able to log in the web page).

#### Multiple user accounts

The multiple user accounts license requires that you have the list of e-mail addresses of the students to whom you want to grant access to your Webots licenses.
You will be able to limit the number of simultaneous instances of Webots used per student to 1, so that a single student cannot use multiple licenses simultaneously.
Hence a single student cannot prevent the others from using Webots.

1. Log in to your Webots user account using your license administration credentials, e.g., the user account which was used to activate your Webots licenses.
2. Create a new user pack from the administration page and call it "Students".
3. Grant access to all your 20 Webots EDU licenses (tick boxes).
4. Set the concurrency value to 1 to prevent a single user to use multiple instances of Webots at the same time.
5. Type (or copy/paste) the list of student e-mail addresses in the "users:" text area.
6. Press the apply button.
The e-mail addresses which are not already registered on Cyberbotics' website will receive an invitation e-mail explaining how to register a Webots account and use the newly granted Webots licenses.
For existing accounts, no e-mail is sent and it is your responsibility to inform the students about their modified license rights.

### Classroom

#### Setup

You can install Webots on all the computers in a classroom, even if you have more computers than licenses.
In our example, if you have 20 licenses and 30 computers, then 20 students could use the software simultaneously on any of the 30 computers.
However, if a 21rst student comes in, he won't be able to start Webots until one of the 20 students stops using Webots.

#### Restrict the license to specific machines

It is possible to restrict the use of your licenses to a specific classroom, or more generally, to a number of specific computers.
This can be achieved from the "Module pack" section of the administration web page: click on the license you want to restrict and a new page entitled "Edit module pack" should be displayed.
On this page, set an IP range value to limit the use of this pack to machines with a specific IP address.
For example: "128.179.67.143, 128.179.67.146, 123.179.67.145" will limit the use of Webots to these 3 IP addresses.
It is also possible to use an IP mask (CIDR notation) to specify a range of IP addresses.
For example, "128.179.67.143/24, 128.178.12.122" will limit the use of Webots to any machine whose IP address starts with 128.179.67 and also to the machine whose IP address is 128.178.12.122.
Machines that do not match the values provided in the IP range field won't be able to access the licenses.

#### Making things even simpler for students

To save the students from having to type an e-mail address and password on the first run of Webots, you may want to do it for them before the class starts.
If you do it from the user account they are supposed to use, this information will be saved and the students won't need to enter it again.
You may also automate this process by copying an already configured Webots preferences to all the user accounts used by the students.
On Windows, the Webots preferences are stored in the registry under the "HKEY\_CURRENT\_USER/SOFTWARE/Cyberbotics" key (so you need to use a tool that copies registry keys across user accounts).
On macOS, the Webots preferences are stored in a file under the user home directory at "~/Library/Preferences/com.cyberbotics.Webots-{{ webots.version.major }}.plist".
On Linux, the Webots preferences are stored in a file under the user home directory at "~/.config/Cyberbotics/Webots-{{ webots.version.major }}.conf".

### Homework

If no IP restriction is set (see above), then the students will be able to use Webots anytime, from any computer, including their own personal computers.
In such a case, it's better to use multiple user accounts rather than a single one, to avoid that a few students use all the licenses permanently.
