0x0F. Load balancer
DevOps
SysAdmin

# Web Server Redundancy and Load Balancing Project

This project aims to improve the reliability and scalability of our web infrastructure by introducing redundancy for the web servers and implementing a load balancer to distribute incoming traffic.

## Overview

In this project, we'll be performing the following tasks:

1. **Double the number of webservers**: Configure `web-02` to be identical to `web-01` and ensure both servers include a custom HTTP response header in Nginx.
   
2. **Install your load balancer**: Install and configure HAProxy on `lb-01` server to distribute traffic between `web-01` and `web-02` using a round-robin algorithm.

## Project Structure

The project consists of the following components:

- `0-custom_http_response_header`: Bash script to configure Nginx with a custom HTTP response header on web servers.
- `1-install_load_balancer.sh`: Bash script to install and configure HAProxy on the load balancer server.
- `README.md`: Overview of the project and instructions for setup and usage.

## Usage

To use the provided scripts:

1. SSH into each server (`web-01`, `web-02`, `lb-01`).
2. Copy the corresponding script (`0-custom_http_response_header` or `1-install_load_balancer.sh`) to the server.
3. Make the script executable (`chmod +x script_name.sh`).
4. Execute the script (`./script_name.sh`) to configure the server according to the task requirements.

## Requirements

- Ubuntu 16.04 LTS
- Bash scripting
- HAProxy for load balancing
- Nginx for web server configuration
- Shellcheck for script validation

## Author

[Your Name]

## License

This project is licensed under the [MIT License](LICENSE).

