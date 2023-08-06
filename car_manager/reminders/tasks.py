from celery import shared_task
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from datetime import date, timedelta

from car_manager.reminders.models import ReminderModel


@shared_task
def send_reminder_emails():
    # Get tomorrow's date
    tomorrow = date.today() + timedelta(days=1)

    # Retrieve reminders with expiration date of tomorrow
    reminders = ReminderModel.objects.filter(end_date=tomorrow)

    # Group reminders by user
    user_reminders = {}
    for reminder in reminders:
        car = reminder.car
        user = car.user

        if user not in user_reminders:
            user_reminders[user] = []

        user_reminders[user].append(reminder)

    # Send emails to related users with their car reminders
    for user, reminders in user_reminders.items():
        email_subject = "Car Expiration Reminders"
        email_body = render_to_string('reminders/reminder.html', {
            'user_name': user,
            'reminders': reminders,
        })

        try:
            send_mail(email_subject, '', 'grozev27@gmail.com', [user.email], html_message=email_body)
            print(f"Successfully sent email to {user.email}")
        except BadHeaderError:
            print("Invalid header found in the email. Email not sent.")
        except TimeoutError:
            print("SMTP server connection timed out. Email not sent.")
        except Exception as e:
            print(f"An error occurred while sending the email: {e}")
