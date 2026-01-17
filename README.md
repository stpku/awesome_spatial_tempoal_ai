# Awesome Spatio-Temporal AI

精选的时空智能（Spatio-Temporal AI）资源合集，涵盖空间智能、世界模型、开源项目、学术期刊、行业媒体等。

## 最新空间智能与世界模型项目

### 空间智能 (Spatial Intelligence)

- **[World Labs - Marble](https://www.worldlabs.ai/)** - 由李飞飞等人创立的World Labs推出的Marble，是一个能生成高拟真、持续存在的3D世界的平台，用户可通过图片、视频、文字描述或3D布局创建世界。 `Python` `3D Generation` `Multimodal`
- **[DeepMind - Genie 2](https://deepmind.google/discover/blog/genie-2/)** - DeepMind发布的"基础世界模型"，能够创建无限种类的可玩3D游戏世界。 `Python` `World Models` `3D Environments`
- **[Spatial Intelligence @ Stanford](https://spatialintelligence.stanford.edu/)** - 斯坦福大学的空间智能研究项目，探索AI如何理解和操作物理世界。 `Python` `Robotics` `3D Perception`

### 世界模型 (World Models)

- **[MaGRITTe](https://github.com/facebookresearch/magritte)** - Meta提出的Masked Geometric Image Transformer for 3D Representation Learning，用于3D表示学习的世界模型。 `Python` `PyTorch` `3D Reconstruction`
- **[PlaNet](https://github.com/google-research/planet)** - Google的PlaNet（Planner Neural Network）是一个基于深度强化学习的世界模型。 `Python` `Reinforcement Learning` `Planning`
- **[DreamerV3](https://danijar.com/project/dreamerv3/)** - 一种用于强化学习的样本高效世界模型，能够在模拟环境中学习复杂行为。 `Python` `Reinforcement Learning` `Efficiency`

## 国际顶会与相关分论坛

### 机器学习顶会

- **[NeurIPS (Conference on Neural Information Processing Systems)](https://neurips.cc/)** - 神经信息处理系统大会，包含多个时空计算和世界模型相关的工作坊。 `Annual` `Machine Learning` `AI`
- **[ICML (International Conference on Machine Learning)](https://icml.cc/)** - 国际机器学习会议，涵盖时空数据学习和世界模型研究。 `Annual` `Machine Learning` `AI`
- **[ICLR (International Conference on Learning Representations)](https://iclr.cc/)** - 国际学习表征会议，包含空间智能和世界模型相关研究。 `Annual` `Deep Learning` `Representation Learning`

### 计算机视觉与图形学顶会

- **[CVPR (Computer Vision and Pattern Recognition)](http://cvpr2025.thecvf.com/)** - 计算机视觉与模式识别会议，包含大量空间智能和3D重建相关研究。 `Annual` `Computer Vision` `3D Graphics`
- **[SIGGRAPH (Special Interest Group on Computer GRAPHics)](https://s2025.siggraph.org/)** - 计算机图形学特别兴趣小组会议，涵盖3D世界生成和空间计算。 `Annual` `Computer Graphics` `3D Modeling`
- **[ECCV (European Conference on Computer Vision)](https://eccv.ecva.net/)** - 欧洲计算机视觉会议，包含空间智能和世界模型相关研究。 `Annual` `Computer Vision` `AI`

### 空间计算与时空分析顶会

- **[ACM SIGSPATIAL](https://sigspatial2025.sigspatial.org/)** - ACM关于空间数据的旗舰会议，聚焦空间数据科学、地理信息学、时空数据库。 `Annual` `Spatial Computing` `GIS`
- **[SpatialConnect Workshop (SIGSPATIAL)](https://dl.acm.org/doi/proceedings/10.1145/3764924)** - SIGSPATIAL的空间智能与智慧社区工作坊。 `Annual` `Spatial Intelligence` `Smart Cities`
- **[GeoIndustry Workshop (SIGSPATIAL)](https://dl.acm.org/doi/proceedings/10.1145/3764919)** - SIGSPATIAL的空间大数据与工业应用工作坊。 `Annual` `Spatial Big Data` `AI`
- **[Spatial Data Science Conference](https://spatial-data-science-conference.com/)** - 汇聚地理空间、分析和数据科学专业人士的会议。 `Annual` `Spatial Data Science` `Analytics`
- **[AAG Annual Meeting](https://www.aag.org/)** - 美国地理学家协会年会，设有空间AI和数据科学前沿专题研讨会。 `Annual` `Geography` `Spatial Analysis`

## 开源项目

### 轨迹预测 (Trajectory Prediction)

- **[LibCity](https://github.com/LibCity/Bigscity-LibCity)** - A unified, comprehensive library for reproducing and developing spatial-temporal prediction methods, facilitating research and application in urban computing. (Stars: 2500, Last Updated: 2024-01-15) `Python` `PyTorch` `TensorFlow`
- **[TorchSpatiotemporal](https://github.com/nnaisense/TorchSpatiotemporal)** - A PyTorch library for spatiotemporal sequence modeling, providing implementations of various spatiotemporal models. (Stars: 850, Last Updated: 2024-01-10) `Python` `PyTorch`

### 城市计算 (Urban Computing)

- **[MovingPandas](https://github.com/anitagraser/movingpandas)** - Processing and visualization of movement data based on GeoPandas, providing trajectory analytics capabilities. (Stars: 1200, Last Updated: 2024-01-12) `Python` `GeoPandas` `Shapely`

### 地理空间机器学习 (Geospatial Machine Learning)

- **[GeoPandas](https://github.com/geopandas/geopandas)** - Python library that extends pandas to allow spatial operations on geometric types, widely used for geospatial ML. (Stars: 4800, Last Updated: 2024-01-16) `Python` `Pandas` `Shapely`
- **[PySAL](https://github.com/pysal/pysal)** - Python Spatial Analysis Library, providing tools for spatial data analysis and modeling. (Stars: 950, Last Updated: 2024-01-11) `Python` `Spatial Statistics`

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

- **燕园时空** - 专注在时空智能领域前沿研究和技术应用
- **未名时空** - 北京大学GeoSoft实验室，专注时空数据分析、城市计算和GeoAI的学术公众号 
- **bigscity** - 北京航空航天大学时空大数据与城市计算领域的学术公众号，关注时空智能、城市感知等前沿技术 (最近更新: 2024-01-14)
- **时空探索之旅** - 分享时空领域最新研究和技术应用

### 国际Newsletter

- **[GeoNe.ws](https://geone.ws/)** - 最受欢迎的地理空间新闻通讯之一，涵盖行业新闻和GIS相关领域的学习资源 (更新频率: Weekly)
- **[Esri GeoAI Newsletter](https://www.esri.com/en-us/arcgis/products/arcgis-geoai/overview)** - Esri公司发布的GeoAI相关资讯，包括最新培训课程和GeoAI模型应用 (更新频率: Monthly)
- **[Spatially Informed](https://spatially.informed.blog/)** - 关注空间数据分析、地理信息系统和空间统计的新闻通讯 (更新频率: Bi-weekly)


## 贡献

欢迎提交Pull Request来完善这份Awesome List！

## 许可证

[MIT License](LICENSE)
