update User
filter .id = <uuid>$id AND .username = <str>$username AND .created = <datetime>$created
set {
  updated := datetime_of_statement(),
  password := <str>$password
}