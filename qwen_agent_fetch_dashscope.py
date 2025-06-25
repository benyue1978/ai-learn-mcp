import os
from qwen_agent.agents import Assistant
from qwen_agent.gui import WebUI
from dotenv import load_dotenv

load_dotenv()

def init_agent_service():
    llm_cfg = {
        'model': 'qwen-max',
        'model_type': 'qwen_dashscope',
        'api_key': os.getenv('DASHSCOPE_API_KEY'),
        'timeout': 30,
        'retry_count': 3,
    }
    tools = [{
        "mcpServers": {
            # "fetch": {
            #     "type": "sse",
            #     "url": os.getenv('FETCH_MCP_SSE_URL')
            # },
            # "bing-cn-mcp-server": {
            #     "type": "sse",
            #     "url": os.getenv('BING_MCP_SSE_URL')
            # },
            "tavily-mcp": {
                "type": "sse",
                "url": os.getenv('TAVILY_MCP_SSE_URL')
            },
            "mcp_documents_server": {
                "command": "uv",
                "args": [
                    "run",
                    "--with",
                    "mcp",
                    "mcp",
                    "run",
                    "mcp_documents_server.py"
                ],
                "env": {
                    "HOME": "/Users/song.yue",
                    "LOGNAME": "song.yue",
                    "PATH": "/Users/song.yue/.npm/_npx/5a9d879542beca3a/node_modules/.bin:/Users/song.yue/git/ai-learn-mcp/node_modules/.bin:/Users/song.yue/git/node_modules/.bin:/Users/song.yue/node_modules/.bin:/Users/node_modules/.bin:/node_modules/.bin:/opt/homebrew/lib/node_modules/npm/node_modules/@npmcli/run-script/lib/node-gyp-bin:/Users/song.yue/.cursor/extensions/ms-python.python-2025.6.1-darwin-arm64/python_files/deactivate/zsh:/Users/song.yue/git/ai-learn-mcp/venv/bin:/opt/homebrew/Cellar/pyenv-virtualenv/1.2.4/shims:/Users/song.yue/.pyenv/shims:/Users/song.yue/.pyenv/bin:/opt/homebrew/Cellar/ruby/3.4.1/bin/:/opt/homebrew/opt/libpq/bin:/opt/homebrew/opt/postgresql@17/bin:/Users/song.yue/miniconda3/condabin:/opt/homebrew/opt/curl/bin:/usr/local/opt/binutils/bin:/usr/local/opt/openssl\\@1.0/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/Users/song.yue/.nvm/versions/node/v22.12.0/bin:/usr/local/opt/maven@3.5/bin:/usr/local/opt/openjdk/bin:/Users/song.yue/.rd/bin:/usr/local/bin:/Applications/IntelliJ IDEA.app/Contents/MacOS:/Users/song.yue/.cursor/extensions/ms-python.python-2025.6.1-darwin-arm64/python_files/deactivate/zsh:/Users/song.yue/git/ai-learn-mcp/venv/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/Library/Apple/usr/bin:/Library/TeX/texbin:/Applications/Wireshark.app/Contents/MacOS:/usr/local/share/dotnet:~/.dotnet/tools:/usr/local/go/bin:/Library/Frameworks/Mono.framework/Versions/Current/Commands:/Users/song.yue/.cargo/bin:/Users/song.yue/.orbstack/bin:/Users/song.yue/Library/Application Support/Coursier/bin:/Users/song.yue/.lmstudio/bin:/Users/song.yue/.lmstudio/bin:/Users/song.yue/git/flutter/bin",
                    "SHELL": "/bin/zsh",
                    "TERM": "xterm-256color",
                    "USER": "song.yue"
                }
            }
        }
    }]
    bot = Assistant(
        llm=llm_cfg,
        name='网页内容助手',
        description='网页内容抓取与总结',
        system_message='你是一个网页内容助手，可以抓取网页内容并总结要点，始终用中文回复。',
        function_list=tools,
    )
    return bot

def test(query='帮我抓取 https://qwenlm.github.io/blog/ 的内容并总结最新进展'):
    bot = init_agent_service()
    messages = [{'role': 'user', 'content': query}]
    print("正在处理您的请求...")
    for response in bot.run(messages):
        print('bot response:', response)

def app_tui():
    bot = init_agent_service()
    messages = []
    while True:
        try:
            query = input('user question: ')
            if not query:
                print('user question cannot be empty！')
                continue
            messages.append({'role': 'user', 'content': query})
            print("正在处理您的请求...")
            response = []
            for r in bot.run(messages):
                print('bot response:', r)
                response.append(r)
            messages.extend(response)
        except Exception as e:
            print(f"处理请求时出错: {str(e)}")
            print("请重试或输入新的问题")

def app_gui():
    bot = init_agent_service()
    WebUI(bot).run()

if __name__ == "__main__":
    # 选择运行模式
    # test()           # 测试模式
    # app_tui()        # 终端交互模式
    app_gui()          # WebUI 图形界面（默认） 