
CREATE INDEX  IF NOT EXISTS ID_INDEX_PF_1 ON Stock_Investments_1(id);
CREATE INDEX  IF NOT EXISTS TICKER_INDEX_PF_1 ON Stock_Investments_1(id, ticker, sell_after);

CREATE INDEX  IF NOT EXISTS ID_INDEX_PF_Q ON Stock_Quarterly(id);
CREATE INDEX  IF NOT EXISTS TICKER_INDEX_PF_Q ON Stock_Quarterly(id, ticker, sell_after);
