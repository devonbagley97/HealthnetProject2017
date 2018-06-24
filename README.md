README

Installation on a personal computer:

Make sure Python 3.4.3 is installed.
Make sure git is installed and in the system's PATH variable.
Open your computer's command line and navigate to the place the Healthnet files are stored.
Make sure you within the "mysite" directory of the healthnet files
Make sure Django 1.9 is installed. This can be done from the command line by running "pip install Django==1.9"
Install the fullcalendar django plugin via command line by running: "pip install -e git+https://github.com/rodrigoamaral/django-fullcalendar.git#egg=django-fullcalendar"
Install Python's time zone manager: "pip install pytz"
Create migrations in the folder that has the manage.py file in it by running: "python manage.py makemigrations"
Migrate: "python manage.py migrate"
Run the server: "python manage.py runserver"

The application should now be available in your web browser by going to "localhost:8000"

Log in as an admin using Username: admin Password: password1234 to see site statistics of past user log in's. To access other admin
tools for the site change the URL to "http://localhost:8000/admin/"

Log in as a patient user using Username: tester Password: password1234 to access the patient version of website.

Log in as a doctor user using Username: testerDoctor Password: password1234 to access the doctor version of the website which has more
functionality than the patients.

Devon Bagley was responsible for the back end functionality of the different views based on the type of user, user profile creation pages
messaging system between doctors and patients, viewing and updating a user's profile information, admission and transfer of patients to
different hospitals, viewing and creation of prescriptions, and the log in/log out pages. He was also lead test coordinator and created
a test planner for different stages of developlment which is the file "TestPlanTracker HealthNet - TestPlan".
He was not responsible for the css that determined the final design or layout of the UI (for best viewing experience zoom out your web
browser until the buttons displayed correctly), the calender plugin used to make appointments, or the
uploading files from a doctor to patient page.

For any questions or issues send Devon Bagley an email at dxb4606@g.rit.edu
