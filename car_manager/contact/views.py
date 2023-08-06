from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('success')

    def _send_email(self, name, question_categories, message, mode_of_contact, phone, email):
        email_subject = "New user contact"
        email_body = render_to_string('contact/user_message.html', {
            'name': name,
            'question_categories': question_categories,
            'message': message,
            'mode_of_contact': mode_of_contact,
            'phone': phone,
            'email': email
        })
        send_mail(email_subject, '', 'grozev27@gmail.com', ['grozev27@yahoo.com'], html_message=email_body)

    def form_valid(self, form):
        form.save()
        self._send_email(
            name=form.cleaned_data['name'],
            question_categories=form.cleaned_data['question_categories'],
            message=form.cleaned_data['message'],
            mode_of_contact=form.cleaned_data['mode_of_contact'],
            phone=form.cleaned_data['phone'],
            email=form.cleaned_data['email'])
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "contact/success.html"
