from fastapi import FastAPI , HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List , Optional
from uuid import UUID , uuid4
#from uvicorn import 

app = FastAPI()

class Task(BaseModel):
    id: Optional[UUID] = None,
    title:str
    description: Optional[str] = None 
    completed : bool = False

tasks = []

@app.post('/tasks/',response_model=Task)
def create_task(task:Task):
    task.id = uuid4()
    tasks.append(task)
    return task


@app.get('/tasks/',response_model=List[Task])
def read_tasks():
    # FastAPI auto converts the object into the JSON format
    return {'All tasks inside':tasks}

@app.put(f'/tasks/{id}',response_model=Task)
def update_task(task_)

@app.get(f'/tasks/{id}',response_model=Task)
def get_task(id:UUID):
    result = list(filter(lambda x:x.uuid == id , tasks))
    if len((result)) == 0 : raise HTTPException(status_code=404,detail='No task found')
    return result[0]

if __name__== '__main__':
    uvicorn.run(app)