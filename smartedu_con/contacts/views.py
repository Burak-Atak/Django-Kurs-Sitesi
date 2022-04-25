from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.contrib import messages

# Without csrf_token
"""def make_contact(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    message = request.POST['message']
    new_contact = Contact(name=first_name, last_name=last_name, email=email, message=message)
    new_contact.save()

    return render(request, 'contact.html')"""


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your message has been sent!')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
