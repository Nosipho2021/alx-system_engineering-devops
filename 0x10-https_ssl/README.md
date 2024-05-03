# Enforcing HTTPS Traffic with HAProxy

## Overview

In this task, we configure HAProxy to enforce HTTPS traffic and automatically redirect HTTP traffic to HTTPS. This ensures that all communication with the website is encrypted, enhancing security and preventing any unencrypted traffic.

## Requirements

- This redirection should be transparent to the user.
- HAProxy should return a 301 status code for the redirection.
- HAProxy should redirect HTTP traffic to HTTPS.
- HAProxy configuration file must be shared as an answer file (`100-redirect_http_to_https`).

## Configuration Steps

1. **Update HAProxy Configuration:** Edit the HAProxy configuration file (`/etc/haproxy/haproxy.cfg`) to include a redirect rule for HTTP traffic.

    ```
    global
        # Global settings...

    defaults
        # Default settings...

    frontend http_front
        bind *:80
        mode http
        option forwardfor
        redirect scheme https code 301 if !{ ssl_fc }

    frontend https_front
        bind *:443 ssl crt /etc/ssl/certs/example.pem
        mode http
        option forwardfor
        # Other HTTPS configuration...

    backend www_backend
        # Backend configuration...

    listen stats
        bind *:8404
        mode http
        stats enable
        stats uri /
    ```

2. **Verify HAProxy Configuration:** Check the configuration for syntax errors using `sudo haproxy -c -f /etc/haproxy/haproxy.cfg`.

3. **Restart HAProxy:** Apply the changes by restarting HAProxy with `sudo service haproxy restart`.

4. **Test Redirection:** Visit your website using HTTP (e.g., `http://www.example.com`) and ensure that you are automatically redirected to HTTPS.

## Sharing HAProxy Configuration

Share your HAProxy configuration file (`/etc/haproxy/haproxy.cfg`) as the answer file (`100-redirect_http_to_https`). You can copy the content of the file to the answer file manually or use a command like `cat /etc/haproxy/haproxy.cfg > 100-redirect_http_to_https`.


