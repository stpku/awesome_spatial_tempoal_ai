# Awesome Spatio-Temporal AI

<p align="left">
  <img alt="entries" src="https://img.shields.io/endpoint?url=https://stpku.github.io/awesome_spatial_temporal_ai/reports/badges/entries.json" />
  <img alt="broken links" src="https://img.shields.io/endpoint?url=https://stpku.github.io/awesome_spatial_temporal_ai/reports/badges/broken_rate.json" />
  <img alt="stale" src="https://img.shields.io/endpoint?url=https://stpku.github.io/awesome_spatial_temporal_ai/reports/badges/stale.json" />
  <img alt="last update" src="https://img.shields.io/endpoint?url=https://stpku.github.io/awesome_spatial_temporal_ai/reports/badges/updated.json" />
  
</p>

精选的时空智能（Spatio-Temporal AI）资源合集，涵盖空间智能、世界模型、开源项目、学术期刊、行业媒体等。

**最后更新**: 2026-01-30

---

## 📊 数据资源概览

本仓库所有数据以结构化 JSON 格式存储，便于程序化处理：

| 数据文件 | 内容 | 数量 |
|---------|------|------|
| `awesomelist/github_projects.json` | GitHub 开源项目 | 24个 |
| `awesomelist/latest_projects.json` | 最新空间智能/世界模型项目 | 14个 |
| `awesomelist/conferences.json` | 学术会议 | 11个 |
| `awesomelist/journals.json` | 学术期刊 | 9个 |
| `awesomelist/datasets.json` | 数据集 | 14个 |
| `awesomelist/media_channels.json` | 媒体渠道 | 10个 |
| `awesomelist/papers.json` | 学术论文 | 40篇 |

**总计**: 122 个资源条目

---

## 最新空间智能与世界模型项目

### 空间智能 (Spatial Intelligence)

