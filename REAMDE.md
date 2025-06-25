# ai-learn-mcp 示例项目

## 简介
本项目演示如何基于 Qwen-Agent、DashScope、fastmcp 框架实现智能体与自定义工具集成，包括：
- 通过 Qwen-Agent + DashScope + fetch 工具实现网页内容抓取与总结
- 基于 fastmcp 实现 documents 目录下 txt 文件统计与列表工具，并支持 MCP Inspector 可视化

## 依赖安装
建议使用 venv 虚拟环境：

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 主要功能
- 智能体网页内容抓取与总结（支持 Gradio/WebUI/终端多模式）
- MCP 文档工具服务（txt 文件数量与列表，带 Inspector）

## 启动方法

### 1. 启动文档 MCP 服务
```bash
python mcp_documents_server.py
```
默认会启动 Inspector，可在浏览器访问 http://localhost:8000/inspector 进行可视化调试。

### 2. 启动智能体（Qwen-Agent + DashScope + fetch 工具）
编辑 `qwen_agent_fetch_dashscope.py`，选择你需要的模式（WebUI/Gradio/终端），然后运行：

```bash
python qwen_agent_fetch_dashscope.py
```

### 3. 使用 mcp dev 进行开发与调试
推荐使用 `mcp dev` 命令进行本地开发和调试 MCP 服务，自动启动 Inspector 并支持热重载：

```bash
mcp dev mcp_documents_server.py
```
首次运行会自动安装 Inspector 依赖。启动后终端会输出访问地址和鉴权 token，例如：

```
MCP Inspector is up and running at http://127.0.0.1:6274
```

可直接在浏览器访问该地址进行可视化调试和接口测试。

## 目录结构
- `qwen_agent_fetch_dashscope.py` 智能体主程序
- `mcp_documents_server.py` 文档工具 MCP 服务
- `workspace/tools/documents/` 存放 txt 文档

---
如需更多自定义或扩展，欢迎随时交流！
