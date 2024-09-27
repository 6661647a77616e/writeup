Sure, here's your information presented in a table format:

| Category       | Tool                             | Link                                                    |
|----------------|----------------------------------|---------------------------------------------------------|
| Forensics      | fotoforensics                    | [fotoforensics.com](https://fotoforensics.com)         |
| Steganography  | check layer of images            | [georgeom.net/StegOnline/image](https://georgeom.net/StegOnline/image) |
| General Purpose| cyberchef                        | [gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/) |
| General Purpose | Wapplyzer                       | [https://www.wappalyzer.com/apps/](https://www.wappalyzer.com/apps/) |
| Cryptography   | rsa                              | [devglan.com/online-tools/rsa-encryption-decryption](https://www.devglan.com/online-tools/rsa-encryption-decryption) |

hack

`eho` any weird string in any encoding
* base64 : echo picoCTF{D1d_u_kn0w_ppts_r_z1p5} | base64 -d




clean empty space using vscode regex replacements

basic enumeration + HTTP probing

`subfinder -d [example.com](http://example.com) | httpx -o example.httpx`

issues an HTTP request to the host

`curl -sk https://yourwebsite`

burte-force with different HTTP method

`ffuf -u [https://yourwebsite.site/FU](https://yourwebsite.site/FUXX)ZZ -w english-words.txt -mc all -fw 6`

`ffuf -x POST -u [https://yourwebsite.site/FU](https://yourwebsite.site/FUXX)ZZ -w english-words.txt -mc all -fw 6`

masscan, probed for HTTP(s) servers, and grabbed the HTTP titles.

`masscan -p 80,443 -iL ranges -oL out.txt`


---

# Wireshark filters

## WireShark filters
© http://www.lovemytool.com/blog/2010/04/top-10-wireshark-filters-by-chris-greer.html

```ip.addr == 10.0.0.1``` Sets a filter for any packet with 10.0.0.1, as either the source or dest

```ip.addr==10.0.0.1  && ip.addr==10.0.0.2``` sets a conversation filter between the two defined IP addresses

```http or dns``` sets a filter to display all http and dns

```tcp.port==4000``` sets a filter for any TCP packet with 4000 as a source or dest port

```tcp.flags.reset==1``` displays all TCP resets

```http.request``` displays all HTTP GET requests

```tcp contains traffic``` displays all TCP packets that contain the word ‘traffic’. Excellent when searching on a specific string or user ID

```!(arp or icmp or dns)``` masks out arp, icmp, dns, or whatever other protocols may be background noise. Allowing you to focus on the traffic of interest

```udp contains 33:27:58``` sets a filter for the HEX values of 0x33 0x27 0x58 at any offset

```tcp.analysis.retransmission``` displays all retransmissions in the trace. Helps when tracking down slow application performance and packet loss

```tcp.flags.syn == 1 && tcp.flags.ack == 1```

https://gist.github.com/githubfoam/08efac0343f98bd727caa32e6c81f655

