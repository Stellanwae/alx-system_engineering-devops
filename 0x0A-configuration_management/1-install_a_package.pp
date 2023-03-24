# Code to install flask from pip3
package { 'flask':
  path => '/usr/bin/'
  ensure => '2.1.0',
  provider => 'pip3',
 }
