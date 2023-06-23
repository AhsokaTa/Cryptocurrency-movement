CREATE TABLE "movements" (
	"id"	INTEGER UNIQUE,
	"date"	TEXT NOT NULL,
	"time"	INTEGER NOT NULL,
	"moneda_from"	TEXT NOT NULL,
	"cantidad_from"	REAL NOT NULL,
	"moneda_to"	TEXT NOT NULL,
	"cantidad_to"	REAL NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
	)  
