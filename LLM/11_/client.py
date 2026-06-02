import asyncio
import sys
from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
import os

async def main():
    # 실행할 서버를 설정
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'

    server_params = StdioServerParameters(
        command=sys.executable, # python  실행파일
        args=['server.py'],
        env=env
    )
    print("Strarting server...")
    # stdio (표준입출력)을 통해서 서버 프로세스를 실행하고 연결
    stdio_client(server_params)
    async with stdio_client(server_params) as (read, write):
        # 세션 열기 및 초기화
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("Server Connected")

            # 서버의 get_greeting Tool 호출
            print(f"[request] calling get_greeting...")
            greeting_result = session.call_tool(
                "get_greeting",
                arguments={"name": "홍길동"}
            )
            print(f"[response] {greeting_result.content[0].text}") 
            # mcp는 텍스트나 또는 json 형태로 감싸서 응답

            # 서버의 multiply Tool 호출
            print(f"[request] calling multiply...")
            multiply_result = session.call_tool(
                "multiply",
                arguments={"a": 10.5, "b": 20.3}
            )
            print(f"[response] {multiply_result.content[0].text}") 

if __name__ == "__main__":
    asyncio.run(main())
    
            # mcp는 텍스트나 또는 json 형태로 감싸서 응답

