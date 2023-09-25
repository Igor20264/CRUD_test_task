import datetime
import edgedb

client = edgedb.create_client()

client.query("""
    INSERT User {
        name := <str>$name,
        dob := <cal::local_date>$dob
    }
""", name="Bob", dob=datetime.date(1984, 3, 1))

user_set = client.query(
    "SELECT User {name, dob} FILTER .name = <str>$name", name="Bob")
# *user_set* now contains
# Set{Object{name := 'Bob', dob := datetime.date(1984, 3, 1)}}

client.close()