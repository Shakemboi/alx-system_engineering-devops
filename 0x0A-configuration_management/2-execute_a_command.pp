# kill process killmenow

exec { 'kill_killmenow_process':
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true,
  provider   => 'shell'
}
