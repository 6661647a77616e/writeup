1. Reader

> Salam jumaat @everyone, here jumaats challenge. It is privilege escalation based on CVE-2019-14287. Feel free to check it out :).
> Privilege escalation is the process by which a user gains elevated access to resources that are normally protected from that user's standard capabilities. This can occur in two main forms:
  
  Vertical Privilege Escalation: A lower-privileged user gains the permissions of a higher-privileged user, such as a regular user becoming an administrator.
  
  Horizontal Privilege Escalation: A user gains the permissions of another user with the same privilege level, often to access information or resources they are not authorized to access.
  
  Privilege escalation can happen due to system vulnerabilities, misconfigurations, or through exploitation of application bugs. It's a critical security issue as it can allow unauthorized users to compromise the entire system or network.
  
  Creds :
  ssh [ctf-player@ice-training.syamilyusof.com](mailto:ctf-player@ice-training.syamilyusof.com) -p 2222
  Password : verysecure
  
  Dockerfile : https://drive.google.com/file/d/1dkbyr81Ji2rmwYn6npOGKQPzM-3LE75y/view?usp=drive_link

1. This challenge based on CVE-2019-14287
    
    <aside>
    💡 In Sudo before 1.8.28, an attacker with access to run as ALL sudoer account can bypass certain policy blacklists and session PAM modules, and can cause incorrect logging, by invoking sudo with a crafted user ID. For example, this allows bypass of !root configuration, and USER= logging, for a "sudo -u \#$((0xffffffff))" command.
    
    </aside>
    
2. To solve this challenge first we need to connect to the challenge using ssh
3. Now we can do sudo -l
    
    <aside>
    💡 sudo -l command is used to list the commands that a user is allowed to run using 'sudo
    
    </aside>
    

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/703f9dd9-36fd-453d-93d3-099f508c8cdf/263919ba-ea01-4c27-9f7f-c8006042f8d9/Untitled.png)

1. The `(ALL, !root) /bin/base64` means that user(ctf-player) in this case can run the /bin/base64 command as any user except root. Base64 command can do some encode and decode in base64.
2. Now we can craft our payload to run as user `-u#-1` in this case Sudo treat it as 0 which is root. 
    1. Payload : `sudo -u#-1 base64 /root/flag.txt`
    2. Explanation : This command encodes the contents of `/root/flag` using Base64 encoding as `root` privileges through sudo. 
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/703f9dd9-36fd-453d-93d3-099f508c8cdf/cb1b164b-d24d-4164-8af9-b59920c0214a/Untitled.png)
    
3. Now we can decode it using `base64 -d`
