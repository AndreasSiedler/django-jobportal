from django import forms

class DynamicArrayWidget(forms.TextInput):

    template_name = '.dynamic_array.html'

    def get_context(self, name, value, attrs):
        value = value or ['']
        context = super().get_context(name, value, attrs)
        final_attrs = context['widget']['attrs']
        id_ = context['widget']['attrs'].get('id')

        subwidgets = []
        for index, item in enumerate(context['widget']['value']):
            widget_attrs = final_attrs.copy()
            if id_:
                widget_attrs['id'] = '%s_%s' % (id_, index)
            widget = forms.TextInput()
            widget.is_required = self.is_required
            subwidgets.append(widget.get_context(name, item, widget_attrs)['widget'])

        context['widget']['subwidgets'] = subwidgets
        return context

    def value_from_datadict(self, data, files, name):
        try:
            getter = data.getlist
        except AttributeError:
            getter = data.get
        return getter(name)

    def format_value(self, value):
        return value or []  