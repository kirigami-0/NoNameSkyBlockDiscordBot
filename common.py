import json
import discord
import ast

class Config:
    def __init__(self):
        with open('config.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)
    
    def getChannelId(self, key):
        """
        チャンネルIDを取得する

        Parameters
        ----------
        key : str
            チャンネル名

        Returns
        -------
        channel
            チャンネルID
        """
        return self.config["channel_id"][key]
    
    def get_lottery(self, key):
        """
        ランダム関数で使用するデータを取得する

        Parameters
        ----------
        key : str
            キー

        Returns
        -------
            取得したデータ
        """
        return self.config["lottery"][key]
    
    def set_config(self):
        """
        config.jsonを書き換える処理
        """
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4)

class Embed:
    def __init__(self, title, description, color=0xffffff):
        self.embed = discord.Embed(title=title ,description=description, color=color)
    
    def set_field(self, names, values, inline=True):
        """
        埋め込みのフィールドを設定する

        Parameters
        ----------
        names : list
            タイトル
        values : list
            内容
        inline : bool, optional
            インラインフラグ, by default True
        """
        for name, value in zip(names, values):
            self.embed.add_field(name, value, inline)
    
    def set_image(self, url, is_thumbnail=False):
        """
        画像を設定する

        Parameters
        ----------
        url : str
            画像URL
        is_thumbnail : bool, optional
            サムネイルフラグ, by default False
        """
        if is_thumbnail:
            self.embed.set_thumbnail(url)
        else:
            self.embed.set_image(url)
    
    def set_author(self, name, url="", icon_url=""):
        """
        作成者を設定する

        Parameters
        ----------
        name : _type_
            ヘッダーテキスト
        url : str, optional
            ヘッダーテキストのURL, by default ""
        icon_url : str, optional
            アイコンの画像URL, by default ""
        """
        self.embed.set_author(name, url, icon_url)
    
    def return_embed(self):
        """
        埋め込みメッセージを返す

        Returns
        -------
        Embed
            埋め込みメッセージ
        """
        return self.embed

def is_empty(data):
    """
    からデータチェック

    Parameters
    ----------
    data : any
        データ

    Returns
    -------
    boolean
        空データかどうかのフラグ
    """
    if data == []:
        return True
    elif data == "":
        return True
    elif data == ():
        return True
    elif data == None:
        return True
    return False

def convert_string_to_list(stringData, type='str'):
    """
    文字列をリストに変換する

    Parameters
    ----------
    stringData : str
        変換したい文字列
    type : str
        データ型

    Returns
    -------
    resultList : list
        変換したリストデータ
    """
    listData = ast.literal_eval(stringData)
    resultList = []
    if type == "str":
        for data in listData:
            resultList.append(str(data))
    elif type == 'int':
        for data in listData:
            resultList.append(int(data))
    elif type == "float":
        for data in listData:
            resultList.append(float(data))
    return resultList

def set_message(id, value):
    pass