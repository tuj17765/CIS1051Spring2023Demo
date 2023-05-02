CREATE TABLE user_info (
    id TEXT NOT NULL PRIMARY KEY,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    userName TEXT NOT NULL,
    pwd TEXT NOT NULL
);

CREATE TABLE closet (
    id TEXT NOT NULL PRIMARY KEY,
    user_id TEXT NOT NULL,
    closet_ame TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_info (id)
);

    