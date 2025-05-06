-- 5-valid_email.sql
DELIMITER $$

CREATE TRIGGER reset_valid_email_before_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email is being changed
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;  -- Reset valid_email to 0 when email changes
    END IF;
END $$

DELIMITER ;
