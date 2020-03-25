# Permission to connect the server withut authentication

file_line { 'change_passw':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton';
}

file_line { 'turn ident off':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => 'PasswordAuthentication yes';
}