- **[World Labs - Marble](https://www.worldlabs.ai/)** - Marble by World Labs (co-founded by Fei-Fei Li) is a platform that generates high-fidelity, persistent 3D worlds. Users can create worlds from images, videos, text descriptions, or 3D layouts. `Python` `3D Generation` `Multimodal`

- **[DeepMind - Genie 2](https://deepmind.google/discover/blog/genie-2/)** - DeepMind's "Foundation World Model" that can create an endless variety of playable 3D game worlds. `Python` `World Models` `3D Environments`

- **[Spatial Intelligence @ Stanford](https://spatialintelligence.stanford.edu/)** - Stanford's spatial intelligence research project exploring how AI can understand and manipulate the physical world. `Python` `Robotics` `3D Perception`

- **[LLaVA-ST](https://github.com/appletea233/LLaVA-ST)** - [CVPR 2025] LLaVA-ST: A Multimodal Large Language Model for Fine-Grained Spatial-Temporal Understanding. `Python` `Multimodal` `LLM`

- **[Oryx](https://github.com/oryx-mllm/oryx)** - [ICLR 2025] MLLM for On-Demand Spatial-Temporal Understanding at Arbitrary Resolution. `Python` `MLLM` `Spatial-Temporal`

- **[SpatialVLA](https://github.com/SpatialVLA/SpatialVLA)** - SpatialVLA: a spatial-enhanced vision-language-action model that is trained on 1.1 Million real robot episodes. Accepted at RSS 2025. `Python` `Vision-Language-Action` `Robotics`

- **[STAR](https://github.com/NJU-PCALab/STAR)** - [ICCV 2025] STAR: Spatial-Temporal Augmentation with Text-to-Video Models for Real-World Video Super-Resolution. `Python` `Text-to-Video` `Super-Resolution`

### 世界模型 (World Models)

- **[MaGRITTe](https://github.com/facebookresearch/magritte)** - Meta's Masked Geometric Image Transformer for 3D Representation Learning, a world model for 3D representation learning. `Python` `PyTorch` `3D Reconstruction`

- **[PlaNet](https://github.com/google-research/planet)** - Google's PlaNet (Planner Neural Network) is a world model based on deep reinforcement learning. `Python` `Reinforcement Learning` `Planning`

- **[DreamerV3](https://danijar.com/project/dreamerv3/)** - A sample-efficient world model for reinforcement learning that can learn complex behaviors in simulated environments. `Python` `Reinforcement Learning` `Efficiency`

- **[WorldGrow](https://github.com/world-grow/WorldGrow)** - WorldGrow: Generating Infinite 3D World [AAAI 2026 Oral]. `Python` `3D Generation` `World Models`

- **[WorldGen](https://github.com/ZiYang-xie/WorldGen)** - WorldGen - Generate Any 3D Scene in Seconds. `Python` `3D Generation` `Text-to-3D`

- **[HunyuanWorld-1.0](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0)** - Generating Immersive, Explorable, and Interactive 3D Worlds from Words or Pixels with Hunyuan3D World Model. `Python` `3D World Model` `Tencent`

- **[Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2)** - High-Resolution 3D Assets Generation with Large Scale Hunyuan3D Diffusion Models. `Python` `3D Diffusion` `High-Resolution`

- **[UltraSTF](https://arxiv.org/abs/2502.20634)** - Ultra-Compact Model for Large-Scale Spatio-Temporal Forecasting. `Python` `Forecasting` `Compact Model`


### 城市计算 (Urban Computing)

- **[MovingPandas](https://github.com/anitagraser/movingpandas)** (Stars: 1500) - Processing and visualization of movement data based on GeoPandas, providing trajectory analytics capabilities. `Python` `GeoPandas` `Shapely`

### 地理空间机器学习 (Geospatial Machine Learning)

- **[GeoPandas](https://github.com/geopandas/geopandas)** (Stars: 5800) - Python library that extends pandas to allow spatial operations on geometric types, widely used for geospatial ML. `Python` `Pandas` `Shapely`

- **[PySAL](https://github.com/pysal/pysal)** (Stars: 1200) - Python Spatial Analysis Library, providing tools for spatial data analysis and modeling. `Python` `Spatial Statistics`

- **[GeoAI](https://github.com/opengeos/geoai)** (Stars: 850) - A comprehensive Python package for integrating artificial intelligence with geospatial data analysis and visualization. `Python` `PyTorch` `Transformers`

- **[SRAI](https://github.com/kraina-ai/srai)** (Stars: 120) - Spatial Representations for Artificial Intelligence - a Python library toolkit for geospatial machine learning focused on creating embeddings for downstream tasks. `Python` `Machine Learning` `Embeddings`

### 世界模型与3D生成 (World Models & 3D Generation)

- **[WorldGrow](https://github.com/world-grow/WorldGrow)** (Stars: 650) - WorldGrow: Generating Infinite 3D World [AAAI 2026 Oral]. `Python` `3D Generation` `World Models`

- **[WorldGen](https://github.com/ZiYang-xie/WorldGen)** (Stars: 843) - WorldGen - Generate Any 3D Scene in Seconds. `Python` `3D Generation` `Text-to-3D`

- **[HunyuanWorld-1.0](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0)** (Stars: 1200) - Generating Immersive, Explorable, and Interactive 3D Worlds from Words or Pixels with Hunyuan3D World Model. `Python` `3D World Model` `Tencent`

- **[Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2)** (Stars: 950) - High-Resolution 3D Assets Generation with Large Scale Hunyuan3D Diffusion Models. `Python` `3D Diffusion` `High-Resolution`

### 时空API服务 (Spatio-Temporal API Services)

- **[Public ST APIs](https://gitee.com/stpku/public-st-apis)** - A scalable collection of geospatial APIs focused on meeting various spatio-temporal service needs, such as mapping services, weather APIs, POI queries, spatial intelligence, etc. `API Collection` `Geospatial` `Spatio-Temporal`

### OSGeo时空分析项目 (OSGeo Spatiotemporal Analysis Projects)

- **[GRASS GIS](https://grass.osgeo.org/)** - A powerful open-source geospatial processing engine that supports advanced modeling, time series analysis, and spatial data management with comprehensive spatiotemporal capabilities. `C` `Python` `Time Series Analysis`

- **[PostGIS](https://postgis.net/)** - Spatial database extender for PostgreSQL that supports temporal dimensions and spatiotemporal queries with robust indexing capabilities. `SQL` `PostgreSQL` `Temporal Queries`

- **[GeoServer](https://geoserver.org/)** - Open source server for sharing geospatial data that provides spatiotemporal data services and dynamic map creation with time-enabled layers. `Java` `OGC Standards` `Time Services`

- **[GDAL/OGR](https://gdal.org/)** - Geospatial data abstraction library supporting spatiotemporal data formats and transformations with extensive format support. `C++` `Python` `Data Formats`

- **[QGIS](https://qgis.org/)** - Leading open source GIS desktop software with plugins supporting spatiotemporal analysis and visualization of time-series data. `C++` `Python` `Visualization`

- **[Open Data Cube](https://www.opendatacube.org/)** - System for analyzing Earth observation data designed specifically for spatiotemporal data cubes and time-series analysis. `Python` `Data Cubes` `Time Series`

- **[MobilityDB](https://www.mobilitydb.com/)** - Open source extension to PostgreSQL for managing and analyzing trajectory data and moving objects with advanced spatiotemporal queries. `PostgreSQL` `Trajectories` `Movement Analysis`

- **[rasdaman](http://www.rasdaman.org/)** - Array database for managing and analyzing multi-dimensional raster data including spatiotemporal data cubes. `C++` `Raster Data` `Array Processing`

- **[Orfeo ToolBox](https://www.orfeo-toolbox.org/)** - Remote sensing image processing library with time series analysis capabilities for spatiotemporal earth observation data. `C++` `Remote Sensing` `Time Series`

- **[TorchGeo](https://torchgeo.rtfd.io/)** - Deep learning library for geospatial data with specific support for spatiotemporal remote sensing datasets. `Python` `PyTorch` `Remote Sensing`

- **[actinia](https://actinia.mundialis.de/)** - REST API for GRASS GIS providing cloud-based spatiotemporal analysis capabilities and processing services. `Python` `REST API` `Cloud Processing`

- **[GeoTools](https://www.geotools.org/)** - Java geospatial toolkit with spatiotemporal data processing capabilities and OGC standard implementations. `Java` `OGC Standards` `Data Processing`

## 学术期刊

### 国际期刊

- **[International Journal of Geographical Information Science (IJGIS)](https://www.tandfonline.com/journals/tgis20)** - Taylor & Francis出版，影响因子2.9，专注GIS理论与算法、时空数据分析

- **[ISPRS Journal of Photogrammetry and Remote Sensing](https://www.journals.elsevier.com/isprs-journal-of-photogrammetry-and-remote-sensing)** - Elsevier出版，影响因子8.9，专注遥感、摄影测量、空间信息科学

- **[Computers, Environment and Urban Systems](https://www.journals.elsevier.com/computers-environment-and-urban-systems)** - Elsevier出版，影响因子6.7，专注城市计算、地理信息系统、空间分析

- **[ISPRS International Journal of Geo-Information (IJGI)](https://www.mdpi.com/journal/ijgi)** - MDPI出版，影响因子2.8，专注地理信息科学、空间信息技术、时空数据分析

- **[IEEE Transactions on Intelligent Transportation Systems (IEEE TITS)](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=6979)** - IEEE出版，影响因子6.8，专注智能交通系统、时空数据分析、移动模式预测

### 中国期刊

- **[测绘学报](http://chxb.sinomaps.com/)** - 中国测绘学会出版，专注大地测量、摄影测量与遥感、地图制图、地理信息系统

- **[遥感学报](http://www.ygxuebao.cn/)** - 中国地理学会出版，专注遥感理论与技术、遥感应用、时空数据分析

- **[地理信息世界](http://www.china-crs.net/)** - 中国地质调查局出版，专注地理信息系统、空间数据挖掘、智慧城市

- **[地球信息科学学报](https://www.dqxxkx.cn/)** - 中国科学院地理科学与资源研究所出版，专注地理信息科学、时空大数据、GeoAI

## 行业媒体

### 中文公众号

- **UrbanComp位置智能和城市感知** - 专注于城市计算、时空大数据挖掘和位置智能的学术公众号，分享前沿研究和技术应用

- **时空大数据与社会感知** - 北京大学黄波教授团队运营，关注时空智能、地理信息科学等领域研究进展

- **GeoAI前沿** - 关注地理空间人工智能(GeoAI)最新研究动态、技术发展和应用案例

- **燕园时空** - 专注在时空智能领域前沿研究和技术应用

- **未名时空** - 北京大学GeoSoft实验室，专注时空数据分析、城市计算和GeoAI的学术公众号

- **bigscity** - 北京航空航天大学时空大数据与城市计算领域的学术公众号，关注时空智能、城市感知等前沿技术

- **时空探索之旅** - 分享时空领域最新研究和技术应用

### 国际Newsletter

- **[GeoNe.ws](https://geone.ws/)** - 最受欢迎的地理空间新闻通讯之一，涵盖行业新闻和GIS相关领域的学习资源 (更新频率: Weekly)

- **[Esri GeoAI Newsletter](https://www.esri.com/en-us/arcgis/products/arcgis-geoai/overview)** - Esri公司发布的GeoAI相关资讯，包括最新培训课程和GeoAI模型应用 (更新频率: Monthly)

- **[Spatially Informed](https://spatially.informed.blog/)** - 关注空间数据分析、地理信息系统和空间统计的新闻通讯 (更新频率: Bi-weekly)

## 贡献

欢迎提交Pull Request来完善这份Awesome List！

## 许可证

[MIT License](LICENSE)

---

## 💾 数据文件与API

所有资源均以结构化 JSON 格式存储，便于程序化处理和自动化分析：

### 数据文件结构

```
awesomelist/
├── github_projects.json      # GitHub 开源项目（24个）
├── latest_projects.json      # 最新项目（14个）
├── conferences.json          # 学术会议（11个）
├── journals.json             # 学术期刊（9个）
├── datasets.json             # 数据集（14个）
├── media_channels.json       # 媒体渠道（10个）
└── papers.json               # 学术论文（40篇）
```

### 使用数据

**命令行查看：**
```bash
# 查看 GitHub 项目
cat awesomelist/github_projects.json | python -m json.tool

# 查看最新项目
cat awesomelist/latest_projects.json | python -m json.tool
```

**Python 读取：**
```python
import json

# 加载项目数据
with open('awesomelist/github_projects.json', encoding='utf-8') as f:
    data = json.load(f)
    for category in data['categories']:
        print(f"## {category['category']}")
        for project in category['projects']:
            print(f"- [{project['name']}]({project['url']}) - {project['description']}")
```

### 徽章API

实时数据徽章（由 GitHub Pages 托管）：
- 总条目数: https://stpku.github.io/awesome_spatial_temporal_ai/reports/badges/entries.json
- 损坏链接率: https://stpku.github.io/awesome_spatial_temporal_ai/reports/badges/broken_rate.json
- 过期项目数: https://stpku.github.io/awesome_spatial_temporal_ai/reports/badges/stale.json
- 最后更新: https://stpku.github.io/awesome_spatial_temporal_ai/reports/badges/updated.json

---

## 🏗️ 项目架构

本项目采用三端架构：

| 端点 | 用途 | 内容 | 访问方式 |
|------|------|------|----------|
| **GitHub/Gitee** | 数据镜像 | 结构化数据 + 徽章 | 公开访问 |
| **GitHub Pages** | 静态展示 | 徽章API端点 | 自动部署 |

### 完整代码仓库

如需获取完整代码（包含自动化维护工具、数据验证脚本、CI/CD配置）：


完整仓库包含：
- `src/` - 模块化 Python 包（配置管理、数据验证、日志系统）
- `scripts/` - 自动化脚本（metrics, linkcheck, stars更新）
- `tools/` - 本地开发工具
- `.github/` - GitHub Actions CI/CD 配置
- 完整的数据验证和自动化工作流

### 数据更新

本仓库为数据镜像，主要数据更新通过以下方式：
1. **GitHub Actions** 自动更新项目 stars（每周一）
2. **论文归档脚本** 自动同步日报内容
3. **手动 PR** 提交新资源

如需提交贡献或获取最新数据，请访问主仓库。

---

## 🔗 相关链接

- **GitHub 镜像**: https://github.com/stpku/awesome_spatial_temporal_ai
- **Gitee 镜像**: https://gitee.com/stpku/awesome_spatial_tempoal_ai
- **在线徽章**: https://stpku.github.io/awesome_spatial_temporal_ai/reports/badges/

