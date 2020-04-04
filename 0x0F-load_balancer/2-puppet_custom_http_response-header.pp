# Puppet script to install a package

package { 'nginx':
  ensure => installed,
}

exec { 'nginx.conf':
  provider => shell,
  command  => 'sudo sed -i "/http {/a \ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf',
}
