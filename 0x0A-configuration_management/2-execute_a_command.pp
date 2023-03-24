# creat manifest that kills a proceess
exec { 'killmenow':
  ensure => 'pkill',
}
