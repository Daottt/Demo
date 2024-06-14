
create TABLE UserType(
    id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create TABLE Users(
    id integer PRIMARY KEY autoincrement,
    fio varchar(50),
    phone_number varchar(50),
    login varchar(50) not null unique,
    password varchar(50) not null,
    user_type_id integer,
    foreign key (user_type_id) references UserType(id)
);

create TABLE TaskStatus(
    id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create TABLE TechType(
    id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create TABLE Task(
    id integer PRIMARY KEY autoincrement,
    status_id integer,
    tech_type_id integer,
    tech_model varchar(50),
    problem_description varchar(100),
    repair_parts varchar(100),
    start_date date,
    completion_date date,
    master_id integer,
    client_id integer,
    foreign key (status_id) references  TaskStatus(id),
    foreign key (tech_type_id) references  TechType(id),
    foreign key (master_id) references  Users(id),
    foreign key (client_id) references  Users(id)
);

create TABLE Comments(
    id integer PRIMARY KEY autoincrement,
    text varchar(200),
    task_id integer,
    master_id integer,
    foreign key (task_id) references  Task(id),
    foreign key (master_id) references  Users(id)
);

insert into UserType(name)
    values("Пользователь"), ("Менеджер"), ("Администратор");

insert into TaskStatus(name)
    values("В ожидании"), ("В работе"), ("Выполнено");

insert into Users(fio, phone_number, login, password, user_type_id)
    values("fio", "111-111-111", "1", "1", "3");