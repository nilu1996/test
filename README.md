CREATE ROLE postgres WITH SUPERUSER LOGIN PASSWORD 'postgres';

ALTER ROLE postgres WITH PASSWORD 'postgres';


pg_restore -U postgres -d your_database_name /home/sva/bison/bison/amex-1109.backup
