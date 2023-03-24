# creating a file using puppet

file { 'school':
  ensure: 'file',
  path: '/tmp/school',
  permission: '0744',
  owner: 'www-data',
  group: 'www-data',
  content: 'I love puppet',
}
