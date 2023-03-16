# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Sequence, Mapping


def create( broker: str ) -> CommonConfig:
    if broker == "yh":
        return YH
    if broker == "ht":
        return HT
    if broker == "gj":
        return GJ
    if broker == "gf":
        return GF
    if broker == "ths":
        return CommonConfig
    if broker == "wk":
        return WK
    if broker == "htzq":
        return HTZQ
    if broker == "universal":
        return UNIVERSAL
    raise NotImplementedError

@dataclass ( frozen = True )
class CommonConfig:
    DEFAULT_EXE_PATH: str = ""
    TITLE: str = "网上股票交易系统5.0"

    # 交易所类型。 深圳A股、上海A股
    TRADE_STOCK_EXCHANGE_CONTROL_ID: int = 1003

    # 撤销界面上， 全部撤销按钮
    TRADE_CANCEL_ALL_ENTRUST_CONTROL_ID: int = 30001

    TRADE_SECURITY_CONTROL_ID: int = 1032
    TRADE_PRICE_CONTROL_ID: int = 1033
    TRADE_AMOUNT_CONTROL_ID: int = 1034

    TRADE_SUBMIT_CONTROL_ID: int = 1006

    TRADE_MARKET_TYPE_CONTROL_ID: int = 1541

    COMMON_GRID_CONTROL_ID: int = 1047

    COMMON_GRID_LEFT_MARGIN: int = 10
    COMMON_GRID_FIRST_ROW_HEIGHT: int = 30
    COMMON_GRID_ROW_HEIGHT: int = 16

    BALANCE_MENU_PATH: Sequence[ str ] = ["查询[F4]", "资金股票"]
    POSITION_MENU_PATH: Sequence[ str ] = ["查询[F4]", "资金股票"]
    TODAY_ENTRUSTS_MENU_PATH: Sequence[ str ] = ["查询[F4]", "当日委托"]
    TODAY_TRADES_MENU_PATH: Sequence[ str ] = ["查询[F4]", "当日成交"]

    BALANCE_CONTROL_ID_GROUP: Mapping[ str, int ] = {
        "资金余额": 1012,
        "可用金额": 1016,
        "可取金额": 1017,
        "股票市值": 1014,
        "总资产": 1015,
    }

    POP_DIALOD_TITLE_CONTROL_ID: int = 1365

    GRID_DTYPE = {
        "操作日期": str,
        "委托编号": str,
        "申请编号": str,
        "合同编号": str,
        "证券代码": str,
        "股东代码": str,
        "资金帐号": str,
        "资金帐户": str,
        "发生日期": str,
    }

    CANCEL_ENTRUST_ENTRUST_FIELD: str = "合同编号"
    CANCEL_ENTRUST_GRID_LEFT_MARGIN: int = 50
    CANCEL_ENTRUST_GRID_FIRST_ROW_HEIGHT: int = 30
    CANCEL_ENTRUST_GRID_ROW_HEIGHT: int = 16

    AUTO_IPO_SELECT_ALL_BUTTON_CONTROL_ID: int = 1098
    AUTO_IPO_BUTTON_CONTROL_ID: int = 1006
    AUTO_IPO_MENU_PATH: Sequence[ str ] = ["新股申购", "批量新股申购"]
    AUTO_IPO_NUMBER: str = '申购数量'


@dataclass ( frozen = True )
class YH( CommonConfig ):
    DEFAULT_EXE_PATH: str = r"C:\双子星-中国银河证券\Binarystar.exe"

    BALANCE_GRID_CONTROL_ID: int = 1308

    GRID_DTYPE = {
        "操作日期": str,
        "委托编号": str,
        "申请编号": str,
        "合同编号": str,
        "证券代码": str,
        "股东代码": str,
        "资金帐号": str,
        "资金帐户": str,
        "发生日期": str,
    }

    AUTO_IPO_MENU_PATH: Sequence[ str ] = ["新股申购", "一键打新"]


@dataclass ( frozen = True )
class HT( CommonConfig ):
    DEFAULT_EXE_PATH: str = r"C:\htzqzyb2\xiadan.exe"

    BALANCE_CONTROL_ID_GROUP: Mapping[ str, int ] = {
        "资金余额": 1012,
        "冻结资金": 1013,
        "可用金额": 1016,
        "可取金额": 1017,
        "股票市值": 1014,
        "总资产": 1015,
    }

    GRID_DTYPE = {
        "操作日期": str,
        "委托编号": str,
        "申请编号": str,
        "合同编号": str,
        "证券代码": str,
        "股东代码": str,
        "资金帐号": str,
        "资金帐户": str,
        "发生日期": str,
    }

    AUTO_IPO_MENU_PATH: Sequence[ str ] = ["新股申购", "批量新股申购"]


@dataclass ( frozen = True )
class GJ( CommonConfig ):
    DEFAULT_EXE_PATH: str = "C:\\全能行证券交易终端\\xiadan.exe"

    GRID_DTYPE = {
        "操作日期": str,
        "委托编号": str,
        "申请编号": str,
        "合同编号": str,
        "证券代码": str,
        "股东代码": str,
        "资金帐号": str,
        "资金帐户": str,
        "发生日期": str,
    }

    AUTO_IPO_MENU_PATH: Sequence[ str ] = ["新股申购", "新股批量申购"]


@dataclass ( frozen = True )
class GF( CommonConfig ):
    DEFAULT_EXE_PATH: str = "C:\\gfzqrzrq\\xiadan.exe"
    TITLE: str = "核新网上交易系统"

    GRID_DTYPE = {
        "操作日期": str,
        "委托编号": str,
        "申请编号": str,
        "合同编号": str,
        "证券代码": str,
        "股东代码": str,
        "资金帐号": str,
        "资金帐户": str,
        "发生日期": str,
    }

    AUTO_IPO_MENU_PATH: Sequence[ str ] = ["新股申购", "批量新股申购"]


@dataclass ( frozen = True )
class WK( HT ):
    pass


@dataclass ( frozen = True )
class HTZQ( CommonConfig ):
    DEFAULT_EXE_PATH: str = r"c:\\海通证券委托\\xiadan.exe"

    BALANCE_CONTROL_ID_GROUP: Mapping[ str, int ] = {
        "资金余额": 1012,
        "可用金额": 1016,
        "可取金额": 1017,
        "总资产": 1015,
    }

    AUTO_IPO_NUMBER: str = '可申购数量'


@dataclass ( frozen = True )
class UNIVERSAL( CommonConfig ):
    DEFAULT_EXE_PATH: str = r"c:\\ths\\xiadan.exe"

    BALANCE_CONTROL_ID_GROUP: Mapping[ str, int ] = {
        "资金余额": 1012,
        "可用金额": 1016,
        "可取金额": 1017,
        "总资产": 1015,
    }

    AUTO_IPO_NUMBER: str = '可申购数量'
