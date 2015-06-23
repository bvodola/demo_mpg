from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import JsonResponse

# Create your views here.
def index(request):
	return render(request,'lpage/index.html')

def send_message(request):

	# Fetch the attributes from the POST request
	name = request.POST.get('name')
	email = request.POST.get('email')
	phone = request.POST.get('phone')
	# if hasattr(request.POST, 'message'):
	message = request.POST.get('message')
	# else:
	# 	message = '(Nenhuma mensagem)'

	# Define Reply-To Header
	headers = {'Reply-To': email}

	message = EmailMessage(
			'[MPG] Formulário de Contato', 
			'Nome: '+name+"\n"+'Telefone: '+phone+"\n"+'Email: '+email+"\n"+'Mensagem: '+message,
			'contato@mediaplanning.com.br',
            ['contato@mediaplanning.com.br'],
            headers = headers
        )

	success = message.send()
	return JsonResponse({"success": success})