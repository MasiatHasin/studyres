from django import forms

types = (
    ('', ''),
    ('Image', 'Image'),
    ('PDF', 'PDF'),
    ('Website', 'Website'),
    ('Video', 'Video')
)
courses = (
    ('', ''),
    ('CSE110', 'CSE110'),
    ('CSE111', 'CSE111'),
    ('CSE220', 'CSE220'),
    ('CSE221', 'CSE221'),
    ('CSE230', 'CSE230'),
    ('CSE250', 'CSE250'),
    ('CSE260', 'CSE260'),
    ('CSE330', 'CSE330'),
    ('CSE331', 'CSE331'),
    ('CSE340', 'CSE340'),
    ('CSE341', 'CSE341'),
    ('CSE350', 'CSE350'),
    ('CSE360', 'CSE360'),
    ('CSE370', 'CSE370'),
    ('CSE421', 'CSE421'),
    ('CSE422', 'CSE422'),
    ('CSE423', 'CSE423'),
    ('CSE460', 'CSE460'),
    ('CSE470', 'CSE470'),
    ('CSE471', 'CSE471'),
)


class ResourceForm(forms.Form):
    title = forms.CharField(max_length=255)
    course = forms.ChoiceField(choices=courses)
    semester = forms.CharField(max_length=100, required= False)
    type = forms.ChoiceField(choices=types)
    url = forms.URLField()


class FilterForm(forms.Form):
    sortList = (
        ('',''),
        ('Descending', 'Descending'),
        ('Ascending', 'Ascending'),
    )
    type = forms.ChoiceField(choices=types, required=False)
    course = forms.ChoiceField(choices=courses, required=False)
    upvotes = forms.ChoiceField(choices=sortList, required=False)
    date = forms.ChoiceField(choices=sortList, required=False)
    clicks = forms.ChoiceField(choices=sortList, required=False)
