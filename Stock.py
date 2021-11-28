class Stock() :
    def __init__(self) -> None:
        pass
    
    def getStockObj(self):
        print("@@@")
        print(self)
        return {
            "거래량" : "quant",
            "매수호가" : "ask_buy",
            "거래대금" : "amount",
            "시가총액" : "market_sum",
            "영업이익" : "operating_profit",
            "PER" : "per",
            "시가" : "open_val",
            "매도호가" : "ask_sell",
            "전일거래량" : "prev_quant",
            "자산총계" : "property_total",
            "영업이익증가율" : "operating_profit_increasing_rate",
            "ROE" : "roe",
            "고가" : "high_val",
            "매수총잔량" : "buy_total",
            "외국인비율" : "frgn_rate",
            "부채총계" : "debt_total",
            "당기순이익" : "net_income",
            "ROA" : "roa",
            "저가" : "low_val",
            "매도총잔량" : "sell_total",
            "상장주식수" : "listed_stock_cnt",
            "매출액" : "sales",
            "주당순이익" : "eps",
            "PBR" : "pbr",
        }