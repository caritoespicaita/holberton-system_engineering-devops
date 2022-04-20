# create a file puppet

file { 'create a file':
  path    => '/tmp/school',
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
