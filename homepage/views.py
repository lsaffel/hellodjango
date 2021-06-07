from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_statement'] = 'Life is really super spectacular fantastic!'
        return context

    def say_bye(self):
        return 'Goodbye'
