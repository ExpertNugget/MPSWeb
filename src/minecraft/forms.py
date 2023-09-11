from django import forms

from minecraft.models import MinecraftPost


class CreateMinecraftPostForm(forms.ModelForm):

	class Meta:
		model = MinecraftPost
		fields = ['title', 'body', 'address', 'image']