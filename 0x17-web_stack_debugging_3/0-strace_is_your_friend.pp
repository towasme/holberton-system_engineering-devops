# change the wrong name placed in a file

exec { 'change name':
  provider => shell,
  command  => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
