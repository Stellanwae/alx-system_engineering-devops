# creat manifest that kills a proceess
exec { 'killmenow':
  command  => 'usr/bin/pkill killmenow',
  provider => 'shell',
}
