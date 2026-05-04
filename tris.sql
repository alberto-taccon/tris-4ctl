CREATE TABLE users (
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(33) NOT NULL,
    CF VARCHAR(33) UNIQUE NOT NULL,
    winrate FLOAT NOT NULL DEFAULT 0.0
);

CREATE TABLE match_users (
    id_m_u INT PRIMARY KEY AUTO_INCREMENT,
    id_user_1 INT NOT NULL,
    id_user_2 INT NOT NULL,
    date datetime NOT NULL,
    FOREIGN KEY (id_user_1) REFERENCES users (id_user),
    FOREIGN KEY (id_user_2) REFERENCES users (id_user)
);

CREATE TABLE match_results (
    id_match_results INT PRIMARY KEY AUTO_INCREMENT,
    id_m_u INT NOT NULL,
    id_user_vincitore INT NULL,
    FOREIGN KEY (id_m_u) REFERENCES match_users (id_m_u),
    FOREIGN KEY (id_user_vincitore) REFERENCES users (id_user)
);