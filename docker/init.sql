CREATE SCHEMA IF NOT EXISTS fastapi;

CREATE TABLE IF NOT EXISTS fastapi.user (
    id uuid DEFAULT gen_random_uuid(),
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    PRIMARY KEY (id)
);

INSERT INTO fastapi.user (id, name, email)
VALUES ('a7549578-7cb4-4d45-8827-f544b077b5df', 'Cloud Strife', 'cloud.strife@ffvii.com');