SELECT exists(
    SELECT User
    filter .username = <str>$username
);