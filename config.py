# -*- coding: utf-8 -*-
"""多模态企业知识库检索：统一配置（密钥走环境变量，不入库）。"""
import os
from openai import OpenAI
import dashscope

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
if not DASHSCOPE_API_KEY:
    raise ValueError("错误：请设置 'DASHSCOPE_API_KEY' 环境变量。")

dashscope.api_key = DASHSCOPE_API_KEY
client = OpenAI(
    api_key=DASHSCOPE_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 知识库目录（放入 .docx / .txt / 图片 / 视频链接均可）
DOCS_DIR = "knowledge_base"
IMG_DIR = os.path.join(DOCS_DIR, "images")
MULTIMODAL_EMBEDDING_MODEL = "tongyi-embedding-vision-plus"
LLM_MODEL = "qwen-flash"

# 索引产物（已被 .gitignore 忽略）
INDEX_FILE = "kb_index.faiss"
METADATA_FILE = "kb_metadata.json"

# 切分参数
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# 视频知识库（示例为远程链接，需联网；可改为本地路径或留空）
VIDEO_KNOWLEDGE = [
    {
        "url": "https://dataset-1255932437.cos.ap-nanjing.myqcloud.com/mp4/car.mp4",
        "description": "汽车剐蹭视频",
    }
]

# 多模态查询意图关键词与距离阈值
IMAGE_KEYWORDS = ["图片", "海报", "照片", "看看", "长什么样", "图"]
VIDEO_KEYWORDS = ["视频", "录像", "影片", "看一下", "播放"]
MEDIA_DISTANCE_THRESHOLD = 3.0
