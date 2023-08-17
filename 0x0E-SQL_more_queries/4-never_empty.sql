USE `hbtn_0d_2`;

-- Create table if not exists
CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id` INT NOT NULL DEFAULT 1,
    `name` VARCHAR(256),
    PRIMARY KEY (`id`)
);
