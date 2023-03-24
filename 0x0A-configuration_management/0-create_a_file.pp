# creating a file using puppet

file { 'Puppet':
  path: '/tmp/schoo',
  permission: '0744',
  owner: 'www-data',
  group: 'www-data',
  content: 'I love puppet',
}
