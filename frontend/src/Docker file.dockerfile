# Step 1: Use an official Python image as the base
FROM python:3.12-slim

# Step 2: Set the directory inside the container where our code will live
WORKDIR /app

# Step 3: Copy the requirements file into the container
COPY requirements.txt .

# Step 4: Install all the libraries listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy all your project files (app.py, agents.py, graph.py, etc.) into the container
COPY . .

# Step 6: Tell Docker which port your FastAPI app runs on
EXPOSE 8000

# Step 7: The command to start your backend server
CMD ["python", "app.py"]