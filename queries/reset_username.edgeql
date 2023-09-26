update User
filter .id = <uuid>$id
set {
  updated := datetime_of_statement(),
  username := <str>$username
}