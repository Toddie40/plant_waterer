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
    sensor_no INTEGER PRIMARY KEY,
    plant_name TEXT NOT NULL,
    moisture FLOAT NOT NULL,
    last_watered TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    moisture_threshold FLOAT NOT NULL
);

INSERT INTO plants (plant_name, moisture, last_watered, moisture_threshold)
VALUES
("empty", 0, "2024-06-04T13:47:26", 0),
("empty", 0, "2024-06-04T13:47:26", 0),
("empty", 0, "2024-06-04T13:47:26", 0);
