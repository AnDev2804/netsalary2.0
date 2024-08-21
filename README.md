
# Employee Salary Consultation System

This is a Python-based application that calculates the total salary for an employee based on various factors such as position, academic degree, age, years of service, and more. The system uses a GUI (Graphical User Interface) built with Tkinter and connects to a MySQL database to retrieve and process employee data.

This mini-project was part of an individual evaluation. The teacher was in charge of supplying us with the images of the conditions that the net salary calculation would have and the creation of the database with the predetermined data for the correct functioning of the queries. We, the students, only had to make the program with its respective GUI and the appropriate conditions given by the teacher.

It should be noted that everything was tested on a local server.

## Key Features
- **Employee Data Management:** Retrieve and display personal, labor, family, and academic data of employees from a MySQL database.
- **Salary Calculation:** Automatically calculate the total salary based on several incentives, including:
  - Age-based incentives: 15% increase for employees aged 50 and above.
  - Service-based incentives: 5% increase for every 4 years of service.
  - Position-based incentives: Percentage increase based on the employee's job title.
  - Academic incentives: Fixed amount added based on the employee's academic achievements.
- **Data Visualization:** Display the results in a user-friendly interface.

## Technologies Used
- **Python:** The core programming language used for logic and operations.
- **Tkinter:** For creating the graphical user interface.
- **MySQL:** For storing and retrieving employee data.
- **SQL:** For querying the database.
- **Connector/Python:** The MySQL driver used to connect Python with the MySQL database.

## Installation Instructions

1. **Clone the repository:**
   ```
   git clone <your-repository-url>
   ```

2. **Configure the database:**
   - Import the `PYQUERY2024.SQL` file into your MySQL server via PHPMyAdmin or the MySQL command line.
   - Update the `conexion.py` file with your database credentials.

3. **Install necessary dependencies:**
   ```
   pip install mysql-connector-python
   ```

4. **Run the application:**
   - Open a terminal or command prompt in the project directory.
   - Execute the following command:
     ```
     python main.py
     ```

## Usage
- **Enter Employee ID:** The user can input an employee ID in the text field and click on "Consultar" to see the employee's total salary based on various factors.
- **View Results:** The results, including the employee's base salary, additional incentives, and total calculated salary, will be displayed in the application window.

## Screenshots
Here are some screenshots of the application in action:
![Special Incentive](./INCENTIVO%20ESPECIAL.jpg)
![Seniority Incentive](./INCENTIVO%20POR%20ANTIGUEDAD.jpg)
![Academic Incentive](./INCENTIVOS%20ACADEMICOS.jpg)
![Family Incentive](./INCENTIVOS%20FAMILIARES.jpg)
![Incentives per Position](./INCENTIVOS%20POR%20CARGO.jpg)

## Warning
The family incentive summation part is in development, as it was the only part I missed on the exam.

## Contribution
Feel free to fork this repository, create your own branch, make improvements, and submit a pull request. All contributions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.
