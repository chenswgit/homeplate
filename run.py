from fastapi import FastAPI

app = FastAPI()  # 实例名必须是 app，Vercel 靠这个识别

@app.get("/")
def read_root():
    return {"message": "Homeplate API is running!"}

# 本地调试用，Vercel 部署时不会执行这里
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("run:app", host="0.0.0.0", port=8001, reload=True)