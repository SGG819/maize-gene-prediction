项目简介
这是一个面向玉米基因数据分析与性状预测的 Web 应用系统，专为农业生物信息学研究与竞赛场景设计。
系统通过可视化界面，实现玉米基因型数据的上传、存储、查询与 AI 预测，助力科研人员快速分析基因与农艺性状（如产量、抗病性）的关联。
技术栈
前端：HTML5 + CSS3
后端：Python + Flask
数据库：MySQL (Render 云数据库)
部署：GitHub + Render
功能特性
✅ 系统首页展示与数据库连通性测试
✅ 玉米基因数据云端存储与管理
✅ 基因 - 性状关联查询接口
🔄 可扩展：数据上传、可视化图表、预测结果下载（待开发）
快速开始
1. 本地运行
bash
运行
# 安装依赖
pip install -r requirements.txt

# 启动服务
python app.py
访问：http://localhost:5000
2. 在线访问
系统已部署至 Render 平台，可通过以下地址访问：
[你的 Render 公网地址，例如：https://maize-gene-prediction.onrender.com]
项目结构
plaintext
maize-gene-prediction/
├── app.py                 # Flask 后端主文件（数据库连接 + 路由）
├── requirements.txt       # Python 依赖清单
├── templates/
│   └── index.html         # 前端页面
└── README.md              # 项目说明文档
数据库说明
本项目使用 Render 托管的 MySQL 云数据库，用于存储：
玉米基因型数据
用户信息（可扩展）
性状预测结果
基因 - 性状关联信息
开发说明
后端接口：/ 首页，/test-db 数据库连通性测试
前端页面：基于纯 HTML/CSS 实现，可快速扩展为 Vue/React 等框架
部署流程：代码推送至 GitHub 后，Render 自动触发构建与部署
未来规划
 实现基因数据文件上传功能
 集成 GBLUP/XGBoost 等预测模型
 添加结果可视化图表（折线图 / 柱状图）
 支持 PDF/Excel 格式预测报告下载
 完善用户登录与权限管理
