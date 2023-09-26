CREATE MIGRATION m1pcynqzxhkx6vazy67qlyjlmku4bkgakv2gchgdytqyzeueku2cla
    ONTO m1ioidv2gkyoh4mglv57zjwse75rhlwula5sj4kszfrryc7tl5leia
{
  ALTER TYPE default::Booking {
      ALTER LINK user_id {
          ON TARGET DELETE DELETE SOURCE;
      };
  };
};
