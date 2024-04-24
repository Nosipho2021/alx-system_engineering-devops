0x0C. Web server

# Web Server Configuration with Bash, Puppet, and Nginx

## Introduction
This repository contains scripts and manifests to automate the installation, configuration, and management of web servers using Bash scripting, Puppet, and Nginx.

## Task List
1. [Transfer a file to your server](#task-0-transfer-a-file-to-your-server)
2. [Setup a domain name](#task-1-setup-a-domain-name)
3. [Redirection](#task-2-redirection)
4. [Not found page 404](#task-3-not-found-page-404)
5. [Install Nginx web server (w/ Puppet)](#task-4-install-nginx-web-server-with-puppet)

## Task 0: Transfer a file to your server
### Description
Write a Bash script that transfers a file from the client to a server using SCP.

### Usage
```bash
./transfer_file.sh PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY

## Task 1: Setup a domain name
### Description
Configure DNS settings to set up a domain name for your server.

### Requirements
Provide the domain name only (e.g., example.tech), no subdomain.
Configure DNS records with an A entry to point to your web-01 IP address.


Got it. Here's how you can structure your README.md file to cover tasks 0 to 5, with the topic focusing on Web Server:

markdown
Copy code
# Web Server Configuration with Bash, Puppet, and Nginx

## Introduction
This repository contains scripts and manifests to automate the installation, configuration, and management of web servers using Bash scripting, Puppet, and Nginx.

## Task List
1. [Transfer a file to your server](#task-0-transfer-a-file-to-your-server)
2. [Setup a domain name](#task-1-setup-a-domain-name)
3. [Redirection](#task-2-redirection)
4. [Not found page 404](#task-3-not-found-page-404)
5. [Install Nginx web server (w/ Puppet)](#task-4-install-nginx-web-server-with-puppet)
------------------------------------------------------------------------------------
## Task 0: Transfer a file to your server
### Description
Write a Bash script that transfers a file from the client to a server using SCP.

### Usage
```bash
./transfer_file.sh PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
-----------------------------------------------------------------------------------
## Task 1: Setup a domain name
### Description
Configure DNS settings to set up a domain name for your server.

### Requirements
Provide the domain name only (e.g., example.tech), no subdomain.
Configure DNS records with an A entry to point to your web-01 IP address.
-----------------------------------------------------------------------------------
## Task 2: Redirection
### Description
Configure Nginx server to redirect /redirect_me to another page.

### Requirements
Use a "301 Moved Permanently" redirection.
Use the Bash script from Task 1 (1-install_nginx_web_server) and modify it to configure the redirection.
-----------------------------------------------------------------------------------
## Task 3: Not found page 404
### Description
Configure Nginx server to have a custom 404 page that contains the string "Ceci n'est pas une page".

### Requirements
Return an HTTP 404 error code.
The page must contain the string "Ceci n'est pas une page".
------------------------------------------------------------------------------------
## Task 4: Install Nginx web server (w/ Puppet)
### Description
Install and configure Nginx server using Puppet.

### Requirements
Nginx should be listening on port 80.
Return "Hello World!" when querying Nginx at its root (/) with a GET request.
Set up a "301 Moved Permanently" redirect for /redirect_me.
-----------------------------------------------------------------------------------

