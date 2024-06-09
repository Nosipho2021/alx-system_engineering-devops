# This Puppet manifest ensures the wp-config.php file exists and has the correct permissions

file { '/var/www/html/wp-config.php':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  content => template('wordpress/wp-config.php.erb'),
}

# Ensure the Apache service is running
service { 'apache2':
  ensure => running,
  enable => true,
}

