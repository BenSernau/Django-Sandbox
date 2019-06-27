from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(widget = forms.TextInput(
			attrs = {
				"placeholder": "Your title here"
			}
		)
	)

	desc = forms.CharField(required = False, label = "Description", widget = forms.Textarea(
			attrs = {
				"class" : "new-class-name two",
				"rows" : 20,
				"columns" : 20
			}
		)
	)

	price = forms.DecimalField();
	
	class Meta:
		model = Product
		fields = [
			'title',
			'desc',
			'price'
		]

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title");
		if not "CFE" in title:
			raise forms.ValidationError("This is not a valid title.");
		return title;

class RawProductForm(forms.Form):
	title = forms.CharField(widget = forms.TextInput(
			attrs = {
				"placeholder": "Your title here"
			}
		)
	)

	desc = forms.CharField(required = False, label = "Description", widget = forms.Textarea(
			attrs = {
				"class" : "new-class-name two",
				"rows" : 20,
				"columns" : 20
			}
		)
	)
	price = forms.DecimalField();