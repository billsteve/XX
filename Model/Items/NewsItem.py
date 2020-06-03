# -*- coding:utf-8 -*-
import time


class NewsItem:
    # 新闻发布时间
    datetime = ""
    # 更多模式
    more_mode = ""
    # create_time
    create_time = int(time.time())
    # 是否有相册
    has_gallery = False
    # 网站id
    id = ""
    # 用户id
    user_id = ""
    # 标题
    title = ""
    # 是否有视频
    has_video = False
    # 视频地址
    videos = []
    # 分享url
    share_url = ""
    # 源链接
    source = ""
    # 评论总数
    comment_count = 0
    # 文章链接
    article_url = ""
    # 评论总数
    comments_count = 0
    # 大模式?
    large_mode = ""
    # 摘要
    abstract = ""
    # 媒体链接
    media_url = ""
    # 媒体头像链接
    media_avatar_url = ""
    # 中等模式
    middle_mode = ""
    # 媒体创建者ID
    media_creator_id = ""
    # 标签id
    tag_id = ""
    # 来源链接
    source_url = ""
    # item id
    item_id = ""
    # 用户信息
    user_auth_info = {}
    # seo链接
    seo_url = ""
    # 关键词
    keyword = ""
    # 成为热点时间
    behot_time = ""
    # 标签
    tag = ""
    # 图片url
    image_url = []
    # 是否有图片
    has_image = False
    # highlight推荐？强调
    highlight = {}
    # 组id
    group_id = ""
    # 图片数量
    image_count = 0
    # 翻页页码
    page_index = 1
    # 内容
    content = ""

    def __init__(self, *arg, **kw):
        self.datetime = kw.pop("datetime", "")
        self.more_mode = kw.pop("more_mode", "")
        self.create_time = kw.pop("create_time", int(time.time()))
        self.has_gallery = kw.pop("has_gallery", False)
        self.id = kw.pop("id", "")
        self.user_id = kw.pop("user_id", "")
        self.title = kw.pop("title", "")
        self.has_video = kw.pop("has_video", False)
        self.videos = kw.pop("videos", [])
        self.share_url = kw.pop("share_url", "")
        self.source = kw.pop("source", "")
        self.comment_count = kw.pop("comment_count", 0)
        self.article_url = kw.pop("article_url", "")
        self.comments_count = kw.pop("comments_count", 0)
        self.large_mode = kw.pop("large_mode", "")
        self.abstract = kw.pop("abstract", "")
        self.media_url = kw.pop("media_url", "")
        self.media_avatar_url = kw.pop("media_avatar_url", "")
        self.middle_mode = kw.pop("middle_mode", "")
        self.media_creator_id = kw.pop("media_creator_id", "")
        self.tag_id = kw.pop("tag_id", "")
        self.source_url = kw.pop("source_url", "")
        self.item_id = kw.pop("item_id", "")
        self.user_auth_info = kw.pop("user_auth_info", {})
        self.seo_url = kw.pop("seo_url", "")
        self.keyword = kw.pop("keyword", "")
        self.behot_time = kw.pop("behot_time", "")
        self.tag = kw.pop("tag", "")
        self.image_url = kw.pop("image_url", [])
        self.has_image = kw.pop("has_image", False)
        self.highlight = kw.pop("highlight", {})
        self.group_id = kw.pop("group_id", "")
        self.image_count = kw.pop("image_count", 0)
        self.page_index = kw.pop("page_index", 1)
        self.content = kw.pop("content", "")


one_data = {
    "datetime": "2018-05-17 03:27:22",
    "more_mode": "false",
    "create_time": "1526498842",
    "has_gallery": "false",
    "id": "6556262604904333838",
    "user_id": 3656017252,
    "title": "联想高层再回应争议的“5G标准投票”事件 称是恶毒攻击",
    "has_video": "false",
    "share_url": "http://rss.cngold.com.cn/Articles/ArtContent/1/20180517d1702n237474655.html",
    "source": "中金网",
    "comment_count": 233,
    "article_url": "http://rss.cngold.com.cn/Articles/ArtContent/1/20180517d1702n237474655.html",
    "comments_count": 233,
    "large_mode": "false",
    "abstract": "5月16日，联想副总裁黄莹称，如果外部力量和不实信息干扰破坏了中国5G企业团结，很可能打破目前中美欧三方力量平衡，导致中国企业在5G标准制定中处于极为不利的位置。",
    "media_url": "http://toutiao.com/m3659626051/",
    "media_avatar_url": "//p1.pstatp.com/medium/1541/4152355309",
    "middle_mode": "false",
    "media_creator_id": 3656017252,
    "tag_id": 6556262604904333838,
    "source_url": "/group/6556262604904333838/",
    "item_id": "6556262604904333838",
    "user_auth_info": {
        "auth_type": "0",
        "other_auth": {
            "pgc": "头条财经作者"
        },
        "auth_info": "头条财经作者"
    },
    "seo_url": "/group/6556262604904333838/",
    "keyword": "联想",
    "behot_time": "1526498842",
    "tag": "news",
    "image_url": "//p3.pstatp.com/list/pgc-image/1526498841878aea1c5d74a",
    "has_image": "true",
    "highlight": {
        "source": [],
        "abstract": [
            [6, 2]
        ],
        "title": [
            [0, 2]
        ]
    },
    "group_id": "6556262604904333838",
    "image_count": 1}

if __name__ == "__main__":
    news = NewsItem()
    print(news)
    print(news.__dict__)
