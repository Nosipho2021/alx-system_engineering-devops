Web tack Debugging #3

## Overview

This project involves debugging a WordPress website running on a LAMP stack (Linux, Apache, MySQL, and PHP). The main task is to identify and fix a 500 Internal Server Error returned by Apache, and automate the solution using Puppet.

## Project Tasks

### Task 0: Strace is Your Friend

**Objective**: Using `strace`, find out why Apache is returning a 500 error, fix the issue, and automate the solution using Puppet.

### Steps to Complete the Task

#### 1. Diagnosing the Problem

1. **Find the Apache Process ID (PID)**:
    ```sh
    ps aux | grep apache2
    ```

2. **Attach `strace` to the Apache Process**:
    ```sh
    sudo strace -p <PID>
    ```

3. **Send a Request to the Server**:
    ```sh
    curl -sI 127.0.0.1
    ```

4. **Analyze `strace` Output**:
    - Look for errors such as missing files, permission issues, or other failures.

#### 2. Fixing the Issue

Assuming the issue is a missing PHP file required by WordPress:

1. **Create or Verify the Missing File**:
    - Ensure the necessary PHP file exists in the correct directory.

2. **Create Puppet Manifest**:

    Create a file named `0-strace_is_your_friend.pp` with the following content:
    ```puppet
    # Puppet manifest to fix missing PHP file for WordPress

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
    ```

#### 3. Applying the Puppet Manifest

Apply the manifest:
```sh
sudo puppet apply 0-strace_is_your_friend.pp

