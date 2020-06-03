# coding: utf-8
from sqlalchemy import Column, Index, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class QqmusicAlbum(Base):
    __tablename__ = 'qqmusic_album'

    id = Column(String(128), primary_key=True, unique=True)
    epoch = Column(String(32))
    web_mid = Column(String(40), nullable=False)
    name = Column(String(200), server_default=text("''"))
    picture_url = Column(String(400), server_default=text("''"))
    pic_str = Column(String(200), server_default=text("''"))
    pic = Column(String(200))
    release_date = Column(String(20), server_default=text("''"))
    artist_web_ids = Column(String(200), server_default=text("''"))
    artist_names = Column(String(255))
    share_num = Column(BIGINT(40))
    comment_num = Column(BIGINT(40))
    play_num = Column(BIGINT(40))
    collect_num = Column(BIGINT(40))
    intro = Column(LONGTEXT)
    music_web_mids = Column(Text)
    status = Column(INTEGER(11))
    createtime = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


t_qqmusic_playinfo = Table(
    'qqmusic_playinfo', metadata,
    Column('id', String(32), nullable=False, index=True),
    Column('epoch', String(20)),
    Column('listenCount', BIGINT(40)),
    Column('topTitle', String(255), server_default=text("''")),
    Column('type', String(255)),
    Column('status', String(255)),
    Column('createtime', TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    Index('web_id', 'id', 'epoch', unique=True)
)


class QqmusicPlaylist(Base):
    __tablename__ = 'qqmusic_playlist'

    id = Column(String(32), primary_key=True, index=True)
    songId = Column(BIGINT(22))
    name = Column(String(200), nullable=False)
    url = Column(String(400), nullable=False)
    web_mid = Column(String(60), index=True)
    artist_web_mids = Column(String(255))
    artist_web_ids = Column(String(255), nullable=False)
    artist_names = Column(String(255))
    album_web_id = Column(INTEGER(10), nullable=False)
    album_web_mid = Column(String(40), server_default=text("''"))
    term = Column(String(32), index=True, server_default=text("''"))
    epoch = Column(String(32))
    rank = Column(INTEGER(11), index=True)
    rankType = Column(INTEGER(11))
    rankValue = Column(String(255))
    recType = Column(INTEGER(11))
    vid = Column(String(255))
    is_only = Column(TINYINT(1), server_default=text("'0'"))
    pay_info = Column(Text)
    pay_month = Column(INTEGER(11))
    price_track = Column(INTEGER(11))
    price_album = Column(INTEGER(11))
    pay_play = Column(INTEGER(11))
    pay_down = Column(INTEGER(11))
    pay_status = Column(INTEGER(11))
    time_free = Column(INTEGER(11))
    status = Column(INTEGER(11), server_default=text("'0'"))
    createtime = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class QqmusicRanklist(Base):
    __tablename__ = 'qqmusic_ranklist'

    id = Column(String(32), primary_key=True)
    name = Column(String(32))
    web_id = Column(String(32))
    epoch = Column(String(255))
    is_del = Column(TINYINT(1), server_default=text("'0'"))
    update_ts = Column(INTEGER(11))
    create_ts = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class QqmusicSong(Base):
    __tablename__ = 'qqmusic_song'
    __table_args__ = (
        Index('i_', 'id', 'epoch'),
    )

    id = Column(String(64), primary_key=True, index=True)
    epoch = Column(String(32))
    web_id = Column(BIGINT(22))
    web_mid = Column(String(60))
    rank_list_id = Column(String(32))
    star = Column(BIGINT(20))
    bullet_num = Column(BIGINT(40))
    comment_num = Column(BIGINT(40), server_default=text("'0'"))
    status = Column(TINYINT(4))
    createtime = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Test(Base):
    __tablename__ = 'test'

    id = Column(INTEGER(11), primary_key=True)
    v1 = Column(String(255))
    v2 = Column(String(255))
