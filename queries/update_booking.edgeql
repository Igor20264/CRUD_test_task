update Booking
filter .id = <uuid>$id
set {
  comment := <str>$comment,
  end_time := <datetime>$end,
  start_time := <datetime>$start,
}