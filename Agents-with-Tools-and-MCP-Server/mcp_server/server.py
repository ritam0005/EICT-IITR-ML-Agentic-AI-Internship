from mcp.server.fastmcp import FastMCP

from mcp_server.tools.kpi_tool import suggest_kpis
from mcp_server.tools.ml_tool import recommend_ml_model

# Create MCP Server
mcp = FastMCP("Analytics MCP Server")


@mcp.tool()
def kpi_tool(domain: str) -> str:
    """
    Suggest KPIs for a business domain.
    """
    return suggest_kpis(domain)


@mcp.tool()
def ml_tool(problem: str) -> str:
    """
    Recommend a Machine Learning model.
    """
    return recommend_ml_model(problem)


if __name__ == "__main__":
    print("Analytics MCP Server")
    print("Transport : STDIO")
    print("Waiting for MCP Client...")
   
    mcp.run(transport="stdio")