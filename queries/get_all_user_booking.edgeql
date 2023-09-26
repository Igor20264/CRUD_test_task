select Booking {user_id,start_time,end_time,comment}
filter .user_id.id = <uuid>$user_id