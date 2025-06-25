from mcp.server.fastmcp import FastMCP
import os

DOCUMENTS_DIR = os.path.join(os.path.dirname(__file__), 'workspace', 'tools', 'documents')

mcp = FastMCP(
    title="Documents MCP Server",
    description="提供documents目录下txt文件统计和列表功能的MCP服务",
    version="0.1.0"
)

@mcp.tool()
def count_txt_files() -> int:
    """统计documents目录下的txt文件数量"""
    if not os.path.exists(DOCUMENTS_DIR):
        return 0
    return len([f for f in os.listdir(DOCUMENTS_DIR) if f.endswith('.txt')])

@mcp.tool()
def list_txt_files() -> list:
    """返回documents目录下所有txt文件名列表"""
    if not os.path.exists(DOCUMENTS_DIR):
        return []
    return [f for f in os.listdir(DOCUMENTS_DIR) if f.endswith('.txt')]

if __name__ == "__main__":
    mcp.run()