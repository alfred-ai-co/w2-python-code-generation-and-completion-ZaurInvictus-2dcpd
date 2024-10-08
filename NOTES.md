# Test the CRUD Operations
Testing your CRUD operations is where theory meets practice. You’ll validate that the API performs as expected under various scenarios, ensuring that each function works correctly and efficiently.

# Start the FastAPI Server:
To begin testing, you need to run the FastAPI application. 
Open your terminal in VS Code and start the server using one of the following commands:

uvicorn app.main:app --reload

# If you prefer alternatives:

fastapi dev app/main.py

fastapi run app/main.py

These commands will start the server and make your API endpoints available for testing.

# Access the Swagger UI:
FastAPI provides an interactive Swagger UI at http://127.0.0.1:8000/docs, which is an excellent tool for testing your API endpoints. 
Navigate to this URL in your web browser to access the documentation and testing interface.

Test Each CRUD Operation: When testing the endpoints, notice how the pydantic model definitions are visible when seeing a preview for the request model on each endpoint. By modifying the pydantic model, we can change both the request and response of the API.

# Create a Project:
Use the POST /projects/ endpoint to create a new project. Input sample data for the name and description fields and submit the request. Verify that the response returns the newly created project with the correct details.

# Retrieve a Project:
Use the GET /projects/{project_id} endpoint to retrieve a project by its ID. Input the ID of the project you just created and confirm that the correct project details are returned.

# Update a Project:
Use the PUT /projects/{project_id} endpoint to update the details of an existing project. Modify the name or description and submit the request. Verify that the response reflects the updated project details.

# Delete a Project:
Use the DELETE /projects/{project_id} endpoint to delete a project by its ID. After deletion, attempt to retrieve the same project to ensure it has been removed from the database.

# Validate the Operations:
Data Integrity: Ensure that the data is correctly stored, retrieved, updated, and deleted from the database. Each operation should work seamlessly, reflecting the correct changes in the database.

Response Times: Pay attention to how quickly the API responds. While minor delays are expected during local testing, the API should generally perform CRUD operations swiftly.
Edge Cases: Test edge cases, such as trying to update or delete a project that doesn’t exist, to see how the API handles such scenarios. This will help you identify if additional error handling is needed.

Final Thoughts
By meticulously reviewing and testing your CRUD operations, you ensure that the code generated by GitHub Copilot is reliable and optimized for real-world applications. This process is essential not only for catching potential issues, but also for refining your code to meet the highest standards of quality and performance. Once satisfied with the results, your API will be well-equipped to handle data management tasks efficiently, setting the stage for further development and enhancements.