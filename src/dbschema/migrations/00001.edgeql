CREATE MIGRATION m1ioidv2gkyoh4mglv57zjwse75rhlwula5sj4kszfrryc7tl5leia
    ONTO initial
{
  CREATE TYPE default::User {
      CREATE REQUIRED PROPERTY created: std::datetime {
          SET default := (std::datetime_of_statement());
          SET readonly := true;
      };
      CREATE REQUIRED PROPERTY password: std::str;
      CREATE REQUIRED PROPERTY updated: std::datetime {
          SET default := (std::datetime_of_statement());
      };
      CREATE REQUIRED PROPERTY username: std::str {
          CREATE CONSTRAINT std::exclusive;
      };
  };
  CREATE TYPE default::Booking {
      CREATE REQUIRED LINK user_id: default::User;
      CREATE PROPERTY comment: std::str;
      CREATE REQUIRED PROPERTY end_time: std::datetime;
      CREATE REQUIRED PROPERTY start_time: std::datetime;
  };
};
