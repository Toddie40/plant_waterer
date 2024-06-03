DROP TABLE IF EXISTS log;
DROP TABLE IF EXISTS plants;

CREATE TABLE log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    req_url TEXT NOT NULL,
    req_origin TEXT NOT NULL,
    req_res TEXT NOT NULL
);

CREATE TABLE plants (
    sensor_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    desired_moisture FLOAT NOT NULL,
    moisture FLOAT NOT NULL,
    last_measured TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);