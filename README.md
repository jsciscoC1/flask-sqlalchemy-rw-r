Experiments with application level load balancing for read-write master, read replica SQL set ups.

### Goal
The goal of this experiment is to figure out a few possible ways to configure Flask + SQLAlchemy to handle horizontally scaled databases. In other words, how to read from read-only replicas and write to just the master database.

### How to get started
* **Starting the local databases**
  * docker-compose up -d
* **Creating tables (e.g. dbinit)**
  * pipenv run flask db upgrade
* **Testing**
  * Connect to each postgres instance via
    * psql -U postgres -h localhost -p 49153 (master)
    * psql -U postgres -h localhost -p 49154 (replica)
    * Confirm entries match
      * select * from books;
      * select * from authors;
