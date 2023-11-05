from django import forms
from .models import Publication
from datetime import date
from ckeditor.widgets import CKEditorWidget

class PublicationCreateForm(forms.ModelForm):

    title = forms.CharField(required=True, label='',
                            widget=forms.TextInput(
                                attrs={"placeholder": "Title"}
                            )
                            )

    body_description = forms.CharField(widget=CKEditorWidget(attrs={
                                "placeholder": "Description" ,
                                "class": "Publication-Class-Name" ,
                                "rows": 8 ,
                                "cols": 32
                            }))

    publication_date = forms.DateField(label=date.today)

    class Meta:
        model = Publication
        fields = [
            'title',
            'body_description',
        ]

    def clean_publication_title(self, *args, **kwargs):

        title = self.cleaned_data.get("title")

        if not len(title):
            raise forms.ValidationError("Invalid Title")
        
        return title