create database if not exists fahrradApp;
use fahrradApp;

create table if not exists Kunden
(
KundenID int auto_increment unique key primary key,
VorName varchar(64) not null,
NachName varchar(64) not null,
Geburtsdatum date not null,
Email varchar(64) not null
);

create table if not exists Fahrrad
(
FahrradID int auto_increment unique key primary key,
Model varchar(64) not null,
Farbe varchar(32) not null,
Reifen varchar(128) not null,
Preis decimal not null
);

create table if not exists Fahrradmarke
(
FahrradMarkenID int auto_increment unique key primary key,
FahrradID int, constraint fahhradForeignKey foreign key (FahrradID) references Fahrrad (FahrradID),
MarkenName varchar(64) not null,
CEO varchar(64) not null,
Email varchar(64) not null,
Standort varchar(128) not null
);

create table if not exists Ausleihen
(
AusleihenID int auto_increment unique key primary key,
AusleiheDatum date not null,
RückgabeDatum date not null,
KundenID int,
FahrradID int
);