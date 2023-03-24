# creating a file using puppet

file { '/tmp/school':
  content  => 'I love puppet',
  ensure   => file,
  mode     => '0744',
  owner    => www-data,
  group    => www-data,
}
