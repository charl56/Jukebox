-- Create Database
CREATE DATABASE jukebox;

-- Use Database
USE jukebox;

-- CREATE TABLE list_cd
CREATE TABLE cd_list(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    artiste varchar(20) NULL,
    album_name varchar(20) NOT NULL,   
    nb_tracks INT NOT NULL,
    pos_x INT,
    pos_y INT,
    dispo BOOLEAN
);

--  Add data
INSERT INTO cd_list ( artiste, album_name, nb_tracks, pos_x, pos_y, dispo) VALUES
    ('Luv Resval', 'Etoile Noire', 19, 0, 0, true),
    ('Freeze Corleone', 'L M F', 17, 0, 0, true),
    ('Zamdane', 'Affamé saison 2', 8, 0, 0, true),
    ('Zamdane', 'Couleur de ma peine', 18, 0, 0, true);

--  Create table tracklist
CREATE TABLE tracklist(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_album INT NOT NULL REFERENCES cd_list(id),
    name varchar(20) NOT NULL
);

--  Add data
INSERT INTO tracklist ( id_album, name) VALUES
    (36, 'Boussole'),    
    (36, 'J rêve'),    
    (36, 'Personne'),    
    (2, 'titre 1'),    
    (2, 'titre 2'),    
    (3, 'titre 1');    