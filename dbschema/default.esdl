module default {
    type User {
        required username: str {
            constraint exclusive;
        }
        required password: str;
        required created: datetime {
            readonly := true;
            default := datetime_of_statement();
        }
        required updated: datetime {
            default := datetime_of_statement();
        }
    }

    type Booking {
        required user_id: User;
        required start_time: datetime;
        required end_time: datetime;
        comment: str;
    }
}
