from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )


class new_user(BaseModel):
    name:str
    email:str
    role:str
    


people =[{
    'name':'Rio horikoshi',
    'email': 'rio_24s1100xxx@nnn.ed.jp',
    'role': 'S高等学校',}
    
    ]
@app.get('/')
def Items():
    return people

@app.post('/endpoint')
async def new_sata(user:new_user):
    
    print(user)
    people.append(user)
    return {"message":'success'}

if __name__ =="__main__":
    uvicorn.run(app,port=8000,log_level='debug')
