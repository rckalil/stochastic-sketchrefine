DROP TABLE IF EXISTS Stock_Investments_90;

DROP TABLE IF EXISTS Stock_Investments_45;

DROP TABLE IF EXISTS Stock_Investments_30;

DROP TABLE IF EXISTS Stock_Investments_15;

DROP TABLE IF EXISTS Stock_Investments_9;

DROP TABLE IF EXISTS Stock_Investments_3;

DROP TABLE IF EXISTS Stock_Investments_1;

DROP TABLE IF EXISTS Stock_Investments_half;

DROP TABLE IF EXISTS Stock_Investments_Volatility_1x;

DROP TABLE IF EXISTS Stock_Investments_Volatility_2x;

DROP TABLE IF EXISTS Stock_Investments_Volatility_5x;

DROP TABLE IF EXISTS Stock_Investments_Volatility_8x;

DROP TABLE IF EXISTS Stock_Investments_Volatility_10x;

DROP TABLE IF EXISTS Stock_Investments_Volatility_13x;

DROP TABLE IF EXISTS Stock_Investments_Volatility_17x;

DROP TABLE IF EXISTS Stock_Investments_Volatility_20x;

DROP TABLE IF EXISTS Stock_Investments_Volatility_Lambda_halfx;

DROP TABLE IF EXISTS Stock_Investments_Volatility_Lambda_1x;

DROP TABLE IF EXISTS Stock_Investments_Volatility_Lambda_2x;

DROP TABLE IF EXISTS Stock_Investments_Volatility_Lambda_3x;

DROP TABLE IF EXISTS Stock_Investments_Volatility_Lambda_4x;

DROP TABLE IF EXISTS Stock_Investments_Volatility_Lambda_5x;

DROP TABLE IF EXISTS Stock_Investments_1;

DROP TABLE IF EXISTS Stock_Investments_1;
CREATE TABLE Stock_Investments_1(
    id int not null unique,
    ticker varchar(10),
    sell_after int,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_5;
CREATE TABLE Stock_Investments_5(
    id int not null unique,
    ticker varchar(10),
    sell_after int,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_10;
CREATE TABLE Stock_Investments_10(
    id int not null unique,
    ticker varchar(10),
    sell_after int,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_15;
CREATE TABLE Stock_Investments_15(
    id int not null unique,
    ticker varchar(10),
    sell_after int,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_20;
CREATE TABLE Stock_Investments_20(
    id int not null unique,
    ticker varchar(10),
    sell_after int,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_25;
CREATE TABLE Stock_Investments_25(
    id int not null unique,
    ticker varchar(10),
    sell_after int,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_30;
CREATE TABLE Stock_Investments_30(
    id int not null unique,
    ticker varchar(10),
    sell_after int,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Quarterly;
CREATE TABLE Stock_Quarterly(
    id int not null unique,
    ticker varchar(10),
    sell_after int,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);