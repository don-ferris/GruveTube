CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role ENUM('admin', 'user') NOT NULL
);

CREATE TABLE subscriptions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    channel_url TEXT NOT NULL,
    subscription_type ENUM('none', 'all', 'limited_number', 'limited_age') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE downloads (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    video_url TEXT NOT NULL,
    status ENUM('queued', 'downloading', 'completed', 'failed') NOT NULL,
    file_path TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
