fest to fix missing PHP file for WordPress

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

