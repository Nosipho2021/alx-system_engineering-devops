#!/usr/bin/env puppet

# Setup New Ubuntu server with nginx

# Update system
exec { 'update_system':
  command => '/usr/bin/apt-get update',
  path    => ['/usr/bin', '/bin'],
  refreshonly => true,
}

# Install nginx package
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update_system'],
}

# Create index.html file
file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure redirection
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location / {
        root /var/www/html;
    }
}
",
  require => Package['nginx'],
}

# Ensure nginx service is running
service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}

