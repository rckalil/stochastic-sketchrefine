DROP TABLE IF EXISTS Stock_Investments_90;
CREATE TABLE Stock_Investments_90(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_45;
CREATE TABLE Stock_Investments_45(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_30;
CREATE TABLE Stock_Investments_30(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_15;
CREATE TABLE Stock_Investments_15(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_9;
CREATE TABLE Stock_Investments_9(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_3;
CREATE TABLE Stock_Investments_3(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);


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

DROP TABLE IF EXISTS Stock_Investments_half;
CREATE TABLE Stock_Investments_half(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_Volatility_1x;
CREATE TABLE Stock_Investments_Volatility_1x(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_Volatility_2x;
CREATE TABLE Stock_Investments_Volatility_2x(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_Volatility_5x;
CREATE TABLE Stock_Investments_Volatility_5x(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);


DROP TABLE IF EXISTS Stock_Investments_Volatility_8x;
CREATE TABLE Stock_Investments_Volatility_8x(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_Volatility_10x;
CREATE TABLE Stock_Investments_Volatility_10x(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_Volatility_13x;
CREATE TABLE Stock_Investments_Volatility_13x(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_Volatility_17x;
CREATE TABLE Stock_Investments_Volatility_17x(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_Volatility_20x;
CREATE TABLE Stock_Investments_Volatility_20x(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_Volatility_Lambda_halfx;
CREATE TABLE Stock_Investments_Volatility_Lambda_halfx(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_Volatility_Lambda_1x;
CREATE TABLE Stock_Investments_Volatility_Lambda_1x(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_Volatility_Lambda_2x;
CREATE TABLE Stock_Investments_Volatility_Lambda_2x(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_Volatility_Lambda_3x;
CREATE TABLE Stock_Investments_Volatility_Lambda_3x(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_Volatility_Lambda_4x;
CREATE TABLE Stock_Investments_Volatility_Lambda_4x(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);

DROP TABLE IF EXISTS Stock_Investments_Volatility_Lambda_5x;
CREATE TABLE Stock_Investments_Volatility_Lambda_5x(
    id int not null unique,
    ticker varchar(10),
    sell_after float,
    price float,
    volatility float,
    volatility_coeff float,
    drift float
);
