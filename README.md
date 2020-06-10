# Level2TeamProject - RadiU

RadiU is a web application for sharing and comparing musical tastes.

## Info

Adding as well as deleting songs and artists can only be done when logged in to a staff account.

In order to do that:
1) Create a superuser in console.
2) Register as a normal user in the website.
3) Log in as the superuser to the admin page and give staff privileges to your registered account.
4) Logout from the superuser account and log in as your registered account.

Do not log in as the superuser in the web page! The superuser does not have a UserProfile and should only be used to access the admin page!

To populate the database:
1) In bash console type 'python manage.py makemigrations radiu'.
2) In bash console type 'python manage.py migrate'.
3) In bash console type 'python populate_radiu.py'.

## Credits

Authors:  
Project Manager: Kacper Beisert  
Chief Architect: Cameron McCosh  
Developers: Darius Darulis & Pearse Graffin

## License

This is an open source project under the GNU General Public License v3.0.  
The contents of the license are available in the LICENSE file.
