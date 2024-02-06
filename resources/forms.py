from django import forms


class ResourceForm(forms.Form):
    title = forms.CharField(max_length=255)
    types = (
      (1, 'Image'),
      (2, 'PDF'),
      (3, 'Website'),
      (4, 'Video')
    )
    courses = (
      (1, 'CSE110'),
      (2, 'CSE111'),
      (3, 'CSE220'),
      (4, 'CSE221'),
      (5, 'CSE230'),
      (6, 'CSE260'),
      (7, 'CSE330'),
      (8, 'CSE331'),
      (9, 'CSE350'),
      (10, 'CSE360'),
      (11, 'CSE370'),
      (12, 'CSE421'),
      (13, 'CSE423'),
      (14, 'CSE470'),
      (15, 'CSE471'),
    )
    course = forms.ChoiceField(choices=courses)
    type = forms.ChoiceField(choices=types)
    url = forms.URLField()
  
class FilterForm(forms.Form):
    types = (
      (1, 'Image'),
      (2, 'PDF'),
      (3, 'Website'),
      (4, 'Video')
    )
    courses = (
      (1, 'CSE110'),
      (2, 'CSE111'),
      (3, 'CSE220'),
      (4, 'CSE221'),
      (5, 'CSE230'),
      (6, 'CSE260'),
      (7, 'CSE330'),
      (8, 'CSE331'),
      (9, 'CSE350'),
      (10, 'CSE360'),
      (11, 'CSE370'),
      (12, 'CSE421'),
      (13, 'CSE423'),
      (14, 'CSE470'),
      (15, 'CSE471'),
    )
    sortList = (
        (1, 'Descending'),
        (2, 'Ascending'),
    )
    type = forms.ChoiceField(choices=types, required=False)
    course = forms.ChoiceField(choices=courses, required=False)
    sort = forms.ChoiceField(choices = sortList, required=False)
