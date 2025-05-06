-- 6-bonus.sql
DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    -- Check if the project exists
    DECLARE project_id INT;

    -- Try to find the project ID
    SELECT id INTO project_id FROM projects WHERE name = project_name LIMIT 1;

    -- If the project doesn't exist, insert it
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Add the correction for the user and project
    INSERT INTO corrections (user_id, project_id, score) 
    VALUES (user_id, project_id, score);
END $$

DELIMITER ;
