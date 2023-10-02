from django.shortcuts import render, redirect

from minecraft.models import MinecraftPost
from minecraft.forms import CreateMinecraftPostForm
from account.models import Account

def create_minecraft_view(request):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = CreateMinecraftPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		form = CreateMinecraftPostForm()

	context['form'] = form

	return render(request, "minecraft/create_mc.html", context)
