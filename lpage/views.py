from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
from django.http import JsonResponse

# Create your views here.
def index(request):
	return render(request,'lpage/index.html')

def confirm(request):
	return render(request,'lpage/confirm.html')

def send_message(request):
	# Fetch the attributes from the POST request
	name = request.POST.get('name')
	email = request.POST.get('email')
	cpf = request.POST.get('cpf')
	ddd = request.POST.get('ddd')
	phone = request.POST.get('phone')
	period = request.POST.get('period')

	#Define Reply-To Header
	headers = {'Reply-To': email}

	message = EmailMessage(
		'[4pet] Solicitação de Proposta',
		'Mensagem',
		'contato@mediaplanning.com.br',
		['contato@mediaplanning.com.br'],
		headers = headers
	)

	success = message.send()
	return redirect('/confirm', success=success)