class BootstrapFormControl:

    @staticmethod
    def apply_class_form_control(fields):
        for field in fields:
            fields[field].widget.attrs['class'] = 'form-control'
