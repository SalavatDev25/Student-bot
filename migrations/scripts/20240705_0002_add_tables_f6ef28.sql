CREATE TABLE IF NOT EXISTS app.users
(
    id                BIGINT        PRIMARY KEY,
    name              VARCHAR(255)  NOT NULL,
    group_number      VARCHAR(255)  NOT NULL
);

CREATE TABLE IF NOT EXISTS app.departament
(
    id                BIGINT        PRIMARY KEY,
    name              VARCHAR(255)  NOT NULL
);

CREATE TABLE IF NOT EXISTS app.statement
(
    id               BIGINT        PRIMARY KEY,
    title            VARCHAR(255)  NOT NULL,
    message          TEXT          NOT NULL,
    user_id          BIGINT        REFERENCES app.users (id) NOT NULL,
    departament_id   BIGINT        REFERENCES app.departament (id) NOT NULL,
    created_at       TIMESTAMPTZ   DEFAULT  CURRENT_TIMESTAMP
);
