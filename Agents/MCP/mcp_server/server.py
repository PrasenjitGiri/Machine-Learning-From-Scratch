import logging
from typing import Any
import httpx

from mcp.server.fastmcp import FastMCP

logger = logging.basicConfig()

mcp = FastMCP(
    name='Calculator',
    host='0.0.0.0',
    port=8090
)


if __name__ == '__main__':
    transport = 'sse'

    if transport == 'studio':
        mcp.run(transport='stdio')
        logger.info('Running sever with stdio transport')
    elif transport == 'streamable-http':
        mcp.run(transport='streamable-http')
        logger.info('Running server with streamable-http')
    else:
        mcp.run(transport='sse')
        logger.info('Running server with sse')