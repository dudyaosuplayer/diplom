\c cnrprod-team-58619;

CREATE SCHEMA IF NOT EXISTS usr;

CREATE TABLE IF NOT EXISTS usr.user (
  id SERIAL PRIMARY KEY,
  full_name VARCHAR(255),
  email VARCHAR(255),
  role INTEGER,
  hash_password VARCHAR(255),
  cookie VARCHAR(8)
);

CREATE SCHEMA IF NOT EXISTS prjct;

CREATE TABLE IF NOT EXISTS prjct.projects (
  id INTEGER,
  name VARCHAR(255),
  description TEXT,
  goals TEXT,
  deadline DATE,
  status INTEGER,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS prjct.assignee (
    id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES prjct.projects(id),
    user_id INTEGER REFERENCES usr.user(id)
);

CREATE TABLE IF NOT EXISTS prjct.task (
  id SERIAL PRIMARY KEY,
  parent_task_id INTEGER,
  project_id INTEGER REFERENCES prjct.projects(id),
  assignee_id INTEGER REFERENCES prjct.assignee(id),
  description TEXT,
  name VARCHAR(255),
  priority INTEGER,
  date_creation timestamptz,
  due_date DATE,
  status INTEGER
);

CREATE TABLE IF NOT EXISTS prjct.comments (
  id SERIAL PRIMARY KEY,
  task_id INTEGER REFERENCES prjct.task(id),
  user_id INTEGER REFERENCES usr.user(id),
  comment TEXT,
  timestamp TIMESTAMP
);

CREATE SCHEMA IF NOT EXISTS lg;

CREATE TABLE lg.log_table (
    log_id SERIAL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    operation_type VARCHAR(50),
    additional_info VARCHAR(255),
    task_id INTEGER REFERENCES prjct.task(id),
    user_id INTEGER REFERENCES usr.user(id)
);

DROP TABLE lg.log_table CASCADE;
DROP TABLE prjct.task CASCADE ;
DROP TABLE prjct.projects CASCADE ;
DROP TABLE usr.user CASCADE ;

INSERT INTO prjct.projects (id, name, description, goals, deadline)
VALUES ('1','Название проекта', 'Описание проекта', 'Цели проекта', '2022-12-31');

INSERT INTO prjct.projects (id, name, description, goals, deadline)
VALUES ('2','Название проекта', 'Описание проекта', 'Цели проекта', '2022-12-31');


-- Удаление внешнего ключа для столбца project_id
ALTER TABLE prjct.task DROP CONSTRAINT IF EXISTS task_project_id_fkey;

-- Удаление внешнего ключа для столбца assignee_id
ALTER TABLE prjct.task DROP CONSTRAINT IF EXISTS task_assignee_id_fkey;


-- Создание внешнего ключа для столбца project_id
ALTER TABLE prjct.task ADD CONSTRAINT task_project_id_fkey FOREIGN KEY (project_id) REFERENCES prjct.projects(id);

-- Создание внешнего ключа для столбца assignee_id
ALTER TABLE prjct.task ADD CONSTRAINT task_assignee_id_fkey FOREIGN KEY (assignee_id) REFERENCES prjct.assignee(id);


TRUNCATE TABLE prjct.task ;