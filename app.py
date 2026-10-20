# 方案A：若 run.py 已包含全部路由（推荐）
from run import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)

# 方案B：若想保留独立根路由（需先导入原app再挂载）
# from run import app as _app
# app = _app
# @app.get("/")
# def read_root():
#     return {"message": "Homeplate API is running!"}
# （注：Vercel 只认最终 `app` 对象，本地 uvicorn 不执行不影响部署）