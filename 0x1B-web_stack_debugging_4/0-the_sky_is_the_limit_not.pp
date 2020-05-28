# change the wrong number placed in a file

exec { 'change number of request':
  provider => shell,
  command  => 'sed -i "s/15/2000/g" /etc/default/nginx',
  command  => 'sudo service nginx restart',
}
