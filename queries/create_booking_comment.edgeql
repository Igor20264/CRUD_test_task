INSERT Booking {
    user_id := (
    select User
    filter .id = <uuid>$id
    ),
    start_time := <datetime>$start,
    end_time := <datetime>$end,
    comment := <str>$comment
};