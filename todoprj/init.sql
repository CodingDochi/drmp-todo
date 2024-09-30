-- backend/init.sql
GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

-- 테이블 ToDoList 생성
CREATE TABLE todo_todolist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- 테이블 ToDoListItem 생성
CREATE TABLE todo_todolistitem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    todo_list_id INT NOT NULL,
    label VARCHAR(255) NOT NULL,
    checked BOOLEAN DEFAULT FALSE,
    item_id CHAR(36) NOT NULL, -- UUID 필드를 위해 CHAR(36) 사용
    FOREIGN KEY (todo_list_id) REFERENCES todo_todolist(id) ON DELETE CASCADE,
    UNIQUE (item_id) -- UUID 필드를 고유하게 설정
);
