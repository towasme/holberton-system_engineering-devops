# create a exec that kills a process

exec { 'kill_process':
  command => '/usr/bin/pkill killmenow';
}
