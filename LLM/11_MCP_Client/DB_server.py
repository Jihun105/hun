from mcp.server.fastmcp import FastMCP
import sqlite3


mcp = FastMCP(name='DBServer')

import os
DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sample.db')

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS emp(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       age INTEGER NOT NULL
                   )
                   ''')
    conn.commit()
    conn.close()

init_db()
@mcp.tool()
def execute_query(query: str) -> str:
    """SELECT 쿼리를 실행하고 결과를 반환"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        return "결과가 없습니다."
    return "\n".join(str(row) for row in rows)

@mcp.tool()
def execute_update(query: str) -> str:
    """INSERT, UPDATE, DELETE 쿼리를 실행"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return f"{affected}개 행이 변경되었습니다."

if __name__ == '__main__':
    mcp.run()

# pip install fastmcp
# 실행은 python server.py
