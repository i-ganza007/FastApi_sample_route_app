from fastapi import FastAPI , HTTPException
import uvicorn
from turtle import update
from pydantic import BaseModel
from typing import List , Optional
from uuid import UUID , uuid4

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
def update_task(id:UUID,task_updated:Task):
    for idx,task in enumerate(tasks):
        if task.id == id:
            new_task = task.copy(update(task_updated.dict(exclude_unset=True) ) )
            tasks[idx] = new_task
            return new_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.get(f'/tasks/{id}',response_model=Task)
def get_task(id:UUID):
    result = list(filter(lambda x:x.uuid == id , tasks))
    if len((result)) == 0 : raise HTTPException(status_code=404,detail='No task found')
    return result[0]

@app.delete('/tasks/{id}', response_model=Task)
def delete_task(id: UUID):
    task_to_remove = next((task for task in tasks if task.id == id), None)
    
    if task_to_remove is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks.remove(task_to_remove)
    
    return task_to_remove

if __name__== '__main__':
    uvicorn.run(app)