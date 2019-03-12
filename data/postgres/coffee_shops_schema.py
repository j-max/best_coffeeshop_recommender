CREATE TABLE IF NOT EXISTS CoffeeShops (
    licenseID varchar(500) NOT NULL
    businessName varchar(500) NOT NULL,
    rating varchar(500) DEFAULT NULL,
    reviews varchar(500) DEFAULT NULL
    address varchar(500) NOT NULL,
    latitude int NOT NULL,
    longitude int NOT NULL,
    PRIMARY KEY (licenseID)
);

CREATE TABLE IF NOT EXISTS CoffeeShops (
   yelpID          varchar(500) NOT NULL,
   yelpAlias       varchar(500) NOT NULL,
   yelpIsClosed    BOOLEAN NOT NULL,
   address_display varchar(500) NOT NULL,
   address1        varchar(500) NOT NULL,
   address_zip     varchar(500) NOT NULL,
   latitude        In NOT NULL,
   longitude       int NOT NULL,
   pricing         varchar(20) DEFAULT NULL
   reviews         varchar(1000) DEFAULT NULL,
   rating          int DEFAULT NULL,
   review_count   int DEFAULT NULL

    PRIMARY KEY (yelpID)


