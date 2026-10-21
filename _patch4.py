# -*- coding: utf-8 -*-
"""multimodal-rag：抽取 config、去品牌化。"""
import io, os

B = r"c:/Users/Asus/Desktop/ai-repos/multimodal-rag"
build = os.path.join(B, "build_index.py")
query = os.path.join(B, "query.py")

sub_build = [
    ('''# 配置
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
if not DASHSCOPE_API_KEY:
    raise ValueError("错误：请设置 'DASHSCOPE_API_KEY' 环境变量。")

dashscope.api_key = DASHSCOPE_API_KEY

DOCS_DIR = "disney_knowledge_base"
IMG_DIR = os.path.join(DOCS_DIR, "images")
MULTIMODAL_EMBEDDING_MODEL = "tongyi-embedding-vision-plus"

# 输出文件
INDEX_FILE = "disney_index.faiss"
METADATA_FILE = "disney_metadata.json"

# 切分参数
CHUNK_SIZE = 500  # 每个chunk的字符数
CHUNK_OVERLAP = 50  # chunk之间的重叠字符数

# 视频知识库
VIDEO_KNOWLEDGE = [
    {
        "url": "https://dataset-1255932437.cos.ap-nanjing.myqcloud.com/mp4/car.mp4",
        "description": "汽车剐蹭视频"
    }
]''',
     "from config import *"),
    ("迪士尼RAG助手 - 知识库构建（索引入库）", "企业知识库多模态检索 - 知识库构建（索引入库）"),
]

sub_query = [
    ('''# 配置
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
if not DASHSCOPE_API_KEY:
    raise ValueError("错误：请设置 'DASHSCOPE_API_KEY' 环境变量。")

dashscope.api_key = DASHSCOPE_API_KEY

client = OpenAI(
    api_key=DASHSCOPE_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

MULTIMODAL_EMBEDDING_MODEL = "tongyi-embedding-vision-plus"
INDEX_FILE = "disney_index.faiss"
METADATA_FILE = "disney_metadata.json"

# 关键词配置
IMAGE_KEYWORDS = ["图片", "海报", "照片", "看看", "长什么样", "图"]
VIDEO_KEYWORDS = ["视频", "录像", "影片", "看一下", "播放"]
MEDIA_DISTANCE_THRESHOLD = 3.0  # 图片/视频匹配的距离阈值''',
     "from config import *"),
    ("迪士尼RAG助手 V2 - 查询处理", "企业知识库多模态检索 V2 - 查询处理"),
    ("你是一个迪士尼客服助手", "你是一个企业知识库客服助手"),
    ('我想了解一下迪士尼门票的退款流程', '我想了解一下门票的退款流程'),
]

for path, subs in [(build, sub_build), (query, sub_query)]:
    with io.open(path, "r", encoding="utf-8") as f:
        t = f.read()
    for old, new in subs:
        if old not in t:
            raise SystemExit(f"[FAIL] 未命中 {os.path.basename(path)}: {old[:40]}")
        t = t.replace(old, new, 1)
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(t)
    print(f"[OK] {os.path.basename(path)}")
print("done")
