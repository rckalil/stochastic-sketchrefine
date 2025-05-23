SELECT PACKAGE(*) AS P
FROM Lineitem_6000000
SUCH THAT 
COUNT(*) <= 30 AND 
SUM(Tax) <= 0.03 AND 
SUM(QUANTITY) <= 10 WITH PROBABILITY >= 0.95 AND 
SUM(PRICE) >= 750000 WITH PROBABILITY >=0.95
MAXIMIZE EXPECTED SUM(PRICE)