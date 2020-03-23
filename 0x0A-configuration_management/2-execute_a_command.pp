# create a exec that kills a process

exec { 'kill_process':
  path => '/usr/bin',
  command => 'pkill killmenow',
}
