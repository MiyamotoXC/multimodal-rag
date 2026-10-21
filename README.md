# 多模态企业知识库检索（multimodal-rag）

> 一个**多模态 RAG** 检索系统：把企业知识库里的 **文档 / 图片 / 视频** 统一向量化，存进本地 FAISS 索引；
> 查询时根据问题自动判断是否需要图片 / 视频，路由到对应的多模态结果，并用检索到的文本片段作为上下文让 LLM 生成答案。
> 文本、图片、视频共享同一套多模态 Embedding（`tongyi-embedding-vision-plus`），无需为图片/视频单独训练。

> 作者：[@MiyamotoXC](https://github.com/MiyamotoXC) ｜ 许可证：MIT ｜ 欢迎 Star / Fork 二次开发。

## 一、能力

- **文档解析**：`.docx`（含表格转 Markdown）、`.txt` 解析 + 固定长度切分
- **多模态向量化**：文本 / 图片 / 视频统一用多模态 Embedding，存入 FAISS（IndexFlatL2）
- **多模态查询路由**：问题含「图片 / 海报 / 视频」等意图词时，自动从检索结果里挑出距离最近的图片 / 视频一并返回
- **RAG 生成**：Top-K 文本片段拼成上下文，交给 `qwen-flash` 生成答案

## 二、目录结构

```
multimodal-rag/
├── config.py            # 统一配置（密钥走环境变量）
├── build_index.py       # 解析知识库 → 切分 → 多模态 Embedding → FAISS 落盘
├── query.py             # 加载索引 → 查询 → 多模态路由 → RAG 生成
├── embed_text.py        # 文本 Embedding 最小验证
├── embed_image.py       # 图片 Embedding 最小验证
├── embed_video.py       # 视频 Embedding 最小验证
├── knowledge_base/      # 示例知识库（.docx / 图片 / 视频链接）
├── requirements.txt
└── LICENSE
```

## 三、快速开始

```bash
pip install -r requirements.txt

# 1) 配置密钥
export DASHSCOPE_API_KEY="你的密钥"      # Windows: set DASHSCOPE_API_KEY=...

# 2) 构建索引
python build_index.py

# 3) 查询（自动处理文本 / 图片 / 视频意图）
python query.py
```

## 四、配置（config.py）

| 项 | 默认 | 说明 |
|---|---|---|
| `DASHSCOPE_API_KEY` | 环境变量 | 多模态 Embedding 与 LLM 密钥（必需，不入库） |
| `DOCS_DIR` | `knowledge_base` | 知识库目录 |
| `MULTIMODAL_EMBEDDING_MODEL` | `tongyi-embedding-vision-plus` | 多模态向量模型 |
| `LLM_MODEL` | `qwen-flash` | 生成答案的 LLM |
| `CHUNK_SIZE` / `CHUNK_OVERLAP` | 500 / 50 | 文本切分参数 |
| `MEDIA_DISTANCE_THRESHOLD` | 3.0 | 图片/视频命中的距离阈值 |

## 五、能力边界（诚实说明）

- 示例知识库为公开主题乐园规则，仅作演示；替换为你的私有文档即可投产
- 视频 Embedding 依赖远程示例链接，断网时可清空 `config.VIDEO_KNOWLEDGE`
- 检索质量上限取决于知识库覆盖度与切分粒度；长文档建议调小 `CHUNK_OVERLAP` 或语义切分

## 六、License

代码以 MIT 发布；示例知识库内容仅作技术演示，不代表任何官方立场。
