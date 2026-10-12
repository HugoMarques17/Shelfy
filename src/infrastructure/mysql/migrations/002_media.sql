CREATE TABLE IF NOT EXISTS media (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    media_type VARCHAR(15) NOT NULL,
    description VARCHAR(255) NULL,
    status VARCHAR(20) NULL,
    cover_url VARCHAR(255) NULL,
    published_at DATETIME NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    deleted_at DATETIME DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS mangas (
    id CHAR(36) PRIMARY KEY,
    chapter_number INT NOT NULL,
    content_rating VARCHAR(15) NOT NULL,
    author VARCHAR(100) NOT NULL,
    artist VARCHAR(100) NOT NULL,
    FOREIGN KEY (id)
        REFERENCES media (id)
        ON DELETE CASCADE
);
