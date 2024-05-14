# Ensure that the parent directory exists
file { '/home/root':
    ensure  => directory,
    owner   => 'root',
    group   => 'root',
    mode    => '0755',
}

# Define SSH directory
file { '/home/root/.ssh':
    ensure  => directory,
    owner   => 'root',
    group   => 'root',
    mode    => '0700',
    require => File['/home/root'],
}

# Define SSH client configuration for connecting to the server
file { '/home/root/.ssh/config':
    ensure  => present,
    owner   => 'root',
    group   => 'root',
    mode    => '0600',
    content => "
Host 266400-web-01
    HostName 100.25.142.221
    User ubuntu
    IdentityFile ~/.ssh/school
    PreferredAuthentications publickey
    PasswordAuthentication no
",
}

