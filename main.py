from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "year 12"
    }
}

@app.get("/")
def index():
    return {"message": "Hello, World"}

@app.get("/get-student/{student_id}")
def get_students(student_id: int = Path(description="The ID of the student you want to view")):
    return students.get(student_id)