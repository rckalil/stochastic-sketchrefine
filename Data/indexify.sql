
CREATE INDEX  IF NOT EXISTS ID_INDEX_PF_1 ON Stock_Investments_1(id);
CREATE INDEX  IF NOT EXISTS TICKER_INDEX_PF_1 ON Stock_Investments_1(id, ticker, sell_after);

CREATE INDEX  IF NOT EXISTS ID_INDEX_PF_Q ON Stock_Quarterly(id);
CREATE INDEX  IF NOT EXISTS TICKER_INDEX_PF_Q ON Stock_Quarterly(id, ticker, sell_after);

CREATE INDEX  IF NOT EXISTS ID_INDEX_PF_5 ON Stock_Investments_5(id);
CREATE INDEX  IF NOT EXISTS TICKER_INDEX_PF_5 ON Stock_Investments_5(id, ticker, sell_after);

CREATE INDEX  IF NOT EXISTS ID_INDEX_PF_10 ON Stock_Investments_10(id);
CREATE INDEX  IF NOT EXISTS TICKER_INDEX_PF_10 ON Stock_Investments_10(id, ticker, sell_after);

CREATE INDEX  IF NOT EXISTS ID_INDEX_PF_15 ON Stock_Investments_15(id);
CREATE INDEX  IF NOT EXISTS TICKER_INDEX_PF_15 ON Stock_Investments_15(id, ticker, sell_after);

CREATE INDEX  IF NOT EXISTS ID_INDEX_PF_20 ON Stock_Investments_20(id);
CREATE INDEX  IF NOT EXISTS TICKER_INDEX_PF_20 ON Stock_Investments_20(id, ticker, sell_after);

CREATE INDEX  IF NOT EXISTS ID_INDEX_PF_25 ON Stock_Investments_25(id);
CREATE INDEX  IF NOT EXISTS TICKER_INDEX_PF_25 ON Stock_Investments_25(id, ticker, sell_after);

CREATE INDEX  IF NOT EXISTS ID_INDEX_PF_30 ON Stock_Investments_30(id);
CREATE INDEX  IF NOT EXISTS TICKER_INDEX_PF_30 ON Stock_Investments_30(id, ticker, sell_after);