# Code to install flask from pip3
package { 'flask':
  path => '/usr/bin/',
  ensure => 'installed',
  provider => 'pip3',
 }
