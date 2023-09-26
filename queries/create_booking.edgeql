INSERT Booking {
    user_id := (
        SELECT User
        filter .id = <uuid>$id),
    start_time := <datetime>$start,
    end_time := <datetime>$end
};