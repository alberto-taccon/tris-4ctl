CREATE TABLE users {
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(33) NOT NULL,
    CF VARCHAR(33) UNIQUE NOT NULL,
    winrate FLOAT(33) NOT NULL
}

CREATE TABLE match {
    id_match INT PRIMARY AUTO_INCREMENT,
    id_m_u INT,
    FOREIGN KEY (id_m_u) REFERENCES match_users (id_m_u)
}

CREATE TABLE match_users {
    id_m_u INT PRIMARY,
    id_user INT,
    id_match INT,
    FOREIGN KEY (id_user) REFERENCES match_users (id_user)
    FOREIGN KEY (id_match) REFERENCES match_users (id_match)
    date datetime
}

