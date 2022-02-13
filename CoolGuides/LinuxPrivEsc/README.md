# Linux Privilege Escalation
This is a guide a made while studying for my OSCP. The lectures that I took notes from are <a href="https://www.udemy.com/course/linux-privilege-escalation/">here</a>. The setup and workshop environment are <a href="https://github.com/sagishahar/lpeworkshop">here</a>.

## Introduction
### Understand Permissions in Linux
Permissions in Linux are a relationship between users, groups, and files & directories. Users can belong to multiple groups and groups can have multiple users. Every file and directory defines its permissions in terms of a user, a group, and "others" (all other users).<br><br>
User accounts are configured in <b>/etc/passwd</b> file and user password hashes are stored in the <b>/etc/shadow</b> file. Users are identified by an integer user ID (UID). The "root" user almost always has a UID of 0, and the system grants this user access to every file.<br><br>
Groups are configured in the <b>/etc/group</b> file. Users have a primary group, and can have multiple secondary (or supplementary) groups. By default, a user's primary group has the same name as their user account. <br><br>
All files & directories have a single owner and group. Permissions are defined in terms of read, write, and execute operations. There are three sets of permissions, one for the owner, one for the group, and one for all "other" users (can also be referred to as "world"). Only the owner can change permissions.<br><br>
There are two special permissions in Linux: setuid (SUID) bit and setgid (SGID) bit. With setuid, when set, files will get executed with the privileges of the file owner. When the SGID bit is set, the file will get executed with the privileges of the file group. When set on a directory, files created within that directory will inherit the group of the directory itself.<br><br>
