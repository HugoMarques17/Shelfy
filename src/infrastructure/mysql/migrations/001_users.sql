CREATE TABLE IF NOT EXISTS users (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash TEXT DEFAULT NULL,
    birth_date DATE NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    deleted_at DATETIME DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS user_permissions (
    id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    permission VARCHAR(100) NOT NULL,
    user_id CHAR(36) NOT NULL,
    scope_type VARCHAR(70) NULL,
    scope_id CHAR(36) NULL,
    granted_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    granted_by CHAR(36) NOT NULL,
    UNIQUE KEY (permission , user_id , scope_type , scope_id),
    FOREIGN KEY (user_id)
        REFERENCES users (id),
    FOREIGN KEY (granted_by)
        REFERENCES users (id)
);
